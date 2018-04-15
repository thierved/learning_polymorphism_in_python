from airplan import Airplan
from car import Car
from boat import Boat

def main():
    
    vehicules = [Car(50), Airplan(5000), Boat(210)]

    for v in vehicules:
            v.move()

if __name__ == '__main__': main()


