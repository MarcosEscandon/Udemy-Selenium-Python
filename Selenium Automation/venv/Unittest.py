import unittest

class method_unittest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("Init of Class")

    def setUp(self):
        print("Init in every test")

    def test_message(self):
        print("message from TestCase")

    def test_num(self):
        print("Num test case")

    def tearDown(self):
        print("End of execution")

    @classmethod
    def tearDownClass(cls) -> None:
        print("End of Class")

if __name__ == "__main__":
    unittest.main()