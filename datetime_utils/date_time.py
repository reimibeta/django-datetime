from datetime import datetime


class DateTime:

    @staticmethod
    def datetimenow():
        return datetime.now()

    @staticmethod
    def datenow():
        return datetime.today().date()
