from data.repositories.post_repository import PostRepository
from config.config import create_session
from packages.models.post import Post


class PostService:

    @classmethod
    def create_post(cls, post_data: Post) -> Post:
        if post_data.content in ("", None):
            raise ValueError("Content can't be empty or null!")
        if post_data.thread_id in (0, None):
            raise ValueError("Thread id not found on request!")
        with create_session() as session:
            repo = PostRepository(session)
            repo.add(post_data)
            return post_data

    @classmethod
    def get_posts(cls, thread_id: int, page_number: int, quantity: int) -> dict:
        with create_session() as session:
            repo = PostRepository(session)
            return repo.get_posts(thread_id, page_number, quantity)