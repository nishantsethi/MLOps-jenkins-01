from sklearn.linear_model import LogisticRegression  
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split  
import joblib



Iris_data = load_iris()  

Xtrain, Xtest, Ytrain, Ytest = train_test_split(Iris_data.data, 
                                                Iris_data.target, 
                                                test_size=0.3, 
                                                random_state=4) 

joblib_file = "joblib_RL_Model.pkl" 
joblib_LR_model = joblib.load(joblib_file)



score = joblib_LR_model.score(Xtest, Ytest)  
# Print the Score

files = open("accuracy.txt","w")
files.write(str(score))
files.close()


