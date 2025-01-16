from .Accounts      import CAccounts
from .Admin         import CAdmin
from .BaseModels    import CBase
from .Disciplines   import CDisciplines
from .Mailbox       import CMailbox
from .Olympiads     import COlympiads
from .Quizzes       import CQuizzes
from .Results       import CResults
from .Session       import CSession
from .Subscriptions import CSubscriptions


async def InitBase() -> None:
    from .BaseModels import _Base
    Base: CBase = CBase()
    async with Base.GetEngine().begin() as conn:
        await conn.run_sync(_Base.metadata.create_all)

from asyncio import run
run(InitBase())

__all__ = [
    'CAccounts',
    'CAdmin',
    'CBase',
    'CDisciplines',
    'CMailbox',
    'COlympiads',
    'CQuizzes',
    'CResults',
    'CSession',
    'CSubscriptions'
]
