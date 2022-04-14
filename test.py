
import math
from itertools import product

words = open('word_lists/default_words.txt', 'r')
word_list = [word for word in words.read().splitlines()]
words.close()


a = []
for _set in product(['g','y','b'], repeat=5):
    a.append(''.join(_set))

valid_permutations = []

for i in a:
    if(i.count('g')==4 and i.count('y')==1):
        continue
    valid_permutations.append(i)
    
gains = []
probs = []

pwords = {}

##for word1 in word_list:
##    word = "slate"
##    entropy = 0
##
##    for pattern in valid_permutations:
##        good_letters = []
##        bad_letters = []
##        right_position = {}
##        for i,k in enumerate(pattern):
##            if k=="g" or k=="y":
##                good_letters.append(word[i])
##            if k=="b":
##                bad_letters.append(word[i])
##            if k=="g":
##                right_position[i] = word[i]
##        possible_words = [word for word in word_list if \
##                          all(good_letter in word for good_letter in good_letters) \
##                          and \
##                          all(bad_letter not in word for bad_letter in bad_letters) \
##                          and \
##                          all(word[i]==right_position[i] for i in right_position.keys())]
##
##        pwords[pattern] = possible_words
##        prob = len(possible_words)/len(word_list)
##        probs.append(prob)
##        if(prob!=0):
##            info = -1 * math.log(prob,2)
##            entropy+= prob * info
##        
##    gains.append([word, entropy])
##    break
##
##
##print(sorted(gains, key=lambda x: x[1], reverse=True)[0])


##for k,v in pwords.items():
##    flag = 0
##    for k1,v1 in pwords.items():
##        if k==k1:
##            continue
##        elif(len(set(v).intersection(set(v1)))!=0):
##            print("YES")
##            print(k,k1)
##            print(set(v).intersection(set(v1)))
##            flag = 1
##            break
##    if flag == 1:
##        break



probs = []

patterns = {}

word = "smash"
entropy = 0


for w in word_list:
    p = ""
    for i in range(len(w)):
        if w[i]==word[i]:
            p+="g"
        elif w[i] in word:
            p+="y"
        elif w[i] not in word:
            p+="b"
    if p in patterns:
        patterns[p]+=1
    else:
        patterns[p]=1

for k,v in patterns.items():
    if v!=0:
        prob = v/len(word_list)
        probs.append(prob)
        info = -1 * math.log(prob,2)
        entropy+=prob*info
        
print(word, entropy)


