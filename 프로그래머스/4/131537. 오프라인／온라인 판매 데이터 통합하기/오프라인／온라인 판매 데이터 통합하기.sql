# 2022년 3월
# 오프라인/온라인 상품 판매
# OFFLINE_SALE 테이블의 판매 데이터의 USER_ID 값은 NULL 로 표시
# 판매일, 상품 ID, 유저 ID
(
    SELECT
        DATE_FORMAT(SALES_DATE,"%Y-%m-%d") AS SALES_DATE,
        PRODUCT_ID,
        USER_ID,
        SALES_AMOUNT
    FROM
        ONLINE_SALE
    WHERE 
        SALES_DATE LIKE "2022-03%"
)
UNION ALL
(
    SELECT
        DATE_FORMAT(SALES_DATE,"%Y-%m-%d") AS SALES_DATE,
        PRODUCT_ID,
        NULL AS USER_ID,
        SALES_AMOUNT
    FROM
        OFFLINE_SALE
    WHERE 
        SALES_DATE LIKE "2022-03%"
)
ORDER BY
    SALES_DATE, PRODUCT_ID, USER_ID