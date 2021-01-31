import secrets
import socket
from typing import List, Optional

from fastapi import FastAPI
from pydantic import BaseModel
from rich.console import Console

# Constants
WHOIS_ENCODING = "utf-8"

console = Console()
app = FastAPI()


class Query(BaseModel):
    inverse: Optional[str]
    types: Optional[str]
    value: str


def whois(server: str, query: str) -> List[dict]:
    s: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    console.log(f"Connecting to {server}")
    s.connect((server, 43))
    console.log(f"Connected to {server}")

    try:
        console.log(f"whois -h {server} {query}")
        s.sendall((query + "\n").encode(WHOIS_ENCODING))

        buffer: bytes = b""
        while True:
            part: bytes = s.recv(8)
            buffer += part
            if len(part) == 0:
                break

        # List of objects to return
        _objects: List[dict] = []

        objects = buffer.decode(WHOIS_ENCODING).strip().split("\n\n")
        if len(objects) == 0 or "No entries found" in objects[0]:
            return []  # No objects found

        for obj in objects:
            new_object = {}
            object_maintainers = []
            attributes = obj.split("\n")
            for attr in attributes:
                attr = attr.split(": ")
                k = attr[0]
                v = attr[1].lstrip(" ")
                new_object[k] = v
                if k == "mnt-by":
                    object_maintainers.append(v)
            new_object["custom-maintainers"] = ",".join(object_maintainers)
            new_object["custom-primary-key"] = new_object[next(iter(new_object))]
            new_object["custom-object-type"] = next(iter(new_object))
            new_object["id"] = secrets.token_hex(16)
            _objects.append(new_object)
    finally:
        s.close()

    return _objects


@app.post("/query")
async def run_query(query: Query):
    query_str: str = ""
    if query.types:
        query_str += f"-T {query.types} "
    if query.inverse:
        query_str += f"-i {query.inverse} {query.value}"

    return whois("whois.radb.net", query_str.strip(" "))
