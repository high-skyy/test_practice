# 처음 출발 (주유소 기름) (기름통의 크기는 무제한)
# 1km당 1리터의 기름 (도시마다 주유소) 주유소마다 리터당 가격이 다름

num_city = int(input())
dist_list = list(map(int, input().split(' ')))
price_list = list(map(int, input().split(' ')))

tot_price = 0
min_price_per_liter = 1000000001
for i in range(len(dist_list)):
    cur_dist = dist_list[i]
    min_price_per_liter = min(price_list[i], min_price_per_liter)
    tot_price += min_price_per_liter * cur_dist
print(tot_price)