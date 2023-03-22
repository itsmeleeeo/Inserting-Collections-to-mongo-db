import csv
def InsertCsv(db):
    cars = db['cars']

    header = ['car_id','car_make','car_model','car_year','credit_card_type','credit_card_num']
    csvFile = open('data\cars-lfe-41.csv', 'r')
    reader = csv.DictReader(csvFile)

    for e in reader:
        row = {}
        for f in header:
            row[f] = e[f]
        print(row)
        cars.insert_one(row)