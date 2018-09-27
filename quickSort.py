def quikSort(input_list, left, right):
    def division(input_list, left, right):
        base=input_list[left]
        while left<right:
            while left<right and base<=input_list[right]:
                right-=1
            input_list[left]=input_list[right]
            while left<right and base >=input_list[left]:
                left+=1
            input_list[right]=input_list[left]
        input_list[left]=base
        return left

    if left<right:
        base_index=division(input_list,left,right)
        quikSort(input_list, left, base_index-1)
        quikSort(input_list, base_index+1, right)



if __name__ == '__main__':
    input_list = [1, 6, 5, 4, 9, 3, 2, 4, 8, 5]
    print('before sort:', input_list)
    quikSort(input_list, 0, len(input_list) - 1)
    print('after sort:', input_list)
