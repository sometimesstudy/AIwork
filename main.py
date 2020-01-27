import AIwork
import pandas as pd
if __name__ == '__main__':
    filename = '../dataset1_(240).xlsx' #确定数据文件
    data = pd.read_excel(filename)
    train_samples = 200					#定义训练集的数量(根据需要自定)
    iec = AIwork.IEC(data)                         #实例化IEC三比值类
    iec.evaluate(data)						#执行IEC三比值预测故障
    train_data, train_label, test_data, test_label = AIwork.train_test_samples(train_samples, filename) #划分训练集和测试集
    knn = AIwork.KNN(3,train_data,train_label,test_data,test_label)						#KNN的参数k为自定参数，可调
    svm = AIwork.SVMMODEL(1,train_data,train_label,test_data,test_label)					#g为可调参数
    rf  = AIwork.RANDOMFORESTS(5)
    rf.train(train_data,train_label)	#n_estimators为可调参数
    rf.evaluate(test_data ,test_label)

