from actions.dialogue_util import DialogueAction, DialogueType


class Greet(DialogueAction):
    action_type = DialogueType.GREET

    sentences = [
        'Hi.',
        "Hello, nice to meet you.",
        "Ho ho ho!",
        "Hello my dear friend!"
    ]

    def __init__(self):
        super().__init__(self.action_type, self.sentences)
