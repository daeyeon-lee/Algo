

while True:
    sentence = input()
    if sentence == '.':
        break
    ans = []
    for letter in sentence:
        if letter == '(':
            ans.append(letter)
        elif letter == '[':
            ans.append(letter)
        elif letter == ')':
            if not ans or ans[-1] != '(': # 빈 스택이거나 top이 '('가 아닌 경우
                print('no')
                break
            else:
                ans.pop(-1)
        elif letter == ']':
            if not ans or ans[-1] != '[':
                print('no')
                break
            else:
                ans.pop(-1)
    else:
        if ans:
            print('no')
        else:
            print('yes')


