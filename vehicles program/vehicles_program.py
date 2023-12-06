import automobile_classes

def main():
    #creating objects from automobile_classes (vehicles) 
    car = automobile_classes.Car('BMW', 2001, 70000, 15000.0, 4) #make model milage price doors

    truck = automobile_classes.Truck('Toyota', 2002, 40000, 12000.0, '4WD') #make model milage price drivetype

    suv = automobile_classes.SUV('volvo', 2000, 30000, 18500.0, 5) #make model milage price passcap

    print('Used car inventory')
    print('==================')

    #display car data
    print('The following car is in inventory')
    print('Make:', car.get_make()) #gets make from automobile classes car subclass which got it from object above
    print('Model:', car.get_model())#same
    print('Milage:', car.get_milage())#same
    print('Price:', car.get_price())#same
    print('Number of doors:', car.get_doors())#same
    print()

    #display truck data
    print('The following truck is in inventory')
    print('Make:', truck.get_make()) #gets make from automobile classes truck subclass (vehicles) which got it from object above
    print('Model:', truck.get_model())#same
    print('Milage:', truck.get_milage())#same
    print('Price:', truck.get_price())#same
    print('Drive type:', truck.get_drive_type())
    print()

    #display suv data
    print('The following truck is in inventory')
    print('Make:', suv.get_make()) #gets make from automobile classes suv subclass (vehicles) which got it from object above
    print('Model:', suv.get_model())#same
    print('Milage:', suv.get_milage())#same
    print('Price:', suv.get_price())#same
    print('Passenget capacity:', suv.get_pass_cap())
    print()

    #call
if __name__ == '__main__':
    main()