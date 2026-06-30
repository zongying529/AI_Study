import numpy as np

# 1. 创建数组与重塑形状  【基础】
# 题目：使用 NumPy 创建一个包含 1 到 30 的一维数组，然后将它重塑为 5 行 6 列的二维数组。
# 要求：输出数组的形状、维度、元素总数，并取出第 2 行到第 4 行、第 3 列到第 5 列的子数组。
a = np.arange(1,31)
print(a)
a.resize(5,6)
print(a)
print("维度："+ str(a.ndim))
print("元素总数："+ str(a.size))
print(a[1:4,2:5])

# 2. 布尔索引与条件筛选  【基础】
# 题目：给定如下数组 arr，请筛选出所有大于 50 且能被 3 整除的元素。
# 要求：计算筛选结果的最大值、最小值、平均值，并将原数组中小于 20 的元素替换为 0。
arr = np.array([12, 18, 21, 33, 45, 54, 66, 72, 81, 95, 102])
b = (arr>50) & (arr %3 == 0)
new_arr = arr[b]
arr[arr<20]=0
print(new_arr)
print(new_arr.max(axis=0))
print(new_arr.min(axis=0))
print(new_arr.mean(axis=0))
print(arr)

# 3. 广播机制与标准化  【中等】
# 题目：给定一个 4 行 3 列的成绩矩阵 scores，每一列分别代表语文、数学、英语。
# 要求：使用广播机制对每一列做标准化处理，公式为：(x - 当前列均值) / 当前列标准差。禁止使用 for 循环。
scores = np.array([[80, 90, 75],
                   [85, 88, 92],
                   [78, 95, 85],
                   [90, 84, 88]])
col_mean = scores.mean(axis=0)
col_std = scores.std(axis=0)
new_scores = (scores - col_mean) / col_std
print(new_scores)

# 4. 矩阵运算与线性代数  【中等】
# 题目：给定矩阵 A 和 B，请完成矩阵乘法、转置、行列式计算。
# 要求：判断矩阵 A 是否可逆，如果可逆，求出 A 的逆矩阵，并验证 A 与其逆矩阵相乘是否接近单位矩阵。
A = np.array([[2, 1],
              [5, 3]])
B = np.array([[1, 4],
              [2, 6]])
print(A @ B)
print(A.T)
print(B.T)
print(np.linalg.det(A))
print(np.linalg.det(B))
inv_A = np.linalg.inv(A)
print(inv_A)
print(A @ inv_A)

# 5. 缺失值处理  【中等】
# 题目：给定一个包含 np.nan 的数组 data。
# 要求：统计缺失值数量；计算忽略缺失值后的均值、中位数；将缺失值替换为该数组的均值。
data = np.array([10, 15, np.nan, 20, 25, np.nan, 30, 35])
print(np.isnan(data).sum())
mean_val = np.nanmean(data)
print(mean_val)
print(np.nanmedian(data))
data[np.isnan(data)] = mean_val
print(data)


import pandas as pd

# 6. DataFrame 创建与基础查看  【基础】
# 题目：使用下面的数据创建一个 DataFrame。
# 要求：查看前 3 行、字段类型、基础统计信息；新增一列 total，表示 math、english、python 三科总分。
data = {
    'name': ['小王', '小李', '小张', '小陈', '小赵'],
    'math': [88, 76, 95, 63, 82],
    'english': [79, 85, 92, 70, 88],
    'python': [90, 72, 98, 68, 86]
}
df = pd.DataFrame(data)
print(df.head(3))
print(df.dtypes)
print(df.describe())

df['total'] = df['math'] + df['english'] + df['python']
print(df)

# 7. 条件筛选与排序  【基础】
# 题目：基于第 6 题的 DataFrame 继续操作。
# 要求：筛选出 total 大于 250 的学生；按照 total 从高到低排序；只保留 name、total 两列。
new_df = df[df['total']>250][['name','total']].sort_values(by='total', ascending = False)
print(new_df)

# 8. 分组统计 groupby  【中等】
# 题目：给定员工销售数据 sales。
# 要求：按 department 分组，统计每个部门的销售总额、平均销售额、人数；找出销售总额最高的部门。
sales = pd.DataFrame({
    'name': ['A', 'B', 'C', 'D', 'E', 'F'],
    'department': ['华东', '华东', '华南', '华南', '华北', '华北'],
    'amount': [1200, 1800, 900, 2300, 1600, 1100]
})
stats = sales.groupby('department').agg(
    销售总额 = ('amount', 'sum'),
    平均销售额 = ('amount', 'mean'),
    人数 = ('name', 'count')
).reset_index()

top_dept = stats.loc[stats['销售总额'].idxmax(), 'department']
print(stats)
print(top_dept)

# 9. 合并 merge  【中等】
# 题目：给定订单表 orders 和用户表 users。
# 要求：根据 user_id 合并两张表；计算每个城市的订单总金额；找出订单金额最高的用户姓名。
orders = pd.DataFrame({
    'order_id': [101, 102, 103, 104],
    'user_id': [1, 2, 1, 3],
    'price': [299, 499, 199, 899]
})

users = pd.DataFrame({
    'user_id': [1, 2, 3],
    'name': ['小王', '小李', '小张'],
    'city': ['青岛', '上海', '北京']
})

result = pd.merge(orders, users, on='user_id')
print(result)
city_total_price = result.groupby('city')['price'].sum().reset_index()
city_total_price.columns = ['city', 'total_price']
print(city_total_price)
print(result.loc[result['price'].idxmax()]['name']) # 单笔
user_total_price = result.groupby(['name', 'user_id'])['price'].sum().reset_index()
print(user_total_price.loc[user_total_price['price'].idxmax()]['name']) # 总计

# 10. 日期时间处理  【中等】
# 题目：给定一份网站访问数据 log。
# 要求：将 date 转换为 datetime 类型；新增 weekday 字段；按日期统计每天访问量；按月份统计访问量。
log = pd.DataFrame({
    'date': ['2026-06-01', '2026-06-01', '2026-06-02',
             '2026-06-15', '2026-07-01'],
    'user': ['u1', 'u2', 'u1', 'u3', 'u2']
})
log['date'] = pd.to_datetime(log['date'])
weekday_map = {0: '周一', 1: '周二', 2: '周三', 3: '周四', 4: '周五', 5: '周六', 6: '周日'}
log['weekday'] = log['date'].dt.weekday.map(weekday_map)
print(log)
print(log.groupby('date').size().reset_index(name='visit_count'))

log['month'] = log['date'].dt.to_period('M') 
# log['date'].dt.strftime('%Y-%m')

monthly_visits = log.groupby('month').size().reset_index(name='visit_count')
print(monthly_visits)

# 11. 缺失值与重复值处理  【中等】
# 题目：给定 customer 数据。
# 要求：删除重复的 id；统计每列缺失值数量；age 缺失值用平均年龄填充；city 缺失值用“未知”填充。
customer = pd.DataFrame({
    'id': [1, 2, 2, 3, 4],
    'name': ['A', 'B', 'B', 'C', 'D'],
    'age': [20, np.nan, np.nan, 35, 40],
    'city': ['北京', '上海', '上海', None, '广州']
})



