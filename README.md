
# Javascript Lesson on classes in Python Dataclass

## What

Codecademy JavaScript lesson on Classes in the Python Dataclass syntax

## Documentation

Enum requires at least Python 3.4 to run the file. Here is the link to documentation: [enum — Support for enumerations](https://docs.python.org/3/library/enum.html)

Dataclasses were first introduced in Python 3.7. They can be backported to Python 3.6 by running **`pip install dataclasses`**.

Here is list of links with more info:

- Official documentation: [dataclasses — Data Classes](https://docs.python.org/3/library/dataclasses.html#module-dataclasses)
- Backport: [dataclasses 0.8](https://pypi.org/project/dataclasses/)
- Real Python article: [Data Classes in Python 3.7+ (Guide)](https://realpython.com/python-data-classes/)

The use of `kw_only=True` and `slots=True` declarations in the `@dataclass` decorator requires Python 3.10. Also, if you are using any Python version less than 3.9, you need to have this import: `from typing import List` and this line `list[str] = field(default_factory=list)` needs to be changed to `List[str] = field(default_factory=list)`

`generate_id` function is contained in `my_python_modules.py`. Make sure that `my_python_modules.py` resides in the same directory as the `dataclass_post_init_and_super.py`.
