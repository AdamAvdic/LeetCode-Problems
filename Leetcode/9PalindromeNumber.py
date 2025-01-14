class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        Str_x = str(x)  # Convert the number to a string
        string_length = len(Str_x)  # Get the length of the string

        # Compare characters from start and end until the middle
        for i in range(0, string_length // 2):
            if Str_x[i] != Str_x[string_length - 1 - i]:
                return False  # Return False if any mismatch is found
        
        return True  # If all checks pass, it's a palindrome