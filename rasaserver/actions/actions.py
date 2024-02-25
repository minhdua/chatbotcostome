# This files contains your custom actions which can be used to run
# custom Python code.
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions
# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from .enum import EntityNameEnum, ResponseMessage, ResponseURL
from .db_operations import check_product_colors_with_categories, check_product_prices_with_categories, check_product_sizes_with_categories, get_category_ids, get_color_user_say, get_colors_product_with_categories, get_products_with_categories, get_size_user_say, get_sizes_product_with_categories, query_dictionary_by_word
from .utils import add_history_api, check_products_call_api, convert_text_to_url, filter_duplicate_in_array, get_entity_value, get_number_in_string
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, FollowupAction
from rasa_sdk.executor import CollectingDispatcher


class ActionBuyFashions(Action):

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
        sizes_format = ""
        if size_clothing != None:
            sizes = get_size_user_say(size_clothing)
        if len(sizes) > 0:
            sizes_format = sizes[0]
        
        #Separate words and get all colors in dictionaries
        #Defined of database 'WHITE', 'BLUE' ,'GREEN' , 'YELLOW', 'ORANGE', 'PINK', 'GREY', 'RED', 'BLACK', 'BROWN', 'PURPLE' corresponding to size product
        colors = []
        colors_format = ""
        if color_clothing != None:
            colors = get_color_user_say(color_clothing)
        if len(colors) > 0:
            colors_format = colors[0]
        
        #Merger all list categories
        categories = category_type
        if clothing != None:
            categories = filter_duplicate_in_array(category_clothing)
        
        #Define product name, size name, color name, category_filter
        product_name = clothing
        size_name = ""
        color_name = ""
        price_from_name = ""
        price_to_name = ""
        category_filter = []
        
        #Set name from slots
        entity_values = get_entity_value(tracker.latest_message['entities'], tracker.latest_message['text'])
        for entity in entity_values:
            if entity['entity'] == EntityNameEnum.CATEGORY_TYPE.value:
                product_name = entity['value']
            elif(category_type_clothing != None):
                product_name = category_type_clothing
            
            if entity['entity'] == EntityNameEnum.CATEGORY.value:
                product_name = entity['value']
            elif(clothing != None):
                product_name = clothing
            
            if entity['entity'] == EntityNameEnum.COLOR.value:
                color_name = entity['value']
            elif(color_clothing != None):
                color_name = color_clothing
            
            if entity['entity'] == EntityNameEnum.SIZE.value:
                size_name = entity['value']
            elif(size_clothing != None):
                size_name = size_clothing
        
        #Get filter category with size
        category_with_sizes = check_product_sizes_with_categories(categories, sizes)
        if len(category_with_sizes) > 0:
            category_filter.extend(category_with_sizes)
        
        #Get filter category with color
        category_with_colors = check_product_colors_with_categories(categories, colors)
        if len(category_with_colors) > 0:
            category_filter.extend(category_with_colors)
        
        #Get filter category with prices
        category_with_prices = check_product_prices_with_categories(categories, price_from, price_to)
        if len(category_with_prices) > 0:
            category_filter.extend(category_with_prices)
        
        #Check category filter
        if len(category_filter) == 0:
            category_filter = categories
        
        #Set price min
        price_min = 0
        if price_from != None:
            price_from_name += f"{ResponseMessage.PRICE_FROM.value} {price_from} VND"
            price_min = get_number_in_string(price_from)
        
        #Set price max
        price_max = 0
        if price_to != None:
            price_to_name = f"{price_to} VND"
            price_max = get_number_in_string(price_to)
            
        #Filter category duplicate
        category_filter = filter_duplicate_in_array(category_filter)
        
        #Convert category ids to string
        category_ids = get_category_ids(category_filter)
        
        #Message text full result to user chat
        product_url = convert_text_to_url(category_ids, sizes_format, colors_format, price_min,  price_max)
        link_click = ResponseURL.TAG_A.value.format(url=product_url, text_user=ResponseMessage.CLICK.value)
        message_text = f"{ResponseMessage.NOTIFICATION.value} ({product_name} {size_name} {color_name} {price_from_name} {price_to_name}) {link_click}"
        
        #Check url has products
        is_products = check_products_call_api(category_ids, sizes_format, colors_format, price_min,  price_max)
        if is_products == False:
            message_text = f"{ResponseMessage.NOT_PRODUCTS_START.value} ({product_name} {size_name} {color_name} {price_from_name} {price_to_name}) {ResponseMessage.NOT_PRODUCTS_END.value}"
        
        dispatcher.utter_message(text=message_text)
        return []
    

