class Solution:

    def __init__(self):
        self.supplies_dict = {}
        self.recipies_dict = {}
        self.ingredients_dict = {}

    def ingredient_in_supplies(self, ingredient) -> bool:

        print(ingredient)
        if ingredient in self.supplies_dict and self.supplies_dict[ingredient] == 1:
            return True

        if ingredient in self.supplies_dict and self.supplies_dict[ingredient] == -1:
            return False

        if ingredient in self.recipies_dict:
            self.supplies_dict[ingredient] = -1
            create_recipie = True
            for ing in self.recipies_dict[ingredient]:
                create_recipie = create_recipie and self.ingredient_in_supplies(ing)
                if not create_recipie:
                    return False

            if create_recipie:
                self.supplies_dict[ingredient] = 1
            else:
                self.supplies_dict[ingredient] = 0

            return create_recipie
        else:
            return False

    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:

        for i in range(len(recipes)):
            self.recipies_dict[recipes[i]] = tuple(ingredients[i])

        for sup in supplies:
            self.supplies_dict[sup] = 1

        result = []
        for rec in recipes:
            if self.ingredient_in_supplies(rec):
                result.append(rec)

        return result





