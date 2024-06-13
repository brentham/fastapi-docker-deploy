from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, TIMESTAMP
from sqlalchemy.orm import relationship
from config.database import Base

# class Listings(Base):
#     __tablename__ = "listings"

#     id = Column (Integer, primary_key=True, index=True)
#     title = Column(String)
#     company = Column(String)
#     location = Column(String)
#     description = Column(String)
#     logo = Column(String)
#     tags = Column(String)
#     email = Column(String)
#     timestamp = Column(TIMESTAMP)
#     owner_id = Column(Integer, ForeignKey("users.id"))

#     owner = relationship("Users", back_populates="listings")