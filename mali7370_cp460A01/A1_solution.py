"""
-----------------------------
CP460 (Fall 2020)
Name: Mohsin Malik
ID:   170987370
Assignment 1
-----------------------------
"""
import utilities
import math

#punctuation = r"""!"#$%&'()*+,-./:;<=>?@[]^_`{|}~"""
punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
all_digits = "0123456789"
dict_file = 'engmix.txt'
lowercase = "abcdefghijklmnopqrstuvwxyz"

"""
----------------------------------------------------
            Task 1: Plaintext Detection
----------------------------------------------------
"""

"""
----------------------------------------------------
Parameters:   dict_file (str): filename
Return:       dict_list (list): 2D list
Description:  Reads a given dictionary file
              dictionary is assumed to be formatted: each word in a separate line
              Returns a list of lists, list 0 contains all words starting with 'a'
              list 1 all words starting with 'b' and so forth.
Asserts:      dict_file is a non-empty string
---------------------------------------------------
"""
def load_dictionary(dict_file):
    #content = file_to_text(dict_file)
    infile = open(dict_file,'r', encoding="ISO-8859-15")
    contents = infile.readlines()
    infile.close()
    dict_list = []
    for c in lowercase:
        letter_content = [x.strip() for x in contents if x.startswith(c)]
        dict_list.append(letter_content)  
    # your code
    return dict_list

"""
----------------------------------------------------
Parameters:   text (str)
Return:       word_list (list)
Description:  Reads a given text
              Returns a list of strings, each pertaining to a word in file
              Words are separated by a white space (space, tab or newline)
              Gets rid of all special characters at the start and at the end
Asserts:      text is a string
---------------------------------------------------
"""
def text_to_words(text):
    """word_list = "".join((char if (char.isalpha() or char == "'" or char == "-" or char.isnumeric() or char == ".") else " ") for char in text).split() 
    for i in range(len(word_list)):
        if word_list[i] == ".":
            word_list.remove(word_list[i])
        elif word_list[i][-1] == ".":
            word_list[i] = word_list[i][:-1]"""
    #word_list = "".join((char if (char.isalpha() or char == "'" or char == "-" or char.isnumeric() or char == ".") else " ") for char in text).split()
    word_list = text.split()
    word_list = [i.strip(punctuation) for i in word_list]
    # your code
    return word_list

"""
----------------------------------------------------
Parameters:   text (str)
              dict_file (str)
Return:       match (int)
              mismatch (int)
Description:  Reads a given text, checks if each word appears in given dictionary
              Returns number of matches and number of mismatches.
              Words are compared in lowercase
              Uses load_dictionary and text_to_words functions
Asserts:      text and dict_file are both strings
---------------------------------------------------
"""
def analyze_text(text, dict_file):
    # your code
    match = 0;
    mismatch = 0;
    dict_list = load_dictionary(dict_file)
    words = text_to_words(text)
    for i in words:
        if(i.isalpha()):
            j = i.lower()
            start_char = ord(j[0])-97
            if j in dict_list[start_char]:
                match+=1;
            else:
                mismatch+=1;
        else:
            mismatch+=1;
    return match,mismatch

"""
----------------------------------------------------
Parameters:   text (str)
              dict_file (str): dictionary file
              threshold (float): number between 0 to 1
Return:       True/False
Description:  Check if a given file is a plaintext
              If #matches/#words >= threshold --> True
                  otherwise --> False
              If invalid threshold or not given, default is 0.9
              An empty string should return False
---------------------------------------------------
"""
def is_plaintext(text, dict_file, threshold=0.9):
    # your code
    if threshold <= 0 or threshold >= 1:
        threshold = 0.9
    match,mismatch = analyze_text(text, dict_file)
    if(match+mismatch == 0):
        return False
    elif (match/(match+mismatch)) >= threshold:
        return True
    return False

"""
----------------------------------------------------
            Task 2: Extended Atbash Cipher
----------------------------------------------------
"""

