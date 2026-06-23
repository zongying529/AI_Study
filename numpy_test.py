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
# sign, modf, isnan, isfinite, flip(反向)
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

### 数组的形状修改
# reshape, ravel（变成一行）, T/transpose（转置矩阵） 均不改变原数组
# resize 改变原数组形状，若新形状大于原形状，则用0填充
# -1 可以让numpy自动计算该维度的大小
###

# 数组堆叠 vstack, hstack 纵向堆叠，横向堆叠
a = np.floor(10*np.random.random((2,2)))
b = np.floor(10*np.random.random((2,2)))
print(np.vstack((a,b)))
print(np.hstack((a,b)))

# 将一维数组按行(纵向)堆叠成二维数组 column_stack, vstack
a = np.array([4., 2.])
print(a)
print(np.column_stack((a,a)))
print(np.vstack((a,a)))

# a[newaxis,:] 一维数组转置，竖边横，a[:, newaxis] 一维数组转置 横变竖
# r_ 将一维数组转置为二维数组，r_[] 横向堆叠，c_[] 竖向堆叠
print(np.r_[1:4,0,4]) # [1 2 3] + [0] + [4]
print(np.c_[np.array([1,2,3]), np.array([4,5,6])])

# 多维数组堆叠 concatenate了解即可

# 数组分割 hsplit, vsplit
a = np.floor(10*np.random.random((2,12)))
print(np.hsplit(a,3)) #横向分割为3个数组
print(np.vsplit(a,2)) #纵向分割为2个数组
# 横向分割为3个数组，前3列为第一个数组，第4列为第二个数组，剩余列为第三个数组
print(np.hsplit(a, (3, 4))) 

# 数组的复制与视图
# 视图 view,浅拷贝，修改视图数据会影响原数组，修改视图形状不会影响原数组
# 复制 copy,深拷贝，修改复制数据不会影响原数组

### 高级索引，花式索引，布尔索引
# 索引数组
a=np.arange(12)**2
i = np.array([1,1,3,8,5])
print(a[i]) # [ 1  1  9 64 25]
j = np.array([[3,4],[9,7]])
print(a[j]) # [[ 9 16] [81 49]]

# 当索引数组为多维数组时，索引数组的形状决定了结果的形状，单个数组指的是第一个维度
# 将标签图像转换为彩色图像
palette = np.array([[0,0,0],
                    [255,0,0],
                    [0,255,0],
                    [0,0,255],
                    [255,255,255]])
image = np.array([[0,1,2,0],
                  [0,3,4,0]])
print(palette[image])

# 多个维度的索引数组可以组合在一起(前提是索引数组的形状相同)，索引数组的每个元素对应于原数组的一个元素
a = np.arange(12).reshape(3,4)
i = np.array([[0,1],
              [1,2]])
j = np.array([[2,1],
              [3,3]])
print(a)
print(a[i,j]) # [[ 2  5] [ 7 11]]

# python中 arr[i,j] 等价于 arr[(i,j)]，因此可以将索引数组组合成一个元组
l = (i,j) # equivalent to a[i, j]
# l = np.array([i, j] 是不可以的，如果一定要用数组为索引，a[tuple(np.array([i, j]))]
print(a[l])

# 布尔索引，返回数组中满足条件的元素
a =np.arange(12).reshape(3,4)
b = a > 4
a[b] = 0 # 将数组中大于4的元素置为0，true位置为0
print(a)

a =np.arange(12).reshape(3,4)
b1 = np.array([True, False, True]) # 第一维的布尔索引
b2 = np.array([False, True, True, False]) # 第二维的布尔索引

print(a[b1,:]) # 第一维的布尔索引 相当于取得a[0,:]和a[2,:]
print(a[:,b2]) # 第二维的布尔索引 相当于取得a[:,1]和a[:,2]
print(a[b1,b2]) # 多维布尔索引 相当于取得a[0,1]和a[2,2]

# ix_函数，组合向量,返回一个元组，元组中每个元素为一个数组
# 例如你想提取三元组的 a+b*c 以及 c
a = np.array([2,3,4,5])
b = np.array([8,5,4])
c = np.array([5,4,6,8,3])
ax, bx, cx = np.ix_(a,b,c)
print(ax.shape) # (4, 1, 1)
print(bx.shape) # (1, 3, 1)
print(cx.shape) # (1, 1, 5) 
print(ax) # [[[2]] [[3]] [[4]] [[5]]]
result = ax + bx * cx
print(result)
# 将向量减除
# def ufunc_reduce(ufct, *vectors):
#    vs = np.ix_(*vectors)
#    r = ufct.identity
#    for v in vs:
#        r = ufct(r, v)
#    return r

