import numpy as np

a = np.array([[1,0,0],
              [0,1,2]])

# ndim 数组轴数（维度）
print("数组维度："+ str(a.ndim))

# shape 矩阵形状，元组的长度为轴的数量（一行为一个元组）
print("数组形状："+ str(a.shape))

# size 数组元素总数
print("数组元素总数："+ str(a.size))

# dtype 数组中元素的类型
print("数组元素类型："+ str(a.dtype))

# itemsize 数组每个元素的字节大小
print("数组元素大小："+ str(a.itemsize))

# data 数组的实际元素，通常不使用

# 创建初始字符占位 zeros,ones,empty 默认为float64
np.zeros((3,4))
np.ones((2,3,4), dtype=np.int16)
np.empty((2,3))

# 等差数列 arange(起始数字，末尾数字，差值)
np.arange(10,30,5)

# 数列分块 linspace(起始数字，末尾数字，等差分后元素个数) 常用于做函数图
np.linspace(0,2,9)

# 打印数组，reshape(a,b,c,d) 最小元组为d个，次大元组有c个d，以此类推
np.arange(6).reshape(2,3)

# 矩阵计算 * 为元素各个积（元素点积）@ 或 dot 为矩阵乘法
A = np.array([[1,1],
              [0,1]])
B = np.array([[2,0],
              [3,4]])
print(A*B)
print(A@B)

# 一元运算 如 sum min max cumsum（累加）为类方法实现 可以用axis指定轴
# reshape(a,b,c,d)，axis=0 则得到矩阵 (b,c,d) axis=1 则为(a,c,d)
b = np.arange(120).reshape(2,3,4,5)
print(b.sum(axis=0))
print(b.min(axis=1))
print(b.cumsum(axis=0))

### 通用函数，all, any, apply_along_axis, argmax, argmin, argsort,
# average, bincount, ceil, clip, conj, corrcoef, cov, cross, 
# cumprod, cumsum, diff, dot, floor, inner, invert, lexsort, 
# max, maximum, mean, median, min, minimum, nonzero, outer, 
# prod, re, round, sort, std, sum, trace, transpose, var, vdot, 
# vectorize, where, sin, cos, tan, exp, log, sqrt, absolute, add,
# sign, modf, isnan, isfinite,
###

# 索引，切片，迭代操作
a[-1] #数组a的最后一个元素
a[2:5] #a[2] a[3] a[4]
a[:6:2] = 100 #从0开始，每隔2个用100替代，a[5]为最后一个
a[::-1] #倒转数组
for i in a:
    i**(1/3)  #输出a中每个元素的1/3次方

### 多维数组可以为每一个轴设置一个索引
# def f(x,y): return 10*x+y
# b = np.fromfunction(f, (3,4), dtype=int)
# b =([[ 0, 1, 2, 3],
#       10,11,12,13],
#       20,21,22,23]) 
# 对多维数组的迭代是相对于 第一轴：for row in b:
# 每个数组执行需要迭代器flat: for e in b.flat:
###


