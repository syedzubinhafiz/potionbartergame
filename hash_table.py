""" Hash Table ADT

Defines a Hash Table using Linear Probing for conflict resolution.
It currently rehashes the primary cluster to handle deletion.
"""
__author__ = 'Brendon Taylor, modified by Jackson Goerner'
__docformat__ = 'reStructuredText'
__modified__ = '21/05/2020'
__since__ = '14/05/2020'

from random import Random, seed

from potion import Potion
from random_gen import RandomGen
from referential_array import ArrayR
from typing import TypeVar, Generic

T = TypeVar('T')


class LinearProbePotionTable(Generic[T]):
    """
    Linear Probe Potion Table

    This potion table does not support deletion.

    attributes:
        count: number of elements in the hash table
        table: used to represent our internal array
        table_size: current size of the hash table
    """

    def __init__(self, max_potions: int, good_hash: bool = True, tablesize_override: int = -1) -> None:
        # Statistic setting
        self.conflict_count = 0
        self.probe_max = 0
        self.probe_total = 0
        # Instantiating variables
        self.max_potions = max_potions
        self.good_hash = good_hash
        if tablesize_override > -1:
            self.count = 0
            self.table = ArrayR(tablesize_override)
        else:
            self.initalise_with_tablesize(max_potions)

    def hash(self, potion_name: str) -> int:
        if self.good_hash is True:
            key = Potion.good_hash(potion_name, len(self.table))
            return key
        else:
            key = Potion.bad_hash(potion_name, len(self.table))
            return key

    def statistics(self) -> tuple:
        return self.conflict_count, self.probe_total, self.probe_max

    def __len__(self) -> int:
        """
        Returns number of elements in the hash table
        :complexity: O(1)
        """
        return self.count

    def __linear_probe(self, key: str, is_insert: bool) -> int:
        """
        Find the correct position for this key in the hash table using linear probing
        :complexity best: O(K) first position is empty
                          where K is the size of the key
        :complexity worst: O(K + N) when we've searched the entire table
                           where N is the table_size
        :raises KeyError: When a position can't be found
        """
        position = self.hash(key)  # get the position using hash

        if is_insert and self.is_full():
            raise KeyError(key)

        counter = 0
        for _ in range(len(self.table)):  # start traversing
            if self.table[position] is None:  # found empty slot
                if is_insert:
                    if counter > 0:
                        self.conflict_count += 1
                    return position
                else:
                    raise KeyError(key)  # so the key is not in
            elif self.table[position][0] == key:  # found key
                return position
            else:  # there is something but not the key, try next
                self.probe_total += 1
                counter += 1
                if counter >= self.probe_max:
                    self.probe_max = counter
                position = (position + 1) % len(self.table)

        raise KeyError(key)

    def __contains__(self, key: str) -> bool:
        """
        Checks to see if the given key is in the Hash Table
        :see: #self.__getitem__(self, key: str)
        """
        try:
            _ = self[key]
        except KeyError:
            return False
        else:
            return True

    def __getitem__(self, key: str) -> T:
        """
        Get the item at a certain key
        :see: #self.__linear_probe(key: str, is_insert: bool)
        :raises KeyError: when the item doesn't exist
        """
        position = self.__linear_probe(key, False)
        return self.table[position][1]

    def __setitem__(self, key: str, data: T) -> None:
        """
        Set an (key, data) pair in our hash table
        :see: #self.__linear_probe(key: str, is_insert: bool)
        :see: #self.__contains__(key: str)
        """
        if len(self) == len(self.table) and key not in self:
            raise ValueError("Cannot insert into a full table.")
        position = self.__linear_probe(key, True)

        if self.table[position] is None:
            self.count += 1
        self.table[position] = (key, data)

    def initalise_with_tablesize(self, tablesize: int) -> None:
        """
        Initialise a new array, with table size given by tablesize.
        Complexity: O(n), where n is len(tablesize)
        """
        self.count = 0
        self.table = ArrayR(tablesize)

    def is_empty(self):
        """
        Returns whether the hash table is empty
        :complexity: O(1)
        """
        return self.count == 0

    def is_full(self):
        """
        Returns whether the hash table is full
        :complexity: O(1)
        """
        return self.count == len(self.table)

    def insert(self, key: str, data: T) -> None:
        """
        Utility method to call our setitem method
        :see: #__setitem__(self, key: str, data: T)
        """
        self[key] = data

    def __str__(self) -> str:
        """
        Returns all they key/value pairs in our hash table (no particular order)
        :complexity: O(N) where N is the table size
        """
        result = ""
        for item in self.table:
            if item is not None:
                (key, value) = item
                result += "(" + str(key) + "," + str(value) + ")\n"
        return result

    """ Gets an array of potion names by:
    1. Randomly getting a word from words array
    2. Appending the word with "potion of"
    :param length: the number of potion names needed
    :complexity: worst O(n*A) where n is the number of words and C is the
    complexity of the random function"""

    def fake_data_generation(self, length: int):
        # words used in potion names
        words = ["nul-spell", "bravery", "faith", "vitality", "haste",
                 "invincibility", "regeneration", "berserk", "havoc", "invisibility",
                 "freeze", "lure", "amnesia", "imprisonment", "confinement",
                 "terror", "paralysis", "poisoning", "drowsiness", "fatigue",
                 "fire", "protection", "poison protection", "arrow protection",
                 "mana", "health regeneration", "mana regeneration", "return",
                 "teleportation", "blink", "ageing", "awakening", "clearance",
                 "attack", "defence", "frost", "hallucination", "light", "levitation",
                 "lightning", "magical vision", "necromancy", "stone", "libido",
                 "acid", "sleep", "toxicity", "electricity", "shock", "sloth",
                 "speed", "explosion", "transparency", "truth", "enigma", "reading mind",
                 "justice", "vengeance", "charm", "charisma", "destruction", "youth",
                 "suspicion", "stealth", "frenzy", "illusion", "cure disease", "increasing luck",
                 "vitality", "lockpicking", "delusion", "mystique", "stamina",
                 "persistence", "fear", "enduring", "endurance", "toughness",
                 "might", "invulnerability", "mind reading", "maximum power", "power",
                 "giants", "sharpness", "bleeding", "heroism", "awkwardness",
                 "thickness", "mundane", "swiftness", "leaping", "slowness",
                 "night vision", "slow harming", "falling", "decay", "water breathing",
                 "enlargement", "enrichment", "nourishment", "height", "incredible strength",
                 "inversion", "lank", "flash", "hibernation", "blindness",
                 "flames", "morphing", "camouflage", "infection", "floating", "melting",
                 "freezing", "abduction", "disaster", "grappling", "slithering", "vision", "night vision"]
        arr = []
        random = RandomGen()
        for i in range(0, length):
            randomIndex = random.randint(len(words))
            word = words[randomIndex]
            arr.append("Potion of " + word)
        return arr


