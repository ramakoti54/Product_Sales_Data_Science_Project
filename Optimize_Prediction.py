import numpy as np;
import pandas as pd;
import matplotlib.pyplot as plt
import math;
import Sequential_Number_Generation as SNG;
import Rectified_Linear_Unit_API as RLU_API;
#from google.colab import drive;
#from google.colab import auth;

#drive_path = drive.mount('https://docs.google.com/spreadsheets/d/1Y_xTNUN1MRj7TjwEPBithwumMfwiCWItRxCTDd89UNE/edit?usp=drive_link);

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
      for i in range(len(X)):
         if(condition_1_rating > 5 and condition_1_rating <=6):
            X.append(X[i]+ Inflation_rate_update_Input*X[i]);
         elif(condition_2_rating >4 and condition_2_rating <=5):
            X.append(X[i]+ Intrest_rate_Change_Input*X[i]);
         elif(condition_3_rating <=4 and condition_3_rating >3):
            X.append(X[i]+ Tarrif_updates * X[i]);
         elif(condition_4_rating <3 and condition_4_rating >=2):
            X.append(X[i]+ Unemployment_Rate_Input * X[i]):
         elif(condition_5_rating <2 and condition_5_rating >=1):
            X.append(X[i]+ Quarterly_results_Input * X[i]):
         elif(condition_6_rating <1 and condition_6_rating >= 0):
            X.append(X[i]+ Yearly_results_Input * X[i]);
         elif(condition_7_rating >6 and condition_7_rating <=7):
            X.append(X[i]+ Social_Economic_Factors * X[i]);
         elif(condition_8_rating >7 and condition_8_rating <= 8):
            X.append(X[i]+ Other_factors_input * X[i]);
         elif(condition_9_rating >8 and condition_9_rating <=9):
            X.append(X[i]+ Intraday_rating_Input * X[i]);             
         else:
            X.append(X[i]);
      return(X);   

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
      Inference_Dataset = Data_Price[9748:10000];
      Y = Data_Price[10001:];
      W = SNG.Sequential_Number_Generation().SNO_Generation(X,i,Dynamic_Number);      
      Y = [];
      Y = self.Optimize_Prediction(X,W,Y,i,maximum_iterations);
      self.Scatter_Plot_Data_Price(Y,Data_Volume); 
      return(None);
