import json

with open('/workspaces/Python/exercise_4/vehicles.json', 'r', encoding='utf-8') as file:
    vehicle_data = json.load(file)

for vehicle in vehicle_data:
    vehicle_type = vehicle['vehicle_type']
    mass = vehicle['mass']
    drag_coefficient = vehicle['drag_coefficient']
    cross_sectional_area = vehicle['cross_sectional_area']
    rolling_resistance_coefficient = vehicle['rolling_resistance_coefficient']

    print(f"\nVehicle Type: {vehicle_type}")

    speed = 120  
    speed_ms = speed * 1000 / 3600  
    air_density = 1.2  
    g = 9.81  
    power = 0.5 * air_density * drag_coefficient * cross_sectional_area * speed_ms**3 + \
        rolling_resistance_coefficient * mass * g * speed_ms
    print(f"Power: {power} W")

    force = power / speed_ms
    acceleration = force / mass
    print(f"Acceleration: {acceleration} m/s^2")

    distance = 1000  
    time = distance / speed_ms
    print(f"Time: {time} s")

    print(f"Distance: {distance} m")

