import json

json_data = '''
[
    {
      "vehicle_type": "car",
      "mass": 1500,
      "drag_coefficient": 0.31,
      "cross_sectional_area": 1.97,
      "rolling_resistance_coefficient": 0.015
    },
    {
      "vehicle_type": "truck",
      "mass": 6500,
      "drag_coefficient": 0.8,
      "cross_sectional_area": 6.5,
      "rolling_resistance_coefficient": 0.013
    },
    {
      "vehicle_type": "motorcycle",
      "mass": 200,
      "drag_coefficient": 0.57,
      "cross_sectional_area": 0.79,
      "rolling_resistance_coefficient": 0.015
    }
]
'''
jason_data2 = '''
[
    {
      "vehicle_type": "car",
      "mass": 2100,
      "drag_coefficient": 0.24,
      "cross_sectional_area": 2.2,
      "rolling_resistance_coefficient": 0.015
    },
    {
      "vehicle_type": "truck",
      "mass": 12000,
      "drag_coefficient": 0.6,
      "cross_sectional_area": 7.3,
      "rolling_resistance_coefficient": 0.013
    },
    {
      "vehicle_type": "motorcycle",
      "mass": 150,
      "drag_coefficient": 0.56,
      "cross_sectional_area": 0.76,
      "rolling_resistance_coefficient": 0.015
    }
]
'''

vehicle_data = json.loads(json_data)
vehicle_data2 = json.loads(jason_data2)

for vehicle in vehicle_data:
    vehicle_type = vehicle['vehicle_type']
    mass = vehicle['mass']
    drag_coefficient = vehicle['drag_coefficient']
    cross_sectional_area = vehicle['cross_sectional_area']
    rolling_resistance_coefficient = vehicle['rolling_resistance_coefficient']

    print(f"\nVehicle Type: {vehicle_type}")
    print(f"Mass: {mass} kg")
    print(f"Drag Coefficient: {drag_coefficient}")
    print(f"Cross-sectional Area: {cross_sectional_area} m^2")
    print(f"Rolling Resistance Coefficient: {rolling_resistance_coefficient}")

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

for vehicle in vehicle_data2:
    vehicle_type = vehicle['vehicle_type']
    mass = vehicle['mass']
    drag_coefficient = vehicle['drag_coefficient']
    cross_sectional_area = vehicle['cross_sectional_area']
    rolling_resistance_coefficient = vehicle['rolling_resistance_coefficient']

    print(f"\nVehicle Type: {vehicle_type}")
    print(f"Mass: {mass} kg")
    print(f"Drag Coefficient: {drag_coefficient}")
    print(f"Cross-sectional Area: {cross_sectional_area} m^2")
    print(f"Rolling Resistance Coefficient: {rolling_resistance_coefficient}")

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