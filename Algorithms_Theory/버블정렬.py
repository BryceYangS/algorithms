def bubblesort(data) :
    for index in range(len(data)-1) :
        swap = False
        for index2 in range(len(data) - index - 1) :
            if data[index2] > data[index2 + 1] :
                data[index2], data[index2 + 1] = data[index2 + 1], data[index2]
                swap = True

        # 한번도 스왑되지 않으면 이미 정렬 되어 있음
        if swap == False :
            break;
    return data

import random
data_list = random.sample(range(100),50)
print(bubblesort(data_list))