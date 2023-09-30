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


for word in txt:
    if re.search("aardvark", word):
        print("we found the word")

# uh hey this isn't done yet