from pydantic import BaseModel

class EventType(BaseModel):

    EventType_ID: int
    EventType_Name: str | None = None
    SendMail: bool | None = None
    CreateTicket: bool | None = None