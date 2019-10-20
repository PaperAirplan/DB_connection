import psycopg2
connection = psycopg2.connect(user="postgres", password="123", host="192.168.1.39", port="5432", database="testdb")
print("Connecting Success")