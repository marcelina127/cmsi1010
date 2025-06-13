import unittest


def third_element(t):
    if not isinstance(t, tuple):
        raise TypeError("Input must be a tuple")
    if len(t) < 3:
        raise IndexError("Tuple must have at least three elements")
    return t[2]


def reverse_pair(t):
    if not isinstance(t, tuple):
        raise TypeError("Input must be a tuple")
    if len(t) != 2:
        raise ValueError("Tuple must have exactly two elements")
    return (t[1], t[0])
    

def middle_element_of_list(a):
    # replace the pass statement with your code
    if not isinstance(a, list):
        raise TypeError("Input must be a list")
    if len(a) == 0:
        raise IndexError("List is empty")
    middle_index = (len(a) - 1) // 2
    return a[middle_index]


def unique_elements(a):
    # replace the pass statement with your code
    if not isinstance(a, list):
        raise TypeError("Input must be a list")
    return set(a)


def contains_duplicates(a):
    if not isinstance(a, list):
        raise TypeError("Input must be a list")
    return len(set(a)) != len(a)


def is_superset(a, b):
    if not isinstance(a, set) or not isinstance(b, set):
        raise TypeError("Both inputs must be sets")
    return a.issuperset(b)


def is_subset(a, b):
    if not isinstance(a, set) or not isinstance(b, set):
        raise TypeError("Both inputs must be sets")
    return a.issubset(b)


def is_disjoint(a, b):
    if not isinstance(a, set) or not isinstance(b, set):
        raise TypeError("Both inputs must be sets")
    return a.isdisjoint(b)



from collections import Counter

def most_frequent_value_or_values(d):
    if not isinstance(d, dict):
        raise TypeError("Input must be a dictionary")
    if not d:
        return None

    value_counts = Counter(d.values())
    max_freq = max(value_counts.values())
    most_frequent = {val for val, freq in value_counts.items() if freq == max_freq}

    return most_frequent


def key_is_in_both_dictionaries(d1, d2, key):
    if not isinstance(d1, dict) or not isinstance(d2, dict):
        raise TypeError("Both inputs must be dictionaries")
    return key in d1 and key in d2


def word_frequencies(s):
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    words = s.split()
    from collections import Counter
    return dict(Counter(words))


class TestDataStructuresCardio(unittest.TestCase):
    def test_third_element(self):
        self.assertEqual(third_element((1, 2, 3, 4)), 3)
        with self.assertRaises(IndexError):
            third_element((1, 2))
        with self.assertRaises(IndexError):
            third_element((1,))
        with self.assertRaises(TypeError):
            third_element([1, 2, 3])
        with self.assertRaises(TypeError):
            third_element("not a tuple")


    def test_reverse_pair(self):
        self.assertEqual(reverse_pair((1, 2)), (2, 1))
        with self.assertRaises(ValueError):
            reverse_pair((1, 2, 3))
        with self.assertRaises(ValueError):
            reverse_pair((1,))
        with self.assertRaises(TypeError):
            reverse_pair([1, 2])
        with self.assertRaises(TypeError):
            reverse_pair("not a tuple")


    def test_middle_element_of_list(self):
        self.assertEqual(middle_element_of_list([1, 2, 3]), 2)
        self.assertEqual(middle_element_of_list([1, 2]), 1)
        self.assertEqual(middle_element_of_list([10, 20, 30, 40]), 20)
        self.assertEqual(middle_element_of_list([5] * 500), 5)
        with self.assertRaises(IndexError):
            middle_element_of_list([])
        with self.assertRaises(TypeError):
            middle_element_of_list((1, 2))
        with self.assertRaises(TypeError):
            middle_element_of_list("not a list")


    def test_unique_elements(self):
        self.assertEqual(unique_elements([1, 2, 2, 3]), {1, 2, 3})
        self.assertEqual(unique_elements([1, 1, 1]), {1})
        self.assertEqual(unique_elements([]), set())
        self.assertEqual(unique_elements([1, 2, 3, 4, 5]), {1, 2, 3, 4, 5})
        self.assertEqual(unique_elements(
            [False, 3, "dog", False, "dog"]), {False, 3, "dog"})
        with self.assertRaises(TypeError):
            unique_elements("not a list")
        with self.assertRaises(TypeError):
            unique_elements({1, 2, 3})

    def test_contains_duplicates(self):
        self.assertTrue(contains_duplicates([1, 2, 2]))
        self.assertFalse(contains_duplicates([1, 2, 3]))
        with self.assertRaises(TypeError):
            contains_duplicates("not a list")
        with self.assertRaises(TypeError):
            contains_duplicates({1, 2, 3})


    def test_is_superset(self):
        self.assertTrue(is_superset({1, 2}, {1}))
        self.assertFalse(is_superset({1}, {1, 2}))
        with self.assertRaises(TypeError):
            is_superset({1}, "not a set")


    def test_is_subset(self):
        self.assertTrue(is_subset({1}, {1, 2}))
        self.assertFalse(is_subset({1, 2}, {1}))
        with self.assertRaises(TypeError):
            is_subset("not a set", {1})


    def test_is_disjoint(self):
        self.assertTrue(is_disjoint({1}, {2}))
        self.assertFalse(is_disjoint({1}, {1}))
        with self.assertRaises(TypeError):
            is_disjoint({1}, "not a set")
        with self.assertRaises(TypeError):
            is_disjoint("not a set", {1})


    def test_most_frequent_value_or_values(self):
        self.assertEqual(most_frequent_value_or_values(
            {'a': 1, 'b': 2, 'c': 1}), {1})
        self.assertEqual(most_frequent_value_or_values(
            {'a': 1, 'b': 2, 'c': 2}), {2})
        self.assertEqual(most_frequent_value_or_values(
            {'a': 1, 'b': 1, 'c': 2, 'd': 2}), {1, 2})
        self.assertEqual(most_frequent_value_or_values({}), None)
        with self.assertRaises(TypeError):
            most_frequent_value_or_values("not a dict")


    def test_key_is_in_both_dictionaries(self):
        self.assertTrue(key_is_in_both_dictionaries(
            {'a': 1, 'b': 2}, {'b': 3, 'c': 4}, 'b'))
        self.assertFalse(key_is_in_both_dictionaries(
            {'a': 1}, {'b': 2}, 'a'))
        with self.assertRaises(TypeError):
            key_is_in_both_dictionaries("not a dict", {'b': 2}, 'b')
        with self.assertRaises(TypeError):
            key_is_in_both_dictionaries({'a': 1}, "not a dict", 'a')


    def test_word_frequencies(self):
        self.assertEqual(word_frequencies("hello world hello"),
                         {'hello': 2, 'world': 1})
        self.assertEqual(word_frequencies("a b a c b a"),
                         {'a': 3, 'b': 2, 'c': 1})
        self.assertEqual(word_frequencies("test test test"), {'test': 3})
        self.assertEqual(word_frequencies(""), {})
        with self.assertRaises(TypeError):
            word_frequencies(12345)
        with self.assertRaises(TypeError):
            word_frequencies(["not", "a", "string"])
        with self.assertRaises(TypeError):
            word_frequencies({"not": "a string"})


if __name__ == "__main__":
    unittest.main()