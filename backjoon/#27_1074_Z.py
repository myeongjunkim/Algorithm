N_r_c = list(map(int,input('').split(' ')))
N, r, c = N_r_c[0], N_r_c[1], N_r_c[2]

# r,c 주어 졌을때
# 전체의 몇사분면인지 판단
# 2**N x 2**N 중 인덱스
# 전체 크기 /2
# r, c 좌표 재부여(몇사분면인지에 따라)

l = 2**N
region_num = 0
while l != 1:
    if r>=l//2:
        r = r-l//2
        if c>=l//2:
            # print("4 region")
            region_num += 3*(l**2//4)
            c = c-l//2
        else:
            # print("3 region")
            region_num += l**2//2
    else:
        if c>=l//2:
            # print("2 region")
            region_num += l**2//4
            c = c-l//2
        else:
            # print("1 region")
            region_num += 0
    l = l//2
    
print(region_num)