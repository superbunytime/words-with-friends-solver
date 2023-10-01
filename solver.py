import re

def read_dict(dict_path):
    """read and return all words in dictionary"""

    dict_file = open(dict_path)
    words = [w.strip() for w in dict_file]
    dict_file.close()
    return words

# print(read_dict("words.txt"))
# cool that works

"""do i make a regex builder"""

txt = read_dict("words.txt")
print(type(txt))
# x = re.search("/aardvark/", txt)
# # if x:
# #     print("yeee")
# # else:
# #     print("NOOOOOOOOOO")


# for word in txt:
#     if re.search("aardvark", word):
#         print(word)



for word in txt:
    if not re.findall("[^tcyvior]", word) and len(word) > 3 and len(word) < 5:
        print(word)
# uh hey this isn't done yet

# let's test with the string on bun's stream

# t g i h n f i g

# correct words: gift hint high thin ting fight night thing gifting fighting
# there may be more words than this, and this doesn't factor in fake letters
# but it's an excellent starting point.

# problem: it allows extra words; like if there's 1 o in the string it will return 
# words that have two o's
# also needs a better dictionary; this one puts out too many nonsense words
# that would never be used in words with friends

# problem: need a handler for mystery word