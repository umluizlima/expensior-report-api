from datetime import datetime as dt


class Record:
    def __init__(self, value, description=None, datetime=None):
        self.value = float(value)
        self.description = description
        self.datetime = datetime or dt.now().isoformat(timespec="seconds")
