from sqlalchemy     import Column, Integer, Text, select
from .BaseModels    import CBase


class CDisciplines(CBase):
    __tablename__ = "Disciplines"

    ID          = Column(Integer, nullable=True, unique=True, primary_key=True, autoincrement=True)
    Subject     = Column(Text, nullable=True)
    Level       = Column(Text, nullable=True)


    @CBase.Create
    async def Create(self, _session): 
        _session.add(self)
        await _session.commit()
        return self.ID
    
    @CBase.Read
    async def Read(self, _session): 
        sQuery = select(CDisciplines)
        anyResult = await _session.execute(sQuery)
        return anyResult.scalars().all()

    @CBase.GetObjectID
    async def GetObjectID(self, nID: int, _session):
        sQuery = select(CDisciplines).filter(CDisciplines.ID == nID)
        anyResult = await _session.execute(sQuery)
        return anyResult.scalars().first()
