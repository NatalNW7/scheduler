from datetime import datetime, time

import pytest

from src.core.domain import Job
from src.core.execptions import InvalidJobException


def test_create_valid():
    now = datetime.now()
    Job(
        url='http://testjob.com',
        branch='testbranch',
        platform='test',
        scheduled_at=time(hour=now.hour + 1, minute=now.minute),
    )


def test_invalid_url():
    now = datetime.now()

    with pytest.raises(InvalidJobException) as e:
        Job(
            url='',
            branch='testbranch',
            platform='test',
            scheduled_at=time(hour=now.hour + 1, minute=now.minute),
        )
    assert 'Invalid URL' in str(e)


def test_invalid_branch():
    now = datetime.now()
    with pytest.raises(InvalidJobException) as e:
        Job(
            url='http://testjob.com',
            branch='',
            platform='test',
            scheduled_at=time(hour=now.hour + 1, minute=now.minute),
        )
    assert 'Invalid Branch' in str(e)


def test_invalid_platform():
    now = datetime.now()
    with pytest.raises(InvalidJobException) as e:
        Job(
            url='http://testjob.com',
            branch='testbranch',
            platform='',
            scheduled_at=time(hour=now.hour + 1, minute=now.minute),
        )
    assert 'Invalid Platform' in str(e)


def test_invalid_scheduled_date():
    now = datetime.now()
    with pytest.raises(InvalidJobException) as e:
        Job(
            url='http://testjob.com',
            branch='testbranch',
            platform='test',
            scheduled_at=time(hour=now.hour - 1, minute=now.minute),
        )

    assert 'Job cannot be scheduled for a past time' in str(e)


def test_invalid_scheduled_date_instance():
    now = datetime.now()
    with pytest.raises(InvalidJobException) as e:
        Job(
            url='http://testjob.com',
            branch='testbranch',
            platform='test',
            scheduled_at='22:00',
        )

    assert 'Invalid schedule date' in str(e)
