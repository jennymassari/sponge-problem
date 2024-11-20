def sponge_case(sentence):
    # Convert the entire sentence to lowercase to start with
    sentence = sentence.lower()
    
    # Split the sentence into words
    words = sentence.split()
    
    # List to hold the modified characters
    result = []
    
    # Iterate over each word in the list
    for word in words:
        # Enumerate over the characters in the word
        for index, char in enumerate(word):
            # Check if the index is even or odd
            if index % 2 == 0:
                # Even index: keep lowercase (it's already lowercase from sentence.lower())
                result.append(char)
            else:
                # Odd index: convert to uppercase
                result.append(char.upper())
        
        # Add a space after each word to maintain the structure
        result.append(' ')
    
    # Join the result list into a string and return it
    return ''.join(result).strip()


# Test cases
assert sponge_case("spongebob") == "sPoNgEbOb"
assert sponge_case("Who are YOU calling A Pinhead") == "wHo aRe yOu cAlLiNg a pInHeAd"
assert sponge_case("WHAT is UP my dude") == "wHaT iS uP mY dUdE"
assert sponge_case("E") == "e"
assert sponge_case("e") == "e"
print("All tests passed!")
print("Discuss time and space complexity if there's time remaining")
