from actions.dialogue_util import DialogueAction, DialogueType

class DeclareMarket(DialogueAction):
  action_type = DialogueType.DECLARE_OPENING_TIMES
  sentences =[
    "Opening times are from 16 to 23"
    "You can visit christmas market from 16 to 23"
  ]
  def __init__(self):
    super().__init__(self.action_type, self.sentences)