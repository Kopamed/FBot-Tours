def num_te(num):
    emojis = [":one:"]
    if num >= 0 and num <=9:
        num = str(num) + " "
    else:
        num = "🧩"
    return num

def num_tt(num):
    nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    try:
        return nums[num]
    except:
        return "jigsaw"

def index_of(key, arr):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1
