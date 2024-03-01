# 사원별 성과금 정보를 조회

WITH SUBQ AS(
    SELECT
        EMP_NO,
        IF(AVG(SCORE)>=96, "S",  
        IF(AVG(SCORE)>=90, "A",
        IF(AVG(SCORE)>=80, "B",
           "C"))) AS GRADE,
        IF(AVG(SCORE)>=96, 0.2,
        IF(AVG(SCORE)>=90, 0.15,
        IF(AVG(SCORE)>=80, 0.1,
           0))) AS BONUS
    FROM
        HR_GRADE
    GROUP BY
        EMP_NO
)

SELECT
    E.EMP_NO,
    E.EMP_NAME,
    B.GRADE,
    E.SAL*B.BONUS AS BONUS
FROM 
    HR_EMPLOYEES E
JOIN
    SUBQ B ON B.EMP_NO = E.EMP_NO
ORDER BY
    E.EMP_NO