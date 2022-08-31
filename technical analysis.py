import pandas as pd
import numpy as np


'''In this part I determine at which time cross-above and cross-below and any cross occured and return all thos timestamps'''

class Task:
    def trigeers(self):

        #location of task3
        l1=[]
        l2=[]
        l3=[]
        path1=r''
        path2=input("Enter the full file path: ")
        path=path1+path2
        df=pd.read_csv(path)

        previous_15 = df['0'].shift(1)
        previous_45 = df['1'].shift(1)

        crossing2 = ((df['0'] > df['1']) & (previous_15 <= previous_45))

        print("Datetime for crossabove: ")
        print("\n")
        crossing_dates = df.loc[crossing2, 'Datetime']
        l1.append(crossing_dates)
        # print(crossing_dates)
        print("\n")
        print(l1)
        print("\n")

        crossing3=((df['0'] < df['1']) & (previous_15 >= previous_45))

        print("Datetime for crossbelow: ")
        print("\n")
        crossing_dates = df.loc[crossing3, 'Datetime']
        l2.append(crossing_dates)
        # print(crossing_dates)
        print("\n")
        print(l2)
        print("\n")


        crossing1 = (((df['0'] < df['1']) & (previous_15 >= previous_45))
            | ((df['0'] > df['1']) & (previous_15 <= previous_45)))


        print("Datetime for cross: ")
        print("\n")
        crossing_dates = df.loc[crossing1, 'Datetime']
        l3.append(crossing_dates)
        # print(crossing_dates)
        print("\n")
        print(l3)
        

p1=Task()

p1.trigeers()

