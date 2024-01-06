import requests
import unittest

from app.domains.berries.service import Berries

class TestBerryService(unittest.TestCase):

    def setUp(self):
        self.berry_stats_url = "http://127.0.0.1:8000/berries/allBerryStats"

    def test_get_berries_stats(self):
        response = requests.get(self.berry_stats_url).json()

        self.assertEqual(2, response.get("min_growth_time"))
