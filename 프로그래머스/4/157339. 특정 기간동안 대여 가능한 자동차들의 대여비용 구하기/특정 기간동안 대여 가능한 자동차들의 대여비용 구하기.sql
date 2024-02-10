# 자동차 종류는 '세단', 'SUV', '승합차', '트럭', '리무진' 
# 자동차 옵션 리스트는 콤마(',')로 구분된 키워드 리스트(예: ''열선시트,스마트키,주차감지센서'')로 되어있으며, 키워드 종류는 '주차감지센서', '스마트키', '네비게이션', '통풍시트', '열선시트', '후방카메라', '가죽시트' 가 있습니다.
# 할인율이 적용되는 대여 기간 종류로는 '7일 이상' (대여 기간이 7일 이상 30일 미만인 경우), '30일 이상' (대여 기간이 30일 이상 90일 미만인 경우), '90일 이상' (대여 기간이 90일 이상인 경우) 이 있습니다. 대여 기간이 7일 미만인 경우 할인정책이 없습니다.

# 요구사항
# 세단, suv // 2022-11-1 ~ 2022-11-30 // 50<=p<200
# 대여금액 decs, 종류, ID decs

SELECT 
    car.CAR_ID,
    car.CAR_TYPE, 
    CAST(car.DAILY_FEE*30 * (100-plan.DISCOUNT_RATE)*0.01 AS signed integer) as FEE
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY as history
    JOIN CAR_RENTAL_COMPANY_CAR as car 
        on car.CAR_ID = history.CAR_ID
    JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN as plan
        on car.CAR_TYPE = plan.CAR_TYPE
        and plan.DURATION_TYPE = '30일 이상'
        
    WHERE car.CAR_TYPE in ("SUV", "세단")
    and car.DAILY_FEE*30 * (100-plan.DISCOUNT_RATE)*0.01 between 500000 and 2000000
    group by car.CAR_ID
    having max(history.END_DATE) < "2022-11-1"
    order by 
        car.DAILY_FEE * 30 * (100-plan.DISCOUNT_RATE) * 0.01 desc,
        car.CAR_TYPE,
        car.CAR_ID desc