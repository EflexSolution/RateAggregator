# test_rateaggregator.py
"""
Tests for RateAggregator module.
"""

import unittest
from rateaggregator import RateAggregator

class TestRateAggregator(unittest.TestCase):
    """Test cases for RateAggregator class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = RateAggregator()
        self.assertIsInstance(instance, RateAggregator)
        
    def test_run_method(self):
        """Test the run method."""
        instance = RateAggregator()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
