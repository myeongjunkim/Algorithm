-- 코드를 입력하세요
SELECT user.USER_ID, user.NICKNAME, SUM(board.PRICE) as "TOTAL_SALES"
    FROM USED_GOODS_BOARD as board
    JOIN USED_GOODS_USER as user on user.USER_ID = board.WRITER_ID
    WHERE board.STATUS = "DONE"
    group by board.WRITER_ID
    having SUM(board.PRICE) >=700000
    order by SUM(board.PRICE)
    

    