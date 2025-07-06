import os
import json

# Function to load favorites from a file
def load_favorites():
    filename = "favorites.json"
    favorites = {}
    if os.path.exists(filename):
        with open(filename, "r") as f:
            favorites = json.load(f)
    else:
        favorites = {
            "color": "blue",
            "food": "pizza",
            "movie": "Interstellar"
        }
    return favorites

# Function to save favorites to a file
def save_favorites(favorites):
    filename = "favorites.json"
    with open(filename, "w") as f:
        json.dump(favorites, f, indent=4)

# Function to display all favorites
def display_favorites(favorites):
    print("\nHere are all your favorites:")
    for category, favorite in favorites.items():
        print(f"{category}: {favorite}")

# Function to look up a favorite
def lookup_favorite(favorites, category):
    if category in favorites:
        result = f"My favorite {category} is {favorites[category]}!"
    else:
        result = f"Sorry, the category '{category}' is not available."

    print(result)  # Still print to the console
    return result  # Also return the result for testing

# Function to add a new favorite
def add_favorite(favorites, category, favorite):
    if category in favorites:
        print(f"The category '{category}' already exists.")
    else:
        favorites[category] = favorite
        print(f"{category} added with favorite {favorite}!")

# Function to update an existing favorite
def update_favorite(favorites, category, new_favorite):
    if category in favorites:
        favorites[category] = new_favorite
        print(f"{category} updated to {new_favorite}!")
    else:
        print(f"Sorry, the category '{category}' does not exist.")

# Function to delete a favorite
def delete_favorite(favorites, category):
    if category in favorites:
        del favorites[category]
        print(f"{category} has been deleted.")
    else:
        print(f"Sorry, the category '{category}' does not exist.")

# Main loop for continuous interaction
def main():
    favorites = load_favorites()

    while True:
        print("\nAvailable categories:", ", ".join(favorites.keys()))
        action = input("\nWhat would you like to do? (lookup/add/update/delete/quit): ").lower()

        if action == "lookup":
            category = input("Enter a category to look up: ")
            lookup_favorite(favorites, category)
        
        elif action == "add":
            category = input("Enter new category: ")
            favorite = input(f"Enter your favorite for {category}: ")
            add_favorite(favorites, category, favorite)
        
        elif action == "update":
            category = input("Which category would you like to update? ")
            new_favorite = input(f"Enter your new favorite for {category}: ")
            update_favorite(favorites, category, new_favorite)
        
        elif action == "delete":
            category = input("Which category would you like to delete? ")
            delete_favorite(favorites, category)
        
        elif action == "quit":
            save_favorites(favorites)
            print("Goodbye!")
            break
        
        else:
            print("Invalid option. Please choose a valid action.")
        
        save_favorites(favorites)

if __name__ == "__main__":
    main()
