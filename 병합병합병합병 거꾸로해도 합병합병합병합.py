mergesort_cnt = 0
merge_two_section_cnt = 0

def MergeTwoSection(unsorted_list,start,mid,end):
    global merge_two_section_cnt
    merge_two_section_cnt += 1
    print(start,end,"in MergeTwoSection cnt :", merge_two_section_cnt)
    leftIdx = start
    rightIdx = mid + 1
    numofData = (end - start) + 1
    temp_list = [0 for i in range(numofData+1)]
    tempIdx = 0
    for i in range(numofData):
        if unsorted_list[leftIdx] <= unsorted_list[rightIdx]:
            temp_list[i] = unsorted_list[leftIdx]
            leftIdx += 1
   
            if leftIdx > mid:
                tempIdx = i + 1
                break
        else:
            temp_list[i] = unsorted_list[rightIdx]
            rightIdx += 1

            if rightIdx > end:
                tempIdx = i + 1
                break
    print('\n\n')
    print(f'temp_list = {temp_list}')
    print('\n\n')
    if leftIdx > mid:
        for i in range(rightIdx,end+1):
            temp_list[tempIdx] = unsorted_list[i]
            tempIdx +=1
    else:
        for i in range(leftIdx,mid+1):
            temp_list[tempIdx] = unsorted_list[i]
            tempIdx +=1
    print('\n\n')
    print(f'temp_list = {temp_list}')
    print('\n\n')
    tempIdx = 0
    for i in range(start,end+1):
        unsorted_list[i] = temp_list[tempIdx]
        tempIdx += 1
    del temp_list
def MergeSort(unsorted_list,start,end):
    if start >= end:
        return
    mid = (start + end) // 2
    MergeSort(unsorted_list,start,mid)
    MergeSort(unsorted_list,mid+1,end)
    MergeTwoSection(unsorted_list,start,mid,end)
unsorted = [8,3,7,1,2,6,4,5,32,454,621652,25545,65442324,653454,4343]
end = len(unsorted) - 1
start = 0
MergeSort(unsorted,start,end)
print(unsorted)
