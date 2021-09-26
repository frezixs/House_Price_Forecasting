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

- Multiple Linear Regression Model is used because we want to predict the total housing price based on the independent variables. 
  Plotting these in a multiple regression model, we could use these features to see their relaitonship to the housing prices. However, multiple linear regression assumes that the data is independent.
- Decision Tree Regression works well on both linear and non-linear problems, but overfitting can easily occur.
- Random Forest Regression has higher accuracy and can perfom good on many problems, however, we need to choose the number of trees and overfitting can easily occur.
- SVM Regression is not biased by outliers and works very well on non-linear problems.
- KNN regression does not learn anything in the training period which makes it faster than other algorithms that require training. However, KNN does not work well with large dataset and high dimensions.
- Light GBM Regression has faster training speed and higher efficiency, and has better accuracy than other boosting algorithm because it produces much more complex trees.
