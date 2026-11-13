import random as r
from pathlib import Path
gold = 10
day = 0
prestige = 0
persuasion = 0

def main_menu():
    input()

""" 
class Item:
    name1: str
    catagory1: str
    base_buy_value1: int
 """

class Item:
    def __init__(self, name, rarity, catagory, base_buy_value, base_sell_value, info, prestige=0, persuasion=0, abilities=None):
        self.name = name
        self.rarity = rarity
        self.catagory = catagory
        self.base_buy_value = base_buy_value
        self.base_sell_value = base_sell_value
        self.info = info
        self.prestige = prestige
        self.persuasion = persuasion
        self.abilities = abilities


# All items
Commen_Items = [
    Item("Baseball Cap", "Commen", "Clothing", 3, 2, "Just a stylish Baseball Cap", persuasion=1),
    Item("Old Wooden Chair", "Commen", "Furniture", 3, 2, "Your mothers Old Wooden Chair")
]
Uncommen_Items = [
    Item("Yamasks Mask", "Uncommen", "Clothing", 10, 7, "Found in a dumpster outside a therapy clinic", prestige=10)
]
Rare_Items = [
    Item("Fedora", "Rare", "Clothing", 15, 12, "Worn by a beaver, a cool beaver", persuasion=25)
]
Legendary_Items = [
    Item("Stylish Cactus", "Legendary", "Furniture", 25, 17, "The best item in the game. Ofc its a Cactus, what else did you expect?", prestige=75),
    Item("Lebrons Basketball", "Legendary", "Tool", 50, 40, "Lebron Lebron Lebroooooonnn, Lebron", prestige=20)
]

inventory = [

]

for item in inventory:
    prestige += item.prestige

for item in inventory:
    persuasion += item.persuasion

def item_stats(choosen_item):
# "\033[A" printer linjen en oppover
    print(f"¨¨{choosen_item.name}¨¨")
    print(f"Rarity: {choosen_item.rarity}")
    print(f"Itemtype: {choosen_item.catagory}")
    print(f"Worth: {choosen_item.base_sell_value} gold")

    if choosen_item.prestige > 0:
        print(f"Prestige: {choosen_item.prestige}")
    if choosen_item.persuasion > 0:
        print(f"Persuasion: {choosen_item.persuasion}")
    print(f'"{choosen_item.info}"')    

def view_inventory(inventory):
    while True:
        for i, Item in enumerate(inventory):
            print(f"{i + 1}: {Item.name}")
        try:
            element_item = int(input("""Which item do you want to inspect
press 0: to close: """))
            if element_item == 0:
                break
            else:
                choosen_item = inventory[element_item - 1]
                item_stats(choosen_item)
        except (ValueError, IndexError):
            print("Invalid item.")

def view_stats():
    while True:
        print("¨¨Stats¨¨")
        print(f"Gold: {gold}")
        print(f"Day: {day}")
        if prestige > 0:
            print(f"Prestige: {prestige}")
        if persuasion > 0:
            print(f"Persuasion: {persuasion}")

        print("Press 1: to view your inventory")
        print("Press 0: to exit stats")
        stats_action = input("> ")

        if stats_action == "1":
            view_inventory()
        elif stats_action == "0":
            break
        if stats_action == "1":
            view_inventory(inventory)
        elif stats_action == "0":
            break
        else:
            print("Invalid input")


BASE_DIR = Path(__file__).parent
NAMES_FILE = BASE_DIR / "Names.txt"

def load_names(filename):

    with open(filename, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]
    
names = load_names(NAMES_FILE)

Obsession = ["Furniture", "Clothing", "Tool", "Food", "Tech"]

class NPC:
    def __init__(self):
        self.name = r.choice(names)
        self.obsession = r.choice(Obsession)
        self.patience = r.randint(1,4)

