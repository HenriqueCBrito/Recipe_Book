class RecipeBook:
    def __init__(self):
        self.recipes = []
        self.load_recipes()

    def load_recipes(self):
        self.recipes = self.load_from_txt('database.txt')
    
    def load_from_txt(self, filename):
        recipes = []
        try:
            with open(filename, encoding='utf-8') as f:
                for line in f:
                    recipe_data = line.strip().split('/')
                    recipe = {
                        'name': recipe_data[0],
                        'country': recipe_data[1],
                        'serves': int(recipe_data[2]),
                        'time': int(recipe_data[3]),
                        'ingredients': recipe_data[4],
                        'description': recipe_data[5],
                    }
                    recipes.append(recipe)
        except FileNotFoundError:
            pass
        return recipes
    