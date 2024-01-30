import psycopg2

# Connect to the database
connection = psycopg2.connect(
    user="postgres",
    password="LSqKdf&E",
    host="localhost",
    port="5432",
    database="chatbotsupportcostume"
)
cursor = connection.cursor()