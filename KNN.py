import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score,confusion_matrix
np.random.seed(50)
height=np.random.randint(140,200,200)
weight=np.random.randint(40,120,200)
bmi = weight/((height/100)**2)

BMI=pd.DataFrame({"Height":height,"Weight":weight,"BMI":bmi})
BMI
def cateogary(bmi):
    bmi=float(bmi)
    if bmi<=19 and bmi>1:
        return "Under Weight"
    if bmi<=25 and bmi>19:
        return "Normal"
    else:
        return "Over Weight"

BMI['Cateogary']=BMI['BMI'].apply(cateogary)
BMI
X=BMI[["Height","Weight"]]
Y=BMI["Cateogary"]
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.3,random_state=50)
print(X_train,X_test,Y_train,Y_test)
model=KNeighborsClassifier(n_neighbors=4)
model.fit(X_train,Y_train)