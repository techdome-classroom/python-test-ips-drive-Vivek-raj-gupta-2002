def longest_substring(s: str) -> int:
    
    """"
    
    Implement the function longest_substring 
    using the provided longest_substring function to find 
    the length of the longest substring without repeating characters.

    """ 
    
    if not s:
        return 0
    
   
    last_seen = {}
    max_length = 0
    start = 0
    
    for end in range(len(s)):
        
        if s[end] in last_seen and last_seen[s[end]] >= start:
            start = last_seen[s[end]] + 1
        
        
        last_seen[s[end]] = end
        
        
        max_length = max(max_length, end - start + 1)

    
    
    return max_length

