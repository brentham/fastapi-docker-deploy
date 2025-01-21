from sqlalchemy import Column, Integer, String, Boolean
from config.database import Base

class EventType(Base):
    __tablename__ = "vmEventType"

    EventType_ID = Column (Integer, primary_key=True, index=True)
    EventType_Name = Column(String, nullable=True)
    SendMail = Column(Boolean, nullable=True, default=False)
    CreateTicket = Column (Boolean, nullable=True)