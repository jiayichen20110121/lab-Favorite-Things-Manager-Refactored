import pytest
from stretch import add_favorite, lookup_favorite, update_favorite, delete_favorite, display_favorites
# Test the add_favorite function
def test_add_favorite():
    favorites = {"color": "blue"}
    add_favorite(favorites, "food", "pizza")
    assert favorites == {"color": "blue", "food": "pizza"}
    
    # Try adding a duplicate category
    add_favorite(favorites, "food", "sushi")
    assert favorites == {"color": "blue", "food": "pizza"}  # Should not change

# Test the lookup_favorite function
def test_lookup_favorite():
    favorites = {"color": "blue", "food": "pizza"}
    result = lookup_favorite(favorites, "color")
    assert result == "My favorite color is blue!"
    
    result = lookup_favorite(favorites, "movie")
    assert result == "Sorry, the category 'movie' is not available."

# Test the update_favorite function
def test_update_favorite():
    favorites = {"color": "blue", "food": "pizza"}
    update_favorite(favorites, "food", "sushi")
    assert favorites["food"] == "sushi"
    
    # Try updating a non-existent category
    update_favorite(favorites, "movie", "Inception")
    assert "movie" not in favorites  # Should not exist

# Test the delete_favorite function
def test_delete_favorite():
    favorites = {"color": "blue", "food": "pizza"}
    delete_favorite(favorites, "food")
    assert "food" not in favorites
    
    # Try deleting a non-existent category
    delete_favorite(favorites, "movie")
    assert "movie" not in favorites

# Optional: Test display_favorites function (using capfd to capture the output)
def test_display_favorites(capfd):
    favorites = {"color": "blue", "food": "pizza"}
    display_favorites(favorites)
    captured = capfd.readouterr()
    assert "color: blue" in captured.out
    assert "food: pizza" in captured.out
