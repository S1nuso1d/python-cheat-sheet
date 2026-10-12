"""SQLAlchemy 2.0 + FastAPI: модель таблицы ≠ Pydantic-схема. Сессия через Depends."""

# pip install sqlalchemy alembic
# async: sqlalchemy[asyncio] + asyncpg  и  create_async_engine

from sqlalchemy import ForeignKey, String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, sessionmaker

# DATABASE_URL = "sqlite:///./app.db"          # файл
# DATABASE_URL = "postgresql+psycopg://user:pass@localhost:5432/app"


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    tasks: Mapped[list["Task"]] = relationship(back_populates="owner")


class Task(Base):
    __tablename__ = "tasks"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200))
    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    owner: Mapped[User] = relationship(back_populates="tasks")


# sync-сессия (для шпаргалки). В FastAPI:
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
# Db = Annotated[Session, Depends(get_db)]

engine = create_engine("sqlite:///:memory:", echo=False)
SessionLocal = sessionmaker(bind=engine)
Base.metadata.create_all(engine)

with SessionLocal() as db:
    u = User(email="anya@test.ru")
    db.add(u)
    db.commit()
    db.refresh(u)
    db.add(Task(title="хлеб", owner_id=u.id))
    db.commit()
    found = db.scalar(select(User).where(User.email == "anya@test.ru"))
    print(found.id, found.email)

# N+1: for user in users: user.tasks  → лишний SELECT на каждого
# лечится: select(User).options(selectinload(User.tasks))
# IntegrityError уникального email → HTTP 409
# Alembic: alembic init alembic; revision --autogenerate -m "users"; upgrade head
# схема Pydantic: model_config = ConfigDict(from_attributes=True)  # UserOut.model_validate(row)
# не делай commit в репозитории и в сервисе дважды — одна транзакция на запрос
print("модель ORM ≠ JSON-схема; сессию закрывай в Depends")
