# models.py
from sqlalchemy import Integer, DateTime, Text
from sqlalchemy.orm import Mapped,mapped_column,relationship
from datetime import datetime
from packages.models.base import Base
class Thread(Base):
    __tablename__ = "threads"
    id:Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title:Mapped[str] = mapped_column(Text, nullable=False)
    created_at:Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    posts: Mapped[list["Post"]|None] = relationship("Post", order_by="Post.id", back_populates="thread", lazy="joined")

    def __init__(self, title:str):
        self.title = title

    
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "created_at": self.created_at,
        }