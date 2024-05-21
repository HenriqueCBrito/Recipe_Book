class RecipeBook:
    def __init__(self):
        self.recipes = []
        self.recipes_favorite = []
        self.load_recipes()

    def load_recipes(self):
        self.recipes = self.load_from_txt('database.txt')
        self.recipes_favorite = self.load_from_txt('database_favorite.txt')

    
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
    
    def save_to_txt(self, filename, recipes):
        with open(filename, 'w', encoding='utf-8') as f:
            for recipe in recipes:
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
    
    def add_to_favorites(self, recipe_name):
        for recipe in self.recipes:
            if recipe['name'] == recipe_name:
                self.recipes_favorite.append(recipe)
                self.save_to_txt('database_favorite.txt', self.recipes_favorite)
                print(f"Recipe '{recipe_name}' added to favorites.")
                return
        print("Recipe not found.")
    
    def print_recipes(self, recipes):
        for recipe in recipes:
            print(f"""
Name: {recipe['name']}

Country: {recipe['country']}

Serves: {recipe['serves']}

Time (mins): {recipe['time']}

Ingredients: {recipe['ingredients']}

Description: {recipe['description']}

***********************************************""")