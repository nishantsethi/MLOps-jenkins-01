from sklearn.linear_model import LogisticRegression  
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split  
import joblib



Iris_data = load_iris()  

Xtrain, Xtest, Ytrain, Ytest = train_test_split(Iris_data.data, 
                                                Iris_data.target, 
                                                test_size=0.3, 
                                                random_state=4)  

LR_Model = LogisticRegression(C=0.1,  
                               max_iter=20, 
                               fit_intercept=True, 
                               n_jobs=3, 
                               solver='liblinear')

# Train the Model
LR_Model.fit(Xtrain, Ytrain)  

joblib_file = "joblib_RL_Model.pkl"  
joblib.dump(LR_Model, joblib_file)