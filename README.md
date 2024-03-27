# Тестовое задание для компании Betting Software
---

## 1. First Steps
1. Create a file (name it as follows `.env`) in the root directory based on `.env.sample`
2. Create a file (name it as follows `db`) in the directory - `_compose/env`, based on `db.sample`
3. Run `docker compose build`
4. Apply migrations `docker compose run --rm app alembic upgrade head`
5. Run `docker compose up`

## 2. Entities
### События
```
|        Event                  |
|---------|---------------------|
|  id     |       result        |
| bigint  |       str           | 
```

- result:
    - `pending` ещё не сыграла (соответствующее событие ещё не завершилось),
    - `win` выиграла (событие завершилось выигрышем первой команды),
    - `lose` проиграла (событие завершилось проигрышем первой команды или ничьей).

### Ставки
```
|                          Predictions                            |
|---------|----|-------------|----------|------------|------------|
|  id     |uuid| event_id    |    bet   |   status   |   amount   |
| bigint  |uuid|    bigint   |  varchar |   float    |  varchar   |
```

- status:
    - `win` выигрыш,
    - `lose` проигрыш
- bet:
    - `win` выиграла (событие завершилось выигрышем первой команды),
    - `lose` проиграла (событие завершилось проигрышем первой команды или ничьей).

## 3. Endpoints
- `GET  /bets/`
```json
curl -X 'GET' \
  'http://0.0.0.0:8000/bets/' \
  -H 'accept: application/json'
```

- `POST /bets/`
```json
curl -X 'POST' \
  'http://0.0.0.0:8000/bets/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "amount": 1000.5,
  "event_id": 1,
  "bet": "win"
}'
```

- `GET /events/`
```json
curl -X 'GET' \
  'http://0.0.0.0:8000/events/' \
  -H 'accept: application/json'
```

- `PUT  /events/{event_id}`
```json
curl -X 'PUT' \
  'http://0.0.0.0:8000/events/1' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "result": "win"
}'
```

## 4. Project Structure
```
.
├── README.md
├── _compose
│   ├── app
│   │   └── Dockerfile
│   ├── db
│   │   └── Dockerfile
│   ├── env
│   │   ├── db
│   │   └── db.sample
│   └── scripts
│       └── start-app
├── alembic
│   ├── README
│   ├── env.py
│   ├── script.py.mako
│   └── versions
│       └── e0d38731af25_.py
├── alembic.ini
├── docker-compose.yml
├── main.py
├── poetry.lock
├── pyproject.toml
└── src
    ├── config.py
    ├── database.py
    ├── events
    │   ├── __init__.py
    │   ├── enums.py
    │   ├── models.py
    │   ├── routers.py
    │   ├── serializers
    │   │   ├── __init__.py
    │   │   └── validators.py
    │   └── services.py
    ├── extensions
    │   ├── __init__.py
    │   ├── dependencies.py
    │   └── models.py
    └── predictions
        ├── __init__.py
        ├── enums.py
        ├── models.py
        ├── routers.py
        ├── serializers
        │   └── __init__.py
        └── services.py
```
