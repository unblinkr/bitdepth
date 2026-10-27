"""Prompt families and graders.

Every prompt and every answer is produced by code from a seed. Nothing is copied
from a public benchmark. Graders compare strings and numbers only.

Each generated prompt is a dict: id, family, prompt, answer, and schema (json only).
"""

from __future__ import annotations

import argparse
import json
import random
import re
import sys
from pathlib import Path
from typing import Any

import jsonschema

from probe import FIXED_SEED

FAMILIES = ["math", "json", "string", "needle", "echo"]
FIXED_COUNTS = {"math": 40, "json": 20, "string": 20, "needle": 20, "echo": 20}
FRESH_COUNTS = {"math": 8, "json": 4, "string": 4, "needle": 4, "echo": 4}
FIXED_PATH = Path("data/prompts/fixed.jsonl")

# Word lists are plain generated vocabulary, used only to build filler and records.
NOUNS = [
    "crate", "ledger", "lantern", "harbor", "orchard", "beacon", "meadow", "furnace",
    "compass", "quarry", "granary", "turbine", "canal", "archive", "saddle", "kiln",
    "pulley", "cistern", "anvil", "trellis", "loom", "ferry", "bellows", "mill",
]
VERBS = [
    "moved", "counted", "sorted", "repaired", "shipped", "weighed", "labelled", "stacked",
    "measured", "painted", "loaded", "inspected", "recorded", "sealed", "cleaned", "tested",
]
ADJECTIVES = [
    "narrow", "copper", "quiet", "heavy", "pale", "distant", "wooden", "steady",
    "crooked", "bright", "hollow", "rusted", "woven", "square", "salted", "frozen",
]
PLACES = [
    "the north yard", "the lower deck", "the east wing", "the old pier", "the back road",
    "the stone hall", "the long shed", "the river bend", "the top floor", "the side gate",
]
FIRST_NAMES = [
    "Mara", "Tobias", "Ilse", "Rafael", "Wen", "Dagny", "Kofi", "Sunniva", "Arvid",
    "Leela", "Ozan", "Pilar", "Hesper", "Joaquin", "Nadia", "Bram", "Yuki", "Soren",
]
LAST_NAMES = [
    "Lindqvist", "Okafor", "Marchetti", "Haddad", "Novak", "Takeda", "Brennan", "Vasquez",
    "Rutherford", "Castellano", "Oyelaran", "Fitzgerald", "Mbeki", "Sorensen", "Delacroix",
]
ITEMS = [
    "brass hinge", "oak plank", "coil of rope", "glass jar", "tin lantern", "wool blanket",
    "iron bracket", "clay tile", "canvas sack", "steel pin", "copper wire", "paper map",
    "wax candle", "linen cloth", "cedar box", "stone weight",
]
ECHO_PIECES = [
    "café", "naïve", "Zürich", "São Paulo", "jalapeño", "smörgåsbord", "Ærø", "Łódź",
    "東京", "北京市", "こんにちは", "서울", "Київ", "Ελλάδα", "ไทย", "मुंबई",
    "🚀", "✅", "🙂", "🌊", "🧭", "🪵", "🔑", "📦",
    "«quoted»", "¿por qué?", "¡hola!", "(aside)", "[note]", "{set}", "a/b", "x~y",
    "3.14159", "1,000,000", "50%", "#7", "@home", "A&B", "key=value", "end.",
]


def _rng(seed: int | str, family: str) -> random.Random:
    return random.Random(f"{seed}-{family}")


def _pseudo_word(rng: random.Random, n: int) -> str:
    return "".join(rng.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(n))


# ---------------------------------------------------------------- math

def gen_math(rng: random.Random, pid: str) -> dict[str, Any]:
    a, b, c, d = (rng.randint(2, 999) for _ in range(4))
    noun = rng.choice(NOUNS) + "s"
    place = rng.choice(PLACES)
    template = rng.randint(0, 3)
    if template == 0:
        # start, receive, ship, receive
        c = min(c, a + b)
        answer = a + b - c + d
        prompt = (
            f"At dawn there are {a} {noun} in {place}. During the morning {b} more {noun} arrive. "
            f"In the afternoon {c} {noun} are shipped out. In the evening {d} more {noun} arrive. "
            f"How many {noun} are in {place} at night? Reply with the final integer only."
        )
    elif template == 1:
        # per batch times batches, minus sold, plus returned
        c = min(c, a * b)
        answer = a * b - c + d
        prompt = (
            f"A workshop in {place} makes {a} {noun} per batch and completes {b} batches. "
            f"It then sends {c} {noun} to a buyer, and later {d} {noun} come back from an earlier order. "
            f"How many {noun} does the workshop hold now? Reply with the final integer only."
        )
    elif template == 2:
        # three deliveries then split evenly: use total minus removed, then add
        c = min(c, a + b)
        answer = (a + b - c) + d
        prompt = (
            f"Three deliveries to {place}: the first brings {a} {noun}, the second brings {b} {noun}, "
            f"then {c} {noun} are found damaged and discarded, and a final delivery brings {d} {noun}. "
            f"How many usable {noun} are there? Reply with the final integer only."
        )
    else:
        # total minus two removals
        total = a + b + d
        c = min(c, total)
        answer = total - c
        prompt = (
            f"A team in {place} counts {a} {noun}, then another {b} {noun}, then another {d} {noun}. "
            f"Afterwards {c} {noun} are moved elsewhere. How many {noun} are left? "
            f"Reply with the final integer only."
        )
    return {"id": pid, "family": "math", "prompt": prompt, "answer": str(answer)}


