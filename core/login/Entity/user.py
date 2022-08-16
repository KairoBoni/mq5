# -*- coding: utf-8 -*-
from typing import NamedTuple


class User(NamedTuple):
    id: int
    password: str
    server: str
