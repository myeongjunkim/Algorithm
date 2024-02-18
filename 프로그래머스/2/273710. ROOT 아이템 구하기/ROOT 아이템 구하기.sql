SELECT
    ITEM_INFO.ITEM_ID,
    ITEM_INFO.ITEM_NAME
FROM
    ITEM_INFO
JOIN 
    ITEM_TREE ON ITEM_INFO.ITEM_ID = ITEM_TREE.ITEM_ID
WHERE
    ITEM_TREE.PARENT_ITEM_ID IS NULL
ORDER BY
    ITEM_ID