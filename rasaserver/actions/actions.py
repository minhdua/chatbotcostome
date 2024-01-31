# This files contains your custom actions which can be used to run
# custom Python code.
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions
# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from .db_operations import get_color_user_say, get_size_user_say, query_dictionary_by_word
from .utils import filter_duplicate_in_array
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionBuyashions(Action):

    def name(self) -> Text:
        return "action_buy_fashions"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Get the entity value from the tracker
        category_type_clothing = tracker.get_slot("category_type_clothing")
        clothing = tracker.get_slot("clothing")
        size_clothing = tracker.get_slot("size_clothing")
        color_clothing = tracker.get_slot("color_clothing")
        price_from = tracker.get_slot("price_from")
        price_to = tracker.get_slot("price_to")
        
        category_type = []
        if category_type_clothing != None:
            category_type = query_dictionary_by_word(category_type_clothing)
        
        category_clothing = []
        if clothing != None:
            category_clothing = query_dictionary_by_word(clothing)
        
        sizes = []
        if size_clothing != None:
            sizes = get_size_user_say(size_clothing)
        
        colors = []
        if color_clothing != None:
            colors = get_color_user_say(color_clothing)
            
        categories = filter_duplicate_in_array(category_type + category_clothing)
        
        result_string = "Không có gì"
        if len(categories) > 0:
            result_string = ", ".join(str(element) for element in categories)
        
        # upper_body = filter() #// confidence cao nhất
        # category = filter() #// cao nhất
        # response = ''
        # params = []
        # for slot in tracker.slots:
        #     if 'clothing' in slot and not slot['clothing']:
        #         response += response + f" loại {slot['clothing']}"
        #         category_id = 'call_api'
        #         params += ["category_ids={category_id}"]
        #     if 'color' in slot and not slot['color']:
        #         color_id = 'call_api'
        #         params += ["color_id={color_id}"]
        #     # prices xử lý roles, attributes, size
            
        # query = "&".join(params)
        # link = "base_url?" + query
        # link
        #link = "<a href={}>{}</a>".format('#',f"{upper_body}")
        # Đặt giá trị cho slot 'your_slot_name'
        # In ra giá trị đã đặt cho kiểm tra
        # print("Slot 'your_slot_name' set to:", value_to_set)
        
        dispatcher.utter_message(text=result_string)
        return []