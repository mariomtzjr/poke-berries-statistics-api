
import unittest

from app.domains.berries.service import Berries

class TestBerryService(unittest.TestCase):

    def setUp(self):
        self.growth_times = [
            2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6,
            6, 6, 8, 8, 8, 8, 8, 8, 8, 12, 15, 15, 15, 15, 15, 18, 18,
            18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18,
            24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24
        ]
        self.berry_service = Berries()

    def test_min_growth_time(self):
        min_growth_times = self.berry_service.min_growth_time(self.growth_times)
        self.assertEqual(2, min_growth_times)
    
    def test_max_growth_time(self):
        max_growth_time = self.berry_service.max_growth_time(self.growth_times)
        self.assertEqual(24, max_growth_time)
    
    def test_frecuency_growth_times(self):
        frecuencies = self.berry_service.frequency_growth_times(self.growth_times)
        self.assertEqual(5, list(frecuencies.items())[0][1])
