word_to_num = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
    "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12,
    "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17,
    "eighteen": 18, "nineteen": 19, "twenty": 20, "thirty": 30, "forty": 40,
    "fifty": 50, "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90,
    "hundred": 100, "thousand": 1000, "million": 1000000}
word=list(map(str,input().split()))
num1=0
if 'negative' in word:
    word=word[1:]
    jude=False
else:
    jude=True

def trans(word1,word_to_num):
    num=0
    if 'hundred' in word1:
        num+=word_to_num[word1[0]]*100
        word1=word1[2:]
    for i in word1:
        num+=word_to_num[i]
    return num

if 'million' in word:
    num1+=trans(word[:word.index('million')],word_to_num)*1000000
    word=word[word.index('million')+1:]
if 'thousand' in word:
    num1+=trans(word[:word.index('thousand')],word_to_num)*1000
    word=word[word.index('thousand')+1:]
num1+=trans(word,word_to_num)
if not jude:
    num1=-num1
print(num1)