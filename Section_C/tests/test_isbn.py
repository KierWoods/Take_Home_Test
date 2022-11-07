import unittest

from isbn import e_input
from isbn import isbn_checker

# Define new test case. 
class TestISBN(unittest.TestCase):
    
    # Test for ISBN checker. 
    def test_isbn(self): 

        result = isbn_checker("817450494X")
        assert(result, 9788174504944)
        
        result2 = isbn_checker("0316066524")
        assert(result2, "Valid")

if __name__ == '__main__':
    unittest.main()