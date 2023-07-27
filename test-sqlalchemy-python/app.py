# Insert, create database, create table, read/fetch data

# import mysql.connector
# import json
# import csv

# class Mysql:
#     def __init__(self, host, user_name, password,db_name,table_name,filename):
#         self.host = host
#         self.user_name = user_name
#         self.password = password
#         self.database = db_name
#         self.table_name = table_name
#         self.csv_file = filename
#         # self.delete_name = delete_name
        
#     def create_connection(self):
#         mydb = mysql.connector.connect(
#             host=self.host,
#             user=self.user_name,
#             password=self.password,
#             database=self.database
#         )
#         # if mydb:
#         #     mydb.close()
       
#         cursor = mydb.cursor()
#         return cursor, mydb

#     def create_database(self):
#         cursor, mydb = self.create_connection()

#         try:
#             cursor.execute(f"CREATE DATABASE {self.database}")
#             print(f"Database '{self.database}' created successfully.")
#         except mysql.connector.Error as err:
#             print(f"Error creating database: {err}")
#         finally:
#             cursor.close()
#             mydb.close()

    # def create_table(self):
    #     # Define your table schema here
    #     table_schema = (
    #         "CREATE TABLE IF NOT EXISTS "
    #         f"{self.table_name} ("
    #         "id INT AUTO_INCREMENT PRIMARY KEY,"
    #         "name VARCHAR(255),"
    #         "age INT,"
    #         "email VARCHAR(255)"
    #         ")"
    #     )

    #     cursor, mydb = self.create_connection()
    #     try:
    #         cursor.execute(table_schema)
    #         mydb.commit()
    #         print(f"Table '{self.table_name}' created successfully.")
    #     except mysql.connector.Error as err:
    #         print(f"Error creating table: {err}")
    #     finally:
    #         cursor.close()
    #         mydb.close()

#     def fetch_data(self):
#         cursor, mydb = self.create_connection()

#         try:
#             cursor.execute(f"SELECT * FROM {self.table_name}")
#             result = cursor.fetchall()
#             return result
#         except mysql.connector.Error as err:
#             print(f"Error fetching data: {err}")
#         finally:
#             cursor.close()
#             mydb.close()

#     def insert_data_from_csv(self, csv_file):
#         cursor, mydb = self.create_connection()
#         # cursor = mydb.cursor()

#         try:
#             with open(csv_file, 'r') as file:
#                 csv_reader = csv.DictReader(file)
#                 for row in csv_reader:
#                     dcid = int(row['dcid'])
#                     Student_Number = float(row['Student_Number'])
#                     StudentEmail = row['StudentEmail']
#                     Username = row['Username']
#                     Password = row['Password']

#                     query = f"INSERT INTO {self.table_name} (DCID, Student_no, Student_email,Usernamae,Passwd) VALUES (%s, %s, %s, %s, %s)"
#                     values = (dcid , Student_Number, StudentEmail,Username,Password)

#                     cursor.execute(query, values)
#                 mydb.commit()

#             print("Data inserted successfully from CSV.")
#         except mysql.connector.Error as err:
#             print(f"Error inserting data: {err}")
#         finally:
#             cursor.close()


    
    
#     def update_data_from_csv(self, csv_file):
#         cursor,mydb = self.create_connection()

#         try:
#             with open(csv_file, 'r') as file:
#                 csv_reader = csv.DictReader(file)
#                 for row in csv_reader:
#                     dcid = row['dcid']
#                     Student_Number= row['Student_Number']
#                     StudentEmail = row['StudentEmail']
#                     Username = row['Username']
#                     Password = row['Password']

#                     # Check if the row with the same 'dcid' already exists in the table
#                     select_query = f"SELECT * FROM {self.table_name} WHERE dcid =%s"
                    
#                     cursor.execute(select_query, (dcid,))
#                     existing_row = cursor.fetchone()

