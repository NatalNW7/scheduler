from datetime import time

import pytest

from src.core.domain.job import Job
from src.core.execptions import JobNotFoundException
from src.ports.job_repository import JobsRepository


def test_save_job(job_repository: JobsRepository):
    job = Job(
        url='github.com/test-repo',
        branch='test_branch',
        scheduled_at=time(22, 0),
        platform='github',
    )

    saved_job = job_repository.save(job)

    assert saved_job.id is not None
    assert saved_job.platform == 'github'


def test_save_batch(job_repository: JobsRepository):
    jobs = [
        Job(
            url='github.com/test-repo1',
            branch='test_branch1',
            scheduled_at=time(22, 0),
            platform='github',
        ),
        Job(
            url='github.com/test-repo2',
            branch='test_branch2',
            scheduled_at=time(22, 0),
            platform='github',
        ),
    ]

    saved_jobs = job_repository.save_batch(jobs)

    assert len(saved_jobs) == len(jobs)


def test_find_job(job_repository: JobsRepository):
    job = Job(
        url='github.com/test-repo',
        branch='test_branch',
        scheduled_at=time(22, 0),
        platform='github',
    )

    saved_job = job_repository.save(job)
    job_found = job_repository.find(saved_job.id)

    assert job_found == saved_job


def test_update_status(job_repository: JobsRepository):
    job = Job(
        url='github.com/test-repo',
        branch='test_branch',
        scheduled_at=time(22, 0),
        platform='github',
    )

    saved_job = job_repository.save(job)
    updated_job = job_repository.update_status(saved_job.id, 'waiting')

    assert updated_job.status == 'waiting'


def test_update_raises_exception(job_repository: JobsRepository):
    with pytest.raises(JobNotFoundException):
        job_repository.update_status(99999, 'waiting')


def test_delete_job(job_repository: JobsRepository):
    job = Job(
        url='github.com/test-repo',
        branch='test_branch',
        scheduled_at=time(22, 0),
        platform='github',
    )

    saved_job = job_repository.save(job)
    job_repository.delete(saved_job.id)

    with pytest.raises(JobNotFoundException):
        job_repository.find(saved_job.id)


def test_delete_raises_exception(job_repository: JobsRepository):
    with pytest.raises(JobNotFoundException):
        job_repository.delete(99999)
