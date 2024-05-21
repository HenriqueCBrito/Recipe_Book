# Recipe_Book

A console-based recipe book application that allows users to add, view, delete, modify, and randomly suggest recipes. Users can also manage favorite recipes and search recipes based on various criteria.

## Features

- Add new recipes to the recipe book.
- Add recipes to favorites.
- View all recipes.
- View recipes filtered by country, number of serves, time, and ingredients.
- View favorite recipes.
- Delete specific recipes or all recipes from a specific country.
- Modify existing recipes.
- Get a random recipe suggestion.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:
   
   git clone https://github.com/HenriqueCBrito/Recipe_Book.git
   cd Recipe_Book

## Usage

### Menu Options

1. **Add Recipe**:
   - Add a new recipe by providing details such as name, country, serves, time, ingredients, and description.
   - Add an existing recipe to the favorites list.

2. **Show Recipes**:
   - Show all recipes.
   - Show recipes filtered by country.
   - Show recipes filtered by the number of serves.
   - Show recipes filtered by preparation time.
   - Show recipes filtered by ingredients.
   - Show favorite recipes.

3. **Delete Recipe**:
   - Delete a specific recipe by name.
   - Delete all recipes from a specific country.

4. **Modify Recipe**:
   - Modify details of an existing recipe.

5. **Get Random Recipe**:
   - Get a random recipe suggestion from the pre-defined random recipes list.

0. **Exit**:
   - Exit the application.

## Example

======= Recipe Book Menu =======
1. Add Recipe
2. Show Recipes
3. Delete Recipe
4. Modify Recipe
5. Get Random Recipe
0. Exit
Enter your choice: 1

======= Add Options =======
1. Add Recipe
2. Add Recipe to Favorites
Enter your choice: 1
Enter recipe name: Spaghetti Bolognese
Enter country: Italy
Enter number of serves: 4
Enter time to prepare (in minutes): 45
Enter recipe ingredients: spaghetti, minced meat, tomato sauce
Enter recipe description: A classic Italian pasta dish.
Recipe added successfully!

## File Structure

- `main.py`: The Python script containing the main function.
- `commands.py`: The Python script containing the RecipeBook class
- `database.txt`: Stores all recipes.
- `database_favorite.txt`: Stores favorite recipes.
- `database_random.txt`: Stores random recipes.