#                     if existing_row:
#                         # Update the existing row with the new data
#                         update_query = f"UPDATE {self.table_name} SET Student_No = %s, Student_email =%s, Usernamae= %s, Passwd =%s WHERE dcid = %s"
#                         cursor.execute(update_query, (Student_Number, StudentEmail,Username,Password, dcid))
#                     else:
#                         # Insert a new row since it doesn't exist in the table
#                         insert_query = f"INSERT INTO {self.table_name} (dcid,  Student_No , Student_email,Usernamae,Passwd ) VALUES (%s, %s, %s, %s, %s)"
#                         cursor.execute(insert_query, (dcid , Student_Number, StudentEmail,Username,Password))
                    
#                 mydb.commit()

#             print("Data inserted/updated successfully from CSV.")
#         except mysql.connector.Error as err:
#             print(f"Error inserting/updating data: {err}")
#         finally:
#             cursor.close()


    # def delete_data(self):
    #     cursor,mydb = self.create_connection()

    #     try:
    #         query = f"DELETE FROM {self.table_name} where delete_name= %s"
    #         values = (self.delete_name,)
    #         cursor.execute(query, values)
    #         mydb.commit()


    #         print("Data deleted successfully")
    #     except mysql.connector.Error as err:
    #         print(f"Error deleted data: {err}")
    #     finally:
    #         cursor.close()

                  

# if __name__ == '__main__':
#     my_sql = Mysql("localhost", "root", "root","test","filledfiller","fieldfiller3")
#     # my_sql.create_database()
#     # name = "SS"
#     # my_sql.delete_data()
#     file= "fieldfiller3.csv"
#     my_sql.update_data_from_csv(file)
   

    # my_sql.create_table()

    # file = "fieldfiller3.csv"
    # my_sql.insert_data_from_csv(file)

    # Insert some data into the table before fetching
    # cursor, mydb = my_sql.create_connection()
    # cursor.execute(f"INSERT INTO {my_sql.table_name} (name, age, email) VALUES ('Dimpal', 12, 'dimpal@example.com')")
    # mydb.commit()

    # data = my_sql.fetch_data()
    # print(data)






# import mysql.connector

# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd = "root"
# )

# my_cursor = mydb.cursor()

# my_cursor.execute("CREATE DATABASE Hello")
# my_cursor.execute("SHOW DATABASES")
# for db in my_cursor:
#     print(db)



# import mysql.connector
# import csv

# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="root",
#     # database="scrapers"
# )


# mycursor = mydb.cursor()
# mycursor.execute("Show tables;")
# tablelist = []

# for table_name in mycursor:
#     print(table_name[0])
#     tablelist.append(table_name[0])
# if "SKU_Union" in tablelist:
#     Query_base = "DROP TBALE SKU_Union;"
#     mycursor.execute(Query_base)

# table1 = input("Enter name of first table: ")
# table2 = input("Enter name o second table: ")
# mycursor.execute("Select * from " + table1)
# mycursor.execute("Select * from " + table2)
# print("Table 1: vInfoLatestQuantitySuppliersNew")
# print("Table 2: bigcommercedata")

# try:
#     Query = "create table SKU_Union as \
#             SELECT vInfoLatestQuantitySuppliersNew.SKU,Stock,Quantity from vInfoLatestQuantitySuppliersNew left outer join bigcommercedata on vInfoLatestQuantitySuppliersNew.SKU= bigcommercedata.Product_SKU \
#             UNION SELECT bigcommercedata.Product_SKU,Stock,Quantity from bigcommercedata left outer join vInfoLatestQuantitySuppliersNew on bigcommercedata.Product_SKU=vInfoLatestQuantitySuppliersNew.SKU;"
            
#     mycursor.execute(Query)

#     Query2 = "ALTER TABLE SKU_Union \
#     RENAME COLUMN Stock to bigcommerce_Stock, \
#     RENAME COLUMN Quantity to vinfolatest_Stock;"
    
#     mycursor.execute(Query2)

#     mycursor.execute("ALTER TABLE SKU_Union \
#         ADD STOCK_EQUAL varchar(5) DEFAULT 'FALSE';")
        
        
#     Query3 = "UPDATE SKU_Comparision \
#     SET STOCK_EQUAL='TRUE' WHERE bigcommerce_Stock = vinfolatest_Stock; "

#     mycursor.execute(Query3)

# finally:
#     mycursor.execute("SELECT * FROM SKU_Union;")
#     myresult = mycursor.fetchall()
    
