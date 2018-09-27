def shellSort(input_list):
    if len(input_list) < 2:
        return input_list
    sorted_list = input_list
    gap=len(sorted_list)//2
    while gap>0:

        for i in range(gap,len(sorted_list)):
            j=i-gap
            tem=sorted_list[i]
            while j>=0 and sorted_list[j]>tem:
                sorted_list[j+gap]=sorted_list[j]
                j-=gap
            sorted_list[j+gap]=tem
            print(sorted_list)
        gap//=2
    return sorted_list

if __name__ == "__main__":
    input_list = [69, 21, 36, 45, 50, 52, 59, 59, 68]
    print("排序前", input_list)
    sorted_list = shellSort(input_list)
    print("排序后", sorted_list)
