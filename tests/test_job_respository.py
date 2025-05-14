from src.core.domain.job import Job
from src.ports.job_repository import JobsRepository
from datetime import time

def test_save_job(job_repository: JobsRepository):
    job = Job(
        url='github.com/test-repo',
        branch='test_branch',
        scheduled_at=time(22, 0),
        platform='github'
    )

    saved_job = job_repository.save(job)

    assert saved_job.id is not None
    assert saved_job.platform == 'github'

def test_find_job(job_repository: JobsRepository):
    job = Job(
        url='github.com/test-repo',
        branch='test_branch',
        scheduled_at=time(22, 0),
        platform='github'
    )

    saved_job = job_repository.save(job)
    job_found = job_repository.find_job(saved_job.id)

    assert job_found == saved_job