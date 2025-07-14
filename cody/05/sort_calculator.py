def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)  # 재귀 호출

def main():
    inputStr = input("입력값을 입력해 주세요 (공백으로 구분)")
    
    try:
        arr = [float(num) for num in inputStr.strip().split()]
    except ValueError:
        print("Invalid input.")
        return
    if not arr:
        print("입력값 없음")
        return
    print(f'Sorted: {quick_sort(arr)}')
    return
    
if __name__=="__main__":
    main()