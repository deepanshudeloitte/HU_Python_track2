original_list = [[1,1,3,2],[9,8,8,1],[0,4,5,0,0,1,4]]

totals = {}
for k, v in original_list:
    totals[k] = totals.get(k, 0) + v

print(totals)