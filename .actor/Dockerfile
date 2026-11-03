FROM apify/actor-python:3.12

COPY actor/requirements.txt ./actor/requirements.txt
RUN pip install --no-cache-dir -r actor/requirements.txt

# Only the code the probe needs. data/, site/, tests/ and tasks/ stay out (.dockerignore).
COPY probe/ ./probe/
COPY actor/ ./actor/

CMD ["python", "-m", "actor"]
