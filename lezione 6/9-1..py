class Restaurant:
    def __init__(self, restaurant_name:str , cuisine_type:str):
        self.restuarant_name= restaurant_name
        self.cuisne_type=cuisine_type
    
    def describe_restaurant(self) ->str:
        return self.restuarant_name,self.cuisne_type

    def open_restaurant(self) ->str:
        return f"{self.restuarant_name} is open."
    

restaurant1: Restaurant = Restaurant(restaurant_name="Open Colona", cuisine_type="Italian cuisine")

print(restaurant1.restuarant_name)
print(restaurant1.cuisne_type)

print(restaurant1.describe_restaurant())
print(restaurant1.open_restaurant())







        