if __name__ == '__main__':
    # tablesize = 120
    good_hash_1 = LinearProbePotionTable(100, True, 120)
    names_1 = good_hash_1.fake_data_generation(70)
    for i in range(len(names_1)):
        good_hash_1[str(names_1[i])] = str(names_1[i])
    print(good_hash_1.statistics())

    bad_hash_1 = LinearProbePotionTable(100, False, 120)
    for i in range(len(names_1)):
        bad_hash_1[str(names_1[i])] = str(names_1[i])
    print(bad_hash_1.statistics())

    # tablesize = 69
    good_hash_2 = LinearProbePotionTable(100, True, 69)
    for i in range(len(names_1)):
        good_hash_2[str(names_1[i])] = str(names_1[i])
    print(good_hash_2.statistics())

    bad_hash_2 = LinearProbePotionTable(100, False, 69)
    for i in range(len(names_1)):
        bad_hash_2[str(names_1[i])] = str(names_1[i])
    print(bad_hash_2.statistics())

    # tablesize = 291
    good_hash_3 = LinearProbePotionTable(100, True, 291)
    for i in range(len(names_1)):
        good_hash_3[str(names_1[i])] = str(names_1[i])
    print(good_hash_3.statistics())

    bad_hash_3 = LinearProbePotionTable(100, False, 291)
    for i in range(len(names_1)):
        bad_hash_3[str(names_1[i])] = str(names_1[i])
    print(bad_hash_3.statistics())


    # tablesize = 200
    good_hash_4 = LinearProbePotionTable(100, True, 200)
    for i in range(len(names_1)):
        good_hash_4[str(names_1[i])] = str(names_1[i])
    print(good_hash_4.statistics())

    bad_hash_4 = LinearProbePotionTable(100, False, 200)
    for i in range(len(names_1)):
        bad_hash_4[str(names_1[i])] = str(names_1[i])
    print(bad_hash_4.statistics())

    # tablesize = 100
    good_hash_5 = LinearProbePotionTable(100, True, 100)
    for i in range(len(names_1)):
        good_hash_5[str(names_1[i])] = str(names_1[i])
    print(good_hash_5.statistics())

    good_hash_5 = LinearProbePotionTable(100, False, 100)
    for i in range(len(names_1)):
        good_hash_5[str(names_1[i])] = str(names_1[i])
    print(good_hash_5.statistics())

