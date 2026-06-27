import pandas as pd
import numpy as np

# Series 一维标记数组
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)

# DataFrame 二维数据结构
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
print(df)

# date_range 使用带日期索引的 DataFrame 
dates = pd.date_range('20230101', periods=6)
print(dates)
df2 = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print(df2)

# 传递一个对象字典，将其转换为 DataFrame 键为列，值为数据
data = {'A': 1.,
        'B': pd.Timestamp('20230102'), 
        'C': pd.Series(1, index=list(range(4)), dtype='float32'),
        'D': np.array([3] * 4, dtype='int32'), 
        'E': pd.Categorical(["test", "train", "test", "train"]),
        'F': 'foo'}
df3 = pd.DataFrame(data)
print(df3)

# 每一列的类型可以通过 dtypes 属性查看
print(df3.dtypes)

# head() 方法返回前 n 行，默认返回前 5 行
print(df3.head())
# tail() 方法返回后 n 行，默认返回后 5 行
print(df3.tail(3))
# info() 方法显示 DataFrame 的简要摘要
print(df3.info())
# describe() 方法显示 DataFrame 的统计摘要
print(df3.describe())
# T 属性返回 DataFrame 的转置
print(df3.T)
# index 属性返回对象的索引（行标签）columns 属性返回对象的列标签
print(df3.index)
print(df3.columns)
# to_numpy() 方法将 DataFrame 转换为 NumPy 数组
print(df3.to_numpy())
# sort_index() 方法按索引排序 sort_values() 方法按值排序
print(df3.sort_index(axis=1, ascending=False)) # 1为索引倒序
print(df3.sort_values(by='A'))  # 按A列数据排序，默认为升序


# [] 操作符用于选择数据
print(df3['A'])  # 选择A列
# 如果标签只包含字母数字和下划线，则可以使用属性访问符（.）来选择列
print(df3.A)  # 选择A列

print(df3[['B', 'A']])  # 选择B，A列作为DataFrame
print(df3[0:3])  # 选择前3行 

# loc, iloc 是用于选择数据的主要方法 at iat 为快速访问或修改单个元素的标量值
print(df2.loc['20230101'])  # 按索引标签选择行
# 标签切片，两个端点都包括
print(df2.loc["20230101":"20230103", ['A', 'B']])  # A列和B列

print(df2.iloc[3])  # 按位置选择行
print(df2.iloc[:, 0:2])  # 选择所有行的前两列 切片类似numpy

# 布尔索引
print(df2[df2.A > 0])  # 选择A列大于0
print(df2[df2 > 0])  # 选择所有大于0的元素 不符合用NaN填充

# where() 方法用于根据条件选择数据 类似于布尔索引，但不会丢失数据
df5 = df2.copy()
print(df5.where(df5 > 0))
print(df5.where(df5 > 0, -df5))  # 不符合条件的值取相反数
print(df5)

# isin() 方法用于过滤数据
df4 = df2.copy()
df4['E'] = ['one', 'one', 'two', 'three', 'four', 'three']
print(df4)
print(df4[df4['E'].isin(['two', 'four'])])  # 选择E列为two或four的行

#  设置新列会自动对齐数据
s1 = pd.Series([1, 2, 3], index=[0, 1, 2])
df["F"] = s1
print(df)
df.at[0, 'A'] = 0  # 设置单个值
df.iat[0, 1] = 0  # 设置单个值
df.loc[:, 'D'] = np.array([5] * len(df))  # 设置整列值
print(df)

# 重新索引允许你改变、增加或删除轴标签
df6 = df2.reindex(index=dates[0:4], columns=list(df2.columns) + ['E'])  # 增加一列E
df6.loc[dates[0]:dates[1], 'E'] = 1
print(df6)

# drop() 方法用于删除指定的行或列
print(df6.drop(['E'], axis=1))  # 删除E列

# dropna() 方法用于删除缺失值
print(df6.dropna(how='any'))  # 删除任何包含NaN的行

# fillna() 方法用于填充缺失值
print(df6.fillna(value=5))  # 用5填充缺失值

# isnull() 方法用于检测缺失值
print(df6.isnull())  # 返回布尔值，True表示缺失值

# isna() 方法用于检测缺失值
print(df6.isna())  # 返回布尔值，True表示缺失值

# 用户自定义函数 
# df.agg() 方法用于对数据进行聚合操作 just like SQL's GROUP BY
# df.transform() 方法用于对数据进行转换操作
# df.apply() 方法用于对数据进行应用操作

# 价值计数 value_counts() 方法用于计算每个唯一值的出现次数
print(df4['E'].value_counts())

# 相关性和协方差 corr() 方法用于计算相关系数 cov() 方法用于计算协方差

# 字符串方法 str() 方法用于对字符串进行操作
# lower() 方法用于将字符串转换为小写 upper() 方法用于将字符串转换为大写
# split() 方法用于将字符串拆分为列表
# contains() 方法用于检查字符串是否包含指定的子字符串
# replace() 方法用于替换字符串中的指定子字符串
# cat() 方法用于将字符串连接在一起
# get_dummies() 方法用于将分类变量转换为虚拟变量


