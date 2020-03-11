# customer = {
#     "1": "one",
#     "2": "two",
#     "3": "three",
#     "4": "four",
#     "5": "five",
#     "6": "six",
#     "7": "seven",
#     "8": "eight",
#     "9": "nice",
#     "0": "zero"
# }
# result = ""
# numbers = input("what is number.....")
# print(numbers)
# for number in numbers:
#     a = type(number)
#     result += customer.get(number) + " "
# print(result)
# #
# # 任何有名字的（数组，列表，字典）都有方法
# for 循环中的变量为 str
# get 方法 在字典中如果没有相对应值 可以在get()方法第二位加默认值


def user_inmagnation(massages):
    customer = {
        ":)": "😂",
        ":(": "😒"
    }
    result = ""
    words = massages.split(' ')
    print(words)
    for word in words:
        result += customer.get(word, word) + " "
    return result


massage = input(">")
print(user_inmagnation(massage))
