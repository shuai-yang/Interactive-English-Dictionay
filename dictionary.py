import mysql.connector
con = mysql.connector.connect(
user = "ardit700_student", password = "ardit700_student",
host = "108.167.140.122", database = "ardit700_pm1database"
)
cursor = con.cursor()
import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

query = cursor.execute("SELECT * FROM Dictionary")
results = cursor.fetchall()
words=[]
for result in results:
    words.append(result[0])
#print(words)

def translate(word):
    query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s' OR Expression = '%s' OR Expression = '%s'" % (word, word.title(), word.upper() ))
    results = cursor.fetchall()
    if results:
        for result in results:
            print (result[1])
    elif len(get_close_matches(word, words)) > 0: 
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word, words)[0])
        if yn.lower() == 'y':
            query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % get_close_matches(word, words)[0])
            results = cursor.fetchall()
            for result in results:
                print (result[0])
        elif yn.lower() == 'n':
            print ("The word doesn't exist. Please double check it.")
        else:
            print ("Please enter Y/N.")
    else:
        print ("The word doesn't exist. Please double check it.")
        
word = input("Enter word: ")
translate(word)