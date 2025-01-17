from sqlalchemy     import Column, Integer, select, ForeignKey
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

    @CBase.GetObject
    async def GetObject(self, _field: any, _value: any, _session):
        sQuery = select(CSession).filter(_field == _value)
        anyResult = await _session.execute(sQuery)
        return anyResult.scalars()
    