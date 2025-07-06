from pathlib import Path
from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine,async_sessionmaker
from packages.models.base import Base

__engine: Engine | None = None


def get_engine() -> Engine:
    """
    Função para configurar a conexão ao banco de dados.
    """
    global __engine

    if __engine:
        return __engine

    arquivo_db = "db/my_chan.db"
    folder = Path(arquivo_db).parent
    folder.mkdir(parents=True, exist_ok=True)

    conn_str = f"sqlite:///{arquivo_db}"
    __engine = create_engine(
        url=conn_str, echo=True, connect_args={"check_same_thread": False}
    )
    return __engine


def create_session() -> Session:
    """
    Função para criar sessão de conexao ao banco de dados.
    """

    if not __engine:
        get_engine()

    __session = sessionmaker(__engine, expire_on_commit=False, class_=Session)

    session: Session = __session()

    return session

def create_async_session() -> AsyncSession:
    """
    Função para criar sessão assíncrona de conexão ao banco de dados.
    """
    arquivo_db = "db/my_chan.db"
    conn_str = f"sqlite+aiosqlite:///{arquivo_db}"
    __async_session = async_sessionmaker(
        bind=create_async_engine(conn_str, echo=True),
        expire_on_commit=False,
        class_=AsyncSession
    )

    session: AsyncSession = __async_session()

    return session

def create_tables() -> None:
    engine = get_engine()
    import packages.models
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

async def create_async_tables() -> None:
    engine = create_async_engine("sqlite+aiosqlite:///db/my_chan.db", echo=True)
    async with engine.begin() as conn:
        import packages.models
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        