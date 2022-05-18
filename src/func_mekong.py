import pandas as pd
import numpy as np

import datetime

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

import folium

#------------------------------ Importamos las funciones auxiliares

def animation_Tanchau(i):
 
    plt.title(f'Año {2005 + i}')

    data_plot=fluxes.Tanchau_fluxe[fluxes.Año==2005 + i]    
    
    ax.plot(months[:len(data_plot)], 
            data_plot, 
            c=plt.cm.viridis(i*2));
    
    return ax
    
def animation_Chaudoc(i):
 
    plt.title(f'Año {2005 + i}')

    data_plot=fluxes.Chaudocfluxes[fluxes.Año==2005 + i]    
    
    ax.plot(months[:len(data_plot)], 
            data_plot, 
            c=plt.cm.viridis(i*2));
    
    return ax
    
def animation_Cantho(i):
 
    plt.title(f'Año {2005 + i}')

    data_plot=fluxes.Cantho_fluxe[fluxes.Año==2005 + i]    
    
    ax.plot(months[:len(data_plot)], 
            data_plot, 
            c=plt.cm.viridis(i*2));
    
    return ax
