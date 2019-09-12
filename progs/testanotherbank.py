import unittest
import bank
class TestBank1(unittest.TestCase):
    def test_sa_create(self):
        sa = bank.SA('Aditya')
        assert sa.b == 1000, "US101: default bal should be 1000"
    def test_ca_create(self):
        ca = bank.CA('Aditya')
        assert ca.b == 0, "US102: default bal should be 0"
    def test_ca_credit(self):
        ca = bank.CA('Aditya')
        ca.credit(100)
        assert ca.b == 100, "US103: default bal should be 100"
    def test_sa_credit(self):
        sa = bank.SA('Aditya')
        sa.credit(100)
        assert sa.b == 1100, "US103: default bal should be 1100"

if __name__ == '__main__':
    unittest.main(verbosity=3)
    #ts = unittest.TestSuite()
    #ts.addTest(TestBank('test_sa_create'))
    #ts.addTest(TestBank('test_sa_credit'))
    #
    #r = unittest.TextTestRunner(verbosity = 3)
    #r.run(ts)






