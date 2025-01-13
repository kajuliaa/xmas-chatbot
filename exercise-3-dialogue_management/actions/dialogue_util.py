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
        elif intent == "find_cookies":
            return DialogueType.REQUEST_RECIPE
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
