from data.repositories.thread_repository import AsyncThreadRepository, ThreadRepository
from config.config import create_session,create_async_session
from packages.models.thread import Thread


class ThreadService:
    def __init__(self):
        self.session = create_session()
        self.repo = ThreadRepository(self.session)
    
    def create_thread(self, thread_data: dict) -> None:
        if thread_data.get('title',None) in ("",None):
            raise ValueError("title can't be empty or null!")
        return self.repo.create(Thread(thread_data.get('title',None)))
    
    def get_all_threads(self,page_number:int,quantity:int) -> dict:
        return self.repo.get_all(page_number,quantity)
    
    def get_thread_by_id(self,thread_id:int) -> dict:
        return self.repo.get_by_id(thread_id)


class AsyncThreadService:
    def __init__(self):
        self.session = create_async_session()
        self.repo = AsyncThreadRepository(self.session)

    async def create_thread(self, thread_data: dict) -> None:
        if thread_data.get('title',None) in ("",None):
            raise ValueError("title can't be empty or null!")
        return await self.repo.create(Thread(thread_data.get('title',None)))
    
    async def get_all_threads(self,page_number:int,quantity:int) -> dict:
        return await self.repo.get_all(page_number,quantity)
    
    async def get_thread_by_id(self,thread_id:int) -> dict:
        return await self.repo.get_by_id(thread_id)