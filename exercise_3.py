class Fleet:
    def __init__(self, name, m, u, c, a):
        self.name = name
        self.m = m
        self.u = u
        self.c = c
        self.a = a

    def __str__(self):
        return self.name


def create_fleet():
    car1 = Fleet("VW Golf", 1500, 0.015, 0.3, 4.0)
    car2 = Fleet("Audi e-tron", 2000, 0.015, 0.41, 2.2)
    car3 = Fleet("BMW i3", 1000, 0.05, 0.31, 1.97)
    car4 = Fleet("Tesla Model S", 2500, 0.02, 0.19, 3.0)
    return [car1, car2, car3, car4]


def get_user_input():
    print("Wie hoch ist der Luftdruck?")
    d = float(input("Luftdruck in hPa: "))
    print("Wie hoch ist die Temperatur?")
    T = float(input("Temperatur in °C: "))
    print("Wie schnell fahren Sie?")
    v = float(input("Geschwindigkeit in km/h: "))
    v = v / 3.6
    return d, T, v


def calculate_consumption(m, u, c, a, d, T, v):
    g = 9.81

    p = d / (287.058 * (T + 273.15))
    Fr = m * g * u
    Fl = c * a * p * v * v * 0.5
    W = (Fr + Fl) * v
    W1 = W / 1000
    return W1


def main():
    fleet_list = create_fleet()

    print("Ihrer Flotte gehören folgende Fahrzeuge an: ")
    for car in fleet_list:
        print(car)

    print("Wählen Sie ein Fahrzeug aus: (car1, car2, car3, car4 als Eingabe)")
    vehicle = input("Fahrzeug: ")

    d, T, v = get_user_input()
    selected_car = next(
        car for car in fleet_list if car.name.lower() == vehicle.lower())
    W1 = calculate_consumption(
        selected_car.m, selected_car.u, selected_car.c, selected_car.a, d, T, v)

    print("Verbrauch in Kilowatt pro Fahrzeug: ", W1)
    if W1 >= 10:
        print("Ihr Fahrzeug ist nicht effizient")
    else:
        print("Ihr Fahrzeug ist effizient")


if __name__ == "__main__":
    main()