#     for x in myresult:
#         print(x)

#     with open("output.csv", "w", newline="") as outfile:
#         writer = csv.writer(outfile, quoting=csv.QUOTE_NONNUMERIC)
#         writer.writerow(col[0] for col in mycursor.description)
#         for row in mycursor:
#             writer.writerow(row)


# import csv

# def read_csv_file_as_dict(csv_file):
#     data = []
#     with open(csv_file, 'r', encoding='latin-1') as file:
#         csv_reader = csv.DictReader(file)
#         for row in csv_reader:
#             data.append(row)
#     return data

# def compare_csv_files(file1, file2, output_file):
#     data1 = read_csv_file_as_dict(file1)
#     data2 = read_csv_file_as_dict(file2)
#     # print(data1)
#     # print(data2)


#     columns1 = data1[0].keys()
#     columns2 = data2[0].keys()
#     print( columns1)
#     print( columns2)

#     # Find the common column names from both files
#     common_columns = list(set(columns1) & set(columns2))
#     print(common_columns)
#     for column in common_columns:
#         print(f"Column: {column}")
        # print(f"File 1 Values:")
        # for row in data1:
        #     print(row[column])
        # print(f"File 2 Values:")
        # for row in data2:
        #     print(row[column])
        # print("="*20)

    # Create a new dictionary for the third file
    # output_data = []

    # for row1 in data1:
    #     for row2 in data2:
    #         if 'Stock_Level' in row1 and 'Quantity' in row2:
    #             # If both 'Stock' and 'Quantity' keys are present, compare their values
    #             if row1['Stock Level'] == row2['Quantity']:
    #                 row1['equal'] = True
    #             else:
    #                 row1['equal'] = False
    #         # elif 'Quantity' in row1 and 'Stock' in row2:
    #         #     # If 'Quantity' in row1 and 'Stock' in row2, compare their values
    #         #     if row1['Quantity'] == row2['Stock']:
    #         #         row1['equal'] = True
    #         #     else:
    #         #         row1['equal'] = False
    #         else:
    #             # If either 'Stock' or 'Quantity' is missing, set 'equal' to False
    #             row1['equal'] = False

    # #         # Create a new dictionary with the available columns
    # new_row = {key: value for key, value in row1.items() if key in data2[0]}
    # new_row['equal'] = row1['equal']
    # output_data.append(new_row) 
    # print(output_data)

    # Write the output dictionary to a new CSV file
    # with open(output_file, 'w', newline='') as file:
    #     fieldnames = list(output_data[0].keys())
    #     csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
    #     csv_writer.writeheader()
    #     csv_writer.writerows(output_data)

# if __name__ == '__main__':
#     # Replace these with the paths to your input CSV files and desired output CSV file
#     file1 = 'file1.csv'
#     file2 = 'file2.csv'
#     output_file = 'output.csv'

#     compare_csv_files(file1, file2, output_file)


# import csv

# with open('file1.csv', 'r', encoding='latin-1') as csv_file:
#     with open('file2.csv', 'r', encoding='latin-1') as csv2_file:
#         with open('output.csv', 'w', newline='') as new_csv_file:
#             csv_reader = csv.reader(csv_file)
#             csv2_reader = csv.reader(csv2_file)
#             csv_writer = csv.writer(new_csv_file)
#             csv_writer.writerow(['SKU', 'Stock_Level', 'Qunatity'])  # Write the header row
        
#         for row in csv_reader:
#             SKU = row[0]
#             Stock_Level = row[2]
#             print(SKU, Stock_Level)
#             csv_writer.writerow([SKU, Stock_Level])
#         for row in csv2_reader:
#             Quantity = row[3]
#             print(SKU, Stock_Level,Quantity)
#             csv_writer.writerow([Quantity])

# import csv

# with open('file1.csv', 'r', encoding='latin-1') as csv_file:
#     with open('file2.csv', 'r', encoding='latin-1') as csv2_file:
#         csv_reader = csv.reader(csv_file)
#         csv2_reader = csv.reader(csv2_file)
#         next(csv2_reader)  # Skip the header row of the second file
#         next(csv_reader)  # Skip the header row of the first file

