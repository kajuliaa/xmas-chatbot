from actions.dialogue_util import DialogueAction, DialogueType

class DeclareRecipe(DialogueAction):
  action_type = DialogueType.DECLARE_RECIPE
  sentences = [
    f"These are the kitchen staples you'll need to make the best chocolate chip cookies of your life: 1 cup butter (softened), 1cup white sugar, 1 cup packed brown sugar, 2 large eggs, 2 teaspoons vanilla extract, 1 teaspoon baking soda, 2 teaspoons hot water, 0.5 teaspoon salt, 3 cups flour, 2 cups chocolate chips, 1 cup chopped nuts.
    \n Here's a very brief overview of what you can expect when you make chocolate chip cookies from-scratch:
    \n1.Beat the butter and sugars, then beat in the eggs and vanilla.
    \n2.Dissolve the baking soda in hot water and add to the mixture.
    \n3.Stir in the flour, chocolate chips, and walnuts.
    \n4.Drop dough onto a prepared baking sheet.
    \n5.Bake until the edges are golden brown.",
    f"Ingredients: 1 cup peanut butter, 1 cup sugar, 1 large egg
    \n Combine the ingredients, roll the dough into balls, make a criss-cross pattern with a fork, and bake until the edges are firm. That’s all there is to it! "
  ]
  def __init__(self):
        super().__init__(self.action_type, self.sentences)