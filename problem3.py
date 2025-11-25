def longest_downward_trend(prices):
    [100, 98, 97, 99, 96, 95, 94, 100]
    i = 0
    new_list = []
    counter = 0
    check = False
    if len(prices) <= 1:
        return 0
    while i <= len(prices)-1:
        if i != len(prices)-1:
            if prices[i] > prices[i+1]:
                counter += 1
                check = True
            elif prices[i] < prices[i+1] and check:
                counter += 1
                new_list.append(counter)
                counter = 0
            else:
                new_list.append(counter)
                counter = 0
        else:
            if prices[i] < prices[i-1]:
                counter += 1
                new_list.append(counter)
        i += 1
    return max(new_list)

prices = [50, 40, 30, 20, 10]
print(longest_downward_trend(prices))

