import re

def word_count(s):
    # Your code here
    list_value =  s.lower().split()
    dict_value = {}
    for word in list_value:
        newword = re.sub("[^a-zA-Z' ]+", "", word)
        if len(newword) >0:
            if newword in dict_value.keys():
                dict_value[newword] += 1
            else:
                dict_value[newword] = 1
    print(dict_value)
    return dict_value


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))