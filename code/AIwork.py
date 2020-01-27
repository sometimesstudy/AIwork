import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.utils import shuffle
from sklearn  import svm
from sklearn.ensemble import RandomForestClassifier


'''
学生：王宇轩
初稿：2020年1月9日
修改：
email：wang7208801@gmail.com
'''


######--------------------------传统变压器三比值法---------------------------------------#######
class IEC():
    def __init__(self, data):
        self.r1 = data.c2h2 / data.c2h4
        self.r2 = data.ch4 / data.h2
        self.r3 = data.c2h4 / data.c2h6
        self.NO_OF_STATE = []
        self.code1l = []
        self.code2l = []
        self.code3l = []
        self.Diagnosis = []
    def Three_ratios_diagosis(self):
        for i in self.r1:
            if i < 0.1:
                code1 = 0
            elif i < 3 :
                code1 = 1
            else:
                code1 = 2
            self.code1l.append(code1)


        for j in self.r2:
            if j < 0.1:
                code2 = 1
            elif j < 1:
                code2 = 0
            else:
                code2 = 2
            self.code2l.append(code2)

        for k in self.r3:
            if k < 1:
                code3 = 0
            elif k < 3:
                code3 = 1
            else:
                code3 = 2
            self.code3l.append(code3)
        self.f = zip(self.code1l,self.code2l,self.code3l)

        for a,b,c in self.f:
            ft = [a,b,c]
            if ft in [[0,0,0]]:
                self.NO_OF_STATE.append(1)
            elif ft in [[0,1,0] ,[1,1,0]]:
                self.NO_OF_STATE.append(3)
            elif ft in [[2,0,2],[2,0,1],[1,0,1]]:
                self.NO_OF_STATE.append(10)
            elif ft in [[1,0,2]]:
                self.NO_OF_STATE.append(12)
            elif ft in [[0,0,1], [0,2,0]]:
                self.NO_OF_STATE.append(4)
            elif ft == [0,2,1] :
                self.NO_OF_STATE.append(7)
            elif ft == [0,2,2]:
                self.NO_OF_STATE.append(9)
            else:
                self.NO_OF_STATE.append(2)

        for i in self.NO_OF_STATE:
            if i == 1:
                self.Diagnosis.append(0)
            elif i == 2:
                self.Diagnosis.append(3)
            elif i == 3:
                self.Diagnosis.append(1)
            elif i == 4:
                self.Diagnosis.append(4)
            elif i == 5:
                self.Diagnosis.append(4)
            elif i == 6:
                self.Diagnosis.append(4)
            elif i == 7:
                self.Diagnosis.append(5)
            elif i == 8:
                self.Diagnosis.append(5)
            elif i == 9:
                self.Diagnosis.append(6)
            elif i == 10:
                self.Diagnosis.append(2)
            elif i == 11:
                self.Diagnosis.append(3)
            elif i == 12:
                self.Diagnosis.append(3)
            elif i == 13:
                self.Diagnosis.append(1)
            else:
                self.Diagnosis.append(0)

    def predict(self,data):
        right = 0
        for i in range(240):
            if self.Diagnosis[i] == data.iloc[i,-1]:
                right += 1
        self.IEC_Threeratios_Accuracy = right/len(self.Diagnosis)

    def evaluate(self,data):
        self.Three_ratios_diagosis()
        self.predict(data)
        print('IEC三比值的分为准确率为: {}'.format(self.IEC_Threeratios_Accuracy)+'\n')

#####-----------------------------划分训练集和测试集------------------------------------#######

def train_test_samples(sample,filename):
    data = pd.read_excel(filename)
    data_shuffle = shuffle(data).reset_index(drop=True)
    train_data = data_shuffle.iloc[:sample,:-1]
    train_label = data_shuffle.iloc[:sample,-1]
    test_data = data_shuffle.iloc[sample:,:-1]
    test_label = data_shuffle.iloc[sample:,-1]
    return train_data, train_label, test_data, test_label

#####-----------------------------Knn------------------------------------#######

def KNN(k,train_data,train_label,test_data,test_label):
    predict_label = []
    for i in range(40):
        dis =(((test_data.iloc[i,:-1]-train_data.iloc[:,:-1]) ** 2).sum(axis=1)) ** 0.5
        data_add = pd.concat([dis,train_label], axis=1)
        data_add.columns = ['dis','label']
        label = list(data_add.sort_values(by='dis').label[:k])
        predict_label.append(max(label,key=label.count))
    knn_Accuracy = (predict_label == test_label).sum() / 40

    print('kNN的分类准确率为: {}'.format(knn_Accuracy)+'\n')

#####-----------------------------SVM------------------------------------#######


def SVMMODEL(g,train_data,train_label,test_data,test_label):

    scaler = StandardScaler()
    train_data1 = scaler.fit_transform(train_data)
    test_data1 = scaler.fit_transform(test_data)
    # svmfit = svm.SVC(C=c,kernel = 'rbf',gamma=g)
    svmfit = svm.SVC(kernel='rbf',gamma=g)
    svmfit.fit(train_data1,train_label)
    svm_Accuracy = svmfit.score(test_data1,test_label)
    print('SVM的分为准确率为: {}'.format(svm_Accuracy)+'\n')

#####-----------------------------随机森林------------------------------------#######
class RANDOMFORESTS():
    def __init__(self, n_estimators):
        self.n_estimators = n_estimators
    def train(self,train_data,train_label):
        x = train_data
        y = train_label
        self.estimator = RandomForestClassifier(n_estimators=self.n_estimators,
                                                random_state=2)
        self.estimator.fit(x, y)
    def evaluate(self,test_data,test_label):
        self.score = self.estimator.score(test_data,test_label)
        print('随机森林分类准确率为: {}'.format(self.score)+'\n')

