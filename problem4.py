def merge_sorted_lists(list1, list2):
    new_list = []
    largest = max(len(list1), len(list2))
    for i in range(largest):
        if largest == len(list1):
            if i < len(list2):
                new_list.append(min(list1[i], list2[i]))
                new_list.append(max(list1[i], list2[i]))
            else:
                new_list.append(list1[i])
            ...
        else:
            if i < len(list1):
                new_list.append(min(list1[i], list2[i]))
                new_list.append(max(list1[i], list2[i]))
            else:
                new_list.append(list2[i])
    print(new_list)

l1 = [1, 5, 9, 10]
l2 = [2, 3, 8]
#merge_sorted_lists(l1, l2)
l3 = []
l4 = [4, 6, 7]
# merge_sorted_lists(l3, l4)
l5 = [10, 20, 30, 40, 50]
l6 = [15, 25]
# merge_sorted_lists(l5, l6)
l7 = []
l8 = []
merge_sorted_lists(l7, l8)