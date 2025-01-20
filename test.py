# test_client.py
# test_client.py
import unittest
from unittest.mock import patch
from client import InventoryClient
import requests
import json

class TestInventoryClient(unittest.TestCase):

    @patch('requests.post')
    def test_define_stuff(self, mock_post):
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {'message': 'Defined type \'widget\' with description \'A useful widget\'.'}
        
        client = InventoryClient("http://server:5000")
        response = client.define_stuff("widget", "A useful widget")
        
        self.assertEqual(response, {'message': 'Defined type \'widget\' with description \'A useful widget\'.'})
        mock_post.assert_called_once_with('http://server:5000/define_stuff', headers={'Content-Type': 'application/json'}, data=json.dumps({"type": "widget", "description": "A useful widget"}))

    @patch('requests.post')
    def test_add(self, mock_post):
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {'message': 'Added 10 of type \'widget\'.'}
        
        client = InventoryClient("http://server:5000")
        response = client.add(10, "widget")
        
        self.assertEqual(response, {'message': 'Added 10 of type \'widget\'.'})
        mock_post.assert_called_once_with('http://server:5000/add', headers={'Content-Type': 'application/json'}, data=json.dumps({"quantity": 10, "type": "widget"}))

    @patch('requests.post')
    def test_remove(self, mock_post):
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {'message': 'Removed 5 of type \'widget\'.'}
        
        client = InventoryClient("http://server:5000")
        response = client.remove(5, "widget")
        
        self.assertEqual(response, {'message': 'Removed 5 of type \'widget\'.'})
        mock_post.assert_called_once_with('http://server:5000/remove', headers={'Content-Type': 'application/json'}, data=json.dumps({"quantity": 5, "type": "widget"}))

    @patch('requests.post')
    def test_undefine(self, mock_post):
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {'message': 'Undefined type \'widget\'.'}
        
        client = InventoryClient("http://server:5000")
        response = client.undefine("widget")
        
        self.assertEqual(response, {'message': 'Undefined type \'widget\'.'})
        mock_post.assert_called_once_with('http://server:5000/undefine', headers={'Content-Type': 'application/json'}, data=json.dumps({"type": "widget"}))
<<<<<<< HEAD

    @patch('requests.get')
    def test_get_count_existing_type(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'count': 10}
        
        client = InventoryClient("http://server:5000")
        response = client.get_count("widget")
        
        self.assertEqual(response, {'count': 10})
        mock_get.assert_called_once_with('http://server:5000/get_count/widget')

    @patch('requests.get')
    def test_get_count_non_existent_type(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'count': -1}
        
        client = InventoryClient("http://server:5000")
        response = client.get_count("nonexistent")
        
        self.assertEqual(response, {'count': -1})
        mock_get.assert_called_once_with('http://server:5000/get_count/nonexistent')

=======
>>>>>>> 5b8fc5ae8c86965ed9500f4cb95076aeef99b3a6

if __name__ == '__main__':
    unittest.main()
