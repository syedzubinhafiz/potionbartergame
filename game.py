from __future__ import annotations
# ^ In case you aren't on Python 3.10
from avl import AVLTree
from hash_table import LinearProbePotionTable
from potion import Potion
from random_gen import RandomGen

"""
ADT used for my approach.
1.) Hash Table ADT.
Reason why I used Hash Table is that it would be a convenient way to store data, since every potion name will be unique,
and the properties of the potion will also be fixed, as per requirement. And since the data used are all unique,
it will be handy since Hash Table ADT allows us to insert, delete and search specific data through hash table.

2.) AVL Tree ADT.
Since height of AVL trees are always balanced, it gives a better search complexity over BST, hence the main reason for 
the usage of AVL over BST. Since it balances itself, it will also be easier for the program to be able to 
undergo deletion, search and insertion processes compared to the standard BST. So, this ADT was used mainly to maintain
a good overall runtime complexity for the methods.
"""


class Game:

    def __init__(self, seed=0) -> None:
        self.rand = RandomGen(seed=seed)
        self.stock = None
        self.hash_table = None

    '''
    Since the method has a for loop which iterates through the entire length of list potion_data, and an inner for loop
    that iterates through the current length of the inventory(AVL Tree): 
    Overall complexity will be O(N * C)
    Complexity : N(1 + 1 + 1 + 1 + C), ignoring the constants, N* C, hence overall complexity is obtained as per above.
    '''

    def set_total_potion_data(self, potion_data: list) -> None:
        # Instantiating hash_table using length of potion data
        self.hash_table = LinearProbePotionTable(len(potion_data))
        for i in range(len(potion_data)):  # O (N), iterates through length of potion_data
            # Accessing data in the potion_data list, [Pot_Type, Name, Price]
            pot_type = potion_data[i][0]  # O(1) array indexing
            name = potion_data[i][1]  # O(1)  ''''
            price = potion_data[i][2]  # O(1) ''''
            # Creating Potion class to be placed in the hash table
            pot = Potion.create_empty(pot_type, name, price)  # O(1) recreates class with updated attributes
            # Inserting Pot object into hash table K = Potion Name, I = Potion object
            self.hash_table[name] = pot  # O(1) as accordance to the functions in hash_table.py

        # If potion classes exist , reset potion's quantities to 0
        if self.stock is not None:
            for j in self.stock:  # O(C) where C is length of potion_name_amount_pairs in function below
                j.item.quantity = 0

        return

    '''
    Has a for loop that iterates through length of potion_name_amount_pairs, within that for loop there is a insertion 
    of data into the AVL tree. So overall complexity of the program:
    O(C * log(N))
    Complexity : C* (1 + 1 + 1 + 1 +1 +1 + log(N)), so ignoring the constants, C* log(N)
    '''

    def add_potions_to_inventory(self, potion_name_amount_pairs: list[tuple[str, float]]) -> None:
        self.stock = AVLTree()  # Setting Potion stock to use AVL
        # iterate according to the number of potions provided
        for i in range(len(potion_name_amount_pairs)):  # O(C) iterating through entire length of
            # potion_name_amount_pairs
            name = potion_name_amount_pairs[i][0]  # O(1) indexing array
            value = potion_name_amount_pairs[i][1]  # ''''

            # If current hash table has corresponding pot name, update the quantity accordingly
            if self.hash_table.__contains__(name):  # O(1) as accordance to the functions in hash_table.py
                pot = self.hash_table[name]  # Retrieving item from hash map (K = Potion_Name) O(1) searching hash table
                pot.quantity = value  # updating quantity, O(1) updating value
                price = pot.buy_price  # getting the potion's price so that we can create AVL using that as the key,
                # O(1) updating value
                self.stock[price] = pot  # creating AVL tree using K = Potion price, I = Potion object , O(log(N))
                # since insertion/searching using a balanced tree(AVL)
        return

    """
    So there are two for loops but they both share the same overall complexity, so we'll just see them individually.
    In the for loop, there exist a deletion method call through a magic method for the AVL to delete a node.
    So the overall complexity of the program :
    O(C * log(N))
    Complexity: (C * (1+1+log(N) + 1 + 1 + 1 + 1 + log(N) ) + C*(1 + log(N)), removing constants and removing duplicates,
    C * log(N)
    """

    def choose_potions_for_vendors(self, num_vendors: int) -> list:

        inventory = []  # Treat this as vendor's inventory
        temp = []  # To re-insert potions back into the AVL tree (prevent duplicate potions among vendors)
        for m in range(num_vendors):  # O(C) iterating through entire length of num_vendors
            # Generates a random number from 1 - Potions with quantity > 0 ( lets call it p)
            p = self.rand.randint(self.stock.__len__())  # O(1) Assumed to be this as stated in requirements

            # Selects the p-th highest price using kth largest
            pot_rand = self.stock.kth_largest(p)  # O(log(N) as accordance to explanation in avl.py
            temp.append(
                pot_rand.item)  # Get the potion item that was added into vendor's inventory to re-append later. O(1)
            # since appending to array
            name = pot_rand.item.name  # O(1) assigning value
            quantity = pot_rand.item.quantity  # O(1) assigning value
            inventory.append((name, quantity))  # O(1) assigning value to array

            self.stock.__delitem__(
                pot_rand.item.buy_price)  # O(log(N) (DELETING) as accordance to explanation in avl.py (basically AVL
            # is a self-balancing tree)

        for j in range(num_vendors):  # O(C) iterating through entire length of num_vendors
            price = temp[j].buy_price  # O(1) assigning value
            self.stock[price] = temp[j]  # O(log(N) (INSERTING) as accordance to explanation in avl.py
        return inventory

    """
    Two different for loops that iterate through different lengths, first for loop that iterates through length of potion_valuations,
    second iterates through len of starting money. In the first for loop there exists a insertion method for the AVL ADT.
    In the second for loop there exists a nested for loop that iterates through length of potion valuations.
    So, overall complexity :
    O( N * log(N) + M * N)
    Complexity: 
    First for loop:
    N * ( 1 + 1 + 1 + 1 + 1 + 1 + log(N)), so removing constants, N*log(N)
    Second for loop:
    M * ( 1 + 1 + 1 + N*( 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1)), so removing constants , M * N
    Combining both for loops:
    N*log(N) + M * N
    """
    """
    First I iterate through the potion_valuations list to obtain the given fixed data, calculate the profits for each potion,
    and insert the profits for each potion into an AVL tree, where the Key = Profit, Item = Potion. Key has been added with random
    numbers so that the AVL tree will accept "duplicate" values, where the profit is the same but the potions are different.
    
    Next, I iterate through the starting money list and begin the simulation of calculating the maximum profit per day,
    where I make it so that I'll always be selling the most profitable potion to adventurers until the quantity empties,
    or just selling the most profitable item until the starting money is depleted.
    """

    def solve_game(self, potion_valuations: list[tuple[str, float]], starting_money: list[int]) -> list[float]:
        potion_profits = []
        profit_map = AVLTree()

        for i in range(len(potion_valuations)):  # O(N) iterating through len of potion_valuations
            name = potion_valuations[i][0]  # name of potion valuation O(1)
            sell_adv = potion_valuations[i][1]  # price sold to adventurers O(1)
            if self.hash_table.__contains__(name):  # O(1) assume hash function to be constant
                pot = self.hash_table[name]  # retrieving pot details from hash map O(1)
                randum = self.rand.randint(5000) / 1234712386  # to make it so that tree accepts duplicate profit
                # inputs O(1)
                profit = (sell_adv - pot.buy_price) + randum  # profit amount from selling to adventurers after
                # buying from vendor O(1)

                if profit > 0:  # if profit was made, throw into AVL tree  # O(1)
                    profit_map[profit] = pot  # O(log(N) inserting data into AVL tree, explanation in avl.py

        for j in range(len(starting_money)):  # O(M) iterating each simulation with different starting money
            available_money = starting_money[j]  # Obtaining values from list O(1)
            money_remain = True  # To indicate when to stop O(1), if adventurer still has money, continue the process
            # of selling, else stop.
            not_net_profit = 0  # How much you scammed them O(1), money profited for the day
            for k in range(
                    len(potion_valuations)):  # O(N) iterating through len of potion_valuations, determining the
                # highest profit potion to sell
                if money_remain:  # O(1)
                    # O(log(N) as per explanation in avl.py, K-largest method, obtaining the k-th most profitable potion
                    highest_value_pot = profit_map.kth_largest(k + 1)
                    # Amount of potions available
                    quantity = highest_value_pot.item.quantity  # O(1) retrieving attributes and assigning into
                    # varaiable
                    # Price that the vendor (us) buy from the supplier
                    buy_cost = highest_value_pot.item.buy_price  # O(1) retrieving attributes and assigning into
                    # varaiable
                    # Total cost to clear the entire stock
                    total_cost = quantity * buy_cost  # Basic mathematical operations O(1)

                    # Both if and else-if are O(1) since it just consists of basic operations
                    # If enough money to clear the entire stock, buy entire stock,
                    if available_money >= total_cost:
                        not_net_profit += (highest_value_pot.key + buy_cost) * quantity  # Non-net profit
                        # of money obtained by selling k-th most profitable potion
                        available_money -= total_cost  # reduce the available amount of money (paying)

                    # if not enough to money to clear entire stock, just buy whatever you can.
                    elif available_money < total_cost:
                        capable_amount = (available_money / total_cost) * quantity  # Getting the maximum
                        # amount of potions you can
                        not_net_profit += capable_amount * (highest_value_pot.key + buy_cost)  # Non-net profit of
                        # money obtained by selling
                        # k-th most profitable potion
                        money_remain = False  # signifies that no money left
                else:
                    not_net_profit = round(not_net_profit, 1)  # round off the profit value to 1 decimal( to pass
                    # testers, otherwise
                    # this would not be here)
                    potion_profits.append(not_net_profit)  # append into output
                    break  # loop ends
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
