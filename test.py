import unittest

def solution(A):
    # Convert the list to a set for faster lookup
    seen = set(A)
    
    # Iterate from 1 to len(A)
    for i in range(1, len(A) + 1):
        # If i is not in the set, it means it's not in A, so return it
        if i not in seen:
            return i
    
    # If we reached the end of the loop without finding a number not in A, return len(A) + 1
    return len(A) + 1


class TestFrogJump(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(solution([1, 3, 6, 4, 1, 2]), 5)

    def test_one(self):
        self.assertEqual(solution([−1, −3]), 1)



if __name__ == "__main__":
    unittest.main()

    
    
# Method 	Equivalent to
# .assertEqual(a, b) 	a == b
# .assertTrue(x) 	bool(x) is True
# .assertFalse(x) 	bool(x) is False
# .assertIs(a, b) 	a is b
# .assertIsNone(x) 	x is None
# .assertIn(a, b) 	a in b
# .assertIsInstance(a, b) 	isinstance(a, b)

# .assertIs(), .assertIsNone(), .assertIn(), and .assertIsInstance() all have opposite methods, named .assertIsNot(), and so forth.