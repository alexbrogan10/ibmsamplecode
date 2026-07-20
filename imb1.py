def solvePalindrome(s):
    # Initialize pointers at the start and end of the string
    left = 0
    right = len(s) - 1
    replacements = 0
    
    # Move towards the center
    while left < right:
        # If characters don't match, we need one replacement
        if s[left] != s[right]:
            replacements += 1
        # Move pointers closer
        left += 1
        right -= 1
        
    return replacements