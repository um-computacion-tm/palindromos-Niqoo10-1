import unittest

from palindromo import palindromo

class TestPalindrome(unittest.TestCase):

    def test_palindromo(self):
        result = palindromo('oso')
    def test_palindrome1(self):
        result = palindromo('neuquen') 
    def test_palindrome2(self):
        result = palindromo('radar')
    def test_palindrome4(self):
        result = palindromo('reconocer')
    def test_palindrome5(self):
        result = palindromo('oto')
       

if __name__ == '__main__':
    unittest.main()