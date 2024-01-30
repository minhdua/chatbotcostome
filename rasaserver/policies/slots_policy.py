from rasa.engine.graph import GraphComponent, ExecutionContext
from rasa.engine.storage.resource import Resource
from rasa.engine.storage.storage import ModelStorage
from rasa.shared.core.trackers import DialogueStateTracker
from rasa_sdk import Tracker
from rasa.shared.core.domain import Domain
from rasa.shared.core.events import UserUttered, BotUttered
from rasa.engine.recipes.default_recipe import DefaultV1Recipe
from typing import List, Dict, Text, Any
from rasa.shared.nlu.training_data.training_data import TrainingData
from rasa.shared.nlu.interpreter import NaturalLanguageInterpreter
from rasa.core.policies.policy import PolicyPrediction
from typing import Optional
import requests
from actions.utils import get_confidence_max, get_entity_value

FLASK_API_URL = "http://127.0.0.1:5000"
FLASK_STATISTICS_API_URL = f"{FLASK_API_URL}/history"
@DefaultV1Recipe.register(
    [DefaultV1Recipe.ComponentType.POLICY_WITHOUT_END_TO_END_SUPPORT], is_trainable=True
)
class SlotsPolicy(GraphComponent):
    def __init__(self, config: Dict[Text, Any]):
        self.config = config

    def predict_action_probabilities(
        self,
        tracker: Tracker,
        domain: Domain,
        rule_only_data: Optional[Dict[Text, Any]] = None,
        **kwargs: Any,
    ) -> PolicyPrediction:
        
        entities_filters = get_confidence_max(tracker.latest_message.entities)
        
        entities_values = get_entity_value(entities_filters, tracker.latest_message.text)
        
        # for entity in entities_values:
        #     if tracker.slots['clothing'] and tracker.slots['clothing'].mappings[0]['entity'] == entity['entity']:
        #         tracker.slots['clothing'].value = entity['value']
        #     if tracker.slots['category_type_clothing'] and tracker.slots['category_type_clothing'].mappings[0]['entity'] == entity['entity']:
        #         tracker.slots['category_type_clothing'].value = entity['value']
        #     if tracker.slots['size_clothing'] and tracker.slots['size_clothing'].mappings[0]['entity'] == entity['entity']:
        #         tracker.slots['size_clothing'].value = entity['value']
        #     if tracker.slots['color_clothing'] and tracker.slots['color_clothing'].mappings[0]['entity'] == entity['entity']:
        #         tracker.slots['clothing'].value = entity['value']
        #     if tracker.slots['price_from'] and tracker.slots['price_from'].name == entity['entity']:
        #         tracker.slots['price_from'].value = entity['value']
        #     if tracker.slots['price_to'] and tracker.slots['price_to'].name == entity['entity']:
        #         tracker.slots['price_to'].value = entity['value']

        return PolicyPrediction.for_action_name(domain, tracker.latest_action['action_name'])

    def _metadata(self) -> Dict[Text, Any]:
        return {"lookup": self.lookup}
    

    def train(self, training_data: TrainingData, domain: Domain) -> Resource:
        # This method is called during the training phase
        # You can add any training code here if necessary
        return Resource(self.__class__.__name__)