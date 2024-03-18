import requests
import os

class FoursqaurClient():
    url="https://api.foursquare.com/v3/places/search"

    def __init__(self):
        self.headers={"accept": "application/json", "Authorization": os.getenv('FOURSQUARE_API_KEY')}

    def make_request_by_categories(self, ll, categories, radius=100000, limit=50):
        params={ 
            'categories':','.join(categories),
            'll': ll,
            'radius': radius,
            'limit': limit
        }
        response = requests.request("GET", FoursqaurClient.url, params=params, headers=self.headers)
        return response

    def request_groceries(self, ll, radius=100000, limit=50):
        categories=['17067','17069', '17070']
        response = self.make_request_by_categories(ll, categories, radius, limit)
        return response
    
    def request_restaurants(self, ll, radius=100000, limit=50):
        categories=['13026','13030','13031','13030','13065', '13064','13055']
        response = self.make_request_by_categories(ll, categories, radius, limit)
        return response
    
    def request_residentials(self, ll, radius=100000, limit=50):
        categories=['12035', '12094', '12122', '12123']
        response = self.make_request_by_categories(ll, categories, radius, limit)
        return response
    