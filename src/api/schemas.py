from pydantic import BaseModel
from enum import StrEnum

class Platform(StrEnum):
    github_actions = 'Github-Actions'

class Job(BaseModel):
    url: str
    branch: str
    scheduled_at: str
    platform: Platform
