from dataclasses import dataclass
from datetime import datetime


@dataclass
class TgMessage:
    username: str
    text: str
    time: datetime