"""
----------------------------------------------------
Parameters:     plaintext(str)
                key (int)
Return:         ciphertext (str)
Description:    Encryption using Atbash Cipher
                If key = 0, uses lower case base
                If key = 1, uses upper case base
                If key = 2: uses upper+lower case
                If key = 3: uses upper+lower+num
                If key = 4: uses upper+lower+num+special
Asserts:      plaintext is a string and key is an integer
---------------------------------------------------
"""
def e_eatbash(plaintext, key):
    # your code
    lower = utilities.get_base("lower")
    upper = utilities.get_base("upper")
    special = utilities.get_base("special")
    alpha = utilities.get_base("alpha")
    alphanum = utilities.get_base("alphanum")
    all = utilities.get_base("all")
    ciphertext = ''
    key= key %5;
    for c in plaintext:
        if(c != ' '):
            if(key == 0 and c.islower()):
                ciphertext+= lower[abs(lower.index(c)-25)]
            elif(key == 1 and c.isupper()):
                ciphertext+= upper[abs(upper.index(c)-25)]
            elif(key == 2 and (c.isupper() or c.islower())):
                ciphertext+= alpha[abs(alpha.index(c)-51)]
            elif(key == 3 and (c.isupper() or c.islower() or c.isnumeric())):
                ciphertext += alphanum[abs(alphanum.index(c)-61)]
            elif(key == 4 and not (c.isspace())):
                ciphertext += all[abs(all.index(c)-93)]
            else:
                ciphertext+= c
        else:
            ciphertext+= ' '
    return ciphertext

"""
----------------------------------------------------
Parameters:   ciphertext(str)
              key (int)
Return:       plaintext (str)
Description:  Decryption using Atbash Cipher
              There is no key (None)
              Decryption can be achieved by encrypting ciphertext!!
Asserts:      ciphertext is a string and key is an integer
----------------------------------------------------
"""
def d_eatbash(ciphertext, key):
    # your code
    lower = utilities.get_base("lower")
    upper = utilities.get_base("upper")
    special = utilities.get_base("special")
    alpha = utilities.get_base("alpha")
    alphanum = utilities.get_base("alphanum")
    all = utilities.get_base("all")
    plaintext = ''
    key= key %5;
    for c in ciphertext:
        if(c != ' '):
            if(key == 0 and c.islower()):
                plaintext+= lower[abs(lower.index(c)-25)]
            elif(key == 1 and c.isupper()):
                plaintext+= upper[abs(upper.index(c)-25)]
            elif(key == 2 and (c.isupper() or c.islower())):
                plaintext+= alpha[abs(alpha.index(c)-51)]
            elif(key == 3 and (c.isupper() or c.islower() or c.isnumeric())):
                plaintext += alphanum[abs(alphanum.index(c)-61)]
            elif(key == 4 and not (c.isspace())):
                plaintext += all[abs(all.index(c)-93)]
            else:
                plaintext+= c
        else:
            plaintext+= ' '
    return plaintext

"""
----------------------------------------------------
Parameters:   ciphertext(str)
Return:       key (str)
              plaintext (str)
Description:  Cryptanalysis of Extended Atbash Cipher
              Key is in the range of 0-4
              Uses default dictionary file and threshold of 0.8
Asserts:      ciphertext is a string
----------------------------------------------------
"""
def cryptanalysis_eatbash(ciphertext):
    # your code
    for key in range (5):
        plaintext = d_eatbash(ciphertext, key)
        if is_plaintext(plaintext, "engmix.txt", 0.8):
            return key, plaintext
    key = None
    plaintext = ''
    return key,plaintext

"""
----------------------------------------------------
            Task 3: Scytale Cipher
----------------------------------------------------
"""

"""
----------------------------------------------------
Parameters:   plaintext(str)
              key (int)
Return:       ciphertext (string)
Description:  Encryption using Scytale Cipher
              Key is the diameter, i.e. # rows
              Assume infinite length rod (infinite #columns)
Asserts:      plaintext is a string
              key is a positive integer
---------------------------------------------------
"""
def e_scytale(plaintext, key):
    # your code
    ciphertext = ''
    r = int(math.ceil((len(plaintext) / key)))
    rod = []
    idx = 0
    for i in range(key):
        row = []
        if(idx < len(plaintext)):
            for j in range(r):
                if(idx < len(plaintext)):
                    row.append(plaintext[idx])
                    idx+= 1
                else:
                    row.append(None)
        rod.append(row)
    for x in range(r):
        for j in range(key):
            if(rod[j][x]):
                ciphertext += rod[j][x]
    return ciphertext

"""
----------------------------------------------------
Parameters:   ciphertext(str)
              key (int)
Return:       plaintext (string)
Description:  Decryption using Scytale Cipher
Asserts:      ciphertext is a string
              key is a positive integer
---------------------------------------------------
"""
def d_scytale(ciphertext, key):
    # your code
    plaintext = ''
    r = int(math.ceil((len(ciphertext) / key)))
    n = (len(ciphertext)%r)
    if n != 0:
        n = r - n
    rod = []
    idx = 0
    for i in range(r):
        row = []
        if(idx < len(ciphertext)):
            for j in range(key):
                if(j == key-1 and n == r-i):
                    row.append(None)
                    n = n - 1
                elif(idx < len(ciphertext)):
                    row.append(ciphertext[idx])
                    idx+= 1
                else:
                    row.append(None)
                    n = n - 1
        else:
            row.append(None)
            n -= 1
        rod.append(row)
    for x in range(key):
        for j in range(r):
            if(rod[j][x] ):
                plaintext += rod[j][x]
    return plaintext

