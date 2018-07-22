"""
Fantasy_Game_Inventory.py

Author: Darryl Ramgoolam

This python script will emulate a players inventory in a fantasy game.
The data structure to model the player’s inventory will be a dictionary
where the keys are string values describing the item in the inventory 
and the value is an integer value detailing how many of that item 
the player has

"""

def displayInventory(inventory):
    print('\nInventory:')
    item_total = 0

    # print the keys and key values from inventory 
    for keys , values in inventory.items():
        print (str(values) + ' ' + str(keys))
        item_total = item_total + values

    # print total number of items
    print('\nTotal number of items: ' + str(item_total))

def addToInventory(inventory, addedItems):

    # Itimized the added Items list
    for items in addedItems:

        # If it's a new item, add it to the inventory defualted at 0
        inventory.setdefault(items,0)

        # if item is already in inventory incriment by one
        inventory[items] = inventory[items] + 1

    return inventory


def main():
    
    Current_Inventory ={'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

    displayInventory(Current_Inventory)

    #new_inventory = {'gold coin': 42, 'rope': 1}
    dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    new_inventory = addToInventory(Current_Inventory, dragonLoot)

    displayInventory(new_inventory)

if __name__ == "__main__":
    main()