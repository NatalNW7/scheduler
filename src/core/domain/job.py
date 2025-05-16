from dataclasses import dataclass
from datetime import datetime, time
from typing import Optional


@dataclass
class Job:
    url: str
    branch: str
    scheduled_at: time
    platform: str
    status: str = 'pending'
    id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
