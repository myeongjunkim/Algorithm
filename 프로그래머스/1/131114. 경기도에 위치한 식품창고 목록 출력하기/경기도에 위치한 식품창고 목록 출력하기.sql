# 경기도에 위치한
# 이때 냉동시설 여부가 NULL인 경우, 'N'으로 출력시켜 주시고
# ID를 기준으로 오름차순 정렬
SELECT
    WAREHOUSE_ID,
    WAREHOUSE_NAME,
    ADDRESS,
    IFNULL(FREEZER_YN,"N") as FREEZER_YN
FROM
    FOOD_WAREHOUSE
WHERE
    SUBSTRING(ADDRESS, 1, 3) = "경기도"
ORDER BY
    WAREHOUSE_ID