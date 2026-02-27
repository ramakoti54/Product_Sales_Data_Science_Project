import numpy as np;
import pandas as pd;
import matplotlib.pyplot as plt;
import math;
#import Analyse_Business_Revenue as ABR;

class Rectified_Linear_Unit_API:
   
   def  model(self,X,w):
      X = w[0] + np.dot(X,w[1:]);
      return(X);

   def Relu(self,X,w):
      
      X = 1/(1+(math.exp(self.model(X,w))))
      return(X);
     
   def Standard_Normalization(self,Train_Dataset_Sales,Train_Dataset_Price,Product_Sales_List,Product_Price_List,i):
      
      Normalized_Value = [];
      Product_Sales_Avg = 0.0;
      method = str(input("Enter Method name for Performing Feature engineering method to impute sales and price of products either 1. Standard Normalization or 2. Gaussian Mean"))
      #status = str(nput("Enter Status name as either Sales volume or Price computation for computing one at a time."))
      Normalized_Value = Train_Dataset_Sales;
      Normalized_Price_Value = Train_Dataset_Price;
      for i in range(len(Normalized_Value)):
         if(i < len(Normalized_Value)):
            
            if(method == "Standard Normalization" and Normalized_Value[i] != 'Nan'):
               Product_Normal_Avg = np.average(Normalized_Value);
               Product_Normal_Std = np.std(Normalized_Value);
               Product_Sales_List.append(Normalized_Value[i]+(Normalized_Value[i]-Product_Normal_Avg))/(len(Normalized_Value)-1); 
            elif(method == "Standard Normalization" and Normalized_Price_Value[i] != 'Nan'):
               Product_Normal_Avg = np.average(Normalized_Price_Value);
               Product_Normal_Std = np.std(Normalized_Price_Value);          
               Product_Price_List.append(Normalized_Price_Value[i]+(Normalized_Price_Value[i]-Product_Normal_Avg))/(len(Normalized_Price_Value)-1); 
            elif(method == "Gaussian Mean" and Normalized_Value[i] != 'Nan'):
               Product_Normal_Avg = np.average(Normalized_Value);
               Product_Normal_Std = np.std(Normalized_Value);          
               Product_Sales_List.append((1/math.sqrt(2*math.pi)*Product_Normal_Std)*math.pow(math.exp(-1*math.pow((Normalized_Value[i]-Product_Normal_Avg),2))/(2*math.pow(Product_Normal_Std,2)))); 
            elif(method == "Gaussian Mean" and Normalized_Price_Value[i] != 'Nan'):   
               Product_Normal_Avg = np.average(Normalized_Price_Value);
               Product_Normal_Std = np.std(Normalized_Price_Value);          
               Product_Price_List.append((1/math.sqrt(2*math.pi)*Product_Normal_Std)*math.pow(math.exp(-1*math.pow((Normalized_Price_Value[i]-Product_Normal_Avg),2))/(2*math.pow(Product_Normal_Std,2))));                
            else:
               continue;
         else:
            continue;  
      return([Product_Sales_List,Product_Price_List]) 

   def SNO_Generation(self,X,i,Dynamic_Number):
      for i in range(Dynamic_Number):
         X.append(i);  
      return(X);   

   def Scatter_Plot_Sales_Price(self,Product_Sales_Volume,Product_Price):
      
      fig, ax = plt.subplots();
      ax.scatter(Product_Sales_Volume,Product_Price);
      plt.xlabel("Product Sales Volume");
      plt.ylabel("Price of Product sold in $");
      plt.show();
      return(None);

   def __init__(self):
      Product_Sales = pd.read_csv('/content/Product_Sales/Business_sales_EDA.csv',delimiter=';');
      #print(Product_Sales['Product ID'])
      Product_ID = Product_Sales['Product ID'];
      Product_Name = Product_Sales['name'];
      Product_Description = Product_Sales['description'];
      Product_Category = Product_Sales['Product Category'];
      Product_Brand = Product_Sales['brand'];
      Product_Seasonal = Product_Sales['Seasonal'];
      Product_Position = Product_Sales['Product Position'];
      Product_Promotion = Product_Sales['Promotion'];
      Product_Sales_Volume = Product_Sales['Sales Volume'];
      Product_Url = Product_Sales['url'];
      Product_Price = Product_Sales['price'];
      Product_Currency = Product_Sales['currency'];
      Product_Terms = Product_Sales['terms'];
      Product_Section = Product_Sales['section'];
      Product_Season = Product_Sales['season'];
      Product_Material = Product_Sales['material'];
      Product_Origin = Product_Sales['origin'];
      Product_Sales = [];
      Product_Cost = [];
      Product_Cost_Computation = [];
      Product_Sales_Computation = [];
      Product_Dollars = 0.0;
      Product_Sales = 0;
      i = 0;
      #print("Product ID: ",self.Product_ID[i],"\nProduct Name: ",self.Product_Name,"\nProduct_Description: ",Product_Description,"\nProduct Brand: ",Product_Brand,"\nProduct Category: ",Product_Category,"\nProduct Seasonal: ",Product_Seasonal,"\nProduct_Position: ",Product_Position,"\nProduct Promotion: ",Product_Promotion,"\nProduct Sales Volume: ",Product_Sales_Volume,"\nProduct url: ",Product_Url,"\nProduct price: ",Product_Price,"\nProduct Currency: ",Product_Currency,"\nProduct Section: ",Product_Section,"\nProduct Season: ",Product_Season,"\nProduct Margin: ",Product_Margin,"\nProduct material: ",Product_Material,"\n Product terms: ",Product_Terms,"\nProduct Origin: ",Product_Origin);
      Product_Info = [Product_ID,Product_Name,Product_Description,Product_Brand,Product_Category,Product_Seasonal,Product_Position,Product_Promotion,Product_Sales_Volume,Product_Url,Product_Price,Product_Currency,Product_Terms,Product_Section,Product_Season,Product_Material,Product_Origin];
      
      Product_Sales_List = [];
      Product_Price_List = [];
      self.Scatter_Plot_Sales_Price(Product_Sales_Volume,Product_Price);

      Train_Dataset_Sales = Product_Sales_Volume[:15000];
      Test_Dataset_Sales= Product_Sales_Volume[15001:];
      Train_Dataset_Price = Product_Price[:15000];
      Test_Dataset_Price = Product_Price[15001:];

      Product_Sales_List = self.Standard_Normalization(Train_Dataset_Sales,Train_Dataset_Price,Product_Sales_List,Product_Price_List,i)[0];
      Product_Price_List = self.Standard_Normalization(Train_Dataset_Sales,Train_Dataset_Price,Product_Sales_List,Product_Price_List,i)[1];
      self.Scatter_Plot_Sales_Price(Product_Sales_List,Product_Price_List);
      Relu_X = [];
      W = [];
      Dynamic_Number = 1500;
      W = self.SNO_Generation(self,W,i,Dynamic_Number)
      #w = ABR.Analyse_Business_Revenue();
      Relu_X = self.Relu(Product_Sales_List,W);
      
      return(None);

Relu = Rectified_Linear_Unit_API();
