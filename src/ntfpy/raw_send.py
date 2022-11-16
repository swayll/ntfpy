import requests
import base64

__all__ = [
    "raw_send"
]

def raw_send(server, topic, message, auth = None, title = None, priority = None, tags = None, click = None, attach = None, actions = None, email = None, delay = None):
    headers = {}
    if auth is not None:
        auth_bytes = auth.encode("ascii")
        b64_bytes = base64.b64encode(auth_bytes)
        b64_s = b64_bytes.decode("ascii")
        headers["Authorization"] = f"Basic {b64_s}"
    if title is not None:
        headers["Title"] = title
    if priority is not None:
        headers["Priority"] = priority
    if tags is not None:
        headers["Tags"] = tags
    if click is not None:
        headers["Click"] = click
    if attach is not None:
        headers["Attach"] = attach
    if actions is not None:
        headers["Actions"] = actions
    if email is not None:
        headers["Email"] = email
    if delay is not None:
        headers["Delay"] = delay
    r = requests.post(f"{server}/{topic}", headers = headers, data = message)
