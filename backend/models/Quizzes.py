from sqlalchemy     import Column, Integer, Text, select
from .BaseModels    import CBase


class CQuizzes(CBase):
    __tablename__ = "Quizzes"

    ID              = Column(Integer, nullable=True, unique=True, primary_key=True, autoincrement=True)
    Quiz_Body       = Column(Text, nullable=True)
    Quiz_Reply      = Column(Text, nullable=True)


    @CBase.Create
    async def Create(self, _session) -> int: 
        _session.add(self)
        await _session.commit()
        return self.ID

    @CBase.Read
    async def Read(self, _session): 
        sQuery = select(CQuizzes)
        anyResult = await _session.execute(sQuery)
        return anyResult.scalars().all()

    @CBase.GetObjectID
    async def GetObjectID(self, nID: int, _session):
        sQuery = select(CQuizzes).filter(CQuizzes.ID == nID)
        anyResult = await _session.execute(sQuery)
        return anyResult.scalars().first()
