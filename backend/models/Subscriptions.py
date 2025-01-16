from sqlalchemy     import Column, Integer, select, ForeignKey
from sqlalchemy.orm import relationship, selectinload
from .BaseModels    import CBase


class CSubscriptions(CBase):
    __tablename__ = "Subscriptions"

    ID              = Column(Integer, nullable=True, unique=True, primary_key=True, autoincrement=True)
    Account_ID      = Column(Integer, ForeignKey('Accounts.ID'), nullable=True)
    Olympiad_ID     = Column(Integer, ForeignKey('Olympiads.ID'), nullable=True)

    __account_relation  = relationship("CAccounts",     backref="Account_Subscription")
    __olympiad_relation = relationship("COlympiads",    backref="Olympiads_Subscription")


    @CBase.Create
    async def Create(self, _session): 
        _session.add(self)
        await _session.commit()
    
    @CBase.Read
    async def Read(self, _session): 
        sQuery = select(CSubscriptions).options(selectinload(CSubscriptions.__olympiad_relation), selectinload(CSubscriptions.__account_relation))
        anyResult = await _session.execute(sQuery)
        return anyResult.scalars().all()

    @CBase.GetObject
    async def GetObject(self, _field: any, _value: any, _session):
        sQuery = select(CSubscriptions).filter(_field == _value).options(selectinload(CSubscriptions.__olympiad_relation), selectinload(CSubscriptions.__account_relation))
        anyResult = await _session.execute(sQuery)
        return anyResult.scalars()

    @CBase.GetObjectID
    async def GetObjectID(self, nID: int, _session):
        sQuery = select(CSubscriptions).filter(CSubscriptions.ID == nID).options(selectinload(CSubscriptions.__olympiad_relation), selectinload(CSubscriptions.__account_relation))
        anyResult = await _session.execute(sQuery)
        return anyResult.scalars().first()
