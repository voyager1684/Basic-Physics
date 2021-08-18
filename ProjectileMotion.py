import math
key = 1
angle = 0
distance = 0
speed = 0
height = 0
g = 9.81
k = 0
l = 0
m = 0
degrees = 0

while key != 0:
    print("\nPress 1 to set the angle of elevation and target distance.")
    print("Press 2 to calculate the launch speed required.\n(Assuming angle of elevation and distance are known)")
    key = int(input("Press 3 to calculate the flight time.\nPress 4 to get the specs.\nPress 0 to exit\n\n"))

    if key == 0:
        exit()
        
    elif key == 1:
        degrees = float(input("Enter the angle of elevation: "))
        angle = math.pi*degrees/180
        distance = float(input("Enter the distance: "))
        k = k + 1
        
    elif key == 2:
        speed = math.sqrt((g*distance)/(2*math.sin(angle)*math.cos(angle)))
        print("Speed required is ", str(speed), "m/s")
        l = l + 1
        
    elif key == 3:
        time = distance/(2*speed*math.cos(angle))
        m = m + 1
        print("Flight time is ",str(time),"seconds")
        
        if distance/(speed*math.cos(angle)) == 2*(speed*math.sin(angle)/g):
            print("The two methods are correct.")
            
        else:
            print("Inconsistent values: ", str(2*(speed*math.sin(angle)/g)), " and ", str(distance/(speed*math.cos(angle))))
            
    elif key == 4:
        if k!=1:
          
            degrees = float(input("Enter the angle of elevation: "))
            angle = math.pi * degrees / 180
            distance = float(input("Enter the distance: "))
            
        if l != 1 :
            speed = math.sqrt((g * distance) / (2 * math.sin(angle) * math.cos(angle)))

        if m != 1:
            time = distance / (2 * speed * math.cos(angle))
