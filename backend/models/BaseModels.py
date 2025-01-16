from sqlalchemy.orm                 import sessionmaker
from typing                         import Coroutine, Any
from sqlalchemy.ext.declarative     import declarative_base
from sqlalchemy.ext.asyncio         import create_async_engine, AsyncEngine, AsyncSession


_Base = declarative_base()
class CBase(_Base): 
    __abstract__ = True 


    def __init__(self) -> None:
        self.m_sSqliteDatabase: str = "sqlite+aiosqlite:///database/app.db"
        self.m_Engine: AsyncEngine = create_async_engine(self.m_sSqliteDatabase, echo=False)
        self.m_Session: sessionmaker = sessionmaker(self.m_Engine, class_ = AsyncSession, expire_on_commit = False)

    def GetEngine(self) -> Any:
        return self.m_Engine

    def GetSession(self) -> sessionmaker:
        return self.m_Session()    

    @classmethod
    def Create(cls, func) -> Coroutine:
        async def wrapper(self, *args, **kwargs):
            async with self.GetSession() as _session:
                return await func(self, _session, *args, **kwargs)
        return wrapper

    @classmethod
    def Read(cls, func) -> Coroutine:
        async def wrapper(self, *args, **kwargs):
            async with self.GetSession() as _session:
                return await func(self, _session, *args, **kwargs)
        return wrapper

    @classmethod
    def Update(cls, func) -> Coroutine:
        async def wrapper(self, nID: int, *args, **kwargs):
            async with self.GetSession() as _session:
                return await func(self, nID, _session, *args, **kwargs)
        return wrapper

    @classmethod
    def Delete(cls, func) -> Coroutine:
        async def wrapper(self, nID: int, *args, **kwargs):
            async with self.GetSession() as _session:
                return await func(self, nID, _session, *args, **kwargs)
        return wrapper

    @classmethod
    def GetObject(cls, func) -> Coroutine:
        async def wrapper(self, _field: any, _value: any, *args, **kwargs):
            async with self.GetSession() as _session:
                return await func(self, _field, _value, _session, *args, **kwargs)
        return wrapper

    @classmethod
    def GetObjectID(cls, func) -> Coroutine:
        async def wrapper(self, nID: int, *args, **kwargs):
            async with self.GetSession() as _session:
                return await func(self, nID, _session, *args, **kwargs)
        return wrapper

