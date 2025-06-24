import logging

from sqlalchemy.orm import Session
from packages.models.post import Post
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
        
        count_registry =  self._session.query(Thread).count()
        data = self._session.query(Thread).offset((page_number - 1) * quantity).limit(quantity).all()   
        return {
            "page": page_number,
            "total_pages": (count_registry + quantity - 1) // quantity,
            "threads": [thread.to_dict() for thread in data]
        }

    def get_by_id(self, thread_id: int) -> dict:
        return self._session.query(Thread).filter(Thread.id == thread_id).first().to_dict()

