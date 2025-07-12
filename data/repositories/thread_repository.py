import logging
from sqlmodel import Session, func,select
from packages.models.thread import Thread

logging.basicConfig(level=logging.INFO)

class ThreadRepository:
    def __init__(self,session:Session):
        self._session =session
    
    def create(self,thread_data:Thread) -> None:
        try:
            self._session.add(thread_data)
            self._session.commit()
            self._session.refresh(thread_data)
        except Exception as e:
            logging.error("An error occur while trying create a thread",exc_info=True)
            self._session.rollback()

    def get_all(self,page_number:int,quantity:int) -> dict:
        # Busca os dados paginados
        statement = select(Thread).offset((page_number - 1) * quantity).limit(quantity)
        result = self._session.exec(statement)
        data = result.all()

        # Conta o total de registros
        count_stmt = select(func.count()).select_from(Thread)
        count_result = self._session.exec(count_stmt)
        total = count_result.one()
        return {
            "page": page_number,
            "total_pages": (total + quantity - 1) // quantity,
            "threads": [thread.to_dict() for thread in data]
        }

    def get_by_id(self, thread_id: int) -> dict|None:
        statement = select(Thread).where(Thread.id == thread_id)
        result = self._session.exec(statement)
        return result.one_or_none().to_dict() if result else None
