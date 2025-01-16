from sqlalchemy     import Column, Integer, select, update, ForeignKey
from .BaseModels    import CBase


class CSession(CBase):
    __tablename__ = "Session"

    ID              = Column(Integer, nullable=True, unique=True, primary_key=True, autoincrement=True)
    Account_ID      = Column(Integer, ForeignKey('Accounts.ID'), nullable=True)
    Olympiad_ID     = Column(Integer, ForeignKey('Olympiads.ID'), nullable=True)
    Start           = Column(Integer, nullable=True)
    End             = Column(Integer, nullable=True)


    @CBase.Create
    async def Create(self, _session): 
        _session.add(self)
        await _session.commit()

    @CBase.Read
    async def Read(self, _session): 
        sQuery = select(CSession)
        anyResult = await _session.execute(sQuery)
        return anyResult.scalars().all()

    @CBase.Update
    async def Update(self, nID: int, _session):
        UpdateField: dict = {}

        if self.Account_ID is not None:
            UpdateField['Account_ID'] = self.Account_ID
        if self.Olympiad_ID is not None:
            UpdateField['Olympiad_ID'] = self.Olympiad_ID
        if self.Start is not None:
            UpdateField['Start'] = self.Start
        if self.End is not None:
            UpdateField['End'] = self.End

        sQuery = update(CSession).where(CSession.ID == nID).values(**UpdateField)
        await _session.execute(sQuery)
        await _session.commit()

    @CBase.GetObject
    async def GetObject(self, _field: any, _value: any, _session):
        sQuery = select(CSession).filter(_field == _value)
        anyResult = await _session.execute(sQuery)
        return anyResult.scalars()

    @CBase.GetObjectID
    async def GetObjectID(self, nID: int, _session):
        sQuery = select(CSession).filter(CSession.ID == nID)
        anyResult = await _session.execute(sQuery)
        return anyResult.scalars().first()

