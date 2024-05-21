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
    
    def save_to_txt(self):
        with open('database.txt', 'w') as f:
            for recipe in self.recipes:
                f.write(f"{recipe['name']}/{recipe['country']}/{recipe['serves']}/{recipe['time']}/{recipe['ingredients']}/{recipe['description']}/\n")
    
    def add_recipe(self, name, country, serves, time, ingredients, description):
        recipe = {
            'name': name,
            'country': country,
            'serves': serves,
            'time': time,
            'ingredients': ingredients,
            'description': description,
        }
        self.recipes.append(recipe)
        self.save_to_txt('database.txt', self.recipes)