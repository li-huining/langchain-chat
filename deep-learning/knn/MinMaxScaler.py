from sklearn.preprocessing import MinMaxScaler

# 1. 准备数据
data = [[90, 2, 10, 40],
        [60, 4, 15, 45],
        [75, 3, 13, 46]]

# 2. 初始化归一化对象
transformer = MinMaxScaler()

# 3. 对原始特征进行变换
data = transformer.fit_transform(data)

# 4. 打印归一化后的结果
print(data)
