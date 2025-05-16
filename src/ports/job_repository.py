from abc import ABC, abstractmethod
from typing import List

from src.core.domain.job import Job


class JobsRepository(ABC):
    @abstractmethod
    def save(self, job: Job) -> Job:
        pass

    @abstractmethod
    def save_batch(self, jobs: List[Job]) -> List[Job]:
        pass

    @abstractmethod
    def find(self, job_id: int) -> Job:
        pass

    @abstractmethod
    def update_status(self, job_id: int, status: str) -> Job:
        pass

    @abstractmethod
    def delete(self, job_id: int) -> None:
        pass
