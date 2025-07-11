from pathlib import Path
from sqlalchemy import Engine
from sqlmodel import create_engine,Session
__engine: Engine | None = None


def get_engine() -> Engine:
    """
    Função para configurar a conexão ao banco de dados.
    """
    global __engine

    if __engine:
        return __engine

    arquivo_db = "db/my_chan_sql_model.db"
    folder = Path(arquivo_db).parent
    folder.mkdir(parents=True, exist_ok=True)

    conn_str = f"sqlite:///{arquivo_db}"
    __engine = create_engine(
        url=conn_str, echo=True, connect_args={"check_same_thread": False}
    )
    return __engine

def create_session() -> Session:
    """
    Função para criar uma sessão de banco de dados.
    """

    engine = get_engine()
    return Session(engine)  

def create_tables():
    """
    Função para criar as tabelas no banco de dados.
    """
    from sqlmodel import SQLModel
    from packages.models.post import Post
    from packages.models.thread import Thread

    engine = get_engine()
    SQLModel.metadata.create_all(engine)

        