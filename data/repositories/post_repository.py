import logging

from sqlmodel import Session, func,select
from packages.models.post import Post
logging.basicConfig(level=logging.INFO)


class PostRepository:
    def __init__(self, session: Session):
        self._session = session

    def add(self, post_data: Post) -> None:
        try:
            self._session.add(post_data)
            self._session.commit()
            self._session.refresh(post_data)
        except Exception as e:
            logging.error(
                "An error occur while trying add post to thread", exc_info=True
            )
            self._session.rollback()

    def get_posts(self, thread_id: int, page_number: int, quantity: int) -> dict:
        statement = select(Post).where(Post.thread_id == thread_id)
        result = self._session.exec(statement)
        posts = result.all()
        #conta o total de registros
        count_stmt = select(func.count()).select_from(Post).where(Post.thread_id == thread_id)
        count_result = self._session.exec(count_stmt)
        total = count_result.one()
        return {
            "page": page_number,
            "total_pages": (total + quantity - 1) // quantity,
            "posts": [post.to_dict() for post in posts],
        }