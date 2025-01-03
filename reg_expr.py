

# Regular Expressions
"""Copilot"""
# Regular expressions are a powerful tool for various kinds of string manipulation. They are a domain specific language (DSL) that is present as a library in most modern programming languages, not just Python. They are useful for two main tasks:
#
# 1. verifying that strings match a pattern (for instance, that a string has the format of an email address),
# 2. performing substitutions in a string (such as changing all American spellings to British ones).
#
# Python's `re` module is used to work with regular expressions. The `re` module raises the exception `re.error` if an error occurs while compiling or using a regular expression.
import re
# The `re` module offers a set of functions that allows us to search a string for a match:
# Function	Description 
# findall	Returns a list containing all matches 
# search	Returns a Match object if there is a match anywhere in the string 
# split	Returns a list where the string has been split at each match
# sub	Replaces one or many matches with a string
# Metacharacters are characters with a special meaning: 
# Character	Description	Example	Try it
# []	A set of characters	"[a-m]"
# \	Signals a special sequence (can also be used to escape special characters)	"\d"
# .	Any character (except newline character)	"he..o"
# ^	Starts with	"^hello"
# $	Ends with	"world$"
# *	Zero or more occurrences	"aix*"
# +	One or more occurrences	"aix+"
# {}	Exactly the specified number of occurrences	"al{2}"
# |	Either or	"falls|stays"
# ()	Capture and group
# Special Sequences
# A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:
# Character	Description	Example	Try it
# \A	Returns a match if the specified characters are at the beginning of the string	"\AThe"
# \b	Returns a match where the specified characters are at the beginning or at the end of a word	r"\bain"
# r"ain\b"
# \B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word	r"\Bain"
# r"ain\B"
# \d	Returns a match where the string contains digits (numbers from 0-9)	"\d"
# \D	Returns a match where the string DOES NOT contain digits	"\D"
# \s	Returns a match where the string contains a white space character	"\s"
# \S	Returns a match where the string DOES NOT contain a white space character	"\S"
# \w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"
# \W	Returns a match where the string DOES NOT contain any word characters	"\W"
# \Z	Returns a match if the specified characters are at the end of the string	"Spain\Z"
# Sets
# A set is a set of characters inside a pair of square brackets [] with a special meaning:
# Set	Description	Try it
# [arn]	Returns a match where one of the specified characters (a, r, or n) are present
# [a-n]	Returns a match for any lower case character, alphabetically between a and n
# [^arn]	Returns a match for any character EXCEPT a, r, and n
# [0123]	Returns a match where any of the specified digits (0, 1, 2, or 3) are present
# [0-9]	Returns a match for any digit between 0 and 9
# [0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59
# The findall() Function
# The `findall()` function returns a list containing all matches.
# The list contains the matches in the order they are found.
# If no matches are found, an empty list is returned:
# Example
# Search for the first white-space character in the string:
txt = "The rain in Spain"
x = re.findall(" ", txt)
print(x)
# The search() Function
# The `search()` function searches the string for a match, and returns a Match object if there is a match.
# If there is more than one match, only the first occurrence of the match will be returned:
# Example
# Search for the first white-space character in the string:
txt = "The rain in Spain"
x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start())
# If no matches are found, the value `None` is returned:
# Example
# Make a search that returns `None` if no match was found:
txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)
# The split() Function
# The `split()` function returns a list where the string has been split at each match:
# Example
# Split at each white-space character:
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)
# You can control the number of occurrences by specifying the `maxsplit` parameter:
# Example
# Split the string only at the first occurrence:
txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)
# The sub() Function
# The `sub()` function replaces the matches with the text of your choice:
# Example
# Replace every white-space character with the number 9:
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)
# You can control the number of replacements by specifying the `count` parameter:
# Example
# Replace the first 2 occurrences:
txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)
# Match Object
# A Match Object is an object containing information about the search and the result.
# If there is no match, the value `None` will be returned, instead of the Match Object.
# The Match object has properties and methods used to retrieve information about the search, and the result:
# .span() returns a tuple containing the start-, and end positions of the match.
# .string returns the string passed into the function
# .group() returns the part of the string where there was a match
# Example
# Do a search that will return a Match Object:
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())
print(x.string)
print(x.group())
# Example
# The regular expression looks for any words that starts with an upper case "S":
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())
# Example
# Print the string passed into the function:
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)
# Example
# Print the part of the string where there was a match:
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())
# Example





x = "yolo string! 123"
x.split(sep=" ", maxsplit=2)
"""["yolo", "string!", "123"]"""
x[1:3:1] #index : slicing : stride or step
x[0:6:2] # this is the same as x[0:6:1] because the default step is 1
x.rsplit(sep=" ", maxsplit=2)
"""["yolo", "string!", "123"]"""
print(x)
x.split(sep=" ", maxsplit=1)
x = x + "\nyo moma\rwutthisdooo" # this will work (what do cariage returns do?)
import time
for i in range(1,11):
    print(f'\rCount: {i}', end='')
    time.sleep(1)
#In this example, the \r moves the cursor back to the beginning of the line, and the end='' argument in the print function prevents it from advancing to the next line. As a result, the output will update the same line with the new count every second. It would be fun to rewrite each line in a mat lib. 

