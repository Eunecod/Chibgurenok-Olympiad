from sqlalchemy     import Column, Integer, Text
from .BaseModels    import CBase


class CMailbox(CBase):
    __tablename__ = "Mailbox"

    ID          = Column(Integer, nullable=True, unique=True, primary_key=True, autoincrement=True)
    Name        = Column(Text, nullable=True)
    Email       = Column(Text, nullable=True)
    Message     = Column(Text, nullable=True)
    IsRead      = Column(Integer, nullable=True, default=0)
    