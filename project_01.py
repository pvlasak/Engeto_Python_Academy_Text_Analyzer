from string import punctuation
TEXTS = [
     """Situated about 10 miles west of Kemmerer,
        Fossil Butte is a ruggedly  ,,, impressive
        topographic feature that rises sharply
        some 1000 feet above Twin Creek Valley
        to an elevation of more than 7500 feet
        above sea level. The butte is located just
        north of US 30N and the Union Pacific Railroad,
        which traverse the valley. """,
     """At the base of Fossil Butte are the bright
        red, purple, yellow and gray beds of the Wasatch
        Formation. Eroded portions of these horizontal
        beds slope gradually upward from the valley floor
        and steepen abruptly. Overlying them and extending
        to the top of the butte are the much steeper
        buff-to-white beds of the Green River Formation,
        which are about 300 feet thick.""",
     """The monument contains 8198 acres and protects
        a portion of the largest deposit of freshwater fish
        fossils in the world. The richest fossil fish deposits
        are found in multiple limestone layers, which lie somepaddlefish,
        100 feet below the top of the butte. The fossils
        represent several varieties of perch, as well as
        other freshwater genera and herring similar to those
        in modern oceans. Other fish such as 
        garpike and stingray are also present.""",
     """Second, in some situations regression analysis can be 
        used to infer causal relationships between the independent 
        and dependent variables. Importantly, regressions by 
        themselves only reveal relationships between a dependent 
        variable and a collection of independent variables 
        in a fixed dataset."""
]

text_count = len(TEXTS)
text_ids = list(range(1, len(TEXTS)+1))

# Usernames and passwords dictionary
user_passwd_dict = {'bob': '123', 'ann': 'pass123', 'mike': 'password123', 'liz': 'pass123'}
#
# Setting of all user names from dictionary
#
users = set(user_passwd_dict.keys())
delimiter_1 = "-" * 60
separator = "." * 4

print(delimiter_1)
print('Dear user, please enter your username and password.')
print(delimiter_1)

#
# Login verification - Start
#
username = input('username: ').lower()
password = input("password: ")
if username in users:
    if password != user_passwd_dict[username]:
        print("Wrong credentials.")
        quit()
    else:
        print(delimiter_1)
        print(f"Welcome to Text Analyzer App, {username.title()}!!")
else:
    print(delimiter_1)
    print("Wrong credentials.")
    quit()
#
# Login verification - End
#
#
# Text ID selection - Start
#
print(delimiter_1)
print(f"We have got {text_count} texts to be analyzed:\n")
for i in text_ids:
    print("(" + str(i) + ")" + separator + "Text " + str(i))

entry_verification = True
while entry_verification:
    selected_text_id = input("Select text ID " + str(text_ids) +" :")
    if selected_text_id.isnumeric() and int(selected_text_id) in text_ids:
        print(f"You selected text nr. {selected_text_id}")
        index = int(selected_text_id) - 1
        entry_verification = False
    else:
        print("Wrong input is given. Please try it again.")

#
# Text ID selection - End
#
print(delimiter_1)
#
# Text Cleaning  - Start
#
list_of_words = TEXTS[index].split()
clean_words = []

clean_words = [
    word.strip(punctuation) for word in list_of_words
    if word.strip(punctuation)
]


print(list_of_words)
print(clean_words)
#
# Text Cleaning  - End
#
list_title = []
list_upper = []
list_lower = []
list_num_str = []

for word in clean_words:
    if word.isnumeric():
        list_num_str.append(word)
    if word.istitle():
        list_title.append(word)
    if word.isupper() and word.isalpha():
        list_upper.append(word)
    if word.islower():
        list_lower.append(word)

print(delimiter_1)
print(list_upper)
print(list_num_str)
print(list_lower)
print(list_title)
print(delimiter_1)
#for i in range(len(list_num_str)):
#    numbers.append(int(''.join([letter for letter in list_num_str[i] if letter.isdigit()])))

#
# Print Output - Start
#
print(
f"There are {len(clean_words)} words in the selected text.\n"
f"There are {len(list_title)} titlecase words.\n"
f"There are {len(list_upper)} uppercase words.\n"
f"There are {len(list_lower)} lowercase words.\n"
f"There are {len(list_num_str)} numeric strings.\n"
f"The sum of all the numbers {sum(map(int, list_num_str))}.")
print(delimiter_1)
#
# Print Output - End
#
#
# Print: Final Table of Occurrences - Start
#
title = "OCCURRENCE"

max_word_length = 0
for word in clean_words:
    if len(word) > max_word_length:
        max_word_length = len(word)

# Dictionary of word length occurrence
word_range = range(1, (max_word_length+1))
word_len_freq_dict = {}
for key in word_range:
    word_len_freq_dict[key] = 0

for word in clean_words:
    word_len_freq_dict[len(word)] = word_len_freq_dict[len(word)] + 1
max_frequency = max(word_len_freq_dict.values())

# Width setting of the output table
if max_frequency > len(title) and max_frequency % 2 == 0:
    table_width = max_frequency
elif max_frequency > len(title) and max_frequency % 2 == 1:
    table_width = max_frequency + 1
else:
    table_width = len(title)

title_spaces = int((table_width - len(title)) / 2)

print("LEN|" + " " * title_spaces + title + " " * title_spaces + "|NR.")
print(delimiter_1)
for k in word_len_freq_dict:
    if k <= 9:
        bar = "*" * word_len_freq_dict[k]
        spaces = (table_width - word_len_freq_dict[k])*" "
        print("  " + f"{k}|" + bar + spaces + "|" + str(word_len_freq_dict[k]))
    else:
        bar = "*" * word_len_freq_dict[k]
        spaces = (table_width - word_len_freq_dict[k])*" "
        print(" " + f"{k}|" + bar + spaces + "|" + str(word_len_freq_dict[k]))
print(delimiter_1)

#
# Print: Final Table of Occurrence - End
#