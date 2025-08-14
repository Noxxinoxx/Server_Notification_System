from typing import Union
from fastapi import FastAPI
from routes.router_notification import Notification_Router

app = FastAPI()

Noti_router = Notification_Router(app)
