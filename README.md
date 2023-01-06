# FastAPI Soft Dashboard

# sqlite
# change path
$cd app
# change env
in app.env
debugging = 1
# migrate
$python backend_pre_start.py
$alembic upgrade head
# exucute
$uvicorn src.app:app --host 0.0.0.0 --port 9090

# docker (docker-compose)
# change env
in app.env
debugging = 0
# exucute
$sudo docker-compose up --build