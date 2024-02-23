import json
import requests
import psycopg2

connection = psycopg2.connect(
    user="postgres",
    password="LSqKdf&E",
    host="localhost",
    port="5432",
    database="chatbotsupportcostume"
)
cursor = connection.cursor()


#================================================================
# Insert data to database
def insert_data_to_table(nlus):
    if nlus is not None:
        for nlu in nlus['data']:
            data = {
                "question": nlu['user_say'],
                "session_user": nlu['user_id']
            }
            response = requests.post(url, headers=headers, json=data)
            if response.status_code == 200:
                print(response.json())
            else:
                print(f"Error: {response.status_code}")
    

# Get data from database
def get_data_from_table(sql_query):
    try:
        cursor.execute(sql_query)
        results = cursor.fetchall()
        return results
    except Exception as err:
        print("Error executing SQL query:", err)
        return None
# Get data from database
def get_data_from_table(sql_query):
    try:
        cursor.execute(sql_query)
        results = cursor.fetchall()
        return results
    except Exception as err:
        print("Error executing SQL query:", err)
        return None


# Load data file json
def read_json_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError as e:
        print(f"Error: File not found: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON data: {e}")
        return None


# Calculate the intelligence level of understanding concepts
def calculate_understanding_concepts(data_test_nlu, obj_slot_db):
    for nlu in data_test_nlu:
        if nlu['slots']['clothing'] == obj_slot_db['clothing'] and nlu['slots']['category_type_clothing'] == obj_slot_db['category_type_clothing'] and nlu['slots']['color_clothing'] == obj_slot_db['color_clothing'] and nlu['slots']['size_clothing'] == obj_slot_db['size_clothing'] and nlu['slots']['price_from'] == obj_slot_db['price_from'] and nlu['slots']['price_to'] == obj_slot_db['price_to']:
            return True
    return False
#================================================================


#================================================================
url = "http://127.0.0.1:5000/chatbot_response"
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

nlus = read_json_file('rasaserver/data/nlu.json')
data_history_nlus = get_data_from_table("SELECT * FROM history_nlus")

correct_case = 0
wrong_case = 0

remove_duplicate_nlus = list(set(data_history_nlus))
if data_history_nlus:
    for row in remove_duplicate_nlus:
        slots = json.loads(row[4])
        is_correct = calculate_understanding_concepts(nlus['data'], slots)
        if is_correct == True:
            correct_case += 1
        else:
            wrong_case += 1
else:
    insert_data_to_table(nlus)
#================================================================


print("==============================================")
print(f"= Correct: {correct_case}")
print(f"= Wrong: {wrong_case}")
print("= Percentage of chatbot intelligence: {:.2f}%".format((correct_case/(correct_case+wrong_case))*100))
print("==============================================")