from sqlalchemy import Column, Integer, String, ForeignKey, JSON
from sqlalchemy.orm import relationship
from app.db.database import Base


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    chapter_id = Column(Integer, ForeignKey("chapters.id"), nullable=False)
    type = Column(String, nullable=False)  # "multiple_choice", "fill_blank", "translation", "match", "true_false"
    prompt = Column(String, nullable=False)
    options_json = Column(JSON, nullable=True)
    correct_answer = Column(String, nullable=False)
    explanation = Column(String, nullable=True)
    points = Column(Integer, default=1)

    chapter = relationship("Chapter", back_populates="questions")
