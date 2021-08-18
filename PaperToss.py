import math

windSpeed = float(input("Enter the wind speed in m/s: "))
#windDirection = float(input("Enter the wind direction (North, South, East, West): "))
distance = 0
height = 0
g = 9.81


key = 5
while key != 0:
    key = int(input(
        "If you know the drop height, press \"1\" to calculate the distance.\nIf you know the distance, press \"2\" to  calculate the drop height."
        "\nPress \"3\" to reset the windpseed.\nPress \"0\" to exit.\n"))


    if key == 1:
        height = float(input("Enter the drop height (in meters): "))
        distance = windSpeed * math.sqrt(2 * height / g)
        print("Distance required: ", str(round(distance)), "meters.")

    if key == 2:
        distance = float(input("Enter the distance to the bin (in meters): "))
        height = (distance ** 2) * g / (2 * (windSpeed ** 2))
        print("Height required: ", str(round(height)), "meters.")

    if key == 3:
        windSpeed = float(input("Enter the wind speed in m/s: "))
