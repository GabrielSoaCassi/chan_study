import logging

from sqlalchemy.orm import Session
from packages.models.post import Post
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
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
        count_registry = (
            self._session.query(Post).filter(Post.thread_id == thread_id).count()
        )
        posts = (
            self._session.query(Post)
            .filter(Post.thread_id == thread_id)
            .offset((page_number - 1) * quantity)
            .limit(quantity)
            .all()
        )
        return {
            "page": page_number,
            "total_pages": (count_registry + quantity - 1) // quantity,
            "posts": [post.to_dict() for post in posts],
        }


class AsyncPostRepository:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def add(self, post_data: Post) -> dict:
        try:
            self._session.add(post_data)
            await self._session.commit()
            await self._session.refresh(post_data)
            return post_data.to_dict()
        except Exception as e:
            logging.error(
                "An error occur while trying add post to thread", exc_info=True
            )
            await self._session.rollback()

    async def get_posts(self, thread_id: int, page_number: int, quantity: int) -> dict:
        # Conta o total de registros
        total_result = await self._session.execute(
            select(Post).where(Post.thread_id == thread_id)
        )
        count_registry = len(total_result.unique().scalars().all())

        # Busca os posts paginados
        result = await self._session.execute(
            select(Post)
            .where(Post.thread_id == thread_id)
            .offset((page_number - 1) * quantity)
            .limit(quantity)
        )
        posts = result.unique().scalars().all()
        return {
            "page": page_number,
            "total_pages": (count_registry + quantity - 1) // quantity,
            "posts": [post.to_dict() for post in posts],
        }
