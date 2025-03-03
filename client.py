
import requests
import json

class InventoryClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def _post(self, endpoint, data=None):
        url = f"{self.base_url}/{endpoint}"
        headers = {"Content-Type": "application/json"}
        response = requests.post(url, headers=headers, data=json.dumps(data) if data else None)
        response.raise_for_status()
        return response.json()

    def define_stuff(self, type, description):
        return self._post('define_stuff', {"type": type, "description": description})

    def undefine(self, type):
        return self._post('undefine', {"type": type})

    def add(self, quantity, type):
        return self._post('add', {"quantity": quantity, "type": type})

    def remove(self, quantity, type):
        return self._post('remove', {"quantity": quantity, "type": type})
        
    def get_count(self, type):
        url = f"{self.base_url}/get_count/{type}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

# Example usage
if __name__ == "__main__":
#dns = ['www.google.com', 'web1.com']
#for obj in dns:
#        url = "https://" + obj
#        try:
#            response = requests.get(url, verify=False, timeout=5)
#        except requests.exceptions.ConnectionError:
#            print("Site not rechable", url)
#

    try:
      client = InventoryClient("http://server:5000")
    except Exception as e:
      logging.error(traceback.format_exc())

    # client = InventoryClient("http://127.0.0.1:5000")
    #client = InventoryClient("http://localhost:5000")
    
    print(client.define_stuff("widget", "A useful widget"))
    print(client.add(10, "widget"))
    print(client.remove(5, "widget"))
    print(client.undefine("widget"))

