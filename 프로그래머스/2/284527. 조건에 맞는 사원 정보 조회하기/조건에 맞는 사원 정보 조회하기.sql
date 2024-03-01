-- 코드를 작성해주세요
WITH SUBQ AS (
    SELECT
        SUM(G.SCORE) AS SCORE,
        E.EMP_NO,
        E.EMP_NAME,
        E.POSITION,
        E.EMAIL
    FROM 
        HR_EMPLOYEES E
    JOIN
        HR_GRADE G ON E.EMP_NO = G.EMP_NO
    WHERE 
        G.YEAR = 2022
    GROUP BY
        E.EMP_NO
)

SELECT * FROM SUBQ WHERE SCORE = (SELECT MAX(SCORE) FROM SUBQ)

    

