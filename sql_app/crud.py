from sqlalchemy.orm import Session
from . import models, schemas


# ユーザー情報取得
def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


# イベント情報取得
def get_events(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Event).offset(skip).limit(limit).all()


# ユーザー登録
def create_user(db: Session, user: schemas.User):
    db_user = models.User(user_name=user.user_name,
                          user_pass=user.password_hash,
                          user_email=user.email,
                          user_image=user.profile_image_path,
                          user_birthday=user.birthday)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# イベント登録
def create_event(db: Session, event: schemas.Event):
    db_event = models.event(event_name=event.event_name,
                            event_description=event.description,
                            event_begin_date=event.begin_date,
                            event_is_allday=event.is_all_day,
                            event_end_date=event.end_date,
                            event_created_at=event.created_at,
                            event_updated_at=event.updated_at,
                            event_deleted_at=event.deleted_at,
                            event_color=event.color)

    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event
