from Restaurant import Restaurant

class Tratoria(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
    
class Ramen(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)

class Steak_House(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
    
Tratoria1:Tratoria=Tratoria(restaurant_name="Ariciarola", cuisine_type="Italian")
Ramen1: Ramen=Ramen(restaurant_name="Shin", cuisine_type="Japanese")
Steak_House1:Steak_House=Steak_House(restaurant_name="Make steak great again", cuisine_type="Texas")

Tratoria1.describe_restaurant()
Ramen1.describe_restaurant()
Steak_House1.describe_restaurant()
