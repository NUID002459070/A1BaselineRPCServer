import unittest
import subprocess
import time
import requests
from client import InventoryClient

TEST_SERVER_NAME="localhost"

class TestEndToEnd(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Start the Flask server
        cls.server_process = subprocess.Popen(['python', 'server.py', TEST_SERVER_NAME])
        # Give the server a moment to start up
        time.sleep(5)
        cls.client = InventoryClient("http://" + TEST_SERVER_NAME + ":5000")

    @classmethod
    def tearDownClass(cls):
        # Stop the Flask server
        cls.server_process.terminate()
        cls.server_process.wait()

    def test_define_and_manage_inventory(self):
        # Define a new item
        response = self.client.define_stuff("widget", "A useful widget")
        self.assertEqual(response, {'message': 'Defined type \'widget\' with description \'A useful widget\'.'})

        # Add items
        response = self.client.add(10, "widget")
        self.assertEqual(response, {'message': 'Added 10 of type \'widget\'.'})

        # Check the count of items
        response = self.client.get_count("widget")
        self.assertEqual(response, {'count': 10})

        # Remove items
        response = self.client.remove(5, "widget")
        self.assertEqual(response, {'message': 'Removed 5 of type \'widget\'.'})

        # Check the count of items again
        response = self.client.get_count("widget")
        self.assertEqual(response, {'count': 5})

        # Undefine the item
        response = self.client.undefine("widget")
        self.assertEqual(response, {'message': 'Undefined type \'widget\'.'})

        # Check the count of undefined items
        response = self.client.get_count("widget")
        self.assertEqual(response, {'count': -1})
        

if __name__ == '__main__':
    unittest.main()