class Merchant(NPC):
    def __init__(self):
        super().__init__()
        self.stock = r.randint(2,5)
        self.items_for_sale = self.merchant_inventory()

    def merchant_inventory(self):
        Merchant_inventory = []
        for i in range(self.stock):
            rarity = r.randint(1,20)
            if 10 > rarity >= 1:
                random_index = r.randint(0, len(Commen_Items)-1)
                Merchant_inventory.append(Commen_Items[random_index])
            elif 17 > rarity >= 10:
                random_index = r.randint(0, len(Uncommen_Items)-1)
                Merchant_inventory.append(Uncommen_Items[random_index])
            elif 20 > rarity >= 17:
                random_index = r.randint(0, len(Rare_Items)-1)
                Merchant_inventory.append(Rare_Items[random_index])
            elif rarity == 20:
                random_index = r.randint(0, len(Legendary_Items)-1)
                Merchant_inventory.append(Legendary_Items[random_index])
        return Merchant_inventory  

    def buy(self):
        global inventory, gold
        print(f'"Hi!, my name is {self.name}, and I was wondering if you would be interested in buying anything from me?"')
        while True:
            for i, Item in enumerate(self.items_for_sale):
                    print(f"{i + 1}: {Item.name}")
            try:
                element_item = int(input("""Which item do you want to look at? (type 0 to exit the NPC): """))
                if element_item == 0:
                    print('''"You dont want any more of my items?
I guess ill just have to find someone else to buy them, bye bye!"
*The NPC left*''')
                    break
                else:
                    choosen_item = self.items_for_sale[element_item - 1]
                    print(f'"Heres my {choosen_item.name}, I can give it to you for {choosen_item.base_buy_value} gold"')
                    item_stats(choosen_item)
                    choice = input(f"""Buy it for {choosen_item.base_buy_value} gold?
type: 1 for yes or 0 for no""")
                    if choice == "1":
                        inventory.append(choosen_item)
                        gold -= choosen_item.base_buy_value
                        del self.items_for_sale[element_item - 1]
                        print(f"You bought {choosen_item} for {choosen_item.base_buy_value} gold")
                    elif choice == "0":
                        print('"Ahh its ok, I have more things you can look at anyways"')
                        True
            except (ValueError, IndexError):
                print("Invalid item.")


class Costumer(NPC):
    def __init__(self):
        super().__init__()
        self.spending_limit = r.randint(2,4)
        

    def sell(self):
        global inventory, gold
        print(f'"Hey!, my name is {self.name}, and Im interested if you have anything in store for me?"')
        while True:
            for i, Item in enumerate(inventory):
                print(f"{i + 1}: {Item.name}")
            try:
                element_item = int(input("""Which item do you want to sell?: """))
                if element_item == 0:
                    print('''"You dont have anything Balright, well i guess ill get going then"''')
                    break
                else:
                    sold_item = inventory[element_item - 1]
                    gold_gained = sold_item.base_sell_value
                    gold += gold_gained
                    del inventory[element_item - 1]
                    print(f"You sold {sold_item.name} for {gold_gained} and now have {gold} gold")
            except (ValueError, IndexError):
                print("Invalid item.")

class Businessman(NPC):
    def __init__(self):
        super().__init__()
        self.deal = 1

NPCs = [
    Merchant(), Costumer()
]
def npc_action(npc):
    if type(npc) == Merchant:
        npc.merchant_inventory()
        npc.buy()
        print(1)
    elif type(npc) == Costumer:
        npc.sell()
        print(2)

daytime = True
while daytime == True:
    print(f"""Its Day {day} of owning the shop.
3 people are standing outside the shop""")
    number = 1
    for i in range(2):
        shop_action = input(f"""Press 1: Talk to the {number}. person standing infront of the shop
Press 0: View stats
""")
        if shop_action == "1":
            npc = NPCs[0]
            npc_action(npc)
        elif shop_action == "0":
            view_stats()
        else:
            print("Invalid input")
        number += 1
    daytime = False


print(gold)
print(persuasion)
print(prestige)

  
""" 
def NPC_action(i):
    if NPC[i] == Merchant(NPC):
        .sell()
 """

""" NPCs[0].sell() """

""" 
    base_sell_value / sell_action
 """

"""
tall = r.randint(100,200) / 100
"""