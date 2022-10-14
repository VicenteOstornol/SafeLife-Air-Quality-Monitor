from dataclasses import dataclass

@dataclass
class Device():
    id:str
    name:str
    wifi_status:float
    reachable:bool

@dataclass
class Ambient():
    id:int
    temperature:float
    humidity:float
    co2:float
    noise:float
    status:str
    