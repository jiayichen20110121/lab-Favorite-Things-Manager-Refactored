import os

# Function to load favorites from a file
def load_favorites():
    filename = "favorites.txt"
    favorites = {}
    if os.path.exists(filename):
        with open(filename, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    category, favorite = line.split(":", 1)
                    favorites[category.strip()] = favorite.strip()
    else:
        favorites = {
            "color": "blue",
            "food": "pizza",
            "movie": "Interstellar"
        }
    return favorites

# Function to save favorites to a file
def save_favorites(favorites):
    filename = "favorites.txt"
    with open(filename, "w") as f:
        for category, favorite in favorites.items():
            f.write(f"{category}: {favorite}\n")

# Function to display all favorites
def display_favorites(favorites):
    print("\nHere are all your favorites:")
    for category, favorite in favorites.items():
        print(f"{category}: {favorite}")

# Function to look up a favorite
def lookup_favorite(favorites):
    category = input("Enter a category to look up: ")
    if category in favorites:
        print(f"My favorite {category} is {favorites[category]}!")
    else:
        print(f"Sorry, the category '{category}' is not available.")

# Function to add a new favorite
def add_favorite(favorites):
    new_category = input("Enter new category: ")
    new_favorite = input(f"Enter your favorite for {new_category}: ")
    favorites[new_category] = new_favorite
    print(f"{new_category} added with favorite {new_favorite}!")

# Function to update an existing favorite
def update_favorite(favorites):
    category = input("Which category would you like to update? ")
    if category in favorites:
        new_favorite = input(f"Enter your new favorite for {category}: ")
        favorites[category] = new_favorite
        print(f"{category} updated to {new_favorite}!")
    else:
        print(f"Sorry, the category '{category}' does not exist.")

# Function to delete a favorite
def delete_favorite(favorites):
    category = input("Which category would you like to delete? ")
    if category in favorites:
        del favorites[category]
        print(f"{category} has been deleted.")
    else:
        print(f"Sorry, the category '{category}' does not exist.")

# Main loop for continuous interaction
def main():
    # Load the favorites dictionary
    favorites = load_favorites()

    while True:
        # Display available categories
        print("\nAvailable categories:", ", ".join(favorites.keys()))

        # Ask what action to take
        action = input("\nWhat would you like to do? (lookup/add/update/delete/quit): ").lower()

        if action == "lookup":
            lookup_favorite(favorites)
        
        elif action == "add":
            add_favorite(favorites)
        
        elif action == "update":
            update_favorite(favorites)
        
        elif action == "delete":
            delete_favorite(favorites)
        
        elif action == "quit":
            save_favorites(favorites)  # Save changes before quitting
            print("Goodbye!")
            break
        
        else:
            print("Invalid option. Please choose a valid action.")
        
        # Save the dictionary to the file after every operation
        save_favorites(favorites)

# Run the program
if __name__ == "__main__":
    main()