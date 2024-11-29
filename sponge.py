def sponge_case(sentence):
    
    words = sentence.split(" ")
    new_sentence = []

    for word in words:
        new_string = ""
        for index, letter in enumerate(word):
            if index % 2 == 0:
                new_string += letter.lower()
            else:
                new_string += letter.upper()
        new_sentence.append(new_string)
        print(new_sentence)
    
    return " ".join(new_sentence)



        
# print(sponge_case("WHAT is UP my dude"))
# print(sponge_case("Who are YOU calling A Pinhead"))

# Test cases
assert sponge_case("spongebob") == "sPoNgEbOb"
assert sponge_case("Who are YOU calling A Pinhead") == "wHo aRe yOu cAlLiNg a pInHeAd"
assert sponge_case("WHAT is UP my dude") == "wHaT iS uP mY dUdE"
assert sponge_case("E") == "e"
assert sponge_case("e") == "e"
print("All tests passed!")
print("Discuss time and space complexity if there's time remaining")

# Clasroom solution:
# # def sponge_case(sentence):
#     # turn the sentence into an array of individual words
#     words = sentence.split()

#     # create a new array of sponge-case words using our helper function
#     new_words = []
#     for word in words:
#         new_words.append(sponge_single_word(word))

#     # Join the new spongy words with spaces
#     return " ".join(new_words)


# # Helper function that converts a single word to sponge-case 
# def sponge_single_word(word):
#     new_word = ""
#     # Instructions say the word must start with a lowercase letter
#     # We will toggle this variable to alternate between lower and upper case
#     lower = True 

#     for letter in word:
#     # if our toggle is set to lowercase, add a lowercase version of the letter
#         if lower:
#             new_word += letter.lower()
#         # if our toggle is set to lowercase, add a uppercase version of the letter
#         else:
#             new_word += letter.upper()
#         # flip our toggle
#         lower = not lower
    
#     return new_word