from time import time
from unicodedata import name
import pandas as pd
import numpy as np
import yfinance as yf

'''In This I fetch the data using yfinance and then remove the unnecessary columns after that I convert it into a .csv file :- task1.csv'''

class Csv:
    def __init__(self,symbol,time_frame,period,precision):
        self.symbol=symbol
        self.timeframe=time_frame
        self.period=period
        self.precision=precision

    def func(self):

        company = yf.Ticker(self.symbol)
        data=company.history(period=self.timeframe, interval=self.period)
        df=pd.DataFrame(data)
        print(df)
        if self.precision:
            for i in self.precision:
                print(i)
                df.drop(i,inplace=True, axis=1)
        df= df.rename(columns=str.lower)
        print(df)
        path=r'C:\Users\Sayel Munsi\Desktop\interasses\yfinance'
        file_name=input("Enter the file name with \ ex:- module1.csv : ")
        path2=path+file_name
        df.to_csv(path2)


name=input("Enter the company name: ")

#duration: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
duration=input("Enter the timeframe: ")

#var/period: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
var=input("Enter the period: ")
l2=[]
n=int(input("How many columns you want to remove: "))
for i in range(n):
    l2.append(input("Enter the name of the column name: "))


p1=Csv(name,duration,var,l2)
p1.func()






