word = input().upper()  # 문자열을 다 대문자로해서 받기
word_alphabet = list(set(word)) # 중복 문자 제거해서 새로운 변수에 저장

lst = [] # 빈 리스트 생성 (카운트를 위함)

for i in word_alphabet:
    count = word.count(i) # 카운트 메서드를 통해 중복문자별 개수 세기
    lst.append(count) # 개수를 lst에 추가


if lst.count(max(lst)) >=2: # lst의 최대값이 lst내에 2개 이상 존재하면
    print("?") # ? 출력
else: # 아니라면
    # 최대값의 인덱스를 중복문자 제거한 word_alphabet 리스트의 인덱스로 사용
    print(word_alphabet[lst.index(max(lst))]) 