import unittest
import inventory

"""
must be run using:
pytest -s  test_inventory.py
"""

class Test_Get_Path(unittest.TestCase):

    def test_funcs(self):
        self.assertTrue(inventory.prompt)
        self.assertTrue(inventory.choices)
        self.assertTrue(inventory.get_data)
        self.assertTrue(inventory.add_inventory)
        self.assertTrue(inventory.delete_item)
        self.assertTrue(inventory.take_items)
        self.assertTrue(inventory.view)
        self.assertTrue(inventory.main)


    def test_type(self):
        prompt = inventory.prompt("phrase")
        assert str(prompt)

        choices = inventory.choices()
        assert list(choices)
        assert str(choices)

        get_data = inventory.get_data()
        assert dict(get_data)

        add_inventory = inventory.add_inventory()
        assert dict(add_inventory)

        delete_item = inventory.delete_item()
        assert dict(delete_item)

        take_items = inventory.take_items()
        assert str(take_items)
