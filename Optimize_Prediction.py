import numpy as np;
import pandas as pd;
import matplotlib.pyplot as plt
import math;
import Sequential_Number_Generation as SNG;
import Rectified_Linear_Unit_API as RLU_API;

class Optimize_Prediction:
   
   def Entropy(self,X,W,i,k,Y):
      L = [];
      L = Y;
      X = self.Relu_API.__init().Relu(X,W,i);
      L = self.Relu_API.__init().Relu(X,W,i);

      for i in range(len(Y)):
         entropy = L[i] - Y[i];
      return(entropy);

   def Input_Prediction(X):
      X.append(for i in range(len(X)));
      return(X)   

   def Optimize_Prediction(self,X,W,Y,i,maximum_iterations):
      k = 0;
      entropy = 0;
      X = self.RLU_API.__init__().Relu(X,W,i);
      for j in range(maximum_iterations):
         entropy = self.Entropy(X,W,i,k,Y);              
      if(entropy == 0 or entropy >= 0.05):
         Z = [];
         Z = self.Input_Prediction(X);
         X = X[:]+ Z[:] 
         self.Optimize_Prediction(Self,X,W,Y,i,maximum_iterations);
      else:
         Y = X;
      return(Y);

   def __init__(self):     
      Stock_Data = pd.read_csv('/content/Stock_Files/JPM.csv',delimiter=',');
      Data_Open = Stock_Data['Open'];
      Data_Close = Stock_Data['Close'];
      Data_Low = Stock_Data['Low'];
      Data_High = Stock_Data['High'];
      Data_Adj_Close = Stock_Data['Adj Close'];
      Data_Volume = Stock_Data['Volume'];
      Data_Date = Stock_Data['Date'];
      Data_Price = [];
      i = 0;
      W = [];
      maximum_iterations = int(input("Enter Maximum iterations to train ML model to form Inference."));
      Dynamic_Number = 10000;
      Data_Price = float(Data_Open + Data_Close + Data_Low + Data_High + Data_Adj_Close)/5.0;
      X = Data_Price[:10000];
      Y = Data_Price[10001:];
      W = SNG.Sequential_Number_Generation().SNO_Generation(X,i,Dynamic_Number);      
      Y = [];
      Y = self.Optimize_Prediction(X,W,Y,i,maximum_iterations);
      self.Scatter_Plot_Data_Price(Y,Data_Volume); 
      return(None);
