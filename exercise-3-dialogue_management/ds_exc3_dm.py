from actions.bye import Bye
from actions.dialogue_util import DialogueType
from actions.greet import Greet

"""
Dialogue Manager takes care of the whole dialogue flow. It requests next 
"""

class DialogueManager(object):
    dialogue_ongoing = True

    def get_next_user_move(self):
        """
        Gets user input from console
        and hands the input to RASA NLU server

        :return: Next User Move as DialogueAction
        """
        # TODO: Get Input from Console (see exercise 2)
        # TODO: Get Intent classification from RASA Server (see exercise 2)
        # TODO: Map Intent & Entities of the user to a DialogueAction and return it
        user_move = Bye()
        return user_move

    def get_next_system_move(self, user_move):
        """
        Based on the previous user move
        this method selects a suitable system move.

        :param user_move: Previous User Move
        :return: Next System Move as DialogueAction
        """
        # If no user move is given, the system starts with a Greet
        if user_move is None:
            return Greet()
        # If the user says goodbye, dialogue will be ended.
        if user_move.get_type() == DialogueType.BYE:
            self.dialogue_ongoing = False
            return Bye()

        # TODO: Create System Logic and choose correct system reply.

        system_move = None
        return system_move

    def handle_dialogue(self):
        """
            Handles dialogue flow. First system will greet.
            Afterwards the dialogue is mostly user driven.
        """
        # First user move is None
        # The system should start with a greeting.
        system_greet = self.get_next_system_move(None)
        print("S:", system_greet.get_sentence())

        while self.dialogue_ongoing:
            user_move = self.get_next_user_move()
            print("U:", user_move.get_sentence())
            system_move = self.get_next_system_move(user_move)
            print("S:", system_move.get_sentence())


DialogueManager().handle_dialogue()
