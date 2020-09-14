def word_count(s):
    # Your code here
    dict = {}
    forbidden = '":;,.-+=/\|[]{}()*^$&'

    word = ""
    for c in s:
        if c != ' ' and c != '\t' and c != '\r' and c != '\n':
            if c not in forbidden:
                word += c
        else:
            if len(word) > 0:
                word = word.lower()
                if word in dict:
                    dict[word] += 1
                else:
                    dict[word] = 1

                word = ""

    if len(word) > 0:
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1

    print(dict)
    return dict







if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))