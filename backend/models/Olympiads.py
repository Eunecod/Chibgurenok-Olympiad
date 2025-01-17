from sqlalchemy     import Column, Integer, Text, select, ForeignKey
from sqlalchemy.orm import relationship, selectinload
from .BaseModels    import CBase


class COlympiads(CBase):
    __tablename__ = "Olympiads"

    ID              = Column(Integer, nullable=True, unique=True, primary_key=True, autoincrement=True)
    Discipline      = Column(Integer, ForeignKey('Disciplines.ID'), nullable=True)
    Passage_Time    = Column(Integer, nullable=True)
    Access_Date     = Column(Integer, nullable=True)
    Quiz            = Column(Integer, ForeignKey('Quizzes.ID'), nullable=True)
    Title           = Column(Text, nullable=True)
    Describe        = Column(Text, nullable=True)
    Path_Preview    = Column(Text, nullable=True)
    Document        = Column(Text, nullable=True)

    __discipline_relation   = relationship("CDisciplines", backref="Olympiad_Discipline")
    __quiz_relation         = relationship("CQuizzes", backref="Olympiad_Quiz")


    def GetDiscipline(self):
        return self.__discipline_relation

    def GetQuiz(self):
        return self.__quiz_relation

    @CBase.Create
    async def Create(self, _session): 
        _session.add(self)
        await _session.commit()
        return self.ID
    
    @CBase.Read
    async def Read(self, _session): 
        sQuery = select(COlympiads).options(selectinload(COlympiads.__discipline_relation), selectinload(COlympiads.__quiz_relation))
        anyResult = await _session.execute(sQuery)
        return anyResult.scalars().all()
    
    @CBase.GetObject
    async def GetObject(self, _field: any, _value: any, _session):
        sQuery = select(COlympiads).filter(_field == _value).options(selectinload(COlympiads.__discipline_relation), selectinload(COlympiads.__quiz_relation))
        anyResult = await _session.execute(sQuery)
        return anyResult.scalars()

    @CBase.GetObjectID
    async def GetObjectID(self, nID: int, _session):
        sQuery = select(COlympiads).filter(COlympiads.ID == nID).options(selectinload(COlympiads.__discipline_relation), selectinload(COlympiads.__quiz_relation))
        anyResult = await _session.execute(sQuery)
        return anyResult.scalars().first()
    