print("\nSet the friction coefficient, mass of the object and the radius of the corner.\n")    # Prints the protocol.
key = int(input("Press 1 to check the speed. \nPress 2 to get the technical information. \nPress 0 to exit.\n"))
if key == 0:
    exit()

µ = float(input("Enter µ, the constant of static friction: "))
mass = float(input("Input Mass (in kilograms): "))
radius = float(input("Input the radius of the chicane/apex (in meters): "))
speed = 0.0
g = 9.81

def speedCheck():
    speed = float(input("Enter speed (in meters per second):  "))
    safe = False
    if speed <= (µ * radius * g) ** (1/2):
        safe = True
    if safe:
        print("Safe.")

    else:
        difference = (speed - (µ * radius * g) ** (1/2))
        print("NOT safe.\nDecrease speed by ", str(float(difference)), "m/s" )


def safeSpeed():
        speed = (µ * radius * g) ** (1 / 2)
        return("\nThe maximum speed you can attain without skidding is " + str(round(speed)) + " m/s (" + str(round(speed)*3.6) + " km/h, "
           + str(round(speed)*2.237) + " mi/h)")


def CentrAcc():

    return (((µ * radius * g) ** (1 / 2)) ** 2 / radius) % 1000

def CentrForce():
   return CentrAcc() * mass % 1000

while key != 0:
    if key == 1:
        speedCheck()
        key = int(input("\n\nPress 1 to check the speed. \nPress 2 to get the technical information. \nPress 0 to exit.\n"))
    elif key == 2:
        print(safeSpeed(), "\nCentripetal acceleartion is ", str(CentrAcc()), " m/s^2", "\nCentripetal force is ",
             str(CentrForce()), " Newtons")
        key = int(input("\n\nPress 1 to check the speed. \nPress 2 to get the technical information. \nPress 0 to exit.\n"))
    else:
        print("Press 1, 2 or 0")
        key = int(input("\n\nPress 1 to check the speed. \nPress 2 to get the technical information. \nPress 0 to exit.\n"))

