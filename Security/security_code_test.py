import pytest
from Security_Code import write_code, set_code


# write_code
assert write_code() is not None
assert str(write_code())
assert len(write_code()) == 2


# set_code
assert set_code() is not None
assert str(set_code())
assert len(set_code()) == 2


print("Passed!")
