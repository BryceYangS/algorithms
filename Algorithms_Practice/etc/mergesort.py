def merge(list1, list2):
    merged_list = list()
    if len(list1) == 0:
        return list2

    while list1:
        left = list1.pop(0)
        while list2:
            right = list2[0]
            if left < right:
                break
            merged_list.append(list2.pop(0))
        merged_list.append(left)

    if len(list2) > 0:
        merged_list += list2

    return merged_list


# 합병 정렬
def merge_sort(my_list):
    if len(my_list) == 1:
        return my_list

    mid_index = len(my_list) // 2
    return merge(merge_sort(my_list[:mid_index]) , merge_sort(my_list[mid_index:]))



# 테스트
print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))
