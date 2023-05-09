import unittest

from mootdx.reader import Reader
from tests.conftest import is_empty


# @pytest.mark.skip
class TestReader(unittest.TestCase):
    reader = None

    # 初始化工作
    def setup_class(self):
        self.reader = Reader.factory(market="std", tdxdir="tests/fixtures")

    # 退出清理工作
    def teardown_class(self):
        self.reader = None

    def test_daily(self):
        result = self.reader.daily(symbol="127021")
        assert not is_empty(result), "股票代码不存在"

        result = self.reader.daily(symbol="000000")
        assert is_empty(result), result

    def test_daily_88(self):
        result = self.reader.daily(symbol="sh881478")
        assert not is_empty(result), result

        result = self.reader.daily(symbol="881478")
        assert not is_empty(result), result

    def test_minute1(self):
        result = self.reader.minute(symbol="688001", suffix="1")
        self.assertFalse(result.empty, result)

    def test_minute5(self):
        result = self.reader.minute(symbol="688001", suffix="5")
        self.assertFalse(result.empty, result)
