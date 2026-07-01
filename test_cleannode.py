# test_cleannode.py
"""
Tests for CleanNode module.
"""

import unittest
from cleannode import CleanNode

class TestCleanNode(unittest.TestCase):
    """Test cases for CleanNode class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CleanNode()
        self.assertIsInstance(instance, CleanNode)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CleanNode()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
