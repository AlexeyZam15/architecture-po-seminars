from seminar_03.OCP.bus import Bus
from seminar_03.OCP.car import Car
from seminar_03.OCP.vehicle import Vehicle

v1: Vehicle = Car(120)
v2: Vehicle = Bus(120)
v3: Vehicle = Vehicle(120, "Vehicle")

print(v1, v2, v3, sep="\n")
