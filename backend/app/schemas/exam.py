from pydantic import BaseModel


class QuestionOut(BaseModel):
    id: int
    chapter_id: int
    type: str
    prompt: str
    options_json: dict | list | None = None
    correct_answer: str
    explanation: str | None = None
    points: int

    class Config:
        from_attributes = True


class ExamOut(BaseModel):
    id: int
    chapter_id: int
    title: str
    passing_score_pct: int
    questions: list[QuestionOut] = []

    class Config:
        from_attributes = True