class ActionDeleteAllSlots(Action):

    def name(self) -> Text:
        return "action_delete_all_slots"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Get the list of all slots defined in your domain
        all_slots = domain['slots'].keys()

        # Create a list of SlotSet events with None values for each slot
        slot_set_events = [SlotSet(slot, None) for slot in all_slots]

        # Add the SlotSet events to the list of events to be returned
        return slot_set_events
    
class ActionSizeAsk(Action):
    def name(self) -> Text:
        return "action_size"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        size_clothing = tracker.get_slot("size_clothing")
        if size_clothing != None:
            return [FollowupAction("action_buy_fashions")]
        
        category_type_clothing = tracker.get_slot("category_type_clothing")
        clothing = tracker.get_slot("clothing")
        
        #Get categories with words: UPPER_BODY, LOWER_BODY, FULL_BODY
        category_type = []
        if category_type_clothing != None:
            category_type = query_dictionary_by_word(category_type_clothing)
        
        #Get categories with words in list dictionaries defined in database
        category_clothing = []
        if clothing != None:
            category_clothing = query_dictionary_by_word(clothing)
            
        #Merger all list categories
        categories = category_type
        if clothing != None:
            categories = filter_duplicate_in_array(category_clothing)
            
        sizes = get_sizes_product_with_categories(categories)
        dispatcher.utter_message(text='Sảm phẩm này hiện tại có {} size là {} bạn chọn size nào?'.format(len(sizes),', '.join(sizes)))
        return []
    

class ActionColorAsk(Action):
    def name(self) -> Text:
        return "action_color"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        color_clothing = tracker.get_slot("color_clothing")
        if color_clothing != None:
            return [FollowupAction("action_buy_fashions")]
        
        category_type_clothing = tracker.get_slot("category_type_clothing")
        clothing = tracker.get_slot("clothing")
        
        #Get categories with words: UPPER_BODY, LOWER_BODY, FULL_BODY
        category_type = []
        if category_type_clothing != None:
            category_type = query_dictionary_by_word(category_type_clothing)
        
        #Get categories with words in list dictionaries defined in database
        category_clothing = []
        if clothing != None:
            category_clothing = query_dictionary_by_word(clothing)
            
        #Merger all list categories
        categories = category_type
        if clothing != None:
            categories = filter_duplicate_in_array(category_clothing)
            
        colors = get_colors_product_with_categories(categories)
        dispatcher.utter_message(text='Sảm phẩm này hiện tại có {} màu là {} bạn chọn màu nào?'.format(len(colors),', '.join(colors)))
        return []


class ActionCategoryAsk(Action):
    def name(self) -> Text:
        return "action_category"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        category_type_clothing = tracker.get_slot("category_type_clothing")
        clothing = tracker.get_slot("clothing")
        size_clothing = tracker.get_slot("size_clothing")
        color_clothing = tracker.get_slot("color_clothing")
        price_from = tracker.get_slot("price_from")
        price_to = tracker.get_slot("price_to")
        name_clothing = category_type_clothing
        
        if size_clothing != None or color_clothing != None or price_from != None or price_to != None:
            return [FollowupAction("action_buy_fashions")]
        
        #Get categories with words: UPPER_BODY, LOWER_BODY, FULL_BODY
        category_type = []
        if category_type_clothing != None:
            category_type = query_dictionary_by_word(category_type_clothing)
        
        #Get categories with words in list dictionaries defined in database
        category_clothing = []
        if clothing != None:
            category_clothing = query_dictionary_by_word(clothing)
            name_clothing = clothing
            
        #Merger all list categories
        categories = category_type
        if clothing != None:
            categories = filter_duplicate_in_array(category_clothing)
            
        products = get_products_with_categories(categories)
        dispatcher.utter_message(text='Hiện tại ({}) bên Shop còn {} sản phẩm. Cho Shop hỏi bạn chọn ({}) như thế nào ạ!'.format(name_clothing, len(products), name_clothing))
        return []


class ActionDefaultFallback(Action):
    def name(self) -> Text:
        return "action_default_fallback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(text='Xin lỗi tôi chưa hiểu ý của bạn. Vui lòng cho câu hỏi rõ hơn!')
        return []