import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pylab import rcParams
rcParams['figure.figsize']=20,10
from keras.models import Sequential
from keras.layers import LSTM,Dropout,Dense
from sklearn.preprocessing import MinMaxScaler
df=pd.read_csv("C:\\Users\\pc\\Downloads\\New folder\\Project\\NSE-Tata-Global-Beverages-Limited")
df.head()
