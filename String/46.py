from math import inf
S = input()

S_S = S.split(" ")
print(S_S)
max_word_l = -inf
for i in range(len(S_S)):
    if S_S[i] != "":
        word = str(S_S[i]) 
        if len(word) > max_word_l:
            max_word_l = len(word)

print(max_word_l)