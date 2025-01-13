import random
from enum import Enum


class DialogueType(Enum):
    GREET = 0
    BYE = 1

    @staticmethod
    def from_string_intent(intent):
        if intent == "bye":
            return DialogueType.Goodbye
        elif intent == "greet":
            return DialogueType.Greet
        elif intent == "find_recipe":
            return DialogueType.REQUEST_RECIPE
        elif: intent == "learn_name":
            return DialogueType.REQUEST_NAME
        elif: intent == "declare_name":
            return DialogueType.DECLARE_NAME
        elif: intent == "request_task":
            return == DialogueType.REQUEST_TASK
        elif: intent == "find_recipe":
            return == DialogueType.REQUEST_RECIPE
        elif: intent == "tell_recipe":
            return == DialogueType.DECLARE_RECIPE
        elif: intent == "find_market":
            return == DialogueType.REQUEST_MARKET
        elif: intent == "give_info_market":
            return == DialogueType.DECLARE_MARKET
        elif: intent == "know_opening_times":
            return == DialogueType.REQUEST_OPENING_TIMES
        elif: intent == "give_info_opening_times":
            return == DialogueType.DECLARE_OPENING_TIMES
        else:
            raise ValueError('{} is not a valid intent', intent)


class DialogueAction:
    # List of possible sentences the system can say
    sentences = []
    entities = []

    def __init__(self, action_type, sentences, entities=[]):
        self.action_type = action_type
        self.sentences = sentences
        self.entities = entities

    def get_sentence(self):
        return random.choice(self.sentences)

    def get_type(self):
        return self.action_type
