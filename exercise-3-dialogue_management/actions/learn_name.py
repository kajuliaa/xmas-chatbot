from actions.dialogue_util import DialogueAction, DialogueType

class LearnName(DialogueAction):
    action_type = DialogueType.REQUEST_NAME

    sentences = [
      "Hello! What is you name?",
      "How can I call you?",
      "What is the name of such cute person?"
      "You are so cute! What is your name?"
    ]
    def __init__(self):
        super().__init__(self.action_type, self.sentences)