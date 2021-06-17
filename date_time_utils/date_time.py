from datetime import datetime


class DateTime:
    # The ellipsis ... means as many : as needed.
    # config (date) & (time)
    config = None

    def __init__(self, config):
        self.config = config

    def now(self):
        if not self.config:
            raise ValueError("Config must not none")
        if self.config == "date":
            return datetime.today().date()
        elif self.config == "datetime":
            return datetime.now()
