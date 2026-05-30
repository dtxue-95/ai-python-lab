# 用几行代码训练一个简单的线性回归模型（示例数据，可直接运行）
import numpy as np
from sklearn.linear_model import LinearRegression

X_train = np.array([[1], [2], [3], [4], [5]])   # 特征
y_train = np.array([2, 4, 6, 8, 10])             # 标签（y ≈ 2*x）

model = LinearRegression()
model.fit(X_train, y_train)
# 训练完成后可用 model.predict() 做预测

# 预测
X_test = np.array([[6], [7], [8]])
y_pred = model.predict(X_test)
print(y_pred)   # [12. 14. 16.]