def ListCars(db):
    cars = db['cars'].find()

    for c in cars:
        print(c)