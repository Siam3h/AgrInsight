# predictor/model_pipeline.py
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split

class CropYieldModel:
    def __init__(self):
        self.model = None
        self.prepare_data()
        self.train_model()
        
    def prepare_data(self):
        df_yield = pd.read_csv('yield.csv')
        df_yield.rename(columns={"Value": "hg/ha_yield"}, inplace=True)
        df_yield = df_yield.drop(['Year Code','Element Code', 'Element','Year Code','Area Code','Domain Code', 'Domain','Unit','Item Code'], axis=1)
        df_yield = df_yield.dropna()
        
        df_rain = pd.read_csv('rainfall.csv')
        df_rain['average_rain_fall_mm_per_year'] = pd.to_numeric(df_rain['average_rain_fall_mm_per_year'], errors='coerce')
        df_rain = df_rain.dropna()
        
        df_main = pd.merge(df_yield, df_rain, on=['Year','Area'], how='outer')
        
        dataframe_pesticide = pd.read_csv('pesticides.csv')
        dataframe_pesticide.rename(columns={"Value": "pesticides_tonnes"}, inplace=True)
        dataframe_pesticide = dataframe_pesticide.drop(['Element','Domain','Unit','Item'], axis=1)
        
        df_main = pd.merge(df_main, dataframe_pesticide, on=['Year','Area'])
        
        dataframe_temp = pd.read_csv('temp.csv')
        dataframe_temp.rename(columns={"year": "Year", "country": 'Area'}, inplace=True)
        
        self.df_main = pd.merge(df_main, dataframe_temp, on=['Year','Area'])

    def train_model(self):
        df_main = self.df_main.dropna()

        X = df_main.drop('hg/ha_yield', axis=1)
        y = df_main['hg/ha_yield']
        
        numeric_features = ['average_rain_fall_mm_per_year', 'pesticides_tonnes', 'temperature']
        categorical_features = ['Year', 'Area']

        numeric_transformer = Pipeline(steps=[
            ('scaler', MinMaxScaler())])

        categorical_transformer = Pipeline(steps=[
            ('onehot', OneHotEncoder(handle_unknown='ignore'))])

        preprocessor = ColumnTransformer(
            transformers=[
                ('num', numeric_transformer, numeric_features),
                ('cat', categorical_transformer, categorical_features)])

        self.model = Pipeline(steps=[
            ('preprocessor', preprocessor),
            ('regressor', RandomForestRegressor())])

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        self.model.fit(X_train, y_train)

    def predict(self, data):
        return self.model.predict(data)
