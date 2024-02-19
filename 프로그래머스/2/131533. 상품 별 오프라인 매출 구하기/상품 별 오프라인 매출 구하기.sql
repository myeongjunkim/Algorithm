-- 코드를 입력하세요
SELECT
    P.PRODUCT_CODE,
    SUM(S.SALES_AMOUNT) * P.PRICE AS SALES
FROM 
    OFFLINE_SALE S
JOIN
    PRODUCT P ON P.PRODUCT_ID = S.PRODUCT_ID
GROUP BY
    P.PRODUCT_CODE
ORDER BY
    SALES DESC, P.PRODUCT_CODE