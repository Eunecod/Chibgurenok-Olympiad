from sqlalchemy     import Column, Integer, Text, select, update, ForeignKey
from sqlalchemy.orm import relationship, selectinload
from .BaseModels    import CBase


class CResults(CBase):
    __tablename__ = "Results"

    ID              = Column(Integer, nullable=True, unique=True, primary_key=True, autoincrement=True)
    Account_ID      = Column(Integer, ForeignKey('Accounts.ID'), nullable=True)
    Olympiad_ID     = Column(Integer, ForeignKey('Olympiads.ID'), nullable=True)
    Assessed        = Column(Integer, nullable=True)
    Reply_Body      = Column(Text, nullable=True)

    __account_relation  = relationship("CAccounts",     backref="Account_Result")
    __olympiad_relation = relationship("COlympiads",    backref="Olympiad__Result")


    def GetAccount(self):
        return self.__account_relation

    def GetOlympiad(self):
        return self.__olympiad_relation

    @CBase.Create
    async def Create(self, _session): 
        _session.add(self)
        await _session.commit()

    @CBase.Read
    async def Read(self, _session): 
        sQuery = select(CResults).options(selectinload(CResults.__olympiad_relation), selectinload(CResults.__account_relation))
        anyResult = await _session.execute(sQuery)
        return anyResult.scalars().all()

    @CBase.Update
    async def Update(self, nID: int, _session):
        UpdateField: dict = {}

        if self.Account_ID is not None:
            UpdateField['Account_ID'] = self.Account_ID
        if self.Olympiad_ID is not None:
            UpdateField['Olympiad_ID'] = self.Olympiad_ID
        if self.Assessed is not None:
            UpdateField['Assessed'] = self.Assessed
        if self.Reply_Body is not None:
            UpdateField['Reply_Body'] = self.Reply_Body

        sQuery = update(CResults).where(CResults.ID == nID).values(**UpdateField)
        await _session.execute(sQuery)
        await _session.commit()

    @CBase.GetObject
    async def GetObject(self, _field: any, _value: any, _session):
        sQuery = select(CResults).filter(_field == _value).options(selectinload(CResults.__olympiad_relation), selectinload(CResults.__account_relation))
        anyResult = await _session.execute(sQuery)
        return anyResult.scalars()

    @CBase.GetObjectID
    async def GetObjectID(self, nID: int, _session):
        sQuery = select(CResults).filter(CResults.ID == nID).options(selectinload(CResults.__olympiad_relation), selectinload(CResults.__account_relation))
        anyResult = await _session.execute(sQuery)
        return anyResult.scalars().first()
