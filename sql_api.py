import requests

dct = {}

for i in range(100):
    response = requests.get(f'https://www.fruityvice.com/api/fruit/{i}')
    if response.status_code == requests.codes.ok:
        var = response.json()
        lst = [x for x in var['nutritions'].values()]
        dct[var['id']] = [var['name'], lst]


import mysql.connector

mydb = mysql.connector.connect(user='', password='', 
host='127.0.0.1', database='', auth_plugin='mysql_native_password')

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE Api_fruits")
mycursor.execute("USE Api_fruits")
mycursor.execute('''CREATE TABLE fruits
                    (id INT NOT NULL PRIMARY KEY, 
                    name VARCHAR(50) UNIQUE,
                    calories FLOAT,
                    fat FLOAT,
                    carbohydrates FLOAT,
                    sugar FLOAT,
                    protein FLOAT)''')

for i in dct.keys():
    mycursor.execute(f'''INSERT INTO fruits(id, name, calories, fat, carbohydrates, sugar, protein) 
    VALUES({i}, '{dct[i][0]}', {dct[i][1][3]}, {dct[i][1][2]}, {dct[i][1][0]}, {dct[i][1][4]}, {dct[i][1][1]})''')
    mydb.commit()

mycursor.execute("SELECT * FROM fruits")

myresult = mycursor.fetchall()

print('id, name, calories, fat, carbohydrates, sugar, protein')
for x in myresult:
    print(x)

print('\nDone!')
