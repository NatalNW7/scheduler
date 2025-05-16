import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.adapters.db.models import Base
from src.adapters.db.postegres_job_repo import PostgresJobRepository


@pytest.fixture(scope='function')
def db_session():
    engine = create_engine('sqlite:///:memory:')
    SessionLocal = sessionmaker(bind=engine)

    Base.metadata.create_all(bind=engine)

    session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


@pytest.fixture
def job_repository(db_session):
    return PostgresJobRepository(db_session)
