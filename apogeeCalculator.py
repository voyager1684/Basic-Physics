g = 9.81
speed = 0
alt = 0
apogee = 0
index = 0
k = 0

thrust = float(input("Enter the known thrust (in Newtons): "))
mass = float(input("Enter the known mass (in kilograms): "))
propellantMass = float(input("Enter the known propellant mass (in kilograms): "))
burnRate = float(input("Enter the known burn rate (in kg/s): "))
index = float(input("Input the interval (dt) for the integral.\nEnter a value less than 0.005 for a better approximation: "))


while speed >= 0 and mass != propellantMass and alt >= 0:
    k = k + 1
    alt = alt + (speed*index + 0.5 * (thrust/(mass-(burnRate*index)) - g) * (index**2))
    speed = speed + (thrust/(mass-(burnRate*index)) - g)*index
    mass = mass - burnRate*index

apogee = alt + (speed**2/(2*g))
time = abs(speed/g)

print("The apogee is ", str(round(alt + apogee)), "m,"," achieved in the ", str(round(k*0.005 + time)),
      "th second. (", str(round((k*0.005 + time)/60)), "th minute.)")
print("The thrust apogee is ", str(round(alt)), "m")
print("\nDrag neglected.")
