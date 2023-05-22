import time

# String matching algorithm on search recomendation system in comment section TikTok

# String matching algorithm :
# KMP (Knuth-Morris-Prastt) algorithm
# BM (Boyer-Moore) algorithm
# Brute Force algorithm

# list of comment
comments = [
    "Macbook Pro M1",
    "Macbook emang keren",
    "Macbook Pro M1 bagus banget",
    "Macbook Pro M1 keren banget",
    "Macbook Pro M1 keren",
    "Macbook Pro M1 bagus",
    "Macbook Pro M1 bagus banget",
    "Pengen banget Macbook Pro M1",
    "Mah beliin aku Macbook Pro M1",
    "Macbook Pro M1 mahal banget",
    "Macbook Pro M1 kurang worth it",
]

# sentence in subtitle tiktok video
sentence = "Hai semuanya, kali ini aku mau unboxing Macbook Pro M1, Macbook Pro M1 ini adalah laptop terbaru dari Apple, Macbook Pro M1 ini memiliki performa yang sangat baik karena menggunakan chip M1, Cocok banget buat kalian yang suka editing video, editing foto, dan lain-lain, Macbook Pro M1 ini juga memiliki desain yang sangat premium, Macbook Pro M1 ini juga memiliki keyboard yang sangat nyaman, Macbook Pro M1 ini juga memiliki layar yang sangat bagus, Macbook Pro M1 ini juga memiliki speaker yang sangat bagus, Macbook Pro M1 ini juga memiliki baterai yang sangat awet, Macbook Pro M1 ini juga memiliki touchpad yang sangat nyaman, Macbook Pro M1 ini juga memiliki port yang sangat lengkap, Macbook Pro M1 ini juga memiliki kamera yang sangat bagus, Macbook Pro M1 ini juga memiliki microphone yang sangat bagus, Macbook Pro M1 ini juga memiliki webcam yang sangat bagus, Macbook Pro M1 ini juga memiliki fitur yang sangat lengkap, Macbook Pro M1 ini juga memiliki harga yang sangat mahal, Macbook Pro M1 ini juga memiliki kualitas yang sangat baik, Macbook Pro M1 ini juga memiliki kualitas yang sangat bagus, Gimana menurut kalian? Apakah Macbook Pro M1 ini worth it?"

# clean the sentence from punctuation
sentence = sentence.replace(",", "")
sentence = sentence.replace(".", "")
sentence = sentence.replace("?", "")
sentence = sentence.replace("!", "")
sentence = sentence.replace("-", "")
sentence = sentence.lower()

# clean comments from punctuation
for i in range(len(comments)):
    comments[i] = comments[i].replace(",", "")
    comments[i] = comments[i].replace(".", "")
    comments[i] = comments[i].replace("?", "")
    comments[i] = comments[i].replace("!", "")
    comments[i] = comments[i].replace("-", "")
    comments[i] = comments[i].lower()

def getWord(sentence):
    # get word from sentence if the word is same with word not append to dictionary
    word = []
    for i in sentence.split():
        if i not in word:
            word.append(i)
    return word

def bruteForce(text, pattern):
    lenPattern = len(pattern)
    lenText = len(text)
    if lenPattern > lenText:
        return 0
    elif lenPattern == lenText:
        if text == pattern:
            return 1
        return 0
    i = 0
    count = 0  # Counter for substring occurrences
    for i in range(0, lenText - lenPattern + 1):
        j = 0
        while j < lenPattern and text[i + j] == pattern[j]:
            j += 1
        if j == lenPattern:
            count += 1
    return count

def kmpTab(pattern, table):
    position, candidate = 2, 0
    table[0], table[1] = -1, 0
    while position < len(pattern):
        if pattern[position - 1] == pattern[candidate]:
            candidate += 1
            table[position] = candidate
            position += 1
        elif candidate > 0:
            candidate = table[candidate]
        else:
            table[position] = 0
            position += 1

def knuthMorrisPratt(text, pattern):
    m, i = 0, 0
    table = [0] * len(pattern)
    kmpTab(pattern, table)
    count = 0  # Counter for substring occurrences
    while m + i < len(text):
        if pattern[i] == text[m + i]:
            if i == len(pattern) - 1:
                count += 1
                m += i - table[i]
                i = table[i]
            else:
                i += 1
        else:
            if table[i] > -1:
                m += i - table[i]
                i = table[i]
            else:
                i = 0
                m += 1
    return count

def bmTab(substr):
    table = [-1] * 256
    for i in range(len(substr)):
        table[ord(substr[i])] = i
    return table

def boyerMoore(text, pattern):
    table = bmTab(pattern)
    lenPattern = len(pattern)
    lenText = len(text)
    if lenPattern > lenText:
        return 0
    elif lenPattern == lenText:
        if text == pattern:
            return 1
        return 0
    i = 0
    count = 0  # Counter for substring occurrences
    while i <= lenText - lenPattern:
        j = lenPattern - 1
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1
        if j < 0:
            count += 1
            i += lenPattern
        else:
            slide = j - table[ord(text[i + j])]
            if slide < 1:
                slide = 1
            i += slide
    return count

def createSubstringDictionary(comments, words, algorithm):
    substr_dict = {}
    for comment in comments:
        for word in words:
            if algorithm == 1:
                count = bruteForce(comment, word)
            elif algorithm == 2:
                count = knuthMorrisPratt(comment, word)
            elif algorithm == 3:
                count = boyerMoore(comment, word)
            if count > 0:
                if word not in substr_dict:
                    substr_dict[word] = count
                else:
                    substr_dict[word] += count
    return substr_dict

# Get recommended word
def find_recommended_words(substr_dict_brute):
    recommended_word = []
    for i in range(3):
        max_key = max(substr_dict_brute, key=substr_dict_brute.get)
        recommended_word.append(max_key)
        substr_dict_brute.pop(max_key)

    recommended_word_sentence = " ".join(recommended_word)
    print("Recommended word: ", recommended_word_sentence)

# Main
words = getWord(sentence)
substr_dict_brute = createSubstringDictionary(comments, words, 1)
print("Brute Force Algorithm")
start = time.time()
print("Substring dictionary : ", substr_dict_brute)
end = time.time()
print("Time : ", end - start)
find_recommended_words(substr_dict_brute)

substr_dict_kmp = createSubstringDictionary(comments, words, 2)
print("Knuth-Morris-Pratt Algorithm")
start = time.time()
print("Substring dictionary : ", substr_dict_kmp)
end = time.time()
print("Time : ", end - start)
find_recommended_words(substr_dict_kmp)

substr_dict_bm = createSubstringDictionary(comments, words, 3)
print("Boyer-Moore Algorithm")
start = time.time()
print("Substring dictionary : ", substr_dict_bm)
end = time.time()
print("Time : ", end - start)
find_recommended_words(substr_dict_bm)