import sqlite3

from src.db.models import PollData


class UserInfo:
    def __init__(self, conn) -> None:
        self._conn = conn

    def create_or_update(self, user_id: str, poll_data: PollData) -> None:
        pass

    def get_poll_by_id(self, user_id: str) -> PollData:
        pass

    def _create(self, user_id: str, poll_data: PollData) -> None:
        pass

    def _update(self, user_id, poll_data: PollData) -> None:
        pass
