# 冒泡排序算法实现

# 待排序数组
arr = [64, 33, 25, 55, 99, 13, 12, 45, 123]

# 排序函数定义
def bubbleSort(arr):
    n = len(arr)
    
    # 遍历所有数组元素
    for i in range(n):
        for j in range(0, n-i-1):
            
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
# 排序函数结束

# 调用排序函数
bubbleSort(arr)

# 打印排序结果
print("排序后的数组：")
for i in range(len(arr)):
    print("%d" % arr[i]),
