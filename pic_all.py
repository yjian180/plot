#coding:utf-8
#饼状图
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False
import matplotlib.pyplot as plt
import numpy as np

labels = [u'中文字符','B','C','D']
fracs = [15,30,45,10]
plt.axes(aspect=1)  #使x y轴比例相同
explode = [0,0,0,0]  # 突出某一部分区域
plt.pie(x=fracs, labels=labels, autopct='%.0f%%', explode=explode)  #autopct显示百分比
plt.title(u'饼状图')
plt.show()


#直方图
import matplotlib.pyplot as plt
import numpy as np
mu = 100
sigma = 20
x = mu + sigma * np.random.randn(20000)  # 样本数量
plt.hist(x,bins=100,color='green',normed=True)   # bins显示有几个直方,normed是否对数据进行标准化
plt.show()

#折线图
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-10,10,100)
y = x**3
plt.plot(x,y,linestyle='--',color='green',marker='<')
plt.show()


#散点图

import matplotlib.pyplot as plt
import numpy as np
x = np.random.randn(1000)
y = x+np.random.randn(1000)*0.5
plt.scatter(x,y,s=5,marker='<')  # s表示面积，marker表示图形
plt.show()

#箱形图
#主要用于显示数据的分散情况。图形分为上边缘、上四分位数、中位数、下四分位数、下边缘。外面的点时异常值
import matplotlib.pyplot as plt
import numpy as np
np.random.seed(100)
data = np.random.normal(size=(1000,4),loc=0,scale=1)
labels = ['A','B','C','D']
plt.boxplot(data,labels=labels)
plt.show()

#一张图上绘制子图

import matplotlib.pyplot as plt
import numpy as np
x=np.arange(1,100)
plt.subplot(221)  # 2行2列第1个图
plt.plot(x,x)
plt.subplot(222)
plt.plot(x,-x)
plt.subplot(223)
plt.plot(x,x*x)
plt.subplot(224)
plt.plot(x,np.log(x))
plt.show()

#生成网格

import matplotlib.pyplot as plt
import numpy as np
y=np.arange(1,5)
plt.plot(y,y*2)
plt.grid(True,color='g',linestyle='--',linewidth='1')
plt.show()

#生成图例

import matplotlib.pyplot as plt
import numpy as np
x = np.arange(1,11,1)
plt.plot(x, x*2)
plt.plot(x, x*3)
plt.plot(x, x*4)
plt.legend(['Normal','Fast','Faster'])
plt.show()

