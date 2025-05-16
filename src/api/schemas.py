from enum import StrEnum

from pydantic import BaseModel


class Platform(StrEnum):
    github_actions = 'Github-Actions'


class Job(BaseModel):
    url: str
    branch: str
    scheduled_at: str
    platform: Platform
