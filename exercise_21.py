vehicles = {
    "car1": "VW Golf",
    "car2": "audi etron",
    "car3": "BMW i3",
    "car4": "Tesla Model S",
}
print("Ihrer Flotte gehören folgende Fahrzeuge an: ")
for key, value in vehicles.items():
    print(key, value)
print("Wählen Sie ein Fahrzeug aus: ")
vehicle = input("Fahrzeug: ")

# Fahrzugdaten
if vehicle == "car":
    m = 1500
    u = 0.015
    c = 0.3
    A = 4.0
elif vehicle == "car2":
    m = 2000
    u = 0.015
    c = 0.41
    A = 2.2
elif vehicle == "car3":
    m = 1000
    u = 0.05
    c = 0.31
    A = 1.97
elif vehicle == "car4":
    m = 2500
    u = 0.02
    c = 0.19
    A = 3.0
else:
    print("Fahrzeug nicht gefunden!")
    exit()

# Konstanten
g = 9.81

# Eingabe
print("Wie hoch ist der Luftdruck?")
d = float(input("Luftdruck in hPa: "))
print("Wie hoch ist die Temperatur?")
T = float(input("Temperatur in °C: "))
print("Wie schnell fahren Sie?")
v = float(input("Geschwindigkeit in km/h: "))
v = v/3.6

# Berechnungen
p = d/(287.058*(T+273.15))
Fr = m * g * u  
Fl = c*A*p*v*v*0.5 
W = (Fr + Fl) * v 
W1 = W/1000 
print("Verbrauch in Kilowatt pro Fahrzeug: ", W1)
if W1 >= 10:
    print("Ihr Fahrzeug ist nicht effizient")
else:
    print("Ihr Fahrzeug ist effizient")
