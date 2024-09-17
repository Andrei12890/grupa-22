import pandas
import mysql.connector
from password import parola

df = pandas.read_csv("date_clienti.csv", header=None)
data_list = []
for item, row in df.iterrows():
    # customer_value = df.iloc[item, 0]
    # address_value = df.iloc[item, 1]
    # city_value = df.iloc[item, 2]
    # postal_code_value = df.iloc[item, 3]
    # country_value = df.iloc[item, 4]
    # data_list.append((customer_value, address_value, city_value, int(postal_code_value),
    #                   country_value))
    data_list.append(row.to_list())
print(data_list)

my_db = mysql.connector.connect(
    host='localhost',
    user='root',
    password=parola,
    database='grupa22'
)
cursor = my_db.cursor()
# cursor.execute('CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY,'
#                'name VARCHAR(100),'
#                'address VARCHAR(150),'
#                'city VARCHAR(100),'
#                'postal_code INT)')
# cursor.execute("ALTER TABLE customers ADD COLUMN country VARCHAR(200)")

sql = "INSERT INTO customers (name, address, city, postal_code, country) VALUES (%s, %s, %s, %s, %s)"
cursor.executemany(sql, data_list)
my_db.commit()