import json
from rasa.engine.graph import GraphComponent, ExecutionContext
from rasa.engine.storage.resource import Resource
from rasa.engine.storage.storage import ModelStorage
from rasa.shared.core.trackers import DialogueStateTracker
from rasa.shared.core.domain import Domain
from rasa.shared.core.events import UserUttered, BotUttered
from rasa.engine.recipes.default_recipe import DefaultV1Recipe
from rasa.shared.nlu.training_data.training_data import TrainingData
from rasa.shared.nlu.interpreter import NaturalLanguageInterpreter
from rasa.core.policies.policy import PolicyPrediction
from typing import Optional, Dict, Text, Any
from actions.db_operations import insert_data
from actions.utils import find_element_nlus, read_json_file

@DefaultV1Recipe.register(
    [DefaultV1Recipe.ComponentType.POLICY_WITHOUT_END_TO_END_SUPPORT], is_trainable=True
)
class ConversationLoggingPolicy(GraphComponent):
    def __init__(self, config: Dict[Text, Any]):
        self.config = config

    def predict_action_probabilities(
        self,
        tracker: DialogueStateTracker,
        domain: Domain,
        rule_only_data: Optional[Dict[Text, Any]] = None,
        **kwargs: Any,
    ) -> PolicyPrediction:
        
        nlus = read_json_file('data/nlu.json');
        data_obj = find_element_nlus(nlus, tracker.latest_message.text)
        
        user_id = ""
        user_say = tracker.latest_message.text
        if data_obj != None:
            user_id = data_obj['user_id']
            user_say = data_obj['user_say']
        
        slots = {
            "clothing": tracker.slots['clothing'].value,
            "category_type_clothing": tracker.slots['category_type_clothing'].value,
            "color_clothing": tracker.slots['color_clothing'].value,
            "size_clothing": tracker.slots['size_clothing'].value,
            "price_from": tracker.slots['price_from'].value,
            "price_to": tracker.slots['price_to'].value
        }
        
        data = {
            "user_id": user_id,
            "user_say": user_say,
            "intent": tracker.latest_message.intent_name,
            "slots": json.dumps(slots, ensure_ascii=True)
        }
        insert_data(data, "history_nlus")
        
        return PolicyPrediction.for_action_name(domain, "action_listen")

    def _metadata(self) -> Dict[Text, Any]:
        return {"lookup": self.lookup}
    

    def train(self, training_data: TrainingData, domain: Domain) -> Resource:
        # This method is called during the training phase
        # You can add any training code here if necessary
        return Resource(self.__class__.__name__)
