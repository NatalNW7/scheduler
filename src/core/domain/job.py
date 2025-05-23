from dataclasses import dataclass
from datetime import datetime, time
from typing import Optional

from src.core.execptions import InvalidJobException


@dataclass
class Job:
    url: str
    branch: str
    platform: str
    scheduled_at: time
    status: str = 'pending'
    id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    def __post_init__(self):
        self.validate()

    def validate(self):
        self.__remove_blank_space()
        self.__check_null_values()
        self.__check_scheduled_date()

    def __remove_blank_space(self):
        self.url = self.url.strip()
        self.branch = self.branch.strip()
        self.platform = self.platform.strip()

    def __check_null_values(self):
        if not self.url:
            raise InvalidJobException(f'Invalid URL: {self.url}')

        if not self.branch:
            raise InvalidJobException(f'Invalid Branch: {self.branch}')

        if not self.platform:
            raise InvalidJobException(f'Invalid Platform: {self.platform}')

    def __check_scheduled_date(self):
        if not isinstance(self.scheduled_at, time):
            raise InvalidJobException(f'Invalid schedule date: {self.scheduled_at}')

        now = datetime.now()
        schedule_time = now.replace(
            hour=self.scheduled_at.hour,
            minute=self.scheduled_at.minute,
            second=0,
            microsecond=0,
        )

        if schedule_time < now:
            raise InvalidJobException(
                f'Job cannot be scheduled for a past time. Scheduled at: {self.scheduled_at}. Time now: {now}'
            )
