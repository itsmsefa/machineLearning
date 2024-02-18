import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.model_selection import cross_val_score

# Read the data
train_data = pd.read_csv('Cross-Validation\\train.csv', index_col='Id')
test_data = pd.read_csv('Cross-Validation\\train.csv', index_col='Id')

# Remove rows with missing target, separate target from predictors
train_data.dropna(axis=0, subset=['SalePrice'], inplace=True)
y = train_data.SalePrice              
train_data.drop(['SalePrice'], axis=1, inplace=True)

# Select numeric columns only
numeric_cols = [cname for cname in train_data.columns if train_data[cname].dtype in ['int64', 'float64']]
X = train_data[numeric_cols].copy()
X_test = test_data[numeric_cols].copy()

my_pipeline = Pipeline(steps=[
    ('preprocessor', SimpleImputer()),
    ('model', RandomForestRegressor(n_estimators=50, random_state=0))

])

def get_score(n_estimators):
    my_pipeline = Pipeline (steps = [
        ('preprocessor', SimpleImputer()),
        ('model', RandomForestRegressor(n_estimators, random_state = 0))
    ])
    
    scores = -1 * cross_val_score(my_pipeline, X, y,
                                 cv = 3,
                                 scoring = 'neg_mean_absolute_error')
    
    return scores.mean()
    
print("Average MAE score:", get_score(200))