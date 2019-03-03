import os
import seaborn as sn
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# <editor-fold desc="Importing all the data">
fileDir = r"Udacity2-2/1/project\data\Stocks/"

stocks_all = []
for num, filename in enumerate(os.listdir(fileDir)):
    statinfo = os.stat(fileDir + filename)
    if statinfo.st_size!=0:
        print(statinfo.st_size)
        data = pd.read_csv(fileDir + filename, header=0)
        data['name'] = filename.split('.us')[0]
        stocks_all.append(data)
        print(num)
        print(filename)
len(stocks_all)
allStocks = pd.concat(stocks_all)
# </editor-fold>



# <editor-fold desc="Data Process">
allStocks.info()
allStocks.head()
allStocks['Date'] = pd.to_datetime(allStocks['Date'])  # converting the str to time
allStocks.drop(['OpenInt'],axis=1,inplace=True)
# </editor-fold>



# <editor-fold desc="Data Slicing">
slb=allStocks[allStocks['name']=='slb']
hal=allStocks[allStocks['name']=='hal']
slb.shape
hal.shape
slb.isnull().sum()
hal.isnull().sum()

slb.set_index('Date',inplace=True)
hal.set_index('Date',inplace=True)
# </editor-fold>


# <editor-fold desc="Open Price">
slb['Open'].plot(label='SLB',figsize=(16,8),title='Open Price')
hal['Open'].plot(label='HAL')
plt.legend()
# </editor-fold>


# <editor-fold desc="Volume of stock traded each day">
slb['Volume'].plot(label='SLB',figsize=(16,8),title='Volume Traded')
hal['Volume'].plot(label='HAL')
plt.legend()
# </editor-fold>

# <editor-fold desc="Where are the peaks">
slb['Volume'].argmax()
hal['Volume'].argmax()
# </editor-fold>

# <editor-fold desc="Total Traded">
slb['Total Traded'] = slb['Open']*slb['Volume']
hal['Total Traded'] = hal['Open']*hal['Volume']

slb['Total Traded'].plot(label='SLB',figsize=(16,8))
hal['Total Traded'].plot(label='HAL')
plt.legend()
plt.ylabel('Total Traded')

# </editor-fold>

# <editor-fold desc="Moving Average">
slb['MA50'] = slb['Open'].rolling(50).mean()
hal['MA50'] = hal['Open'].rolling(50).mean()
slb['MA200'] = slb['Open'].rolling(200).mean()
hal['MA200'] = hal['Open'].rolling(200).mean()

slb['MA50'].plot(label='SLB',figsize=(16,8),title='Open Price')
hal['MA50'].plot(label='HAL')
plt.legend()

# </editor-fold>

#