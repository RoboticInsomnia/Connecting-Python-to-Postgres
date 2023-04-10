import psycopg2

con = psycopg2.connect(
database="roboticinsomnia",
user="postgres",
password="orion",
host="localhost",
port= '5432'
)

cursor_obj =  con.cursor()
cursor_obj.execute("SELECT * FROM mem_list")
result = cursor_obj.fetchall()
print("Results: ", "\n", result)

