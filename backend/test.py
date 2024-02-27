import json
import requests
import psycopg2

CHATBOT_RESPONSE = "http://127.0.0.1:5000/chatbot_response"
NLUS = "http://127.0.0.1:5000/get_nlus"
HEADERS = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

connection = psycopg2.connect(
    user="diemphammf",
    password="chatbotadmin",
    host="localhost",
    port="5432",
    database="chatbotcostome_new1"
)
cursor = connection.cursor()


#================================================================
# Insert data to database
def insert_data_to_table(url, headers, nlus):
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
                

# Get nlu json file api
def get_nlus(url_link):
    response = requests.get(url=url_link)
    return response.json()


# Get data from database
def get_data_from_table(sql_query):
    try:
        cursor.execute(sql_query)
        results = cursor.fetchall()
        return results
    except Exception as err:
        print("Error executing SQL query:", err)
        return None


# Calculate the intelligence level of understanding concepts
def calculate_understanding_concepts(data_test_nlu, obj_db):
    if len(data_test_nlu) > 0:
        for nlu in data_test_nlu:
            if nlu['user_id'] == obj_db[1]:
                obj_slot_db = json.loads(row[4])
                if nlu['slots']['clothing'] == obj_slot_db['clothing'] and nlu['slots']['category_type_clothing'] == obj_slot_db['category_type_clothing'] and nlu['slots']['color_clothing'] == obj_slot_db['color_clothing'] and nlu['slots']['size_clothing'] == obj_slot_db['size_clothing'] and nlu['slots']['price_from'] == obj_slot_db['price_from'] and nlu['slots']['price_to'] == obj_slot_db['price_to']:
                    return True
    return False
#================================================================


#================================================================

nlus = get_nlus(NLUS)
history_nlu_db = get_data_from_table("SELECT * FROM history_nlus")

correct_case = 0
wrong_case = 0
intelligence = 0

if len(history_nlu_db) > 0:
    remove_duplicate_nlus = list(set(history_nlu_db))
    for row in remove_duplicate_nlus:
        is_correct = calculate_understanding_concepts(nlus['data'], row)
        if is_correct == True:
            correct_case += 1
        else:
            wrong_case += 1
else:
    insert_data_to_table(CHATBOT_RESPONSE, HEADERS, nlus)

if correct_case > 0 and wrong_case > 0:
    intelligence = (correct_case/(correct_case+wrong_case))*100
#================================================================


print("==============================================")
print(f"= Correct: {correct_case}")
print(f"= Wrong: {wrong_case}")
print("= Percentage of chatbot intelligence: {:.2f}%".format(intelligence))
print("==============================================")