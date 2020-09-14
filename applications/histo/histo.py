# Your code here
import sys
longest = 0
def word_count(s):
    # Your code here
    dict = {}
    forbidden = '":;,.-+=/\|[]{}()*^$&'
    global longest

    word = ""
    for c in s:
        if c != ' ' and c != '\t' and c != '\r' and c != '\n':
            if c not in forbidden:
                word += c
        else:
            length = len(word)
            if length > 0:
                word = word.lower()
                if word in dict:
                    dict[word] += 1
                else:
                    dict[word] = 1
                    if length > longest:
                        longest = length

                word = ""

    length = len(word)
    if length > 0:
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1
            if length > longest:
                longest = length

    return dict

with open(sys.argv[1]) as f:
    words = f.read()

def criteria(e):
    return e[1]


dict = word_count(words)
array1 = list(dict.items())
array1.sort(reverse=True, key=criteria)

longest += 2
histogram = ""
for e in array1:
    histogram += e[0]

    for i in range(len(e[0]), longest):
        histogram += " "

    for i in range(int(e[1])):
        histogram += "#"

    histogram += "\n"

if histogram[-1] == '\n':
    histogram = histogram.strip('\n')
print(histogram)
#dict.sort()
#print(dict)

