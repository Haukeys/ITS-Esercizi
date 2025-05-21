from typing import Any
def car_information(manufacturer:str, model_name:str,**kwargs) ->dict[Any, Any]:
    return {"manufacturer":manufacturer, "model":model_name, **kwargs}