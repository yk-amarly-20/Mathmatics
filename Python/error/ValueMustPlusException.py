import sys
sys.path.append("../../")
from Python.error.Base import BaseError

class ValueMustPlusException(BaseError):
    def __init__(self, value_name: str, value):

        self.value_name = value_name
        self.value = value

    def __str__(self) -> str:
        return '{0} [{1} must plus: {2} = {3}]'.format(
            self.__class__.__name__, self.value_name,
            self.value_name, self.value
        )

    def __repr__(self) -> str:
        return super().__repr__()