new = x.splitlines() 
new
x
print(x)
# CONCATENATE
sep = " "
new2 = sep.join(new) # sep is the separator, iterable is the list of strings to join
new2
print(" ".join(new)) # this is the same as new2


my_string = " This string will be stripped\n"
my_string
print(my_string)
my_string.strip()
my_string.lstrip()
my_string.rstrip()

my_string.strip(" T")


movie = "$I supposed that coming from MTV Films I should expect no less$"
# Convert to lowercase and print the result
movie_lower = movie.lower()
print(movie_lower)
# Remove specified character and print the result
movie_no_sign = movie_lower.strip("$")
print(movie_no_sign)
# Split the string into substrings and print the result
movie_split = movie_no_sign.split()
print(movie_split)
# Select root word and print the result
word_root = movie_split[1][:-1]
print(word_root)
print(movie)


""" splitting the string and joining it back again without the commas."""
str = "hel,llo, word, wut up,!"
l = str.split(sep=",")
m = " ".join(l)
l
m


str.find("llo")
str.index("llo")
str.find("llo", 3)
str.index("llo", 3) # this will raise an error
str.count("llo")
str.replace("llo", "llooo")
str.replace("llo", "llooo", 1) # this will only replace the first instance of "llo"


#yolo

movies = ["actor actor actor movie", "actor actor movie", "actor movie", "movie"]

for movie in movies:
  	# If actor is not found between character 37 and 41 inclusive
    # Print word not found
    if movie.find("actor", 37, 41) == -1:
        print("Word not found")
    # Count occurrences and replace two with one
    elif movie.count("actor") == 2:  
        print(movie.replace("actor actor", "actor"))
    else:
        # Replace three occurrences with one
        print(movie.replace("actor actor actor", "actor"))


"""
Finding Substrings:
The .find() method searches for a specified substring and returns the lowest index where it is found. If not found, it returns -1.
The .index() method works similarly to .find() but raises an exception if the substring is not found. This can be handled using a try-except block.

Counting Substrings:
The .count() method returns the number of non-overlapping occurrences of a substring within the target string.

Replacing Substrings:
The .replace() method replaces occurrences of a substring with a new substring. You can specify how many occurrences to replace.
"""



# Import class datetime from datetime 
from datetime import datetime

# Assign date to get_date
get_date = datetime.now()

# Add named placeholders with format specifiers
message = "Good morning. Today is {today:%B %d, %Y}. It's {today:%H:%M} ... time to work!"

# Use the format method replacing the placeholder with get_date
print(message.format(today=get_date))


o = "I am a string"
print(f"{o!r}"+f" {o!s} "+f"{o!a}") # !r calls repr(), !s calls str(), !a calls ascii()
# :e :d :.2f is for scientific notation, (d) decimal, and (f) float

# ACCESING DATETIME OBJECT ATTRIBUTES
west = {'date': datetime.datetime(2006, 5, 26, 0, 0), 'price': 1432673}
print(f"The price for a house in the west neighborhood was ${west['price']} in {west['date']:%m-%d-%Y}.") #kinda like :.2f 



# TEMPLATE STRINGS:
from string import Template
temp = Template("Template example with placeholder : $placeholder")
sub = "***"
print(temp.substitute(placeholder=sub))





# REGULAR EXPRESSIONS FOR PATTERN MATCHING
import re #search, match, and manipulate strings using regex patterns
string = "all is one but two ... all"
re.findall(r"all",string) #returns a list of strings each time it is found
re.split(r"a",string) #returns a list of strings split (excludes the a)
re.sub(r"ll","lso",string) 
re.findall(r"User\d", "The winners are: User9, usern, UserD, userJ") #supported metacharacters \d digit
re.findall(r"User\D", "The winners are: User9, usern, UserD, user8") #\D non-digit
re.findall(r"\W\d","ice cream costed $5")  #\w word
re.findall(r"\w\d","this skirt is on sale! Only $5 dollars today!")  #\W non-word && digit
re.findall(r"Data\sScience","I enjoy learning Data Science") #\s whitespace
re.sub(r"ice\Scream","ice cream", "i luve ice-cream") #\S no-whitespace. 
# * zero or more times
# + once or more
# ? zero or once
# Tokenization is the process of breaking a string into lexical units or, in simpler terms, words. 
sentiment_analysis = "ITS NOT ENOUGH TO SAY THAT IMISS U #MissYou #SoMuch #Friendship #Forever"
regex = r"#\w+"
no_hashtag = re.sub(regex, "", sentiment_analysis)
print(re.split(r"\s+", no_hashtag))
# Periods are used to match any character (except newline)
my_links = "Just check out this link: www.amazingpics.com. It has amazing photos!"
re.findall(r"www.+com", my_Links) #['www.amazingpics.com']
re.search(r"www.+com", my_Links) #<re.Match object; span=(23, 40), match='www.amazingpics.com
re.match(r"www.+com", my_Links) #None because it only matches the start of the string. 
# \. is used to escape the period character in the regex, ^ is used to match the start of a string, and $ is used to match the end of a string.

