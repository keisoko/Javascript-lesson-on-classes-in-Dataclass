
# Javascript Lesson on classes in Python Dataclass

## What

Codecademy JavaScript lesson on Classes in the Python Dataclass syntax

## Documentation

This code is written against Python version 3.10, which permits the use of `kw_only=True` and `slots=True` declarations in the `@dataclass` decorator. You will get errors with anything less than Python 3.10. Also, if you are using any Python version less than 3.9, you need to have this import: `from typing import List` and this line `list[str] = field(default_factory=list)` needs to be changed to `List[str] = field(default_factory=list)`
