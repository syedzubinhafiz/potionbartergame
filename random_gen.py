from typing import Generator


def lcg(modulus: int, a: int, c: int, seed: int) -> Generator[int, None, None]:
    """Linear congruential generator."""
    while True:
        seed = (a * seed + c) % modulus
        yield seed


class RandomGen:

    def __init__(self, seed: int = 0) -> None:
        self.seed = seed
        self.x = lcg(pow(2, 32), 134775813, 1, self.seed)

    def randint(self, k: int) -> int:
        random_array = []
        temp_bin = ""
        for i in range(5):  # Generate the first 5 random numbers
            random_array.append(next(self.x))

        output_16 = []
        for j in range(len(random_array)):  # converting the random number into 32 bits
            x1 = "{:032b}".format(random_array[j])
            output_16.append((x1[0:16]))  # only taking the first 16 bits

        for m in range(len(output_16[0])):  # summing each bit column
            sum_col = 0
            for l in range(len(output_16)):
                sum_col += int(output_16[l][m])
            if sum_col > 2:  # if sum of column > 2, append 1 into temp_bin
                temp_bin = temp_bin + "1"
            else:  # else appends 0
                temp_bin = temp_bin + "0"
        temp_int = int(temp_bin, 2)  # converts binary to integer form
        int_mod = temp_int % k
        output = int_mod + 1
        return output


if __name__ == "__main__":
    Random_gen = lcg(pow(2, 32), 134775813, 1, 0)
