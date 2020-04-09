a_string = 'What is this book about? This book is about python coding'
new_string = ""
for char in a_string:
    if not 33 <= ord(char) <= 64:
        new_string = new_string + char
new_string_list = new_string.lower().split()

## 1
# count_of_words = {}
# for a_word in new_string_list:
#    if a_word not in count_of_words:
#        count_of_words[a_word] = 1
#    else:
#        count_of_words[a_word] += 1
##print(count_of_words)

# 2
count_of_words = {a_word: new_string_list.count(a_word) for a_word in new_string_list}
print(count_of_words)
