from sqlalchemy     import Column, Integer, Text, select, update
from .BaseModels    import CBase


class CMailbox(CBase):
    __tablename__ = "Mailbox"

    ID          = Column(Integer, nullable=True, unique=True, primary_key=True, autoincrement=True)
    Name        = Column(Text, nullable=True)
    Email       = Column(Text, nullable=True)
    Message     = Column(Text, nullable=True)
    IsRead      = Column(Integer, nullable=True, default=0)


    @CBase.Create
    async def Create(self, _session): 
        _session.add(self)
        await _session.commit()

    @CBase.Read
    async def Read(self, _session): 
        sQuery = select(CMailbox)
        anyResult = await _session.execute(sQuery)
        return anyResult.scalars().all()

    @CBase.Update
    async def Update(self, nID: int, _session):
        UpdateField: dict = {}

        if self.Name is not None:
            UpdateField['Name'] = self.Name
        if self.Email is not None:
            UpdateField['Email'] = self.Email
        if self.Message is not None:
            UpdateField['Message'] = self.Message
        if self.IsRead is not None:
            UpdateField['IsRead'] = self.IsRead

        sQuery = update(CMailbox).where(CMailbox.ID == nID).values(**UpdateField)
        await _session.execute(sQuery)
        await _session.commit()

    @CBase.GetObject
    async def GetObject(self, _field: any, _value: any, _session):
        sQuery = select(CMailbox).filter(_field == _value)
        anyResult = await _session.execute(sQuery)
        return anyResult.scalars()

    @CBase.GetObjectID
    async def GetObjectID(self, nID: int, _session):
        sQuery = select(CMailbox).filter(CMailbox.ID == nID)
        anyResult = await _session.execute(sQuery)
        return anyResult.scalars().first()
