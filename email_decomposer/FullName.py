
import pandas as pd


class FullName:

    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name if first_name is None else first_name.title()
        self.last_name = last_name if last_name is None else last_name.title()

    def is_empty(self) -> bool:
        return (self.first_name is None or self.first_name == '') \
               and (self.last_name is None or self.last_name == '')

    def is_full(self):
        return self.first_name is not None and self.first_name != '' \
               and \
               self.last_name is not None and self.last_name != ''

    def to_dict(self) -> dict:
        return {'first_name': self.first_name, 'last_name': self.last_name}

    def to_series(self) -> pd.Series:
        return pd.Series(self.to_dict())

