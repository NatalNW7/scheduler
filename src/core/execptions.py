class JobNotFoundException(Exception):
    def __init__(self, job_id: int):
        super().__init__(f'Job with id "{job_id}" was not found.')


class InvalidJobException(Exception):
    pass