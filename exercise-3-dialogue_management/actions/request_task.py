from actions.dialogue_util import DialogueAction, DialogueType

class RequestTask(DialogueAction):
    action_type = DialogueType.REQUEST_TASK

    sentences = [
      "What do you want to know?"
      "What can I do for you?"
    ]

    def __init__(self):
      super().__init__(self.action_type, self.sentences)