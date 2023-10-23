from seminar_03.DIP.car import Car
from seminar_03.DIP.diesel_engine import DieselEngine
from seminar_03.DIP.petrol_engine import PetrolEngine

car1: Car = Car(PetrolEngine())
car2: Car = Car(DieselEngine())

car1.start()
car2.start()
