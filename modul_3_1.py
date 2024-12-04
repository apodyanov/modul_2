
calls = 0

def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    length = len(string)
    upper_str = string.upper()
    low_str = string.lower()
    return length, upper_str, low_str


def is_contains(string, list_to_search):
    count_calls()
    string = string.lower()
    for item in list_to_search:
        if string == item.lower():
            return True
        else:
            return False


func1 = string_info('ARMAGEDON')
func2 = string_info('MoscowNeverSleep')
func3 = string_info('MoscowNeverSleepWithOutYou')
func4 = is_contains('ARMAGEDON', ['Moscow', 'Never', 'Sleep'])
func5 = is_contains('MOSCOW', ['Moscow', 'Never', 'Sleep'])


print(func1)
print(func2)
print(func3)
print(func4)
print(func5)

print(calls)