from data.repositories.thread_repository import ThreadRepository
from config.config import create_session
from packages.models.thread import Thread


class ThreadService:

    @classmethod
    def create_thread(cls, thread_data: Thread) -> None:
        if thread_data.title in ("", None):
            raise ValueError("title can't be empty or null!")
        with create_session() as session:
            repo = ThreadRepository(session)
            return repo.create(thread_data)

    @classmethod
    def get_all_threads(cls, page_number: int, quantity: int) -> dict:
        with create_session() as session:
            repo = ThreadRepository(session)
            return repo.get_all(page_number, quantity)

    @classmethod
    def get_thread_by_id(cls, thread_id: int) -> dict:
        with create_session() as session:
            repo = ThreadRepository(session)
            return repo.get_by_id(thread_id)
