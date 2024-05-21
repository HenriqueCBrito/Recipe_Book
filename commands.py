import random

class RecipeBook:
    
    def __init__(self):
        self.recipes = []
        self.recipes_favorite = []
        self.recipes_random = []
        self.load_recipes()

    def load_recipes(self):
        self.recipes = self.load_from_txt('database.txt')
        self.recipes_favorite = self.load_from_txt('database_favorite.txt')
        self.recipes_random = self.load_from_txt('database_random.txt')

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

    def show_all_recipes(self):
        if self.recipes:
            print("\nAll Recipes:")
            self.print_recipes(self.recipes)
        else:
            print("No recipes found.")

    def show_by_country(self, country):
        print(f"Recipes from {country}:")
        found = False
        for recipe in self.recipes:
            if recipe['country'].lower() == country.lower():
                found = True
                print(f"""
Name: {recipe['name']}
                      
Country: {recipe['country']}

Serves: {recipe['serves']}

Time (mins): {recipe['time']}

Ingredients: {recipe['ingredients']}

Description: {recipe['description']}

***********************************************""")
        if not found:
            print("No recipes found for the given country.")

    def show_by_serves(self, serves):
        print(f"Recipes serving {serves} people:")
        found = False
        for recipe in self.recipes:
            if recipe['serves'] == serves:
                found = True
                print(f"""
Name: {recipe['name']}
                      
Country: {recipe['country']}

Serves: {recipe['serves']}

Time (mins): {recipe['time']}

Ingredients: {recipe['ingredients']}

Description: {recipe['description']}

***********************************************""")
        if not found:
            print("No recipes found for the given number of serves.")

    def show_by_time(self, time):
        print(f"Recipes taking {time} minutes or less to prepare:")
        found = False
        for recipe in self.recipes:
            if recipe['time'] <= time:
                found = True
                print(f"""
Name: {recipe['name']}
                      
Country: {recipe['country']}

Serves: {recipe['serves']}

Time (mins): {recipe['time']}

Ingredients: {recipe['ingredients']}

Description: {recipe['description']}

***********************************************""")
        if not found:
            print("No recipes found within the given time.")
            
    def show_by_ingredient(self, ingredient):
        print(f"Recipes containing {ingredient} as a ingredient:")
        found = False
        for recipe in self.recipes:
            if ingredient in recipe['ingredients']:
                found = True
                print(f"""
Name: {recipe['name']}
                      
Country: {recipe['country']}

Serves: {recipe['serves']}

Time (mins): {recipe['time']}

Ingredients: {recipe['ingredients']}

Description: {recipe['description']}

***********************************************""")
        if not found:
            print("No recipes found with the given ingredient.")

    def show_favorite_recipes(self):
        if self.recipes_favorite:
            print("Favorite Recipes:")
            self.print_recipes(self.recipes_favorite)
        else:
            print("No favorite recipes found.")

    def delete_recipe(self, recipe_name):
        self.recipes = [r for r in self.recipes if r['name'] != recipe_name]
        self.recipes_favorite = [r for r in self.recipes_favorite if r['name'] != recipe_name]
        self.save_to_txt('database.txt', self.recipes)
        self.save_to_txt('database_favorite.txt', self.recipes_favorite)
        print(f"Recipe '{recipe_name}' deleted.")

    def delete_all_from_country(self, country):
        self.recipes = [r for r in self.recipes if r['country'].lower() != country.lower()]
        self.recipes_favorite = [r for r in self.recipes_favorite if r['country'].lower() != country.lower()]
        self.save_to_txt('database.txt', self.recipes)
        self.save_to_txt('database_favorite.txt', self.recipes_favorite)
        print(f"All recipes from '{country}' deleted.")

    def modify_recipe(self, recipe_name, new_name=None, new_country=None, new_serves=None, new_time=None, new_ingredients=None, new_description=None, ):
        recipe_found = False
        for recipe in self.recipes:
            if recipe['name'] == recipe_name:
                if new_name:
                    recipe['name'] = new_name
                if new_country:
                    recipe['country'] = new_country
                if new_serves:
                    recipe['serves'] = new_serves
                if new_time:
                    recipe['time'] = new_time
                if new_ingredients:
                    recipe['ingredients'] = new_ingredients
                if new_description:
                    recipe['description'] = new_description
                self.save_to_txt("database.txt", self.recipes)
                print(f"Recipe '{recipe_name}' modified successfully.")
                recipe_found = True
                continue
            
        for recipe in self.recipes_favorite:
            if recipe['name'] == recipe_name:
                if new_name:
                    recipe['name'] = new_name
                if new_country:
                    recipe['country'] = new_country
                if new_serves:
                    recipe['serves'] = new_serves
                if new_time:
                    recipe['time'] = new_time
                if new_ingredients:
                    recipe['ingredients'] = new_ingredients
                if new_description:
                    recipe['description'] = new_description
                self.save_to_txt("database_favorite.txt", self.recipes_favorite)
                print(f"Recipe '{recipe_name}' modified successfully in favorites.")
                return
        if recipe_found == False:
            print("Recipe not found.")


    def random_suggestion(self):
        if self.recipes_random:
            random_recipe = random.choice(self.recipes_random)
            print(f"""
Name: {random_recipe['name']}

Country: {random_recipe['country']}

Serves: {random_recipe['serves']}

Time (mins): {random_recipe['time']}

Ingredients: {random_recipe['ingredients']}

Description: {random_recipe['description']}""")
        else:
            print("No random recipes available.")