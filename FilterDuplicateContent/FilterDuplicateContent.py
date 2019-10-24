# 去掉字符串中重复字符的方法


import os

from collections import OrderedDict

context = "重复内容重复内容"

# If order does not matter, you can use
# 方法一：如果顺序不重要，你可以使用 set(context)
print("".join(set(context)))

# If order does matter, you can use collections.OrderedDict:
# 方法二：如果顺序很重要，你可以使用 collections.OrderedDict.fromkeys(context):
print("".join(OrderedDict.fromkeys(context)))

# os.system("pause")