_INT_RE = re.compile(r"-?\d[\d,]*")


def grade_math(output: str, answer: str) -> bool:
    found = _INT_RE.findall(output or "")
    if not found:
        return False
    last = found[-1].replace(",", "")
    return last == answer


# ---------------------------------------------------------------- json

JSON_SCHEMA = {
    "type": "object",
    "required": ["name", "dates", "amounts", "items"],
    "additionalProperties": False,
    "properties": {
        "name": {"type": "string"},
        "dates": {"type": "array", "minItems": 3, "maxItems": 3, "items": {"type": "string"}},
        "amounts": {"type": "array", "minItems": 2, "maxItems": 2, "items": {"type": "number"}},
        "items": {"type": "array", "minItems": 4, "maxItems": 4, "items": {"type": "string"}},
    },
}


def gen_json(rng: random.Random, pid: str) -> dict[str, Any]:
    name = f"{rng.choice(FIRST_NAMES)} {rng.choice(LAST_NAMES)}"
    dates = []
    for _ in range(3):
        y = rng.randint(2019, 2031)
        m = rng.randint(1, 12)
        d = rng.randint(1, 28)
        dates.append(f"{y:04d}-{m:02d}-{d:02d}")
    amounts = [round(rng.randint(100, 999999) / 100, 2) for _ in range(2)]
    items = rng.sample(ITEMS, 4)
    record = {"name": name, "dates": dates, "amounts": amounts, "items": items}
    prompt = (
        "Produce a JSON object with exactly these four fields and no others: "
        "\"name\" (a string), \"dates\" (an array of exactly three strings in YYYY-MM-DD form), "
        "\"amounts\" (an array of exactly two numbers), \"items\" (an array of exactly four strings). "
        f"The name is {name}. The dates, in order, are {dates[0]}, {dates[1]} and {dates[2]}. "
        f"The amounts, in order, are {amounts[0]:.2f} and {amounts[1]:.2f}. "
        f"The items, in order, are {items[0]}, {items[1]}, {items[2]} and {items[3]}. "
        "Reply with the JSON object only: no prose, no code fences."
    )
    return {
        "id": pid,
        "family": "json",
        "prompt": prompt,
        "answer": json.dumps(record, ensure_ascii=False),
        "schema": JSON_SCHEMA,
    }


def _extract_json_object(text: str) -> str | None:
    s = (text or "").strip()
    if s.startswith("```"):
        s = re.sub(r"^```[a-zA-Z]*\s*", "", s)
        s = re.sub(r"\s*```$", "", s)
    start = s.find("{")
    end = s.rfind("}")
    if start == -1 or end == -1 or end < start:
        return None
    return s[start : end + 1]


def grade_json(output: str, answer: str, schema: dict[str, Any] | None = None) -> bool:
    body = _extract_json_object(output)
    if body is None:
        return False
    try:
        got = json.loads(body)
    except json.JSONDecodeError:
        return False
    try:
        jsonschema.validate(got, schema or JSON_SCHEMA)
    except jsonschema.ValidationError:
        return False
    want = json.loads(answer)
    if got["name"] != want["name"]:
        return False
    if list(got["dates"]) != list(want["dates"]):
        return False
    if list(got["items"]) != list(want["items"]):
        return False
    try:
        if any(round(float(g), 2) != round(float(w), 2) for g, w in zip(got["amounts"], want["amounts"])):
            return False
    except (TypeError, ValueError):
        return False
    return True


# ---------------------------------------------------------------- string

def gen_string(rng: random.Random, pid: str) -> dict[str, Any]:
    op = rng.choice(["reverse", "count", "caesar", "sort"])
    word = _pseudo_word(rng, rng.randint(6, 10))
    if op == "reverse":
        answer = word[::-1]
        prompt = f"Reverse the letters of the word \"{word}\". Reply with the reversed word only."
    elif op == "count":
        letter = rng.choice(word)
        answer = str(word.count(letter))
        prompt = f"How many times does the letter \"{letter}\" appear in the word \"{word}\"? Reply with the number only."
    elif op == "caesar":
        k = rng.randint(1, 25)
        answer = "".join(chr((ord(ch) - 97 + k) % 26 + 97) for ch in word)
        prompt = (
            f"Apply a Caesar shift of {k} to the word \"{word}\" (shift each letter forward by {k} places "
            f"in the alphabet, wrapping from z to a). Reply with the shifted word only."
        )
    else:
        answer = "".join(sorted(word))
        prompt = f"Sort the letters of the word \"{word}\" into alphabetical order. Reply with the sorted letters only, as one word."
    return {"id": pid, "family": "string", "prompt": prompt, "answer": answer}


