from src.core.domain.job import Job
from src.adapters.db.models import JobModel


def job_mapper(job: JobModel) -> Job:
    return Job(
        id=job.id,
        url=job.url,
        branch=job.branch,
        platform=job.platform,
        scheduled_at=job.scheduled_at,
        status=job.status,
        created_at=job.created_at,
        updated_at=job.updated_at
    )