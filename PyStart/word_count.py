def read_file_content(filename):
    f = open(filename, "r")
    return f.read()


#           OR
# def read_file_content(filename):
#    with open(filename, "r") as f:
#        return f.read()

def count_words():
    text = read_file_content("./story.txt")
    story_list = text.split()
    count_dict = {}
    for word in story_list:
        count = 0
        for word1 in story_list:
            if word1 == word:
                count += 1
        count_dict[word] = count
    return count_dict


#                OR
#        def count_words():
#           text = read_file_content("./story.txt")
#          story_list = text.split()
#         count_dict = {}
#        for word in story_list:
#       return count_dict


print(count_words())
