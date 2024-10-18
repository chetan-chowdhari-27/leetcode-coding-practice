from statistics import mean
def average(array):
   setss = mean(set(array))
   return setss

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
