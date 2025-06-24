import logging

from sqlalchemy.orm import Session
from packages.models.post import Post

logging.basicConfig(level=logging.INFO)

class PostRepository:
    def __init__(self,session:Session):
        self._session =session
    
    def add(self,post_data:Post) -> None:
        try:
            self._session.add(post_data)
            self._session.commit()
            self._session.refresh(post_data)
        except Exception as e:
            logging.error("An error occur while trying add post to thread",exc_info=True)
            self._session.rollback()

    def get_posts(self, thread_id: int, page_number: int, quantity: int) -> dict:
        count_registry = self._session.query(Post).filter(Post.thread_id == thread_id).count()
        posts = self._session.query(Post).filter(Post.thread_id == thread_id).offset((page_number - 1) * quantity).limit(quantity).all()
        return {
            "page": page_number,
            "total_pages": (count_registry + quantity - 1) // quantity,
            "posts": [post.to_dict() for post in posts]
        }


