vegetables = ["tomatoes", "potatoes", "onions"]

vegetables.remove("onions")
vegetables.append("carrots")
vegetables.append("cucumbers")
vegetables.sort()
print(f"Updated Vegetable Inventory: {vegetables}")

if ("carrots" in vegetables) and ("cucumbers" in vegetables):
    print(f"Carrots are already in the list.")
    print(f"Cucumbers are already in the list.")
elif "carrots" in vegetables:
    print(f"Carrots are already in the list.")
elif "cucumbers" in vegetables:
    print(f"Cucumbers are already in the list.")
