import unittest
from app import services
from app.config import Config
from app.services.riskIQPassive import riskiq_quota


class TestRiskIQSearch(unittest.TestCase):
    def test_riskiq_search(self):
        self.assertTrue(Config.RISKIQ_KEY)
        self.assertTrue(Config.RISKIQ_EMAIL)
        quota = riskiq_quota()
        print("query balances: {}".format(quota))
        self.assertTrue(quota > 0)
        domain = "tophant.com"
        data = services.riskiq_search(domain)
        print("search {}, resule {}".format(domain, len(data)))
        print("result 10, {}".format(" ".join(data[:10])))
        self.assertTrue(len(data) >= 1)


if __name__ == '__main__':
    unittest.main()
