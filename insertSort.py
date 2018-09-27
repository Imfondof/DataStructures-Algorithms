def insertSort(input_list):
    if len(input_list) == 0:
        return []
    sorted_list = input_list
    for i in range(1, len(sorted_list)):
        j = i - 1
        temp = sorted_list[i]
        while j >= 0 and sorted_list[j] > temp:
            sorted_list[j + 1] = sorted_list[j]
            j -= 1
        sorted_list[j + 1] = temp
        print('排序' + str(i), sorted_list)
    return sorted_list


if __name__ == "__main__":
    input_list = [69, 21, 36, 45, 50, 52, 59, 59, 68]
    print("排序前", input_list)
    sorted_list = insertSort(input_list)
    print("排序后", sorted_list)
"""
插入排序法
    从第一个元素开始，该元素可以认为已经被排序；
    取出下一个元素，在已经排序的元素序列中从后向前扫描；
    如果该元素（已排序）大于新元素，将该元素移到下一个位置；
    重复步骤3，直到找到已排序的元素小于或者等于新元素的位置；
    将新元素插入到该位置后；
    重复步骤2-5

排序类别：
    交换排序
时间复杂度：
    平均情况 O(N^2)
    最坏情况 O(N^2)
    最好情况 O(N)
空间复杂度
    O(1)
稳定性：
    稳定
复杂性：
    简单
"""



