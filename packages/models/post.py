from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column , relationship
from sqlalchemy import ForeignKey,func
from packages.models.base import Base

class Post(Base):
    __tablename__ = "posts"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    thread_id: Mapped[int] = mapped_column(ForeignKey("threads.id"))
    content: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now,server_default=func.now())
    thread: Mapped["Thread"] = relationship("Thread", back_populates="posts", lazy="joined")


    def __init__(self,thread_id:int,content:str):
        self.thread_id = thread_id
        self.content = content

    def to_dict(self) -> dict:
        return {
            "content": self.content,
            "created_at": self.created_at
        }