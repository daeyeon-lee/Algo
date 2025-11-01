S = input()


alphabet = [101] * 26


for i in range(len(S)):
    if S[i] == 'a' and alphabet[0] == 101:
        alphabet[0] = i
    if S[i] == 'b' and alphabet[1] == 101:
        alphabet[1] = i
    if S[i] == 'c' and alphabet[2] == 101:
        alphabet[2] = i
    if S[i] == 'd' and alphabet[3] == 101:
        alphabet[3] = i
    if S[i] == 'e' and alphabet[4] == 101:
        alphabet[4] = i
    if S[i] == 'f' and alphabet[5] == 101:
        alphabet[5] = i
    if S[i] == 'g' and alphabet[6] == 101:
        alphabet[6] = i
    if S[i] == 'h' and alphabet[7] == 101:
        alphabet[7] = i
    if S[i] == 'i' and alphabet[8] == 101:
        alphabet[8] = i
    if S[i] == 'j' and alphabet[9] == 101:
        alphabet[9] = i
    if S[i] == 'k' and alphabet[10] == 101:
        alphabet[10] = i
    if S[i] == 'l' and alphabet[11] == 101:
        alphabet[11] = i
    if S[i] == 'm' and alphabet[12] == 101:
        alphabet[12] = i
    if S[i] == 'n' and alphabet[13] == 101:
        alphabet[13] = i
    if S[i] == 'o' and alphabet[14] == 101:
        alphabet[14] = i
    if S[i] == 'p' and alphabet[15] == 101:
        alphabet[15] = i
    if S[i] == 'q' and alphabet[16] == 101:
        alphabet[16] = i
    if S[i] == 'r' and alphabet[17] == 101:
        alphabet[17] = i
    if S[i] == 's' and alphabet[18] == 101:
        alphabet[18] = i
    if S[i] == 't' and alphabet[19] == 101:
        alphabet[19] = i
    if S[i] == 'u' and alphabet[20] == 101:
        alphabet[20] = i
    if S[i] == 'v' and alphabet[21] == 101:
        alphabet[21] = i
    if S[i] == 'w' and alphabet[22] == 101:
        alphabet[22] = i
    if S[i] == 'x' and alphabet[23] == 101:
        alphabet[23] = i
    if S[i] == 'y' and alphabet[24] == 101:
        alphabet[24] = i
    if S[i] == 'z' and alphabet[25] == 101:
        alphabet[25] = i

for j in range(len(alphabet)):
    if alphabet[j] == 101:
        alphabet[j] = -1
print(*alphabet)