# Backend Server features
- RESTful API Server Sample code based on Python FastAPI
- Database such as Sqlite is accessed such as insert, select, update and delete (CRUD) via SQLAlchemy JPA
- ~~LockModeType.PESSIMISTIC_WRITE 를 이용한 데이터 동시성 제어~~
- Container creation and execution using Docker
- execution file creation by Pyinstaller
- Writing test code in order to execute by Pytest
- applying Basic Authentication and OAuth Token

## 1. Frameworks And Tools
- Python 3.12
- FastAPI
- Uvicorn
- Pydantic
- SQLAlchemy
- SQLite
- Docker
- Swagger UI
- pytest

## 2. Local execution test
```
- uvicorn train.app.application:app --host 0.0.0.0 --port 9084
- python train\app\application.py
  -  set PYTHONPATH=%PYTHONPATH%;%cd%
- pip freeze > requirements.txt
```
## 3. Execution file creation - Windows environment
```
- pyinstaller main.spec
```
## 4. Container execution test
```
- docker build -t pyserver:local .  && docker run --gpus=all -p 9084:9083 pyserver:local --port 9083
- docker-compse up 
```

## 5. Execution of test code
```
- pytest test\controller
```

## 6. API spec URL
```
- Swagger UI : http://localhost:9084/docs
```


