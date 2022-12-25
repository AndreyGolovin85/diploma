from dataclasses import field
from typing import List, Optional

import marshmallow_dataclass
from marshmallow_dataclass import dataclass
from marshmallow import EXCLUDE


@dataclass
class MessageFrom:
    id: int
    is_bot: bool
    first_name: Optional[str]
    last_name:  Optional[str]
    username: Optional[str]

    class Meta:
        unknown = EXCLUDE


@dataclass
class MessageChat:
    id: int
    username: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    type: str
    title: Optional[str]

    class Meta:
        unknown = EXCLUDE


@dataclass
class Message:
    message_id: int
    from_: MessageFrom = field(metadata={'data_key': 'from'})
    chat: MessageChat
    date: int
    text: Optional[str]

    class Meta:
        unknown = EXCLUDE


@dataclass
class UpdateOdj:
    update_id: int
    message: Message

    class Meta:
        unknown = EXCLUDE


@dataclass
class GetUpdatesResponse:
    ok: bool
    result: List[UpdateOdj]

    class Meta:
        unknown = EXCLUDE


@dataclass
class SendMessageResponse:
    ok: bool
    result: Message

    class Meta:
        unknown = EXCLUDE


GET_UPDATES_RESPONSE_SCHEMA = marshmallow_dataclass.class_schema(GetUpdatesResponse)()
SEND_MESSAGE_RESPONSE_SCHEMA = marshmallow_dataclass.class_schema(SendMessageResponse)()
