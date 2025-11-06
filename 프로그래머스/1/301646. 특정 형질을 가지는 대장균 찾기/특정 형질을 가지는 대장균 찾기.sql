-- 코드를 작성해주세요
# 4번 형질은 1000 = 8
# 3번 형질은 0100 = 4
# 2번 형질은 0010 = 2
# 1번 형질은 0001 = 1
# & 연산자는 둘 다 1이면 2 출력, 둘 중에 하나라도 0이 있으면 0 출력
SELECT COUNT(*) as COUNT
FROM ECOLI_DATA
WHERE (GENOTYPE & 2) = 0
AND ((GENOTYPE & 1) > 0 OR (GENOTYPE & 4) > 0)