import pandas as pd
import joblib
from sklearn.compose import ColumnTransformer
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.metrics import r2_score,mean_squared_error
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.pipeline import Pipeline

df=pd.read_csv('student_performance_dataset.csv')

X=df.drop('Predicted_Percentage',axis=1)
y=df["Predicted_Percentage"]

categorical_cols=df.select_dtypes(include=object).columns.tolist()
numerical_cols=[cols for cols in X.columns if cols not in categorical_cols]


#prepocessing pipline
prepocessor=ColumnTransformer([
    ('cat',OneHotEncoder(handle_unknown='ignore'),categorical_cols),
    ('num',StandardScaler(),numerical_cols)
])

model=Pipeline([
    ('pre',prepocessor),
    ('knn',KNeighborsRegressor())
])

#GridSearchCV for hyperparameter tuning
params={
    'knn__n_neighbors':[3,5,7,8,9,10,12,15,20]
}

best_model=GridSearchCV(model,params,cv=5,scoring='r2')
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)


best_model.fit(X_train,y_train)
print(best_model.best_params_)

#Prediction and evaluation done
# y_pred_train=best_model.predict(X_train)
# print("training mse score:",mean_squared_error(y_train,y_pred_train))
# print("training r2 score:",r2_score(y_train, y_pred_train))

# y_pred=best_model.predict(X_test)
# print("training mse score:",mean_squared_error(y_test,y_pred))
# print("testing r2 score:",r2_score(y_test,y_pred))

# # Best cross-validated score during training
# print("Best CV R² score during training:", best_model.best_score_)

# print(df.columns)
new_data = pd.DataFrame([{
    'Hours_Studied_Per_Day': 0,
    'Total_Study_Days':0,
    'Past_Percentage': 0,
    'Attendance_Percentage': 0,
    'Parental_Support': 'Yes',
    'Internet_Access': 'Yes',
    'School_Type': 'Private',
    'Sleep_Hours': 7,
    'Social_Media_Hours': 5,
    'Coaching': 'No',
    'Gender': 'Female'
}])

prediction = best_model.predict(new_data)
print("Predicted Percentage for new student:", prediction)
joblib.dump(best_model, "student_knn_model.pkl")

