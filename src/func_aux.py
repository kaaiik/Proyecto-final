import warnings

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

import statsmodels.api as sm
from fbprophet import Prophet

from matplotlib.animation import FuncAnimation

#-----------------------------------------------------------------

def comparador(df_real, df_pred, referencia):
    plt.plot(df_real)
    plt.plot(df_pred)
    plt.legend(['Realidad', 'Predicción'])
    plt.ylim((min(referencia), max(referencia)));
    
def train_and_predict(df):
    # renombramos el df para que lo pueda leer bien el modelo
    ts = df.rename(columns={'Time':'ds', 'GMSL':'y','GMSL uncertainty':'yhat'})

    ts.columns=['ds','y','yhat']
    model1 = Prophet(yearly_seasonality=True) 
    model1.fit(ts);
    
    # predicción de la próxima década
    future = model1.make_future_dataframe(periods = 121, freq = 'M')  
    # now lets make the forecasts
    forecast = model1.predict(future)
    df_pred = forecast[['ds', 'yhat']].tail(120)
    df_pred = df_pred.set_index(df_pred.ds)
    return df_pred
    
def train_and_predict_till2050(df):
    # renombramos el df para que lo pueda leer bien el modelo
    ts = df.rename(columns={'Time':'ds', 'GMSL':'y','GMSL uncertainty':'yhat'})

    ts.columns=['ds','y','yhat']
    model1 = Prophet(yearly_seasonality=True)
    model1.fit(ts);
    
    # predicción de la próxima década
    future = model1.make_future_dataframe(periods = 361+72, freq = 'M')  
    # now lets make the forecasts
    forecast = model1.predict(future)
    df_pred = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(360+72)
    df_pred = df_pred.set_index(df_pred.ds)
    return df_pred
    



