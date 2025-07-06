import logging

from sqlalchemy.orm import Session
from packages.models.thread import Thread
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

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
        
        count_registry =  self._session.query(Thread).count()
        data = self._session.query(Thread).offset((page_number - 1) * quantity).limit(quantity).all()   
        return {
            "page": page_number,
            "total_pages": (count_registry + quantity - 1) // quantity,
            "threads": [thread.to_dict() for thread in data]
        }

    def get_by_id(self, thread_id: int) -> dict:
        return self._session.query(Thread).filter(Thread.id == thread_id).first().to_dict()


class AsyncThreadRepository:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def create(self, thread_data: Thread) -> dict:
        try:
            self._session.add(thread_data)
            await self._session.commit()
            await self._session.refresh(thread_data)
            return thread_data.to_dict()
        except Exception as e:
            logging.error("An error occurred while trying to create a thread", exc_info=True)
            await self._session.rollback()

    async def get_all(self, page_number: int, quantity: int) -> dict:
        # Conta o total de registros
        total_result = await self._session.execute(select(Thread))
        count_registry = len(total_result.unique().scalars().all())

        # Busca os threads paginados
        result = await self._session.execute(
            select(Thread)
            .offset((page_number - 1) * quantity)
            .limit(quantity)
        )
        data = result.unique().scalars().all()
        return {
            "page": page_number,
            "total_pages": (count_registry + quantity - 1) // quantity,
            "threads": [thread.to_dict() for thread in data]
        }

    async def get_by_id(self, thread_id: int) -> dict:
        result = await self._session.execute(
            select(Thread).where(Thread.id == thread_id)
        )
        thread = result.unique().scalar_one_or_none()
        if thread:
            return thread.to_dict()
        return None