#         with open('output.csv', 'w', newline='') as new_csv_file:
#             csv_writer = csv.writer(new_csv_file)
#             csv_writer.writerow(['SKU', 'Stock_Level', 'Quantity', 'Equal'])  # Write the header row

#             for row1, row2 in zip(csv_reader, csv2_reader):
#                 SKU = row1[0]
#                 Stock_Level = row1[2]
#                 Quantity = row2[3]
#                 # print(SKU, Stock_Level, Quantity)
#                 # csv_writer.writerow([SKU, Stock_Level, Quantity])
#                 Equal = Stock_Level == Quantity
#                 csv_writer.writerow([SKU, Stock_Level, Quantity,Equal])
                # print(SKU , Stock_Level, Quantity, Equal)


# import csv
# # Load data from the two CSV files
# file1 = "file1.csv"
# file2 = "file2.csv"

# # Read data from file1 and create a dictionary with SKU as key and Stock Level as value
# sku_stock_dict = {}
# with open(file1, 'r') as f1:
#     header1 = f1.readline().strip().split(',')
#     for line in f1:
#         sku, _, stock_level = line.strip().split(',')
#         sku_stock_dict[sku] = stock_level
# print(sku_stock_dict)

# Read data from file2 and create a dictionary with SKU as key and Quantity as value
# sku_quantity_dict = {}
# with open(file2, 'r') as f2:
#     header2 = f2.readline().strip().split(',')
#     for line in f2:
#         _, sku, _, quantity, _ = line.strip().split(',')
#         sku_quantity_dict[sku] = quantity

# Find the union of SKUs from both dictionaries
# all_skus = set(sku_stock_dict.keys()) | set(sku_quantity_dict.keys())


# Create a list to store the merged data
# merged_data = []
# for sku in all_skus:
#     stock = sku_stock_dict.get(sku, '')
#     quantity = sku_quantity_dict.get(sku, '')
#     merged_data.append([sku, stock, quantity])
    
    
# Save the merged data to a new CSV file
# output_file = "merged_data.csv"
# with open(output_file, 'w') as f_out:
#     f_out.write(','.join(['SKU', 'Stock', 'Quantity']) + '\n')
#     for row in merged_data:
#         f_out.write(','.join(row) + '\n')

# print("Merged data has been saved to", output_file)
import csv
# Load data from the two CSV files
file1 = "file1.csv"
file2 = "file2.csv"

# Read data from file1 and create a dictionary with SKU as key and Stock Level as value
# sku_stock_dict = {}
# with open(file1, 'r',  encoding='latin-1') as f1:
#     header1 = f1.readline().strip().split(',')
#     for line in f1:
#         elements = line.strip().split(',')
#         if len(elements) >= 3:
#             sku, _, stock_level = elements[:3]
#             sku_stock_dict[sku] = stock_level

sku_stock_dict = {}
with open(file1, 'r',  encoding='latin-1') as f1:
    csv_reader = csv.reader(f1)
    header1 = next(csv_reader)  # Skip the header row
    for row in csv_reader:
        if len(row) >= 3:
            sku, _, stock_level = row[:3]
            sku_stock_dict[sku] = stock_level

# Read data from file2 and create a dictionary with SKU as key and Quantity as value
# sku_quantity_dict = {}
# with open(file2, 'r',  encoding='latin-1') as f2:
#     header2 = f2.readline().strip().split(',')
#     for line in f2:
#         elements = line.strip().split(',')
#         if len(elements) >= 5:
#             _, sku, _, quantity, _ = elements[:5]
#             sku_quantity_dict[sku] = quantity
            # print(sku_quantity_dict)

sku_quantity_dict = {}
with open(file2, 'r', encoding='latin-1') as f2:
    csv_reader = csv.reader(f2)
    header1 = next(csv_reader)  # Skip the header row
    for row in csv_reader:
        if len(row) >= 3:
            _, sku, _, quantity, _ = row[:5]
            sku_quantity_dict[sku] = quantity

# Find the union of SKUs from both dictionaries
all_skus = set(sku_stock_dict.keys()) | set(sku_quantity_dict.keys())
# print(all_skus)


