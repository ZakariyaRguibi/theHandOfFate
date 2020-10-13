# helper file
# todo: maybe add async await model ?

# insert a string inside another string in a specific index
# if the index isn't valid aka -1 then return the original string
def insert_sting_middle(str, word, index):
    if index == -1:
        print("index not valid")
        return str
    else:
        return str[:index] + word + str[index:]


# insert a string inside another string before a specific word
# eg: insert "." before "+" in "2 + 3"
def insert_string_before(sentance, word, word_to_input):
    index = sentance.find(word)
    return insert_sting_middle(sentance, word_to_input, index)


def chunks(s, n):
    """Produce `n`-character chunks from `s`."""
    schunked_string = []
    for start in range(0, len(s), n):
        schunked_string.append(s[start : start + n])
    return schunked_string
