from abc import ABC, abstractmethod
from typing import List

from src.core.domain.job import Job


class JobsRepository(ABC):
    @abstractmethod
    def save(self, job: Job) -> Job:
        pass

    # TODO: tobe implemented
    # @abstractmethod
    # def save_batch(self, jobs: List[Job]) -> None:
    #     pass

    @abstractmethod
    def find_job(self, job_id: int) -> Job:
        pass

    # TODO: tobe implemented
    # @abstractmethod
    # def update_status(self, job_id: int, status: str) -> None:
    #     pass