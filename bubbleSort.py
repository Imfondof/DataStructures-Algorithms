# 优化后的代码
def bubbleSort(input_list):
    if len(input_list) == 0:
        return []
    sorted_list = input_list
    for i in range(len(sorted_list) - 1):
        print("第%d趟排序" % (i + 1))
        flag = False
        for j in range(len(sorted_list) - 1 - i):  # 优化1
            if sorted_list[j + 1] < sorted_list[j]:
                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
                flag = True
        print(sorted_list)
        if not flag:  # 优化2
            return sorted_list
    return sorted_list


if __name__ == "__main__":
    input_list = [69, 21, 36, 45, 50, 52, 59, 59, 68]
    print("排序前", input_list)
    sorted_list = bubbleSort(input_list)
    print("排序后", sorted_list)

"""
冒泡排序法
    冒泡排序是一种交换排序。什么是交换排序呢？答曰：两两比较待排序的关键字，并交换不满足次序要求的那对数，直到整个表都满足次序要求为止。
    冒泡排序就是要每趟排序过程中通过两两比较相邻元素，将小的数字放到前面，大的数字放在后面。
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

"""
#初始代码
def bubbleSort(input_list):
    if len(input_list) == 0:
        return []
    sorted_list = input_list
    for i in range(len(sorted_list) - 1):
        print("第%d趟排序" % (i + 1))
        for j in range(len(sorted_list) - 1):  # 这里可以进行优化，因为第一次排序后最大的就会排到最后边，第二次比较的时候只需要比较前i-1个
            if sorted_list[j + 1] < sorted_list[j]:
                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]#这里可以进行优化，如果在进行第某次判断时没有替换操作，说明已经完成了排序，直接返回即可
        print(sorted_list)
    return sorted_list
"""



