import csv
csv_columns = ['id','name','price']
dict_data = [
    {'id': 1, 'name':'A',  'price' :1000},
    {'id': 2, 'name': 'B', 'price': 2000},
    {'id': 3, 'name': 'C', 'price': 3000},
    {'id': 4, 'name': 'D', 'price': 4000},
    {'id': 5, 'name': 'E', 'price': 5000},
    {'id': 6, 'name': 'F', 'price': 6000},
    {'id': 7, 'name': 'G', 'price': 7000},
    {'id': 8, 'name': 'H', 'price': 58000},
    {'id': 9, 'name': 'I', 'price': 9000},
    {'id': 10, 'name': 'J', 'price': 10000},


]
csv_file = 'csv_files.csv'


with open('../config/data.csv', 'w') as fp:
    writer = csv.DictWriter(fp, fieldnames=csv_columns)
    writer.writeheader()
    for data in dict_data:
        writer.writerow(data)





