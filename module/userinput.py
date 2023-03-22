def InsertCars(db):
    vin = input("Insert VIN number: ")
    make = input("Insert car make: ")
    model = input("Insert car model: ")
    year = input("Insert car year: ")
    credName = input("Insert credit card number: ")
    cardNum = input("Insert card operator: ")
    cars = db['cars']

    newCar = {"car_id": vin, 
              "car_make": make, 
              "car_model": model, 
              "car_year": year, 
              "credit_card_type": credName, 
              "credit_card_num": cardNum
              }

    try:
        cars.insert_one(newCar)
        print("New car added")
    except Exception as e:
        print('Unexpected Error: ', type(e), e)