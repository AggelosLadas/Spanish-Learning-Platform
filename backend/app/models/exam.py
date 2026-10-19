from sqlalchemy import Column, Integer, String, ForeignKey, JSON
from sqlalchemy.orm import relationship
from app.db.database import Base


class Exam(Base):
    __tablename__ = "exams"

    id = Column(Integer, primary_key=True, index=True)
    chapter_id = Column(Integer, ForeignKey("chapters.id"), nullable=False, unique=True)
    title = Column(String, nullable=False)
    passing_score_pct = Column(Integer, default=60)
    question_ids_json = Column(JSON, nullable=True)

    chapter = relationship("Chapter", back_populates="exam")
