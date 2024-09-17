import pytest

from fuel import convert, gauge


def test_convert():

    with pytest.raises(ValueError):
        convert
