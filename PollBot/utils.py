emojis = ["0️⃣", "1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]
text_nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "keycap_ten"]


def num_te(num):
    if 0 <= num <= 10:
        return emojis[num]
    else:
        return "🧩"


def num_tt(num):
    try:
        return text_nums[num]
    except:
        return "jigsaw"


def index_of(key, arr):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


def get_keys(dict):
    keys = []
    for i in dict:
        keys.append(i)
    return keys


def safe_append(arr, var):
    if var not in arr:
        arr.append(var)


def to_str(arr):
    return "".join(i for i in arr)
