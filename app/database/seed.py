# from db import conn
from typing import Any, List, Dict

from json import load


def loadfile(file_dir: str):
    with open(file_dir) as f:
        data = load(f)
        return data


def seed_statuses():
    file_loc = "./seeds/statuses.json"
    data: List[Dict(str, Any)] = loadfile(file_loc)
    values = ""
    for v in data:
        values += f"({v['status']}, {v['code']}),"

    exc_script = f"INSERT INTO statuses(status, code) VALUES{values[:-1]}"

    # c = conn.cursor()

    # c.execute("INSERT INTO ")



if __name__ == "__main__":
    seed_statuses()


