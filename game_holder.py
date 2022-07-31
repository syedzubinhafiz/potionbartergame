from __future__ import annotations
# ^ In case you aren't on Python 3.10
from avl import AVLTree
from hash_table import LinearProbePotionTable
from potion import Potion
from random_gen import RandomGen


class Game:

    def __init__(self, seed=0) -> None:
        self.rand = RandomGen(seed=seed)
        self.stock = None
        self.hash_table = None

    def set_total_potion_data(self, potion_data: list) -> None:
        self.hash_table = LinearProbePotionTable(len(potion_data))
        for i in range(len(potion_data)):  # O(n)
            # Accessing data in the potion_data list, [Pot_Type, Name, Price]
            pot_type = potion_data[i][0]  # O(1)
            name = potion_data[i][1]  # O(1)
            price = potion_data[i][2]  # O(1)
            # Creating Potion class to be placed in the hash table (Quantity 0)
            pot = Potion.create_empty(pot_type, name, price)  # O(1)
            # Inserting Pot object into hash table K = Potion Name, I = Potion object
            self.hash_table[name] = pot  # O(1)
            # print("clock")

        # If potion classes exist , reset potion's quantities to 0
        if self.stock is not None:
            for j in self.stock:  # O(C)
                j.item.quantity = 0
        # print ("1st mark")
        return

    def add_potions_to_inventory(self, potion_name_amount_pairs: list[tuple[str, float]]) -> None:
        self.stock = AVLTree()  # Setting Potion stock to use AVL
        # iterate according to the number of potions provided
        for i in range(len(potion_name_amount_pairs)):
            name = potion_name_amount_pairs[i][0]
            value = potion_name_amount_pairs[i][1]
            # print("clock2")
            # If current hash table has corresponding pot name, update the quantity accordingly
            if self.hash_table.__contains__(name):
                pot = self.hash_table[name]  # Retrieving item from hash map (K = Potion_Name)
                pot.quantity = value  # updating quantity
                price = pot.buy_price  # getting the potion's price so that we can create AVL using that as the key
                self.stock[price] = pot  # creating AVL tree using K = Potion price, I = Potion object
        # self.stock.draw()
        # print ("2nd mark")
        return

    def choose_potions_for_vendors(self, num_vendors: int) -> list:

        inventory = []  # Treat this as vendor's inventory
        temp = []  # To re-insert potions back into the AVL tree (prevent duplicate potions among vendors)
        for m in range(num_vendors):
            # Generates a random number from 1 - Potions with quantity > 0 ( lets call it p)
            p = self.rand.randint(self.stock.__len__())
            # Selects the p-th highest price using kth largest
            # print("random number: " + str(p))

            pot_rand = self.stock.kth_largest(p)
            # self.stock.draw()
            # print(pot_rand)

            # print("price: " + str(pot_rand.item.buy_price))
            # print("node price: " + str(pot_rand.key))

            temp.append(pot_rand.item)  # Get the potion item that was added into vendor's inventory to re-append later.
            name = pot_rand.item.name
            quantity = pot_rand.item.quantity
            inventory.append((name, quantity))

            # self.stock.draw()
            # print(pot_rand)

            self.stock.__delitem__(pot_rand.item.buy_price)

            # self.stock.draw()
            # print("clock3")

        # self.stock.draw()
        # print(self.stock.kth_largest(1))

        for j in range(num_vendors):
            price = temp[j].buy_price
            self.stock[price] = temp[j]
        # print ("3rd mark")
        # self.stock.draw()
        return inventory

    def solve_game(self, potion_valuations: list[tuple[str, float]], starting_money: list[int]) -> list[float]:
        global profit_map
        potion_profits = []
        profit_map = AVLTree()
        for i in range(len(potion_valuations)):
            name = potion_valuations[i][0]  # name of potion valuation
            sell_adv = potion_valuations[i][1]  # price sold to adventurers
            if self.hash_table.__contains__(name):
                pot = self.hash_table[name]  # retrieving pot details from hash map
                randum = self.rand.randint(5000) / 1234712386
                profit = (
                                     sell_adv - pot.buy_price) + randum  # profit amount from selling to adventurers after buying from vendor
                if profit > 0:  # if profit was made, throw into AVL tree
                    profit_map[profit] = pot
        profit_map.draw()
        for j in range(len(starting_money)):
            available_money = starting_money[j]
            money_remain = True
            not_net_profit = 0
            temp_holder = []
            for k in range(len(profit_map)):
                if money_remain:
                    highest_value_pot = profit_map.kth_largest(k + 1)
                    quantity = highest_value_pot.item.quantity
                    buy_cost = highest_value_pot.item.buy_price
                    total_cost = quantity * buy_cost
                    if available_money >= total_cost:
                        not_net_profit += highest_value_pot.key
                        available_money -= total_cost
                        highest_value_pot.item.quantity = 0
                    elif available_money < total_cost:
                        capable_amount = (available_money / total_cost) * quantity
                        not_net_profit += capable_amount * highest_value_pot.key
                        highest_value_pot.item.quantity -= capable_amount
                        money_remain = False
                else:
                    potion_profits.append(not_net_profit)
                    break
        return potion_profits


if __name__ == '__main__':
    g = Game()
    list_1 = [
        ("Potion of Health Regeneration", 4),
        ("Potion of Extreme Speed", 5),
        ("Potion of Instant Health", 3),
        ("Potion of Increased Stamina", 10),
        ("Potion of Untenable Odour", 5)
    ]
    list_2 = [
        # Name, Category, Buying price from vendors.
        ["Health", "Potion of Health Regeneration", 20],
        ["Buff", "Potion of Extreme Speed", 10],
        ["Damage", "Potion of Deadly Poison", 45],
        ["Health", "Potion of Instant Health", 5],
        ["Buff", "Potion of Increased Stamina", 25],
        ["Damage", "Potion of Untenable Odour", 1]
    ]

    g.set_total_potion_data(list_2)
    g.add_potions_to_inventory(list_1)
    print(g.hash_table)

    print(g.choose_potions_for_vendors(5))
