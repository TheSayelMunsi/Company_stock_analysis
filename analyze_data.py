
import pandas as pd
import numpy as np

'In this part I analyze the data and according the condition I add a extra column where I put colour according to the condition example:-FB2.csv'

class new_column:
    def __init__(self,path):
        self.path=path

    def color(self):
        df=pd.read_csv(self.path)
        df['color'] = np.where((df['open'] < df['close']), 'green', 'red')
        print(df)
        #saving in csv
        #location and file name
        module_name=input("Enter module name with \ ex:-\module1.csv: ")
        path3=r'C:\Users\Sayel Munsi\Desktop\interasses\yfinance'
        location=path3+module_name
        df.to_csv(location,index=False)


#location of the file
pth=r'C:\Users\Sayel Munsi\Desktop\interasses\Screening Test_Support files\Screening Test_Support files\data'
fi=input("Enter the file name with \ from data folder ex:-\FB.csv : ")
pth2=pth+fi
p1=new_column(pth2)
p1.color()