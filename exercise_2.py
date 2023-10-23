# Fahrzugdaten
m = 1500 # Masse
v = 22.2 # Geschwindigkeit
g = 9.81 # Erdbeschleunigung
u = 0.015 # Reibungskoeffizient
c = 0.31 # Luftwiderstandskoeffizient
A = 1.97 # Querschnittsfläche
p = 1.204 # Dichte der Luft

# Eingabe
print("Wie hoch ist der Luftdruck?")
d = float(input("Luftdruck in hPa: "))
print("Wie hoch ist die Temperatur?")
T = float(input("Temperatur in °C: "))
print("Wie schnell fahren Sie?")
v = float(input("Geschwindigkeit in km/h: "))
v = v/3.6
print("Wie groß ist Ihre Flotte an Fahrzeugen?")
n = int(input("Anzahl der Fahrzeuge: "))

# Berechnungen
p = d/(287.058*(T+273.15))	
Fr = m * g * u  
Fl = c*A*p*v*v*0.5 
W = (Fr + Fl) * v 
W1 = W/1000 
print("Verbrauch in Kilowatt pro Fahrzeug: ", W1)
W2 = W1 * n
print("Verbrauch in Kilowatt für die gesamte Flotte: ", W2)
if W1 >= 10:
    print("Der Verbrauch ist zu hoch! Ihr Fahrzeug ist nicht effizient genug!")