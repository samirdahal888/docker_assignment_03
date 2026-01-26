import time

import psycopg2
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()
app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]
)


class Todo(BaseModel):
    task: str


def get_db():
    return psycopg2.connect(
        host="database", database="tododb", user="todouser", password="todopass"
    )


@app.on_event("startup")
def startup():
    time.sleep(3)
    conn = get_db()
    conn.cursor().execute(
        "CREATE TABLE IF NOT EXISTS todos (id SERIAL PRIMARY KEY, task TEXT)"
    )
    conn.commit()
    conn.close()


@app.get("/api/todos")
def get_todos():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT id, task FROM todos")
    todos = [{"id": r[0], "task": r[1]} for r in cur.fetchall()]
    conn.close()
    return todos


@app.post("/api/todos")
def add_todo(todo: Todo):
    conn = get_db()
    conn.cursor().execute("INSERT INTO todos (task) VALUES (%s)", (todo.task,))
    conn.commit()
    conn.close()
    return {"msg": "added"}


@app.delete("/api/todos/{id}")
def delete_todo(id: int):
    conn = get_db()
    conn.cursor().execute("DELETE FROM todos WHERE id=%s", (id,))
    conn.commit()
    conn.close()
    return {"msg": "deleted"}
