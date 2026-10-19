"""
Add YouTube video section to chapter 4 (Η Οικογένεια) in an existing database.
Run: python -m app.db.add_chapter4_family_video
"""
from app.db.database import SessionLocal
from app.models.chapter import Chapter
from app.models.section import Section

VIDEO_URL = "https://www.youtube.com/watch?v=3Odc-nGvKzM"
VIDEO_CONTENT = {
    "title": "Βίντεο: Η Οικογένεια",
    "youtube_url": VIDEO_URL,
    "description": "Δες και άκουσε τα μέλη της οικογένειας στα Ισπανικά πριν συνεχίσεις με το λεξιλόγιο.",
}


def add_video():
    db = SessionLocal()

    chapter = db.query(Chapter).filter(Chapter.order_index == 4).first()
    if not chapter:
        print("Chapter 4 (Η Οικογένεια) not found. Run seed first.")
        db.close()
        return

    existing = (
        db.query(Section)
        .filter(
            Section.chapter_id == chapter.id,
            Section.type == "video",
        )
        .first()
    )
    if existing:
        print("Video section already exists for chapter 4. Skipping.")
        db.close()
        return

    sections = (
        db.query(Section)
        .filter(Section.chapter_id == chapter.id, Section.order_index >= 2)
        .order_by(Section.order_index.desc())
        .all()
    )
    for section in sections:
        section.order_index += 1

    video = Section(
        chapter_id=chapter.id,
        order_index=2,
        type="video",
        content_json=VIDEO_CONTENT,
    )
    db.add(video)
    db.commit()
    db.close()
    print("Video section added to chapter 4 (Η Οικογένεια).")


if __name__ == "__main__":
    add_video()
