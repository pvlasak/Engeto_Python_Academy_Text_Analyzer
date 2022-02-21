TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie somepaddlefish,
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as 
garpike and stingray are also present.'''
]

text_1 = TEXTS[0]
text_2 = TEXTS[1]
text_3 = TEXTS[2]

# Usernames and passwords dictionary
user_passwd_dict = {
    'bob' : '123',
    'ann' : 'pass123',
    'mike' : 'password123',
    'liz' : 'pass123'
}

# Set of all user names from dictionary
users = set(user_passwd_dict.keys())
delimiter_1 = "-" * 60
separator = "." * 4

print(delimiter_1)
print('Dear user, please enter your username and password.')
print(delimiter_1)
username = input('username: ').lower()

if username in users:
    while (password := input("password: ")) != user_passwd_dict[username]:
        print("Password is wrong. Try it again!")
    else:
        print(delimiter_1)
        print(f"Welcome to Text Analyzer App, {username.title()}!!")
else:
    print(delimiter_1)
    print('Username does not exist! Program is quiting...')
    quit()

print(delimiter_1)
print("We have got 3 texts to be analyzed:\n"
      "(1)" + separator + "Text 1\n"
      "(2)" + separator + "Text 2\n"
      "(3)" + separator + "Text 3"
      )
index = int(input("Select text ID (1,2,3): ")) - 1
print(delimiter_1)

list_of_words = TEXTS[index].split()
list_title = []
list_upper = []
list_lower = []
list_num_str = []
numbers =[]

for word in list_of_words:
    for i in range(len(word)):
        if word[i].isdigit():
            list_num_str.append(word)
            break
    if word.istitle() and word not in list_num_str:
        list_title.append(word)
    if word.isupper() and word not in list_num_str:
        list_upper.append(word)
    if word.islower() and word not in list_num_str:
        list_lower.append(word)

for i in range(len(list_num_str)):
    numbers.append(int(''.join([letter for letter in list_num_str[i] if letter.isdigit()])))

print(
f"There are {len(list_of_words)} words in the selected text.\n"
f"There are {len(list_title)} titlecase words.\n"
f"There are {len(list_upper)} uppercase words.\n"
f"There are {len(list_lower)} lowercase words.\n"
f"There are {len(list_num_str)} numeric strings.\n"
f"The sum of all the numbers {sum(numbers)}.")
print(delimiter_1)

word_range = range(1,16)

word_len_dict = {}
for key in word_range:
    word_len_dict[key] = 0

for word in list_of_words:
    word_len_dict[len(word)] = word_len_dict[len(word)] + 1


print("LEN|" + " "*4 + "OCCURENCES" + " "*4 + "|NR.")
print(delimiter_1)
for k in word_len_dict:
    if k <= 9:
        spacer = "*" * word_len_dict[k]
        spaces = (18 - word_len_dict[k])*" "
        print("  " + f"{k}|" + spacer + spaces + "|" + str(word_len_dict[k]))
    else:
        spacer = "*" * word_len_dict[k]
        spaces = (18 - word_len_dict[k])*" "
        print(" " + f"{k}|" + spacer + spaces + "|" + str(word_len_dict[k]))
print(delimiter_1)