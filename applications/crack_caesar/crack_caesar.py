# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
import string
order = "ETAOHNRISDLWUGFBMYCPKVQJXZ"
with open("ciphertext.txt") as f:
    words = f.read()

freq = {}
for c in words:
    if c not in string.ascii_letters:
        continue

    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1

freq_array = list(freq.items())
freq_array.sort(reverse=True, key=lambda e:e[1])

freqstr =""
for e in freq_array:
    freqstr += e[0]


decoded = ""

for c in words:
    if c not in string.ascii_letters:
        decoded += c
    else:
        index = freqstr.find(str(c))
        #print(c, freq_array[index][0])
        decoded += order[index]

print(decoded)


