def cakes(recipe, available):
    max_cakes = float('inf')  # Initialize with infinity
    for ingredient, amount in recipe.items():
        if ingredient not in available:
            return 0  # If any required ingredient is missing, return 0
        max_cakes = min(max_cakes, available[ingredient] // amount)
    return max_cakes

# Test cases
print(cakes({'flour': 500, 'sugar': 200, 'eggs': 1}, {'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200}))  # Output: 2
print(cakes({'apples': 3, 'flour': 300, 'sugar': 150, 'milk': 100, 'oil': 100}, {'sugar': 500, 'flour': 2000, 'milk': 2000}))  # Output: 0
