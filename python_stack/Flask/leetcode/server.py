def areOccurrencesEqual(text):
    counts = {}
    
    for char in text:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
            
    frequencies = list(counts.values())
    first_frequency = frequencies[0]
    
    for f in frequencies:
        if f != first_frequency:
            return False 
            
    return True 


test1 = "abacbc"
print(f"Input: '{test1}' -> Result: {areOccurrencesEqual(test1)}") 

test2 = "aaabb"
print(f"Input: '{test2}' -> Result: {areOccurrencesEqual(test2)}")

test3 = "vvvvvv"
print(f"Input: '{test3}' -> Result: {areOccurrencesEqual(test3)}")
