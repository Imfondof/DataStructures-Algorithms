# -*- coding:utf-8 -*-
def MergeSort(input_list):
    def merge(input_list,left,mid,right,tem):
        i=left
        j=mid+1
        k=0
        while i<=mid and j<=right:
            if input_list[i]<input_list[j]:
                tem[k]=input_list[i]
                i+=1
            else:
                tem[k]=input_list[j]
                j+=1
            k+=1
        while i<=mid:
            tem[k]=input_list[i]
            i+=1
            k+=1
        while j<=right:
            tem[k]=input_list[j]
            j+=1
            k+=1
        k=0
        while left<=right:
            input_list[left]=tem[k]
            left+=1
            k+=1


    def merge_sort(input_list,left,right,tem):
        if left>=right:
            return
        mid=(left+right)//2
        merge_sort(input_list,left,mid,tem)
        merge_sort(input_list,mid+1,right,tem)
        merge(input_list,left,mid,right,tem)

    if len(input_list)==0:
        return []
    tem=[0]*len(input_list)
    sorted_list=input_list
    merge_sort(sorted_list,0,len(sorted_list)-1,tem)
    return sorted_list

if __name__ == '__main__':
    input_list = [6, 4, 8, 9, 2, 3, 1]
    print('排序前:', input_list)
    sorted_list = MergeSort(input_list)
    print('排序后:', sorted_list)