def _clean_short(text: str) -> str:
    s = (text or "").strip()
    s = s.strip("`\"'“”‘’ \n\t")
    s = s.rstrip(".")
    return s.strip()


def grade_string(output: str, answer: str) -> bool:
    return _clean_short(output) == answer


# ---------------------------------------------------------------- needle

def _filler_sentence(rng: random.Random) -> str:
    return (
        f"The {rng.choice(ADJECTIVES)} {rng.choice(NOUNS)} was {rng.choice(VERBS)} near "
        f"{rng.choice(PLACES)} before the {rng.choice(ADJECTIVES)} {rng.choice(NOUNS)} was "
        f"{rng.choice(VERBS)} again."
    )


def gen_needle(rng: random.Random, pid: str, words: int = 2500) -> dict[str, Any]:
    code = "".join(rng.choice("ABCDEFGHJKLMNPQRSTUVWXYZ23456789") for _ in range(8))
    sentences: list[str] = []
    count = 0
    while count < words:
        s = _filler_sentence(rng)
        sentences.append(s)
        count += len(s.split())
    pos = rng.randint(len(sentences) // 10, len(sentences) - len(sentences) // 10)
    sentences.insert(pos, f"The access code for the archive is {code}.")
    body = " ".join(sentences)
    prompt = (
        "Read the following notes and then answer the question at the end.\n\n"
        f"{body}\n\n"
        "Question: What is the access code for the archive? Reply with the code only."
    )
    return {"id": pid, "family": "needle", "prompt": prompt, "answer": code}


def grade_needle(output: str, answer: str) -> bool:
    return answer in (output or "")


# ---------------------------------------------------------------- echo

def gen_echo(rng: random.Random, pid: str) -> dict[str, Any]:
    n = rng.randint(8, 14)
    pieces = [rng.choice(ECHO_PIECES) for _ in range(n)]
    # a few plain words so the line reads as text
    for _ in range(rng.randint(2, 4)):
        pieces.insert(rng.randint(0, len(pieces)), rng.choice(NOUNS))
    text = " ".join(pieces)
    prompt = (
        "Repeat exactly the text between the markers, character for character, with nothing added "
        "before or after it. Do not include the markers.\n<<<\n"
        f"{text}\n>>>"
    )
    return {"id": pid, "family": "echo", "prompt": prompt, "answer": text}


def grade_echo(output: str, answer: str) -> bool:
    return (output or "").strip() == answer


# ---------------------------------------------------------------- dispatch

GENERATORS = {
    "math": gen_math,
    "json": gen_json,
    "string": gen_string,
    "needle": gen_needle,
    "echo": gen_echo,
}


def grade(family: str, output: str, answer: str, schema: dict[str, Any] | None = None) -> bool:
    if family == "math":
        return grade_math(output, answer)
    if family == "json":
        return grade_json(output, answer, schema)
    if family == "string":
        return grade_string(output, answer)
    if family == "needle":
        return grade_needle(output, answer)
    if family == "echo":
        return grade_echo(output, answer)
    raise ValueError(f"unknown family {family}")


def generate_set(seed: int | str, counts: dict[str, int], prefix: str) -> list[dict[str, Any]]:
    """Generate prompts in round-robin family order so any leading slice is a mix."""
    per_family: dict[str, list[dict[str, Any]]] = {}
    for fam in FAMILIES:
        rng = _rng(seed, fam)
        per_family[fam] = [
            GENERATORS[fam](rng, f"{prefix}-{fam}-{i + 1:03d}") for i in range(counts.get(fam, 0))
        ]
    out: list[dict[str, Any]] = []
    idx = {fam: 0 for fam in FAMILIES}
    remaining = sum(len(v) for v in per_family.values())
    while remaining:
        for fam in FAMILIES:
            if idx[fam] < len(per_family[fam]):
                out.append(per_family[fam][idx[fam]])
                idx[fam] += 1
                remaining -= 1
    return out


def fixed_set() -> list[dict[str, Any]]:
    return generate_set(FIXED_SEED, FIXED_COUNTS, "fixed")


def fresh_set(date: str) -> list[dict[str, Any]]:
    """24 prompts for one night, seeded by the date as an integer YYYYMMDD."""
    seed = int(date.replace("-", ""))
    return generate_set(seed, FRESH_COUNTS, f"fresh-{date}")


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    with path.open(encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write-fixed", action="store_true", help="write data/prompts/fixed.jsonl once")
    args = ap.parse_args(argv)
    if args.write_fixed:
        if FIXED_PATH.exists():
            n = len(load_jsonl(FIXED_PATH))
            print(f"{FIXED_PATH} exists with {n} prompts; not rewriting")
            return 0
        rows = fixed_set()
        write_jsonl(FIXED_PATH, rows)
        print(f"wrote {len(rows)} prompts to {FIXED_PATH}")
        return 0
    ap.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
