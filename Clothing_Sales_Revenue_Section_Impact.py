import numpy as np;
import pandas as pd;
import matplotlib.pyplot as plt;
import math;
import Analyse_Business_Revenue as ABR;
import Even_Odd_Random_Number_Generator as eong;

class Clothing_Sales_Revenue_Section_Impact:
   def Clothing_Sales_Revenue_Section(self,Product_Sales_File,Product_Section,Product_Materials,Product_Terms,i,Product_Sales_List,Product_Cost_List,Product_Price_List,W_Product_Terms_Tshirts_Sales_List,W_Product_Terms_Tshirts_Price_List,W_Product_Terms_Tshirts_Cost_List,W_Product_Terms_Jackets_Sales_List,W_Product_Terms_Jackets_Price_List,W_Product_Terms_Jackets_Cost_List,W_Product_Terms_Jeans_Sales_List,W_Product_Terms_Jeans_Price_List,W_Product_Terms_Jeans_Cost_List,M_Product_Terms_Tshirts_Sales_List,M_Product_Terms_Tshirts_Price_List,M_Product_Terms_Tshirts_Cost_List,M_Product_Terms_Jackets_Sales_List,M_Product_Terms_Jackets_Price_List,M_Product_Terms_Jackets_Cost_List,M_Product_Terms_Jeans_Sales_List,M_Product_Terms_Jeans_Price_List,M_Product_Terms_Jeans_Cost_List):
      Product_Sales_Volume = [];
      Product_Price = [];
      Product_ID = [];
      Product_ID = Product_Sales_File[0];
      Product_Sales_Volume = Product_Sales_File[8];
      Product_Price = Product_Sales_File[10];
      Product_Section = Product_Sales_File[9];
      Product_Materials = Product_Sales_File[15];
      Product_Terms = Product_Sales_File[3];

      Product_Cost_List = ABR.Analyse_Business_Revenue().Adjust_Product_Price(Product_Price,Product_Sales_Volume,Product_ID,i,Product_Cost_List);
      
      for i in range(len(Product_ID)):
         if(i < len(Product_ID) and Product_Section[i] == 'WOMAN' and (Product_Materials[i] == 'Wool' or Product_Materials[i] == 'Wool Blend' or Product_Materials[i] == 'Linen' or Product_Materials[i] == 'Linen Blend' or Product_Materials[i] == 'Cotton')):
            if(Product_Terms[i] == 't-shirts'):
               W_Product_Terms_Tshirts_Sales_List.append(Product_Sales_Volume[i]);
               W_Product_Terms_Tshirts_Price_List.append(Product_Price[i]);
               W_Product_Terms_Tshirts_Cost_List = Product_Cost_List[i];
            elif(Product_Terms[i] == 'jackets'):
               W_Product_Terms_Jackets_Sales_List.append(Product_Sales_Volume[i]);
               W_Product_Terms_Jackets_Price_List.append(Product_Price[i]);
               W_Product_Terms_Jackets_Cost_List.append(Product_Cost_List[i]);
            elif(Product_Terms[i] == 'jeans'):
               W_Product_Terms_Jeans_Sales_List.append(Product_Sales_Volume[i]);
               W_Product_Terms_Jeans_Price_List.append(Product_Price[i]);
               W_Product_Terms_Jeans_Cost_List.append(Product_Cost_List[i]);

         elif(i < len(Product_ID) and Product_Section[i] == 'MAN' and (Product_Materials[i] == 'Wool' or Product_Materials[i] == 'Wool Blend' or Product_Materials[i] == 'Linen' or Product_Materials[i] == 'Linen Blend' or Product_Materials[i] == 'Cotton')):  
            if(Product_Terms[i] == 't-shirts'):
               M_Product_Terms_Tshirts_Sales_List.append(Product_Sales_Volume[i]);
               M_Product_Terms_Tshirts_Price_List.append(Product_Price[i]);
               M_Product_Terms_Tshirts_Cost_List = Product_Cost_List[i];
            elif(Product_Terms[i] == 'jackets'):
               M_Product_Terms_Jackets_Sales_List.append(Product_Sales_Volume[i]);
               M_Product_Terms_Jackets_Price_List.append(Product_Price[i]);
               M_Product_Terms_Jackets_Cost_List.append(Product_Cost_List[i]);
            elif(Product_Terms[i] == 'jeans'):
               M_Product_Terms_Jeans_Sales_List.append(Product_Sales_Volume[i]);
               M_Product_Terms_Jeans_Price_List.append(Product_Price[i]);
               M_Product_Terms_Jeans_Cost_List.append(Product_Cost_List[i]);
         else:
            print("Exception in the code execution. Check with Developer for further information on the error.")
            break;
      Product_Sales_List = [W_Product_Terms_Tshirts_Sales_List,W_Product_Terms_Jackets_Sales_List,W_Product_Terms_Jeans_Sales_List,M_Product_Terms_Tshirts_Sales_List,M_Product_Terms_Jackets_Sales_List,M_Product_Terms_Jeans_Sales_List]  
      Product_Cost_List =[W_Product_Terms_Tshirts_Cost_List,W_Product_Terms_Jackets_Cost_List,W_Product_Terms_Jeans_Cost_List,M_Product_Terms_Tshirts_Cost_List,M_Product_Terms_Jackets_Cost_List,M_Product_Terms_Jeans_Cost_List];     
      Product_Price_List = [W_Product_Terms_Tshirts_Price_List,W_Product_Terms_Jackets_Price_List,W_Product_Terms_Jeans_Price_List,M_Product_Terms_Tshirts_Price_List,M_Product_Terms_Jackets_Price_List,M_Product_Terms_Jeans_Price_List]     
      return([Product_Sales_List,Product_Cost_List,Product_Price_List]);

   def Scatter_Plot_Sales_Price_Cost(self,Sales_List_Name,Price_List_Name,Cost_List_Name):
      plt.style.use('_mpl-gallery-nogrid')
      # make data
      x = Sales_List_Name;#Product_Section_Output; #[1, 2, 3, 4]
      y = Price_List_Name;#Product_Season_Output;
      z = Cost_List_Name;#Product_Position_Output;
      #Product_Material_Output;
      #Product_Origin_Output;
      # Plot colour addition to shell pie charts.
      colours = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len(x)))
      # ploting
      fig, ax = plt.subplots()
      ax.scatter(x,y,colors=colours);
      plt.xlabel('Sales Volume');
      plt.ylabel('Price');
      plt.show();

      ax.scatter(y,z,colors=colours);
      plt.xlabel('Sales Volume');
      plt.ylabel('Clothing Revenue');
      plt.show();

      ax.scatter(x,z,colors=colours);
      plt.xlabel('Sales Volume');
      plt.ylabel('Zabra Revenue');
      plt.show();
      return(None);



   def __init__(self):
      Product_Sales = pd.read_csv('/content/Product_Sales/Business_sales_EDA.csv', delimiter = ';');
      Product_ID = Product_Sales['Product ID'];
      Product_Name = Product_Sales['name'];
      Product_Description = Product_Sales['description'];
      Product_Terms = Product_Sales['terms'];
      Product_Promotion = Product_Sales['Promotion'];
      Product_Position = Product_Sales['Product Position'];
      Product_URL = Product_Sales['url'];
      Product_Category = Product_Sales['Product Category'];
      Product_Sales_Volume = Product_Sales['Sales Volume'];
      Product_Section = Product_Sales['section'];
      Product_Price = Product_Sales['price'];
      Product_Seasonal = Product_Sales['Seasonal'];
      Product_Season = Product_Sales['season'];
      Product_Currency = Product_Sales['currency'];
      Product_Material = Product_Sales['material'];
      Product_Origin = Product_Sales['origin'];
      Product_Brand = Product_Sales['brand'];
      Product_Sales_File = [Product_ID,Product_Name,Product_Description,Product_Terms,Product_Promotion,Product_Position,Product_URL,Product_Category,Product_Sales_Volume,Product_Section,Product_Price,Product_Seasonal,Product_Season,Product_Currency,Product_Material,Product_Origin,Product_Brand];
      Product_Sales_List = [];
      Product_Cost_List =[];
      Product_Price_List = [];
      i = 0;
      Product_Section = [];
      Product_Materials = [];
      Product_Terms = [];
      W_Product_Terms_Tshirts_Sales_List = [];
      W_Product_Terms_Tshirts_Price_List = [];
      W_Product_Terms_Tshirts_Cost_List = [];
      W_Product_Terms_Jackets_Sales_List = [];
      W_Product_Terms_Jackets_Price_List = [];
      W_Product_Terms_Jackets_Cost_List = [];
      W_Product_Terms_Jeans_Sales_List = [];
      W_Product_Terms_Jeans_Price_List = [];
      W_Product_Terms_Jeans_Cost_List = [];
      M_Product_Terms_Tshirts_Sales_List = [];
      M_Product_Terms_Tshirts_Price_List = [];
      M_Product_Terms_Tshirts_Cost_List = [];
      M_Product_Terms_Jackets_Sales_List = [];
      M_Product_Terms_Jackets_Price_List = [];
      M_Product_Terms_Jackets_Cost_List = [];
      M_Product_Terms_Jeans_Sales_List = [];
      M_Product_Terms_Jeans_Price_List = [];
      M_Product_Terms_Jeans_Cost_List = [];

      W_Product_Terms_Tshirts_Sales_List = self.Clothing_Sales_Revenue_Section(Product_Sales_File,Product_Section,Product_Materials,Product_Terms,i,Product_Sales_List,Product_Cost_List,Product_Price_List,W_Product_Terms_Tshirts_Sales_List,W_Product_Terms_Tshirts_Price_List,W_Product_Terms_Tshirts_Cost_List,W_Product_Terms_Jackets_Sales_List,W_Product_Terms_Jackets_Price_List,W_Product_Terms_Jackets_Cost_List,W_Product_Terms_Jeans_Sales_List,W_Product_Terms_Jeans_Price_List,W_Product_Terms_Jeans_Cost_List,M_Product_Terms_Tshirts_Sales_List,M_Product_Terms_Tshirts_Price_List,M_Product_Terms_Tshirts_Cost_List,M_Product_Terms_Jackets_Sales_List,M_Product_Terms_Jackets_Price_List,M_Product_Terms_Jackets_Cost_List,M_Product_Terms_Jeans_Sales_List,M_Product_Terms_Jeans_Price_List,M_Product_Terms_Jeans_Cost_List)[0][0];
      W_Product_Terms_Jackets_Sales_List =  self.Clothing_Sales_Revenue_Section(Product_Sales_File,Product_Section,Product_Materials,Product_Terms,i,Product_Sales_List,Product_Cost_List,Product_Price_List,W_Product_Terms_Tshirts_Sales_List,W_Product_Terms_Tshirts_Price_List,W_Product_Terms_Tshirts_Cost_List,W_Product_Terms_Jackets_Sales_List,W_Product_Terms_Jackets_Price_List,W_Product_Terms_Jackets_Cost_List,W_Product_Terms_Jeans_Sales_List,W_Product_Terms_Jeans_Price_List,W_Product_Terms_Jeans_Cost_List,M_Product_Terms_Tshirts_Sales_List,M_Product_Terms_Tshirts_Price_List,M_Product_Terms_Tshirts_Cost_List,M_Product_Terms_Jackets_Sales_List,M_Product_Terms_Jackets_Price_List,M_Product_Terms_Jackets_Cost_List,M_Product_Terms_Jeans_Sales_List,M_Product_Terms_Jeans_Price_List,M_Product_Terms_Jeans_Cost_List)[0][1];
      W_Product_Terms_Jeans_Sales_List = self.Clothing_Sales_Revenue_Section(Product_Sales_File,Product_Section,Product_Materials,Product_Terms,i,Product_Sales_List,Product_Cost_List,Product_Price_List,W_Product_Terms_Tshirts_Sales_List,W_Product_Terms_Tshirts_Price_List,W_Product_Terms_Tshirts_Cost_List,W_Product_Terms_Jackets_Sales_List,W_Product_Terms_Jackets_Price_List,W_Product_Terms_Jackets_Cost_List,W_Product_Terms_Jeans_Sales_List,W_Product_Terms_Jeans_Price_List,W_Product_Terms_Jeans_Cost_List,M_Product_Terms_Tshirts_Sales_List,M_Product_Terms_Tshirts_Price_List,M_Product_Terms_Tshirts_Cost_List,M_Product_Terms_Jackets_Sales_List,M_Product_Terms_Jackets_Price_List,M_Product_Terms_Jackets_Cost_List,M_Product_Terms_Jeans_Sales_List,M_Product_Terms_Jeans_Price_List,M_Product_Terms_Jeans_Cost_List)[0][2];
      M_Product_Terms_Tshirts_Sales_List = self.Clothing_Sales_Revenue_Section(Product_Sales_File,Product_Section,Product_Materials,Product_Terms,i,Product_Sales_List,Product_Cost_List,Product_Price_List,W_Product_Terms_Tshirts_Sales_List,W_Product_Terms_Tshirts_Price_List,W_Product_Terms_Tshirts_Cost_List,W_Product_Terms_Jackets_Sales_List,W_Product_Terms_Jackets_Price_List,W_Product_Terms_Jackets_Cost_List,W_Product_Terms_Jeans_Sales_List,W_Product_Terms_Jeans_Price_List,W_Product_Terms_Jeans_Cost_List,M_Product_Terms_Tshirts_Sales_List,M_Product_Terms_Tshirts_Price_List,M_Product_Terms_Tshirts_Cost_List,M_Product_Terms_Jackets_Sales_List,M_Product_Terms_Jackets_Price_List,M_Product_Terms_Jackets_Cost_List,M_Product_Terms_Jeans_Sales_List,M_Product_Terms_Jeans_Price_List,M_Product_Terms_Jeans_Cost_List)[0][3];
      M_Product_Terms_Jackets_Sales_List =  self.Clothing_Sales_Revenue_Section(Product_Sales_File,Product_Section,Product_Materials,Product_Terms,i,Product_Sales_List,Product_Cost_List,Product_Price_List,W_Product_Terms_Tshirts_Sales_List,W_Product_Terms_Tshirts_Price_List,W_Product_Terms_Tshirts_Cost_List,W_Product_Terms_Jackets_Sales_List,W_Product_Terms_Jackets_Price_List,W_Product_Terms_Jackets_Cost_List,W_Product_Terms_Jeans_Sales_List,W_Product_Terms_Jeans_Price_List,W_Product_Terms_Jeans_Cost_List,M_Product_Terms_Tshirts_Sales_List,M_Product_Terms_Tshirts_Price_List,M_Product_Terms_Tshirts_Cost_List,M_Product_Terms_Jackets_Sales_List,M_Product_Terms_Jackets_Price_List,M_Product_Terms_Jackets_Cost_List,M_Product_Terms_Jeans_Sales_List,M_Product_Terms_Jeans_Price_List,M_Product_Terms_Jeans_Cost_List)[0][4];
      M_Product_Terms_Jeans_Sales_List = self.Clothing_Sales_Revenue_Section(Product_Sales_File,Product_Section,Product_Materials,Product_Terms,i,Product_Sales_List,Product_Cost_List,Product_Price_List,W_Product_Terms_Tshirts_Sales_List,W_Product_Terms_Tshirts_Price_List,W_Product_Terms_Tshirts_Cost_List,W_Product_Terms_Jackets_Sales_List,W_Product_Terms_Jackets_Price_List,W_Product_Terms_Jackets_Cost_List,W_Product_Terms_Jeans_Sales_List,W_Product_Terms_Jeans_Price_List,W_Product_Terms_Jeans_Cost_List,M_Product_Terms_Tshirts_Sales_List,M_Product_Terms_Tshirts_Price_List,M_Product_Terms_Tshirts_Cost_List,M_Product_Terms_Jackets_Sales_List,M_Product_Terms_Jackets_Price_List,M_Product_Terms_Jackets_Cost_List,M_Product_Terms_Jeans_Sales_List,M_Product_Terms_Jeans_Price_List,M_Product_Terms_Jeans_Cost_List)[0][5];

      W_Product_Terms_Tshirts_Cost_List = self.Clothing_Sales_Revenue_Section(Product_Sales_File,Product_Section,Product_Materials,Product_Terms,i,Product_Sales_List,Product_Cost_List,Product_Price_List,W_Product_Terms_Tshirts_Sales_List,W_Product_Terms_Tshirts_Price_List,W_Product_Terms_Tshirts_Cost_List,W_Product_Terms_Jackets_Sales_List,W_Product_Terms_Jackets_Price_List,W_Product_Terms_Jackets_Cost_List,W_Product_Terms_Jeans_Sales_List,W_Product_Terms_Jeans_Price_List,W_Product_Terms_Jeans_Cost_List,M_Product_Terms_Tshirts_Sales_List,M_Product_Terms_Tshirts_Price_List,M_Product_Terms_Tshirts_Cost_List,M_Product_Terms_Jackets_Sales_List,M_Product_Terms_Jackets_Price_List,M_Product_Terms_Jackets_Cost_List,M_Product_Terms_Jeans_Sales_List,M_Product_Terms_Jeans_Price_List,M_Product_Terms_Jeans_Cost_List)[1][0];
      W_Product_Terms_Jackets_Cost_List =  self.Clothing_Sales_Revenue_Section(Product_Sales_File,Product_Section,Product_Materials,Product_Terms,i,Product_Sales_List,Product_Cost_List,Product_Price_List,W_Product_Terms_Tshirts_Sales_List,W_Product_Terms_Tshirts_Price_List,W_Product_Terms_Tshirts_Cost_List,W_Product_Terms_Jackets_Sales_List,W_Product_Terms_Jackets_Price_List,W_Product_Terms_Jackets_Cost_List,W_Product_Terms_Jeans_Sales_List,W_Product_Terms_Jeans_Price_List,W_Product_Terms_Jeans_Cost_List,M_Product_Terms_Tshirts_Sales_List,M_Product_Terms_Tshirts_Price_List,M_Product_Terms_Tshirts_Cost_List,M_Product_Terms_Jackets_Sales_List,M_Product_Terms_Jackets_Price_List,M_Product_Terms_Jackets_Cost_List,M_Product_Terms_Jeans_Sales_List,M_Product_Terms_Jeans_Price_List,M_Product_Terms_Jeans_Cost_List)[1][1];
      W_Product_Terms_Jeans_Cost_List = self.Clothing_Sales_Revenue_Section(Product_Sales_File,Product_Section,Product_Materials,Product_Terms,i,Product_Sales_List,Product_Cost_List,Product_Price_List,W_Product_Terms_Tshirts_Sales_List,W_Product_Terms_Tshirts_Price_List,W_Product_Terms_Tshirts_Cost_List,W_Product_Terms_Jackets_Sales_List,W_Product_Terms_Jackets_Price_List,W_Product_Terms_Jackets_Cost_List,W_Product_Terms_Jeans_Sales_List,W_Product_Terms_Jeans_Price_List,W_Product_Terms_Jeans_Cost_List,M_Product_Terms_Tshirts_Sales_List,M_Product_Terms_Tshirts_Price_List,M_Product_Terms_Tshirts_Cost_List,M_Product_Terms_Jackets_Sales_List,M_Product_Terms_Jackets_Price_List,M_Product_Terms_Jackets_Cost_List,M_Product_Terms_Jeans_Sales_List,M_Product_Terms_Jeans_Price_List,M_Product_Terms_Jeans_Cost_List)[1][2];
      M_Product_Terms_Tshirts_Cost_List = self.Clothing_Sales_Revenue_Section(Product_Sales_File,Product_Section,Product_Materials,Product_Terms,i,Product_Sales_List,Product_Cost_List,Product_Price_List,W_Product_Terms_Tshirts_Sales_List,W_Product_Terms_Tshirts_Price_List,W_Product_Terms_Tshirts_Cost_List,W_Product_Terms_Jackets_Sales_List,W_Product_Terms_Jackets_Price_List,W_Product_Terms_Jackets_Cost_List,W_Product_Terms_Jeans_Sales_List,W_Product_Terms_Jeans_Price_List,W_Product_Terms_Jeans_Cost_List,M_Product_Terms_Tshirts_Sales_List,M_Product_Terms_Tshirts_Price_List,M_Product_Terms_Tshirts_Cost_List,M_Product_Terms_Jackets_Sales_List,M_Product_Terms_Jackets_Price_List,M_Product_Terms_Jackets_Cost_List,M_Product_Terms_Jeans_Sales_List,M_Product_Terms_Jeans_Price_List,M_Product_Terms_Jeans_Cost_List)[1][3];
      M_Product_Terms_Jackets_Cost_List =  self.Clothing_Sales_Revenue_Section(Product_Sales_File,Product_Section,Product_Materials,Product_Terms,i,Product_Sales_List,Product_Cost_List,Product_Price_List,W_Product_Terms_Tshirts_Sales_List,W_Product_Terms_Tshirts_Price_List,W_Product_Terms_Tshirts_Cost_List,W_Product_Terms_Jackets_Sales_List,W_Product_Terms_Jackets_Price_List,W_Product_Terms_Jackets_Cost_List,W_Product_Terms_Jeans_Sales_List,W_Product_Terms_Jeans_Price_List,W_Product_Terms_Jeans_Cost_List,M_Product_Terms_Tshirts_Sales_List,M_Product_Terms_Tshirts_Price_List,M_Product_Terms_Tshirts_Cost_List,M_Product_Terms_Jackets_Sales_List,M_Product_Terms_Jackets_Price_List,M_Product_Terms_Jackets_Cost_List,M_Product_Terms_Jeans_Sales_List,M_Product_Terms_Jeans_Price_List,M_Product_Terms_Jeans_Cost_List)[1][4];
      M_Product_Terms_Jeans_Cost_List = self.Clothing_Sales_Revenue_Section(Product_Sales_File,Product_Section,Product_Materials,Product_Terms,i,Product_Sales_List,Product_Cost_List,Product_Price_List,W_Product_Terms_Tshirts_Sales_List,W_Product_Terms_Tshirts_Price_List,W_Product_Terms_Tshirts_Cost_List,W_Product_Terms_Jackets_Sales_List,W_Product_Terms_Jackets_Price_List,W_Product_Terms_Jackets_Cost_List,W_Product_Terms_Jeans_Sales_List,W_Product_Terms_Jeans_Price_List,W_Product_Terms_Jeans_Cost_List,M_Product_Terms_Tshirts_Sales_List,M_Product_Terms_Tshirts_Price_List,M_Product_Terms_Tshirts_Cost_List,M_Product_Terms_Jackets_Sales_List,M_Product_Terms_Jackets_Price_List,M_Product_Terms_Jackets_Cost_List,M_Product_Terms_Jeans_Sales_List,M_Product_Terms_Jeans_Price_List,M_Product_Terms_Jeans_Cost_List)[1][5];

      W_Product_Terms_Tshirts_Price_List = self.Clothing_Sales_Revenue_Section(Product_Sales_File,Product_Section,Product_Materials,Product_Terms,i,Product_Sales_List,Product_Cost_List,Product_Price_List,W_Product_Terms_Tshirts_Sales_List,W_Product_Terms_Tshirts_Price_List,W_Product_Terms_Tshirts_Cost_List,W_Product_Terms_Jackets_Sales_List,W_Product_Terms_Jackets_Price_List,W_Product_Terms_Jackets_Cost_List,W_Product_Terms_Jeans_Sales_List,W_Product_Terms_Jeans_Price_List,W_Product_Terms_Jeans_Cost_List,M_Product_Terms_Tshirts_Sales_List,M_Product_Terms_Tshirts_Price_List,M_Product_Terms_Tshirts_Cost_List,M_Product_Terms_Jackets_Sales_List,M_Product_Terms_Jackets_Price_List,M_Product_Terms_Jackets_Cost_List,M_Product_Terms_Jeans_Sales_List,M_Product_Terms_Jeans_Price_List,M_Product_Terms_Jeans_Cost_List)[2][0];
      W_Product_Terms_Jackets_Price_List =  self.Clothing_Sales_Revenue_Section(Product_Sales_File,Product_Section,Product_Materials,Product_Terms,i,Product_Sales_List,Product_Cost_List,Product_Price_List,W_Product_Terms_Tshirts_Sales_List,W_Product_Terms_Tshirts_Price_List,W_Product_Terms_Tshirts_Cost_List,W_Product_Terms_Jackets_Sales_List,W_Product_Terms_Jackets_Price_List,W_Product_Terms_Jackets_Cost_List,W_Product_Terms_Jeans_Sales_List,W_Product_Terms_Jeans_Price_List,W_Product_Terms_Jeans_Cost_List,M_Product_Terms_Tshirts_Sales_List,M_Product_Terms_Tshirts_Price_List,M_Product_Terms_Tshirts_Cost_List,M_Product_Terms_Jackets_Sales_List,M_Product_Terms_Jackets_Price_List,M_Product_Terms_Jackets_Cost_List,M_Product_Terms_Jeans_Sales_List,M_Product_Terms_Jeans_Price_List,M_Product_Terms_Jeans_Cost_List)[2][1];
      W_Product_Terms_Jeans_Price_List = self.Clothing_Sales_Revenue_Section(Product_Sales_File,Product_Section,Product_Materials,Product_Terms,i,Product_Sales_List,Product_Cost_List,Product_Price_List,W_Product_Terms_Tshirts_Sales_List,W_Product_Terms_Tshirts_Price_List,W_Product_Terms_Tshirts_Cost_List,W_Product_Terms_Jackets_Sales_List,W_Product_Terms_Jackets_Price_List,W_Product_Terms_Jackets_Cost_List,W_Product_Terms_Jeans_Sales_List,W_Product_Terms_Jeans_Price_List,W_Product_Terms_Jeans_Cost_List,M_Product_Terms_Tshirts_Sales_List,M_Product_Terms_Tshirts_Price_List,M_Product_Terms_Tshirts_Cost_List,M_Product_Terms_Jackets_Sales_List,M_Product_Terms_Jackets_Price_List,M_Product_Terms_Jackets_Cost_List,M_Product_Terms_Jeans_Sales_List,M_Product_Terms_Jeans_Price_List,M_Product_Terms_Jeans_Cost_List)[2][2];
      M_Product_Terms_Tshirts_Price_List = self.Clothing_Sales_Revenue_Section(Product_Sales_File,Product_Section,Product_Materials,Product_Terms,i,Product_Sales_List,Product_Cost_List,Product_Price_List,W_Product_Terms_Tshirts_Sales_List,W_Product_Terms_Tshirts_Price_List,W_Product_Terms_Tshirts_Cost_List,W_Product_Terms_Jackets_Sales_List,W_Product_Terms_Jackets_Price_List,W_Product_Terms_Jackets_Cost_List,W_Product_Terms_Jeans_Sales_List,W_Product_Terms_Jeans_Price_List,W_Product_Terms_Jeans_Cost_List,M_Product_Terms_Tshirts_Sales_List,M_Product_Terms_Tshirts_Price_List,M_Product_Terms_Tshirts_Cost_List,M_Product_Terms_Jackets_Sales_List,M_Product_Terms_Jackets_Price_List,M_Product_Terms_Jackets_Cost_List,M_Product_Terms_Jeans_Sales_List,M_Product_Terms_Jeans_Price_List,M_Product_Terms_Jeans_Cost_List)[2][3];
      M_Product_Terms_Jackets_Price_List =  self.Clothing_Sales_Revenue_Section(Product_Sales_File,Product_Section,Product_Materials,Product_Terms,i,Product_Sales_List,Product_Cost_List,Product_Price_List,W_Product_Terms_Tshirts_Sales_List,W_Product_Terms_Tshirts_Price_List,W_Product_Terms_Tshirts_Cost_List,W_Product_Terms_Jackets_Sales_List,W_Product_Terms_Jackets_Price_List,W_Product_Terms_Jackets_Cost_List,W_Product_Terms_Jeans_Sales_List,W_Product_Terms_Jeans_Price_List,W_Product_Terms_Jeans_Cost_List,M_Product_Terms_Tshirts_Sales_List,M_Product_Terms_Tshirts_Price_List,M_Product_Terms_Tshirts_Cost_List,M_Product_Terms_Jackets_Sales_List,M_Product_Terms_Jackets_Price_List,M_Product_Terms_Jackets_Cost_List,M_Product_Terms_Jeans_Sales_List,M_Product_Terms_Jeans_Price_List,M_Product_Terms_Jeans_Cost_List)[2][4];
      M_Product_Terms_Jeans_Price_List = self.Clothing_Sales_Revenue_Section(Product_Sales_File,Product_Section,Product_Materials,Product_Terms,i,Product_Sales_List,Product_Cost_List,Product_Price_List,W_Product_Terms_Tshirts_Sales_List,W_Product_Terms_Tshirts_Price_List,W_Product_Terms_Tshirts_Cost_List,W_Product_Terms_Jackets_Sales_List,W_Product_Terms_Jackets_Price_List,W_Product_Terms_Jackets_Cost_List,W_Product_Terms_Jeans_Sales_List,W_Product_Terms_Jeans_Price_List,W_Product_Terms_Jeans_Cost_List,M_Product_Terms_Tshirts_Sales_List,M_Product_Terms_Tshirts_Price_List,M_Product_Terms_Tshirts_Cost_List,M_Product_Terms_Jackets_Sales_List,M_Product_Terms_Jackets_Price_List,M_Product_Terms_Jackets_Cost_List,M_Product_Terms_Jeans_Sales_List,M_Product_Terms_Jeans_Price_List,M_Product_Terms_Jeans_Cost_List)[2][5];
      
      Section_List_Name = str(input("Enter the Sales List Name for Illustrating results of Sales and Revenue of specific Product attributes."));
      Price_List_Name = str(input("Enter the Sales List Name for Illustrating results of Sales and Revenue of specific Product attributes."));
      Cost_List_Name = str(input("Enter the Sales List Name for Illustrating results of Sales and Revenue of specific Product attributes."));
      
      Sales_List = [];
      Price_List = [];
      Cost_List = [];
      
      Sales_List = Section_List_Name;
      Price_List = Price_List_Name;
      Cost_List = Cost_List_Name;

      self.Scatter_Plot_Sales_Cost_Price(Sales_List,Price_List,Cost_List);      
      return(None);

Clothing_Sales_Revenue = Clothing_Sales_Revenue_Section_Impact();
