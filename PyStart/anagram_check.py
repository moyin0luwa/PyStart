def find_anagram(word, anagram):
    return word.lower() == anagram.lower()[::-1]


user_word = input(f'Please input your word _')
user_anagram = input(f'Please input your supposed anagram _')
anagram_check = find_anagram(user_word, user_anagram)
if anagram_check:
    print(f'The word {user_anagram} is an anagram of {user_word}')
else:
    print(f'{user_word} and {user_anagram} are not anagrams')