"""
----------------------------------------------------
Parameters:   ciphertext (str)
Return:       key (int)
              plaintext (str)
Description:  Apply brute-force to break scytale cipher
              Bruteforce range from 1 to 100
Asserts:      ciphertext is a string
---------------------------------------------------
"""
def cryptanalysis_scytale(ciphertext):
    # your code here
    for key in range (1,100):
        plaintext = d_scytale(ciphertext, key)
        if is_plaintext(plaintext, "engmix.txt", 0.9):
            return key, plaintext
    key = None
    plaintext = ''
    return None,''

"""
----------------------------------------------------
            Task 4: Polybius Cipher
----------------------------------------------------
"""

"""
----------------------------------------------------
Parameters:   start (str): an ASCII character
              size (int) number of rows & columns in square
Return:       square (str): A string representing a Polybius square
Description:  Creates a string that begins with 'start' character and 
              contains consecutive ASCII characters that are good to fill
              the given size of a polybius square
Asserts:      start is a single character string
              size is an integer >= 2
---------------------------------------------------
"""
def get_polybius_square(start,size):
    # your code
    ascii_value = ord(start) 
    polybius_square = ''
    string_length = size*size
    if(string_length > 94):
        return polybius_square
    for i in range(string_length):
        polybius_square += chr(ascii_value)
        ascii_value += 1
        if(ascii_value > 126):
            ascii_value = 32
    return polybius_square

"""--------------------------------------------------------------
Parameters:   plaintext (str)
              key (tuple(str,int))
Return:       ciphertext (str)
Description:  Encryption using Polybius Square
Asserts:      plaintext is a string
              key is a tuple containing a single character and an integer
--------------------------------------------------------------
"""
def e_polybius(plaintext, key):
    # your code
    ciphertext = ''
    polybius_square = get_polybius_square(key[0], key[1])
    if(polybius_square == ''):
        print("Error(e_polybius): invalid polybius square")
        return ciphertext
    for c in plaintext:
        if (c in polybius_square):
            row_num = math.ceil((polybius_square.index(c) + 1)/key[1])
            col_num = (polybius_square.index(c) + 1) % key[1]
            if (col_num == 0):
                col_num = key[1]
            ciphertext += str(row_num)
            ciphertext += str(col_num)
        else:
            ciphertext += c
    return ciphertext

"""
-------------------------------------------------------
Parameters:   ciphertext(str)
              key (tuple(str,int))
Return:       plaintext (str)
Description:  Decryption using Polybius Square
Asserts:      ciphertext is a string
              key is a tuple containing a single character and an integer
-------------------------------------------------------
"""
def d_polybius(ciphertext, key):
    # your code
    plaintext = ''
    char_spot = 0
    c = 0
    polybius_square = get_polybius_square(key[0], key[1])
    #print(polybius_square)
    #print(ciphertext)
    if(polybius_square == ''):
        print("Error(d_polybius): invalid polybius square")
        return plaintext
    while c < len(ciphertext):
        if(ciphertext[c].isnumeric() and c < len(ciphertext)-1):
            if(int(ciphertext[c]) <= key[1] and ciphertext[c+1].isnumeric()):
                if(int(ciphertext[c+1]) <= key[1]):
                    char_spot = (int(ciphertext[c])-1)*key[1] + int(ciphertext[c+1])-1
                    plaintext += polybius_square[char_spot]
                    c+= 1
                else:
                    plaintext+= ciphertext[c]
            else:
                plaintext+= ciphertext[c]
        else:
            plaintext+= ciphertext[c]
        c+= 1        
    return plaintext

"""
----------------------------------------------------
Parameters:   ciphertext (str)
              size (int)
Return:       key (str)
              plaintext (str)
Description:  Apply brute-force to break polybius cipher
              The size of the polybius square is given
              The square is always located between [' ', '~'] ASCII characters
              Use threshold of 0.93
Asserts:      ciphertext is a string
              size is an integer
---------------------------------------------------
"""
def cryptanalysis_polybius(ciphertext,size):
    # your code here
    for ascii_value in range(127):
        key = chr(ascii_value)
        plaintext = d_polybius(ciphertext, (key,size))
        if is_plaintext(plaintext, "engmix.txt", 0.93):
            return (key,size), plaintext
    return None,''