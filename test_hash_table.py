import unittest

from hash_table import LinearProbePotionTable


class TestTable(unittest.TestCase):

    def test_tablesize(self):
        c1 = LinearProbePotionTable(100, True, 120)
        c2 = LinearProbePotionTable(100, True, -1)
        # Should be exactly 120.
        self.assertEqual(len(c1.table), 120)
        # Should at least accomodate all positions.
        self.assertGreaterEqual(len(c2.table), 100)

    def test_stats(self):
        # Using a dictionary in the tester file for hash table ;)
        lookup = {
            "s1": 5,
            "s2": 5,
            "s3": 5,
            "s4": 7
        }
        h = lambda self, k: lookup[k]
        saved = LinearProbePotionTable.hash
        LinearProbePotionTable.hash = h
        # What the above code does is essentially work around using good_hash or bad hash.
        # This is the example given in the section on conflict and probe counting
        # max_potions: int, good_hash: bool = True, tablesize_override: int=-1
        l = LinearProbePotionTable(10, True, 10)
        l["s1"] = "s1"
        l["s2"] = "s2"
        l["s3"] = "s3"
        l["s4"] = "s4"
        LinearProbePotionTable.hash = saved

        self.assertEqual(l.statistics(), (3, 4, 2))

    def test_stats2(self):
        # Using a dictionary in the tester file for hash table ;)
        lookup = {
            "s1": 3,
            "s2": 5,
            "s3": 3,
            "s4": 3
        }
        h = lambda self, k: lookup[k]
        saved = LinearProbePotionTable.hash
        LinearProbePotionTable.hash = h
        # What the above code does is essentially work around using good_hash or bad hash.
        # This is the example given in the section on conflict and probe counting
        l = LinearProbePotionTable(10, True, 10)
        l["s1"] = "s1"
        l["s2"] = "s2"
        l["s3"] = "s3"
        l["s4"] = "s4"
        LinearProbePotionTable.hash = saved

        self.assertEqual(l.statistics(), (2, 4, 3))

    def test_stats3(self):
        # Using a dictionary in the tester file for hash table ;)
        lookup = {
            "s1": 4,
            "s2": 1,
            "s3": 3,
            "s4": 3
        }
        h = lambda self, k: lookup[k]
        saved = LinearProbePotionTable.hash
        LinearProbePotionTable.hash = h
        # What the above code does is essentially work around using good_hash or bad hash.
        # This is the example given in the section on conflict and probe counting
        l = LinearProbePotionTable(10, True, 10)
        l["s1"] = "s1"
        l["s2"] = "s2"
        l["s3"] = "s3"
        l["s4"] = "s4"
        LinearProbePotionTable.hash = saved

        self.assertEqual(l.statistics(), (1, 2, 2))

    def test_stats4(self):
        # Using a dictionary in the tester file for hash table ;)
        lookup = {
            "s1": 4,
            "s2": 3,
            "s3": 4,
            "s4": 3,
            "s5": 4
        }
        h = lambda self, k: lookup[k]
        saved = LinearProbePotionTable.hash
        LinearProbePotionTable.hash = h
        # What the above code does is essentially work around using good_hash or bad hash.
        # This is the example given in the section on conflict and probe counting
        l = LinearProbePotionTable(10, True, 10)
        l["s1"] = "s1"
        l["s2"] = "s2"
        l["s3"] = "s3"
        l["s4"] = "s4"
        l["s5"] = "s5"
        LinearProbePotionTable.hash = saved

        self.assertEqual(l.statistics(), (3, 7, 3))

    def test_stats5(self):
        # Using a dictionary in the tester file for hash table ;)
        lookup = {
            "s1": 1,
            "s2": 2,
            "s3": 3,
            "s4": 4
        }
        h = lambda self, k: lookup[k]
        saved = LinearProbePotionTable.hash
        LinearProbePotionTable.hash = h
        # What the above code does is essentially work around using good_hash or bad hash.
        # This is the example given in the section on conflict and probe counting
        l = LinearProbePotionTable(10, True, 10)
        l["s1"] = "s1"
        l["s2"] = "s2"
        l["s3"] = "s3"
        l["s4"] = "s4"
        LinearProbePotionTable.hash = saved

        self.assertEqual(l.statistics(), (0, 0, 0))

    def test_stats6(self):
        # Using a dictionary in the tester file for hash table ;)
        lookup = {
            "s1": 4,
            "s2": 4,
            "s3": 4,
            "s4": 4
        }
        h = lambda self, k: lookup[k]
        saved = LinearProbePotionTable.hash
        LinearProbePotionTable.hash = h
        # What the above code does is essentially work around using good_hash or bad hash.
        # This is the example given in the section on conflict and probe counting
        l = LinearProbePotionTable(10, True, 10)
        l["s1"] = "s1"
        l["s2"] = "s2"
        l["s3"] = "s3"
        l["s4"] = "s4"
        LinearProbePotionTable.hash = saved

        self.assertEqual(l.statistics(), (3, 6, 3))

    def test_stats7(self):
        # Using a dictionary in the tester file for hash table ;)
        lookup = {
            "s1": 7,
            "s2": 7,
            "s3": 7,
            "s4": 3
        }
        h = lambda self, k: lookup[k]
        saved = LinearProbePotionTable.hash
        LinearProbePotionTable.hash = h
        # What the above code does is essentially work around using good_hash or bad hash.
        # This is the example given in the section on conflict and probe counting
        l = LinearProbePotionTable(10, True, 10)
        l["s1"] = "s1"
        l["s2"] = "s2"
        l["s3"] = "s3"
        l["s4"] = "s4"
        LinearProbePotionTable.hash = saved

        self.assertEqual(l.statistics(), (2, 3, 2))

    def test_stats8(self):
        # Using a dictionary in the tester file for hash table ;)
        lookup = {
            "s1": 5,
            "s2": 2,
            "s3": 2,
            "s4": 5
        }
        h = lambda self, k: lookup[k]
        saved = LinearProbePotionTable.hash
        LinearProbePotionTable.hash = h
        # What the above code does is essentially work around using good_hash or bad hash.
        # This is the example given in the section on conflict and probe counting
        l = LinearProbePotionTable(10, True, 10)
        l["s1"] = "s1"
        l["s2"] = "s2"
        l["s3"] = "s3"
        l["s4"] = "s4"
        LinearProbePotionTable.hash = saved

        self.assertEqual(l.statistics(), (2, 2, 1))

    def test_stats9(self):
        # Using a dictionary in the tester file for hash table ;)
        lookup = {
            "s1": 3,
            "s2": 3,
            "s3": 1,
            "s4": 1
        }
        h = lambda self, k: lookup[k]
        saved = LinearProbePotionTable.hash
        LinearProbePotionTable.hash = h
        # What the above code does is essentially work around using good_hash or bad hash.
        # This is the example given in the section on conflict and probe counting
        l = LinearProbePotionTable(10, True, 10)
        l["s1"] = "s1"
        l["s2"] = "s2"
        l["s3"] = "s3"
        l["s4"] = "s4"
        LinearProbePotionTable.hash = saved

        self.assertEqual(l.statistics(), (2, 2, 1))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTable)
    unittest.TextTestRunner(verbosity=0).run(suite)
