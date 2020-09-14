def no_dups(s):
    # Your code here
    dict = {}
    forbidden = '":;,.-+=/\|[]{}()*^$&'

    word = ""
    no_dups = ""
    for c in s:
        if c != ' ' and c != '\t' and c != '\r' and c != '\n':
            if c not in forbidden:
                word += c
        else:
            if len(word) > 0:
                #word = word.lower()
                if word not in dict:
                    dict[word] = 1
                    if len(no_dups) == 0:
                        no_dups += word
                    else:
                        no_dups += f' {word}'

                word = ""

    if len(word) > 0:
        #word = word.lower()
        if word not in dict:
            dict[word] = 1
            if len(no_dups) == 0:
                no_dups += word
            else:
                no_dups += f' {word}'

        word = ""

    return no_dups


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))