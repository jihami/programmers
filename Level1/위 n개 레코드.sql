-- 코드를 입력하세요
SELECT NAME
FROM (SELECT * 
      FROM ANIMAL_INS
      ORDER BY DATETIME
)
WHERE ROWNUM < 2; -- 위에서 첫번째만 가져오기
