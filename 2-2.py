#문제 2

import pandas as pd

def sort_dataset(dataset_df):
	#TODO: Implement this function
    return data_df.sort_values(by='year')

def split_dataset(dataset_df):	
	#TODO: Implement this function
    salary_arr = dataset_df['salary']*0.001
    dataset_df['salary'] = salary_arr
    d_df = dataset_df.drop(['salary'],axis=1)
    l_df = dataset_df['salary']
    x_train = d_df[:1718]
    y_train = l_df[:1718]
    x_test = d_df[1718:]
    y_test = l_df[1718:]
    return x_train,x_test,y_train,y_test

def extract_numerical_cols(dataset_df):
	#TODO: Implement this function
    return dataset_df[['age','G','PA','AB','R','H','2B','3B','HR','RBI','SB','CS','BB','HBP','SO','GDP','fly','war']]

def train_predict_decision_tree(X_train, Y_train, X_test):
	#TODO: Implement this function
    from sklearn.tree import DecisionTreeRegressor
    dc_reg=DecisionTreeRegressor()
    dc_reg.fit(X_train,Y_train)
    return dc_reg.predict(X_test)

def train_predict_random_forest(X_train, Y_train, X_test):
	#TODO: Implement this function
    from sklearn.ensemble import RandomForestRegressor
    rf_reg = RandomForestRegressor()
    rf_reg.fit(X_train,Y_train)
    return rf_reg.predict(X_test)


def train_predict_svm(X_train, Y_train, X_test):
	#TODO: Implement this function
    from sklearn.svm import SVR
    from sklearn.pipeline import make_pipeline
    from sklearn.preprocessing import StandardScaler
    svm_pipe = make_pipeline(StandardScaler(),SVR())
    svm_pipe.fit(X_train,Y_train)
    return svm_pipe.predict(X_test)

def calculate_RMSE(labels, predictions):
	#TODO: Implement this function
    import numpy as np
    return np.sqrt(np.mean((predictions-labels)**2))

if __name__=='__main__':
	#DO NOT MODIFY THIS FUNCTION UNLESS PATH TO THE CSV MUST BE CHANGED.
	data_df = pd.read_csv('2019_kbo_for_kaggle_v2.csv')
	
	sorted_df = sort_dataset(data_df)	
	X_train, X_test, Y_train, Y_test = split_dataset(sorted_df)
	
	X_train = extract_numerical_cols(X_train)
	X_test = extract_numerical_cols(X_test)

	dt_predictions = train_predict_decision_tree(X_train, Y_train, X_test)
	rf_predictions = train_predict_random_forest(X_train, Y_train, X_test)
	svm_predictions = train_predict_svm(X_train, Y_train, X_test)
	
	print ("Decision Tree Test RMSE: ", calculate_RMSE(Y_test, dt_predictions))	
	print ("Random Forest Test RMSE: ", calculate_RMSE(Y_test, rf_predictions))	
	print ("SVM Test RMSE: ", calculate_RMSE(Y_test, svm_predictions))