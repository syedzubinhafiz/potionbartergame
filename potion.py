import primes


class Potion:

    def __init__(self, potion_type: str, name: str, buy_price: float, quantity: float) -> None:
        self.potion_type = potion_type
        self.name = name
        self.buy_price = buy_price
        self.quantity = quantity

    @classmethod
    def create_empty(cls, potion_type: str, name: str, buy_price: float) -> 'Potion':
        return cls(potion_type, name, buy_price, 0)

    @classmethod
    def good_hash(cls, potion_name: str, tablesize: int, hash_base: int = primes.largest_prime(10000)) -> int:
        is_start_potion = False
        if len(potion_name) > 10:
            if potion_name[0:10] == "Potion of ":
                is_start_potion = True

        result = 0
        # If it is a potion that starts with Potion of, get the keyword only
        # E.g: Potion of Health, Health is the keyword.
        if is_start_potion:
            for i in range(10, len(potion_name)):
                result = (result * hash_base + ord(potion_name[i])) % tablesize
        # If it does not start with Potion of, hash the entire potion name.
        else:
            for char in str(potion_name):
                result = (result * hash_base + ord(char)) % tablesize

        return result

    @classmethod
    def bad_hash(cls, potion_name: str, tablesize: int, hash_base: int = primes.largest_prime(10000)) -> int:
        is_start_potion = False
        if len(potion_name) > 10:
            if potion_name[0:10] == "Potion of ":
                is_start_potion = True

        result = 0
        # If it is a potion that starts with Potion of, get the first letter of the keyword only
        # E.g: Potion of Health, H is the letter.
        if is_start_potion:
            result = (ord(potion_name[11]) * hash_base) % tablesize
        # If it does not start with Potion of, hash only the first letter of the string.
        else:
            result = (ord(potion_name[0]) * hash_base) % tablesize

        return result

    def __str__(self) -> str:
        """
        Returns all they key/value pairs in our hash table (no particular order)
        :complexity: O(N) where N is the table size
        """
        return "Name: " + str(self.name) + ", Type: " + str(self.potion_type) + ", Quantity: " + str(
            self.quantity) + ",Price: " + str(self.buy_price)
