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