# 合并
# concat() 方法用于将多个 DataFrame 或 Series 沿指定轴连接在一起（按行）

# merge() 方法用于根据指定的键将两个 DataFrame 合并在一起（按列全连接）
left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})
print(pd.merge(left, right, on='key'))  # 按key列合并 如果有多个键，则可以使用 on 参数传递一个列表

# groupby() 将数据分组，对每个组独立应用函数，将结果合成
df = pd.DataFrame(
                {
                "A":["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
                "B": ["one", "one", "two", "three", "two", "two", "one", "three"],
                "C": np.random.randn(8),
                "D": np.random.randn(8),
                }
        )
print(df)
print(df.groupby("A")[["C", "D"]].sum()) # 将A列中相同的标签的C列D列分别求和
print(df.groupby(["A", "B"]).sum()) # 将A,B列中相同的标签的 其他列的值 分别求和

# 堆叠 stack() unstack()

# 原df
#               A       B
# first second
# bar   one     1       0
#       tow     2       4
# baz   one     3       5
#       tow     1       4

# stack()后
# first second
# bar   one     A       1
#               B       0
#       tow     A       2
#               B       4
# baz   one     A       3
#               B       5
#       two     A       1
#               B       4

# unstack()为原df
#               A       B
# first second
# bar   one     1       0
#       tow     2       4
# baz   one     3       5
#       tow     1       4

# unstack(0)                    unstack(1)
# first         bar     baz     second          one     two
# second                        first
# one   A       1       3       bar     A       1       2
#       B       0       5               B       0       4
# tow   A       2       1       baz     A       3       1
#       B       4       4               B       5       4

# 透视表 pivot_table() 方法用于创建透视表
print(df)
# 以列A和B作为行索引‌，‌列C的值作为列标题‌，并对D的数据进行聚合 默认aggfunc='mean'
print(pd.pivot_table(df, values="D", index=["A", "B"], columns=["C"]))

## 时间序列
# 创建了从 2012-01-01 00:00:00 开始，共 100 个点、间隔为‌1秒‌的时间序列
rng = pd.date_range("1/1/2012", periods=100, freq="s")
# 生成 100 个 0-499 之间的随机整数作为值，以上述时间序列为索引，构成时间序列对象
ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng) 
#  将数据按‌5分钟‌（300秒）为区间进行下采样, 300秒＞100秒，故只有一个值
print(ts.resample("5Min").sum())

# Series.tz_localize() 本地化时区 Series.tz_convert() 转化为另一个时区

## 类别分类
df = pd.DataFrame(
     {"id": [1, 2, 3, 4, 5, 6], 
      "raw_grade": ["a", "b", "b", "a", "a", "e"]}
     ) 
# Series.astype() 转换为分类数据类型
df["grade"] = df["raw_grade"].astype("category")
print(df["grade"])

# Series.cat.rename_categories() 类别重命名
new_categories = ["very good", "good", "very bad"]
df["grade"] = df["grade"].cat.rename_categories(new_categories)
print(df['grade'])

# Series.cat.set_categories() 重新排序类别并同时添加缺失类别(不会影响原本分类)
df["grade"] = df["grade"].cat.set_categories(
    ["very bad", "bad", "medium", "good", "very good"]
)
print(df)

# Series.sort_values(by="") 按照设定类别的顺序排序
df.sort_values(by="grade")
print(df)

# Series.groupby(observed=False) 按分类列分组还显示空类,统计分类后每类元素个数
print(df.groupby("grade", observed=False).size())

## 绘图
import matplotlib.pyplot as plt

# 绘制时间序列图形，ts.cumsum()为累积值，绘图必须使用show()方法才能展现出来图。
ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()
ts.plot()

# 绘制带标签的所有列
df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index,
                   columns=['A', 'B', 'C', 'D'])
df = df.cumsum()
df.plot()
# plt.figure() 隐式建立一个图像
plt.legend(loc='best')
plt.show() 

### 获取数据输入/输出
## CSV
df.to_csv('foo.csv') # 写入csv
print(pd.read_csv('foo.csv'))  # 读取csv

## Excel
df.to_excel('foo.xlsx', sheet_name='Sheet1') # 写入Excel
print(pd.read_excel('foo.xlsx', 'Sheet1', index_col=None, na_values=['NA'])) # 读取Excel


# 如果你对 Series 或 DataFrame 执行布尔运算，可能会报错
# ValueError: The truth value of a Series is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().
# 从以下网址获取详细信息
# https://link.zhihu.com/?target=http%3A//pandas.pydata.org/pandas-docs/version/0.20/basics.html%23basics-compare
# https://link.zhihu.com/?target=http%3A//pandas.pydata.org/pandas-docs/version/0.20/gotchas.html%23gotchas