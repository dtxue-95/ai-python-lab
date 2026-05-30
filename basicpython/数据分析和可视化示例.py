# import pandas as pd
# import matplotlib.pyplot as plt
#
# data = pd.DataFrame({"month": ["1月", "2月", "3月"], "revenue": [100, 150, 120]})
#
# # 一行代码画图
# data.plot(x="month", y="revenue", kind="bar")
# plt.show()

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("sales.csv")

# 画销售额的条形图
data.plot(x="month", y="revenue", kind="bar", legend=True)
plt.title("Monthly Revenue")
plt.ylabel("Revenue")
plt.show()