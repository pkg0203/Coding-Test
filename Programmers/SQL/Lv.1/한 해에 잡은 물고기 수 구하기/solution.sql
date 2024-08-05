-- https://school.programmers.co.kr/learn/courses/30/lessons/298516

SELECT count(*) FISH_COUNT
FROM FISH_INFO
WHERE SUBSTR(TIME,1,4)="2021"