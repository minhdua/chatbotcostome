# This files contains your custom actions which can be used to run
# custom Python code.
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions
# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from .enum import EntityNameEnum, ResponseMessage, ResponseURL
from .db_operations import check_product_colors_with_categories, check_product_sizes_with_categories, get_category_ids, get_color_user_say, get_size_user_say, query_dictionary_by_word
from .utils import filter_duplicate_in_array, get_entity_value
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionBuyashions(Action):

    def name(self) -> Text:
        return "action_buy_fashions"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        #Get slots withh tracker
        category_type_clothing = tracker.get_slot("category_type_clothing")
        clothing = tracker.get_slot("clothing")
        size_clothing = tracker.get_slot("size_clothing")
        color_clothing = tracker.get_slot("color_clothing")
        price_from = tracker.get_slot("price_from")
        price_to = tracker.get_slot("price_to")
        
        #Get categories with words: UPPER_BODY, LOWER_BODY, FULL_BODY
        category_type = []
        if category_type_clothing != None:
            category_type = query_dictionary_by_word(category_type_clothing)
        
        #Get categories with words in list dictionaries defined in database
        category_clothing = []
        if clothing != None:
            category_clothing = query_dictionary_by_word(clothing)
        
        #Separate words and get all sizes: 'S', 'M', 'L', 'XL', 'XXL', 'XXXL' corresponding to size product
        sizes = []
        if size_clothing != None:
            sizes = get_size_user_say(size_clothing)
        sizes_format = ",".join(str(size) for size in sizes)
        
        #Separate words and get all colors in dictionaries
        #Defined of database 'WHITE', 'BLUE' ,'GREEN' , 'YELLOW', 'ORANGE', 'PINK', 'GREY', 'RED', 'BLACK', 'BROWN', 'PURPLE' corresponding to size product
        colors = []
        if color_clothing != None:
            colors = get_color_user_say(color_clothing)
        colors_format = ",".join(str(color) for color in colors)
        
        #Merger all list categories
        categories = category_type
        if category_type_clothing != None and clothing != None:
            categories = filter_duplicate_in_array(category_clothing)
        
        #Define product name, size name, color name, category_filter
        product_name = category_type_clothing
        size_name = ""
        color_name = ""
        
        entity_values = get_entity_value(tracker.latest_message['entities'], tracker.latest_message['text'])
        for entity in entity_values:
            if entity['entity'] == EntityNameEnum.CATEGORY_TYPE.value:
                product_name = entity['value']
            else:
                product_name = category_type_clothing
            
            if entity['entity'] == EntityNameEnum.CATEGORY.value:
                product_name = entity['value']
            elif(category_type_clothing != None and clothing != None):
                product_name = clothing
            
            if entity['entity'] == EntityNameEnum.COLOR.value:
                color_name = entity['value']
            else:
                color_name = color_clothing
            
            if entity['entity'] == EntityNameEnum.SIZE.value:
                size_name = entity['value']
            else:
                size_name = size_clothing
        
        #Get filter category with size
        category_with_sizes = check_product_sizes_with_categories(categories, sizes)
        if len(category_with_sizes) > 0:
            categories.extend(category_with_sizes)
        
        #Get filter category with color
        category_with_colors = check_product_colors_with_categories(categories, colors)
        if len(category_with_colors) > 0:
            categories.extend(category_with_colors)
        
        category_filter = filter_duplicate_in_array(categories)
        category_ids = get_category_ids(category_filter)
        
        #Message text full result to user chat
        product_url = ResponseURL.URL.value.format(categories=category_ids, size=sizes_format, color=colors_format)
        link_click = ResponseURL.TAG_A.value.format(url=product_url, text_user=ResponseMessage.CLICK.value)
        message_text = f"{ResponseMessage.NOTIFICATION.value} {product_name} {size_name} {color_name} {link_click}"
        
        dispatcher.utter_message(text=message_text)
        return []