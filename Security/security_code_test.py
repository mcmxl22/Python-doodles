import pytest
from Security_Code import write_code, set_code


assert write_code is not None
assert set_code("day_code") is str
