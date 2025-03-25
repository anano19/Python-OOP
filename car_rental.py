class Cars:
    def __init__(self, list_of_cars):
        self.avaliable_cars = list_of_cars



    def display_cars(self):
        for car, price in self.avaliable_cars.items():
            print(car, price, "$ per day")

    def type_of_car(self, requested_car):
        if requested_car in self.avaliable_cars:
            price = self.avaliable_cars[requested_car]
            del self.avaliable_cars[requested_car]
            return price
        else:
            print("Sorry,", requested_car, "is not avaliable" )
            quit()



cars = Cars({"Hatchback": 30, "Sedan": 50, "SUV": 100})
cars.display_cars()
requested_car = input("welcome to our dealership! which car would you like to rent for a day? ")
car_price = cars.type_of_car(requested_car)
car_days = int(input("How many days would you like to rent it? "))
car_days_total = car_days * car_price
print("you are renting", requested_car, "for", car_days, "days, that will be $", car_days_total)