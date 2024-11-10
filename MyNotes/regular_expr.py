import re
from re import search


def regex_basic_example():
    pattern = r"Python"
    text = "I'm learning Python, Python12, Python56"

#для поиска 1 совпадения
    match = re.search(pattern, text)
    if match:
        print("match found: ", match.group())
    else:
        print("Not found match ")

regex_basic_example()



def regex_special_character():
    text="Email me at test test@email.com or admin@example.com"

    pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9._]+\.[A-Z|a-z]{2,}\b"

# для поиска всех совпадений
    matches = re.findall (pattern, text)
    print ("Found email", matches)

regex_special_character()

def regex_methods_example():
    text = "The price is between $50 and $160"

    match = re.match(r"The price", text)
    if match:
        print("Results of match: ", match.group())
    else:
        print("Matches are not found")

    search = re.search(r"\$\d+", text)
    print("Results of search: ",search.group() if search else "Matches are not found")


regex_methods_example()