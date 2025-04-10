FROM python:3.10-slim

WORKDIR /app
COPY . .

RUN pip install --upgrade pip && pip install -r requirements.txt

CMD ["streamlit", "run", "insurance_rag_claim_qa/app.py"]
