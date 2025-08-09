# test_resourceprovisioning.py
"""
Tests for ResourceProvisioning module.
"""

import unittest
from resourceprovisioning import ResourceProvisioning

class TestResourceProvisioning(unittest.TestCase):
    """Test cases for ResourceProvisioning class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ResourceProvisioning()
        self.assertIsInstance(instance, ResourceProvisioning)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ResourceProvisioning()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
