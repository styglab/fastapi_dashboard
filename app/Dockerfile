FROM python:3.9.16

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY . /app
#CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]

WORKDIR /app
#CMD ["python","backend_pre_start.py"]
#CMD ["alembic","upgrade","head"]
#CMD ["/app/prestart.sh"]

EXPOSE 8000