from commands import RecipeBook

def main():
    recipe_book = RecipeBook()
    show_options = ['Add Recipe', 'Show Recipes', 'Delete Recipe', 'Modify Recipe', 'Get Random Recipe']

    while True:
        
            print("\n======= Recipe Book Menu =======")
            for idx, option in enumerate(show_options, start=1):
                print(f"{idx}. {option}")
            print("0. Exit")

            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print('Invalid choice. Choose a number between 0 and 5.')
                continue
            if choice == 1:
                while True:
                    print("\n======= Add Options =======")
                    print("1. Add Recipe")
                    print("2. Add Recipe to Favorites")
                    try:
                        sub_choice = int(input("Enter your choice: "))
                    except ValueError:
                        print('Invalid input. Please enter an integer.')
                        continue

                    if sub_choice == 1:
                        name = input("Enter recipe name: ")
                        country = input("Enter country: ")
                        while True:
                            try:
                                serves = int(input("Enter number of serves: "))
                                break
                            except ValueError:
                                print("Invalid input for number of serves. Please enter an integer.")
                        while True:
                            try:
                                time = int(input("Enter time to prepare (in minutes): "))
                                break
                            except ValueError:
                                print("Invalid input for time to prepare. Please enter an integer.")
                        ingredients = input("Enter recipe ingredients: ")
                        description = input("Enter recipe description: ")
                        recipe_book.add_recipe(name, country, serves, time, ingredients, description)
                        break
                    elif sub_choice == 2:
                        recipe_name = input("Enter recipe name to add to favorites: ")
                        recipe_book.add_to_favorites(recipe_name)
                        break
                    else:
                        print('Invalid input. Choose an integer between 1 and 2.')
                        
            elif choice == 2:
                while True:
                    print("\n======= Show Options =======")
                    print("1. Show All Recipes")
                    print("2. Show Recipes by Country")
                    print("3. Show Recipes by Number of Serves")
                    print("4. Show Recipes by Time")
                    print("5. Show Recipes by Ingredient")
                    print("6. Show Favorite Recipes")
                    try:
                        sub_choice = int(input("Enter your choice: "))
                    except ValueError:
                        print('Invalid input. Please enter an integer.')
                        continue
                    if sub_choice == 1:
                        recipe_book.show_all_recipes()
                        break
                    elif sub_choice == 2:
                        country = input("Enter country: ")
                        recipe_book.show_by_country(country)
                        break
                    elif sub_choice == 3:
                        serves = int(input("Enter number of serves: "))
                        recipe_book.show_by_serves(serves)
                        break
                    elif sub_choice == 4:
                        time = int(input("Enter maximum time (in minutes): "))
                        recipe_book.show_by_time(time)
                        break
                    elif sub_choice == 5:
                        ingredient = input("Enter ingredient: ")
                        recipe_book.show_by_ingredient(ingredient)
                        break
                    elif sub_choice == 6:
                        recipe_book.show_favorite_recipes()
                        break
                    else:
                        print('Invalid input. Choose an integer between 1 and 6.')
                        
            elif choice == 3:
                while True:
                    print("\n======= Delete Options =======")
                    print("1. Delete Recipe")
                    print("2. Delete All Recipes from a Country")

                    try:
                        sub_choice = int(input("Enter your choice: "))
                    except ValueError:
                        print('Invalid input. Please enter an integer.')
                        continue

                    if sub_choice == 1:
                        recipe_name = input("Enter recipe name to delete: ")
                        recipe_book.delete_recipe(recipe_name)
                        break
                    elif sub_choice == 2:
                        country = input("Enter country to delete all recipes from: ")
                        recipe_book.delete_all_from_country(country)
                        break
                    else:
                        print('Invalid input. Choose an integer between 1 and 2.')