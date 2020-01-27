# 人工智能作业

### 基于变压器油中溶解气体的机器学习和传统方法故障诊断的可调参python模块

#### 程序讲解

1.1 开发环境 macOS mojave 10.14.6    win10和ubuntu测试可用

1.2 本程序分为四个算法：

+ 传统三比值法
+ k-NearestNerghbors
+ SVM
+ 随机森林

**其中传统三比值和k-NearestNeighbors是用python原生模块写的，SVM和随机森林调用了python的机器学习库scikit-learn。所有代码都是自己想的，没有抄袭。程序输入为5种油中溶解气体以及对应的故障类型，输出为四种算法的分类准确率**

1.3 模块的调用方法，将AIwork.py文件放在自己的主程序所在的文件夹

````python
import AIwork
import pandas as pd
if __name__ == '__main__':
    filename = '../dataset/dataset1_(240).xlsx'            #确定数据文件
    data = pd.read_excel(filename)								 #读取文件的数据
    train_samples = 200														 #定义训练集的数量(根据需要自定)
    iec = AIwork.IEC(data)                         #实例化IEC三比值类
    iec.evaluate(data)														 #执行IEC三比值预测故障
    train_data, train_label, test_data, test_label =    	AIwork.train_test_samples(train_samples, filename) #划分训练集和测试集
    knn = AIwork.KNN(k,train_data,train_label,test_data,test_label)	#KNN的参数k为自定参数，可调
    svm = AIwork.SVMMODEL(g,train_data,train_label,test_data,test_label)		#g为可调参数
    rf  = AIwork.RANDOMFORESTS(n_estimators)			 #n_estimators为可调参数
    rf.train(train_data,train_label)							 #训练随机森林模型
    rf.evaluate(test_data ,test_label)						 #输出随机森林的准确率
````

1.4 程序放在我的GitHub https://github.com/1428409697/AIwork 上面

