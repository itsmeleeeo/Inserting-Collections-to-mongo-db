from module import database, cars, csv, json, userinput

config = database.getConfig()
conn = database.connect(config)
choice = ""

while(choice != 'q'):
    choice = input('Please enter your option (L) to list, (I) to insert manually, (C) insert from csv, (J) insert from json or (Q) to quit: ').lower()

    match choice:
        case 'l':
            cars.ListCars(conn)
        case 'i':
            userinput.InsertCars(conn)
        case 'c':
            csv.InsertCsv(conn)
        case 'j':
            json.InsertJson(conn)
        case 'q':
            print('Good Bye!')