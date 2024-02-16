# 상반기 아이스크림 총주문량이 3,000보다 높으면서 아이스크림의 주 성분이 과일인 아이스크림
SELECT
    FIRST_HALF.FLAVOR
FROM
    FIRST_HALF
JOIN
    ICECREAM_INFO ON FIRST_HALF.FLAVOR = ICECREAM_INFO.FLAVOR
WHERE
    TOTAL_ORDER > 3000 AND
    INGREDIENT_TYPE = 'fruit_based'
ORDER BY
    TOTAL_ORDER DESC