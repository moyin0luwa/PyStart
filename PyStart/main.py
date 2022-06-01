def read_file_content(filename):
    with open(filename, "r") as f:
        return f.read()

def count_words():
    text = read_file_content("./story.txt")
    story_list = text.split()
    count_dict = {}
    for word in story_list:
        count_dict[word] = story_list.count(word)
    return count_dict

count = count_words()
print(count)