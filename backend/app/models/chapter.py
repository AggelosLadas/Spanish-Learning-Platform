from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.db.database import Base


class Chapter(Base):
    __tablename__ = "chapters"

    id = Column(Integer, primary_key=True, index=True)
    order_index = Column(Integer, nullable=False, unique=True)
    title_greek = Column(String, nullable=False)
    title_spanish = Column(String, nullable=False)
    difficulty_level = Column(String, nullable=False)  # "beginner", "elementary", "intermediate"
    is_published = Column(Boolean, default=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    sections = relationship("Section", back_populates="chapter", order_by="Section.order_index")
    questions = relationship("Question", back_populates="chapter")
    exam = relationship("Exam", back_populates="chapter", uselist=False)
