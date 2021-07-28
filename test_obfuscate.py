import unittest
from obfuscate import Obfuscate


class TestObfuscate(unittest.TestCase):
    def test_init(self):
        t = Obfuscate(".example.py")

        self.assertTrue(type(t.code_data) is list)
        self.assertTrue(len(t.code_data) > 0)

    # def test_generate_strings(self):

    # def test_load_file(self):

    # def test_obfuscate_func_names(self):

    # def test_obfuscate_var_names(self):


if __name__ == "__main__":
    unittest.main()
