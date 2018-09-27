def selectionSort(input_list):
    if len(input_list) == 0:
        return []
    sorted_list = input_list
    for i in range(0, len(sorted_list)):
        miniIndex = i
        for j in range(i, len(sorted_list)):
            if sorted_list[j] < sorted_list[miniIndex]:
                miniIndex = j
        sorted_list[i], sorted_list[miniIndex] = sorted_list[miniIndex], sorted_list[i]
        print("排序:", sorted_list)
    return sorted_list


if __name__ == "__main__":
    input_list = [69, 21, 36, 45, 50, 52, 59, 59, 68]
    print("排序前", input_list)
    sorted_list = selectionSort(input_list)
    print("排序后", sorted_list)

"""
排序算法的稳定性大家应该都知道，通俗地讲就是能保证排序前2个相等的数其在序列的前后位置顺序和排序后它们两个的前后位置顺序相同
选择排序
    从待排序序列中，找到关键字最小的元素；
    如果最小元素不是待排序序列的第一个元素，将其和第一个元素互换；
    从余下的 N - 1 个元素中，找出关键字最小的元素，重复(1)、(2)步，直到排序结束。

排序类别：
    交换排序
时间复杂度：
    平均情况 O(N^2)
    最坏情况 O(N^2)
    最好情况 O(N)
空间复杂度
    O(1)
稳定性：
    不稳定
复杂性：
    简单
"""



