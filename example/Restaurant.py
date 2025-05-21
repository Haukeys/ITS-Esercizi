class Restaurant:
    def __init__(self, restaurant_name:str , cuisine_type:str):
        self.restuarant_name= restaurant_name
        self.cuisne_type=cuisine_type
    
    def describe_restaurant(self) ->str:
        print(self.restuarant_name,self.cuisne_type)
    
    def open_restaurant(self) ->str:
        return f"{self.restuarant_name} is open."
    