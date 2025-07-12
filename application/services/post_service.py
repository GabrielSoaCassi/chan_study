from data.repositories.post_repository import PostRepository
from config.config import create_session
from packages.models.post import Post


class PostService:

    @classmethod
    def create_post(cls, post_data: dict) -> Post:
        if post_data.get("content", None) in ("", None):
            raise ValueError("Contet can't be empty or null!")
        if post_data.get("thread_id", None) in (0, None):
            raise ValueError("Thread id not found on request!")
        with create_session() as session:
            repo = PostRepository(session)
            repo.add(Post(post_data.get("thread_id"), post_data.get("content")))

    @classmethod
    def get_posts(cls, thread_id: int, page_number: int, quantity: int) -> dict:
        with create_session() as session:
            repo = PostRepository(session)
            return repo.get_posts(thread_id, page_number, quantity)