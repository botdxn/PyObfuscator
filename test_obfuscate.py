import unittest
from obfuscate import Obfuscate


class TestObfuscate(unittest.TestCase):
    def test_load_file(self):
        t = Obfuscate(".example.py")
        t_file = t.load_file()

        self.assertTrue(type(t_file) is list)
        self.assertTrue(len(t_file) > 0)

    # def test_generate_strings(self):

    # def test_load_file(self):

    # def test_obfuscate_func_names(self):

    # def test_obfuscate_var_names(self):


if __name__ == "__main__":
    unittest.main()
