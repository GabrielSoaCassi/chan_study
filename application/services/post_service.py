from data.repositories.post_repository import AsyncPostRepository, PostRepository
from config.config import create_session,create_async_session
from packages.models.post import Post


class PostService:
    def __init__(self):
        self.session = create_session()
        self.repo = PostRepository(self.session)

    def create_post(self, post_data: dict) -> Post:
        if post_data.get("content", None) in ("", None):
            raise ValueError("Contet can't be empty or null!")
        if post_data.get("thread_id", None) in (0, None):
            raise ValueError("Thread id not found on request!")
        return self.repo.add(Post(post_data.get("thread_id"), post_data.get("content")))

    def get_posts(self, thread_id: int, page_number: int, quantity: int) -> dict:
        return self.repo.get_posts(thread_id, page_number, quantity)

class AsyncPostService:
    def __init__(self):
        self.session = create_async_session()
        self.repo = AsyncPostRepository(self.session)

    async def create_post(self, post_data: dict) -> Post:
        if post_data.get("content", None) in ("", None):
            raise ValueError("Content can't be empty or null!")
        if post_data.get("thread_id", None) in (0, None):
            raise ValueError("Thread id not found on request!")
        return await self.repo.add(Post(post_data.get("thread_id"), post_data.get("content")))

    async def get_posts(self, thread_id: int, page_number: int, quantity: int) -> dict:
        return await self.repo.get_posts(thread_id, page_number, quantity)