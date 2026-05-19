from math import inf
S = input()

S_S = S.split()
print(S_S)
min_word_l = inf
for i in range(len(S_S)):
    if S_S[i] != "":
        word = str(S_S[i]) 
        if len(word) < min_word_l:
            min_word_l = len(word)

print(min_word_l)