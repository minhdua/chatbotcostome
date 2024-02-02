import psycopg2

# Connect to the database
connection = psycopg2.connect(
    user="diemphammf",
    password="chatbotadmin",
    host="localhost",
    port="5432",
    database="chatbotcostome_new"
)
cursor = connection.cursor()