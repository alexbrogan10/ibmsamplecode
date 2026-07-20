def decode(encoded):
    # Step 1: Reverse the string of digits
    reversed_str = encoded[::-1]
    
    decoded_chars = []
    i = 0
    n = len(reversed_str)
    
    # Step 2 & 3: Iterate through the string and parse ASCII values
    while i < n:
        # Check if it's a 3-digit ASCII value (starts with '1')
        if reversed_str[i] == '1':
            ascii_val = int(reversed_str[i:i+3])
            i += 3
        else:
            # Otherwise, it must be a 2-digit ASCII value
            ascii_val = int(reversed_str[i:i+2])
            i += 2
            
        # Convert the numerical ASCII value to its character representation
        decoded_chars.append(chr(ascii_val))
        
    # Join all the decoded characters into a single string
    return "".join(decoded_chars)