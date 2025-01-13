from actions.dialogue_util import DialogueAction, DialogueType


class Bye(DialogueAction):
    action_type = DialogueType.BYE

    sentences = [
        'Bye.',
        "See you.",
        "Goodbye. Have a nice day",
        "Have a nice day.",
        "Goodbye and merry Christmas to you!"
    ]

    def __init__(self):
        super().__init__(self.action_type, self.sentences)



