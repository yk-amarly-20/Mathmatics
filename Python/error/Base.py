class BaseError(Exception):
    def __init__(self, message: str):
        self.message = message

    def __str__(self):
        return '{0} [{1}]'.format(
            self.__class__.__name__, self.message
        )

    def __repr__(self) -> str:
        return str(self)
