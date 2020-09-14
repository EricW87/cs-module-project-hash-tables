import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here
words = words.split()
markov_dict = {}

index = 0
for w in words:
    if w not in markov_dict:
        markov_dict[w] = []

    if index + 1 < len(words):
            markov_dict[w].append(words[index + 1])

    index += 1

#remove keys with no values

#print(markov_dict)
# TODO: construct 5 random sentences
# Your code here

count = 1
num_sentences = 5
sentences = ""
open_quote = False
open_parenthesis = False
while count <= num_sentences:
    word = random.choice(list(markov_dict.keys()))
    while not (word[0] >= 'A' and word[0] <= 'Z') and word[0] != '"' or (')' in word or word[-1] == '"'): #Get a "Start word"
        word = random.choice(list(markov_dict.keys()))

    if(word[0] == '"'):
        open_quote = True
    elif(word[0] == '('):
        open_parenthesis = True

    sentences += word + " " #Add to sentences string
    word = random.choice(markov_dict[word]) #get next word from list in dictionary 

    #check if word is a stop word; break from while loop if it is
    while open_quote or open_parenthesis or not (word[-1] == '.' or word[-1] == '?' or word[-1] == '!'):
        if word[-1] == '"' and not open_quote and not open_parenthesis and (word[-2] == '.' or word[-2] == '?' or word[-2] == '!'):
            break

        sentences += word + " " #add word to sentences string
        word = random.choice(markov_dict[word]) #get next word

        while ')' in word and not open_parenthesis:
            word = random.choice(markov_dict[word])

        while word[-1] == '"' and not open_quote:
            word = random.choice(markov_dict[word])

        while '(' in word and open_parenthesis:
            word = random.choice(markov_dict[word])

        while word[0] == '"' and open_quote:
            word = random.choice(markov_dict[word])

        if(open_quote):
            if '"' in word:
                open_quote = False
        elif open_parenthesis:
            if ')' in word:
                open_parenthesis = False
        elif(word[0] == '"'):
            open_quote = True
        elif '(' in word:
            open_parenthesis = True

    sentences += word #add stop word to sentences
    if count != num_sentences: #Don't need these line breaks if final sentence
        sentences += "\n\n"
    count += 1 #increase count

print(sentences)




