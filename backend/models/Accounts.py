from sqlalchemy     import Column, Integer, Text, select, update, delete
from .BaseModels    import CBase


class CAccounts(CBase):
    __tablename__ = "Accounts"

    ID          = Column(Integer, nullable=True, unique=True, primary_key=True, autoincrement=True)
    School      = Column(Text, nullable=True)
    Class       = Column(Text, nullable=True)
    Fullname    = Column(Text, nullable=True)
    Login       = Column(Text, nullable=True)
    Passhash    = Column(Text, nullable=True)


    @CBase.Create
    async def Create(self, _session) -> int: 
        _session.add(self)
        await _session.commit()
        return self.ID
    
    @CBase.Read
    async def Read(self, _session): 
        sQuery = select(CAccounts)
        anyResult = await _session.execute(sQuery)
        return anyResult.scalars().all()

    @CBase.Update
    async def Update(self, nID: int, _session):
        sQuery = (
            update(CAccounts)
            .where(CAccounts.ID == nID)
            .values(
                School      = self.School,
                Class       = self.Class,
                Fullname    = self.Fullname,
                Login       = self.Login,
                Passhash    = self.Passhash,
            )
        )   

        await _session.execute(sQuery)
        await _session.commit()

    @CBase.Delete
    async def Delete(self, nID: int, _session):
        sQuery = (
            delete(CAccounts)
            .where(CAccounts.ID == nID)
        )

        await _session.execute(sQuery)
        await _session.commit()

    @CBase.GetObject
    async def GetObject(self, _field: any, _value: any, _session):
        sQuery = select(CAccounts).filter(_field == _value)
        anyResult = await _session.execute(sQuery)
        return anyResult.scalars()

    @CBase.GetObjectID
    async def GetObjectID(self, nID: int, _session):
        sQuery = select(CAccounts).filter(CAccounts.ID == nID)
        anyResult = await _session.execute(sQuery)
        return anyResult.scalars().first()
    