# Create a list to store the merged data
# merged_data = []
# for sku in all_skus:
#     stock = sku_stock_dict.get(sku, '')
#     print(stock)
#     quantity = sku_quantity_dict.get(sku, '')
#     merged_data.append([sku, stock, quantity])

merged_data = []
for sku in all_skus:
    # print(sku)
    stock = sku_stock_dict.get(sku, '')
    # print(stock)
    quantity = sku_quantity_dict.get(sku, '')
    # print(quantity)
    equal = stock == quantity  # Check if Stock and Quantity are equal
    merged_data.append([sku, stock, quantity, equal])
    # print(merged_data)


# Save the merged data to a new CSV file
# output_file = "merged_data.csv"
# with open(output_file, 'w') as f_out:
#     f_out.write(','.join(['SKU', 'Stock', 'Quantity', 'Equal']) + '\n')
#     for row in merged_data:
#         row_str = [str(element) for element in row]
#         f_out.write(','.join(row_str) + '\n')

# print("Merged data has been saved to", output_file)
import csv

output_file = "merged.csv"
with open(output_file, 'w', newline='') as f_out:
    csv_writer = csv.writer(f_out)
    csv_writer.writerow(['SKU', 'Stock', 'Quantity', 'Equal'])
    csv_writer.writerows(merged_data)
print("Merged data has been saved to", output_file)


# import csv

# def read_csv_file_as_dict(csv_file):
#     data = []
#     with open(csv_file, 'r', newline='') as file:
#         csv_reader = csv.DictReader(file)
#         for row in csv_reader:
#             data.append(row)
#     return data

# import csv

# def read_csv_file_as_dict(csv_file):
#     data = []
#     with open(csv_file, 'r', newline='') as file:
#         csv_reader = csv.DictReader(file)
#         for row in csv_reader:
# #             data.append(row)
# #     return data

# with open('file1.csv', 'r', encoding='latin-1') as csv_file1:
#     with open('file2.csv', 'r', encoding='latin-1') as csv_file2:
#         with open('output.csv', 'w', newline='') as new_csv_file:
#             data1 = read_csv_file_as_dict(csv_file1)
#             data2 = read_csv_file_as_dict(csv_file2)

#             # Create a dictionary to store quantity values based on SKU
#             sku_quantity_dict = {row['SKU']: row['Quantity'] for row in data2}

#             # Write the header row
#             csv_writer = csv.writer(new_csv_file)
#             csv_writer.writerow(['SKU', 'Stock_Level', 'Quantity'])

#             # Merge the data from both files and write to the output file
#             for row in data1:
#                 SKU = row['SKU']
#                 Stock_Level = row['Stock_Level']
#                 quantity = sku_quantity_dict.get(SKU, '')  # Get the quantity value from the dictionary, or an empty string if not found
#                 csv_writer.writerow([SKU, Stock_Level, quantity])





# import csv

# def read_csv_file_as_dict(csv_file):
#     data = []
#     with open(csv_file, 'r', newline='') as file:
#         csv_reader = csv.DictReader(file)
#         for row in csv_reader:
#             data.append(row)
#     return data

# with open('file1.csv', 'r', encoding='latin-1') as csv_file1:
#     with open('file2.csv', 'r', encoding='latin-1') as csv_file2:
#         with open('output.csv', 'w', newline='') as new_csv_file:
#             data1 = read_csv_file_as_dict(csv_file1)
#             data2 = read_csv_file_as_dict(csv_file2)

#             # Create dictionaries to store Stock and Quantity values based on SKU
#             sku_stock_dict = {row['SKU']: row['Stock'] for row in data1}
#             sku_quantity_dict = {row['SKU']: row['Quantity'] for row in data2}

#             # Write the header row
#             csv_writer = csv.writer(new_csv_file)
#             csv_writer.writerow(['SKU', 'Stock', 'Quantity'])

#             # Merge the data from both files and write to the output file
#             for sku, stock in sku_stock_dict.items():
#                 quantity = sku_quantity_dict.get(sku, '')  # Get the quantity value from the dictionary, or an empty string if not found
#                 csv_writer.writerow([sku, stock, quantity])














