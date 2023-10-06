from typing import Any, List, Dict
from json import load

from .db import conn


def loadfile(file_dir: str):
    with open(file_dir) as f:
        data = load(f)
        return data


def seed_statuses(cursor):
    file_loc = "app/database/seeds/statuses.json"
    data: List[Dict(str, Any)] = loadfile(file_loc)
    values = ""
    for v in data:
        values += f"('{v['status']}', '{v['code']}'),"

    exc_script = f"INSERT INTO statuses(status, code) VALUES{values[:-1]}"
    cursor.execute(exc_script)


def seed_priorities(cursor):
    file_loc = "app/database/seeds/priorities.json"
    data: List[Dict(str, Any)] = loadfile(file_loc)
    values = ""
    for v in data:
        values += f"('{v['priority']}', '{v['code']}'),"

    exc_script = f"INSERT INTO priorities(priority, code) VALUES{values[:-1]}"
    cursor.execute(exc_script)


def run():
    cursor = conn.cursor()
    seed_statuses(cursor)
    seed_priorities(cursor)
    conn.commit()
    conn.close()
