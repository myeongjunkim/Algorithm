# 생일이 3월인 여성 
# 이때 전화번호가 NULL인 경우는 출력대상에서 제외
#  회원ID를 기준으로 오름차순
SELECT
    MEMBER_ID,
    MEMBER_NAME,
    GENDER,
    DATE_FORMAT(DATE_OF_BIRTH, "%Y-%m-%d")
FROM
    MEMBER_PROFILE
WHERE
    TLNO is not null AND
    MONTH(DATE_OF_BIRTH) = 3 AND
    GENDER = "W"
ORDER BY
    MEMBER_ID