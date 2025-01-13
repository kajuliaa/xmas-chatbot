from actions.dialogue_util import DialogueAction, DialogueType

class DeclareMarket(DialogueAction):
  action_type = DialogueType.DECLARE_MARKET
  sentences =[
    "Nearest market is on Maxplatz"
    "Maxplatz, Bamberg"
  ]
  def __init__(self):
    super().__init__(self.action_type, self.sentences)