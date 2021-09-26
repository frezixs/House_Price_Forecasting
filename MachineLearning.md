# Machine Learning Model

## Preprocessing
1. We dropped the columns that have no meaning to machine learning, such as `HouseName`, `id`. 
Dropping `ConstructionTime` because there are too many null values in this column.
2. We used `isnull()` method to check whether we have null values in our dataset or not, then used `dropna()` to drop the rows that contain null values.
3. Using `Labelencoder()` to transfer strings into numbers.
4. Since our features are not on the same scale, we need to perform Standardization by using `StandardScaler()` to avoid this issue.

## Feature Selection
The features we chose are `City`, `District`, `Floor`, `FloorType`, `BuildingType`, `BuildingStructure`, `RenovationCondition`, and `Elevator`.
- We dropped `Price` and `Square` because we used `TotalPrice` as our outcomes.
- We dropped `Lng` and `Lat` because we are using `city` and `district`.

We used feature importance to indicates the relative importance features when making a prediction. Feature importance scores can be calculated for problems that involve predicting a numerical value.

## Data Splitting
We split the data to 80% of training and 20% of testing.

## Model Choice
Since we would like to predict the housing prices based on different features which is predicting continuous values. Therefore, we chose to use supervised learning regression model.

![image](https://user-images.githubusercontent.com/82549782/134827513-ff54956b-9615-4d20-8d65-1b0227afea58.png)

We fit the data into multiple models: linear regression, decision tree, random forest, LGBM regression, SVR, KNN and Lasso. Then, we used R2 and mean squared error to compare which model is the best fit model. The result shows that LGBM is our best fit model because it has the lowest MSE and the highest R2.
