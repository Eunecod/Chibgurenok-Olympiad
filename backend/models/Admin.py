from sqlalchemy     import Column, Integer, Text, select
from .BaseModels    import CBase


class CAdmin(CBase):
    __tablename__ = "Admin"

    ID          = Column(Integer, nullable=True, unique=True, primary_key=True, autoincrement=True)
    Fullname    = Column(Text, nullable=True)
    Login       = Column(Text, nullable=True)
    Passhash    = Column(Text, nullable=True)
    Key         = Column(Text, nullable=True)
    Active      = Column(Text, nullable=True, default=1)


    @CBase.Create
    async def Create(self, _session) -> int: 
        _session.add(self)
        await _session.commit()
        return self.ID

    @CBase.GetObject
    async def GetObject(self, _field: any, _value: any, _session):
        sQuery = select(CAdmin).filter(_field == _value)
        anyResult = await _session.execute(sQuery)
        return anyResult.scalars()
    