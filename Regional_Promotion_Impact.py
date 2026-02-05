import numpy as np;
import pandas as pd;
import matplotlib.pyplot as plt;
import Analyse_Business_Revenue as ABR;
import Even_Odd_Random_Number_Generator as eong;
import math;

class Regional_Promotion_Impact:

  def Region_Clothing_Sales(self,Product_Sales_File,Product_Sales_List,Product_Price_List,Product_Cost_List,Product_Sales_Argentina,Product_Sales_Bangladesh,Product_Sales_Brazil,Product_Sales_Cambodia,Product_Sales_China,Product_Sales_India,Product_Sales_Morocco,Product_Sales_Pakistan,Product_Sales_Portugal,Product_Sales_Spain,Product_Sales_Turkey,Product_Sales_Vietnam,Product_Price_Argentina,Product_Price_Bangladesh,Product_Price_Brazil,Product_Price_Cambodia,Product_Price_China,Product_Price_India,Product_Price_Morocco,Product_Price_Pakistan,Product_Price_Portugal,Product_Price_Spain,Product_Price_Turkey,Product_Price_Vietnam,Product_Cost_Argentina,Product_Cost_Bangladesh,Product_Cost_Brazil,Product_Cost_Cambodia,Product_Cost_China,Product_Cost_India,Product_Cost_Morocco,Product_Cost_Pakistan,Product_Cost_Portugal,Product_Cost_Spain,Product_Cost_Turkey,Product_Cost_Vietnam,i):   
      Product_ID = Product_Sales_File[0];
      Product_Promotion = Product_Sales_File[4];
      Product_Sales_Volume = Product_Sales_File[8];
      Product_Price = Product_Sales_File[10];
      Product_Origin = Product_Sales_File[15];
      #print(len(Product_Sales_Volume))

      Product_Cost_List = ABR.Analyse_Business_Revenue().Adjust_Product_Price(Product_Price,Product_Sales_Volume,Product_ID,i,Product_Cost_List);
      #ABR.__init__().Adjust_Product_Price(Product_Price,Product_Sales_Volume,Product_ID,i,Product_Cost_List);

      for i in range(len(Product_ID)):
         if(i < len(Product_ID) and Product_Origin[i] == 'Argentina' and Product_Promotion[i] == 'Yes'):
            Product_Sales_Argentina.append(Product_Sales_Volume[i]);
            Product_Cost_Argentina.append(Product_Cost_List[i]);
            Product_Price_Argentina.append(Product_Price[i]);
         elif(i < len(Product_ID) and Product_Origin[i] == 'Bangladesh' and Product_Promotion[i] == 'Yes'):
            Product_Sales_Bangladesh.append(Product_Sales_Volume[i]);
            Product_Cost_Bangladesh.append(Product_Cost_List[i]);
            Product_Price_Bangladesh.append(Product_Price[i]);
         elif(i < len(Product_ID) and Product_Origin[i] == 'Brazil' and Product_Promotion[i] == 'Yes'):
            Product_Sales_Brazil.append(Product_Sales_Volume[i]);
            Product_Cost_Brazil.append(Product_Cost_List[i]);
            Product_Price_Brazil.append(Product_Price[i]);
         elif(i < len(Product_ID) and Product_Origin[i] == 'Cambodia' and Product_Promotion[i] == 'Yes'):
            Product_Sales_Cambodia.append(Product_Sales_Volume[i]);
            Product_Cost_Cambodia.append(Product_Cost_List[i]);
            Product_Price_Cambodia.append(Product_Price[i]);
         elif(i < len(Product_ID) and Product_Origin[i] == 'China' and Product_Promotion[i] == 'Yes'):
            Product_Sales_China.append(Product_Sales_Volume[i]);
            Product_Cost_China.append(Product_Cost_List[i]);
            Product_Price_China.append(Product_Price[i]);
         elif(i < len(Product_ID) and Product_Origin[i] == 'India' and Product_Promotion[i] == 'Yes'):
            Product_Sales_India.append(Product_Sales_Volume[i]);
            Product_Cost_India.append(Product_Cost_List[i]);
            Product_Price_India.append(Product_Price[i]);
         elif(i < len(Product_ID) and Product_Origin[i] == 'Morocco' and Product_Promotion[i] == 'Yes'):
            Product_Sales_Morocco.append(Product_Sales_Volume[i]);
            Product_Cost_Morocco.append(Product_Cost_List[i]);
            Product_Price_Morocco.append(Product_Price[i]);
         elif(i < len(Product_ID) and Product_Origin[i] == 'Pakistan' and Product_Promotion[i] == 'Yes'):
            Product_Sales_Pakistan.append(Product_Sales_Volume[i]);
            Product_Cost_Pakistan.append(Product_Cost_List[i]);
            Product_Price_Pakistan.append(Product_Price[i]);
         elif(i < len(Product_ID) and Product_Origin[i] == 'Portugal' and Product_Promotion[i] == 'Yes'):
            Product_Sales_Portugal.append(Product_Sales_Volume[i]);
            Product_Cost_Portugal.append(Product_Cost_List[i]);
            Product_Price_Portugal.append(Product_Price[i]);
         elif(i < len(Product_ID) and Product_Origin[i] == 'Spain' and Product_Promotion[i] == 'Yes'):
            Product_Sales_Spain.append(Product_Sales_Volume[i]);
            Product_Cost_Spain.append(Product_Cost_List[i]);
            Product_Price_Spain.append(Product_Price[i]);
         elif(i < len(Product_ID) and Product_Origin[i] == 'Turkey' and Product_Promotion[i] == 'Yes'):
            Product_Sales_Turkey.append(Product_Sales_Volume[i]);
            Product_Cost_Turkey.append(Product_Cost_List[i]);
            Product_Price_Turkey.append(Product_Price[i]);
         elif(i < len(Product_ID) and Product_Origin[i] == 'Vietnam' and Product_Promotion[i] == 'Yes'):
            Product_Sales_Vietnam.append(Product_Sales_Volume[i]);
            Product_Cost_Vietnam.append(Product_Cost_List[i]);
            Product_Price_Vietnam.append(Product_Price[i]);
         elif(i == len(Product_ID)):

            print("Sales, Price and Cost List are computed and returned in the function.");
            break;
      #print(Product_Sales_Spain,"\n",Product_Cost_Spain,"\n",Product_Price_Spain);      
      Product_Sales_List = [Product_Sales_Volume,Product_Sales_Argentina,Product_Sales_Bangladesh,Product_Sales_Brazil,Product_Sales_Cambodia,Product_Sales_China,Product_Sales_India,Product_Sales_Morocco,Product_Sales_Pakistan,Product_Sales_Portugal,Product_Sales_Spain,Product_Sales_Turkey,Product_Sales_Vietnam]; 
      Product_Cost_List =  [Product_Cost_List,Product_Cost_Argentina,Product_Cost_Bangladesh,Product_Cost_Brazil,Product_Cost_Cambodia,Product_Cost_China,Product_Cost_India,Product_Cost_Morocco,Product_Cost_Pakistan,Product_Cost_Portugal,Product_Cost_Spain,Product_Cost_Turkey,Product_Cost_Vietnam];
      Product_Price_List = [Product_Price,Product_Price_Argentina,Product_Price_Bangladesh,Product_Price_Brazil,Product_Price_Cambodia,Product_Price_China,Product_Price_India,Product_Price_Morocco,Product_Price_Pakistan,Product_Price_Portugal,Product_Price_Spain,Product_Price_Turkey,Product_Price_Vietnam];
      return([Product_Sales_List,Product_Price_List,Product_Cost_List]);

   def Scatter_Plot_Sales_Price_Cost(self,Sales_List_Name,Price_List_Name,Cost_List_Name):

            break;
      #print(Product_Sales_Spain,"\n",Product_Cost_Spain,"\n",Product_Price_Spain);      
      Product_Sales_List = [Product_Sales_Argentina,Product_Sales_Bangladesh,Product_Sales_Brazil,Product_Sales_Cambodia,Product_Sales_China,Product_Sales_India,Product_Sales_Morocco,Product_Sales_Pakistan,Product_Sales_Portugal,Product_Sales_Spain,Product_Sales_Turkey,Product_Sales_Vietnam]; 
      Product_Cost_List =  [Product_Cost_Argentina,Product_Cost_Bangladesh,Product_Cost_Brazil,Product_Cost_Cambodia,Product_Cost_China,Product_Cost_India,Product_Cost_Morocco,Product_Cost_Pakistan,Product_Cost_Portugal,Product_Cost_Spain,Product_Cost_Turkey,Product_Cost_Vietnam];
      Product_Price_List = [Product_Price_Argentina,Product_Price_Bangladesh,Product_Price_Brazil,Product_Price_Cambodia,Product_Price_China,Product_Price_India,Product_Price_Morocco,Product_Price_Pakistan,Product_Price_Portugal,Product_Price_Spain,Product_Price_Turkey,Product_Price_Vietnam];
      return([Product_Sales_List,Product_Price_List,Product_Cost_List]);

   def Scatter_Plot_Sales_Price_Cost(Sales_List_Name,Price_List_Name,Cost_List_Name):
    
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
      Product_Regions = [];

      Product_Sales_Argentina = [];
      Product_Sales_Bangladesh = [];
      Product_Sales_Brazil = [];
      Product_Sales_Cambodia = [];
      Product_Sales_China = [];
      Product_Sales_India = [];
      Product_Sales_Morocco = [];
      Product_Sales_Pakistan = [];
      Product_Sales_Portugal = [];
      Product_Sales_Spain = [];
      Product_Sales_Turkey = [];
      Product_Sales_Vietnam = [];

      Product_Cost_Argentina = [];
      Product_Cost_Bangladesh = [];
      Product_Cost_Brazil = [];
      Product_Cost_Cambodia = [];
      Product_Cost_China = [];
      Product_Cost_India = [];
      Product_Cost_Morocco = [];
      Product_Cost_Pakistan = [];
      Product_Cost_Portugal = [];
      Product_Cost_Spain = [];
      Product_Cost_Turkey = [];
      Product_Cost_Vietnam = [];

      Product_Price_Argentina = [];
      Product_Price_Bangladesh = [];
      Product_Price_Brazil = [];
      Product_Price_Cambodia = [];
      Product_Price_China = [];
      Product_Price_India = [];
      Product_Price_Morocco = [];
      Product_Price_Pakistan = [];
      Product_Price_Portugal = [];
      Product_Price_Spain = [];
      Product_Price_Turkey = [];
      Product_Price_Vietnam = [];

      Product_Sales_List = self.Region_Clothing_Sales(Product_Sales_File,Product_Sales_List,Product_Price_List,Product_Cost_List,Product_Sales_Argentina,Product_Sales_Bangladesh,Product_Sales_Brazil,Product_Sales_Cambodia,Product_Sales_China,Product_Sales_India,Product_Sales_Morocco,Product_Sales_Pakistan,Product_Sales_Portugal,Product_Sales_Spain,Product_Sales_Turkey,Product_Sales_Vietnam,Product_Price_Argentina,Product_Price_Bangladesh,Product_Price_Brazil,Product_Price_Cambodia,Product_Price_China,Product_Price_India,Product_Price_Morocco,Product_Price_Pakistan,Product_Price_Portugal,Product_Price_Spain,Product_Price_Turkey,Product_Price_Vietnam,Product_Cost_Argentina,Product_Cost_Bangladesh,Product_Cost_Brazil,Product_Cost_Cambodia,Product_Cost_China,Product_Cost_India,Product_Cost_Morocco,Product_Cost_Pakistan,Product_Cost_Portugal,Product_Cost_Spain,Product_Cost_Turkey,Product_Cost_Vietnam,i)[0][0];
      Product_Sales_Argentina = self.Region_Clothing_Sales(Product_Sales_File,Product_Sales_List,Product_Price_List,Product_Cost_List,Product_Sales_Argentina,Product_Sales_Bangladesh,Product_Sales_Brazil,Product_Sales_Cambodia,Product_Sales_China,Product_Sales_India,Product_Sales_Morocco,Product_Sales_Pakistan,Product_Sales_Portugal,Product_Sales_Spain,Product_Sales_Turkey,Product_Sales_Vietnam,Product_Price_Argentina,Product_Price_Bangladesh,Product_Price_Brazil,Product_Price_Cambodia,Product_Price_China,Product_Price_India,Product_Price_Morocco,Product_Price_Pakistan,Product_Price_Portugal,Product_Price_Spain,Product_Price_Turkey,Product_Price_Vietnam,Product_Cost_Argentina,Product_Cost_Bangladesh,Product_Cost_Brazil,Product_Cost_Cambodia,Product_Cost_China,Product_Cost_India,Product_Cost_Morocco,Product_Cost_Pakistan,Product_Cost_Portugal,Product_Cost_Spain,Product_Cost_Turkey,Product_Cost_Vietnam,i)[0][1];
      Product_Sales_Bangladesh = self.Region_Clothing_Sales(Product_Sales_File,Product_Sales_List,Product_Price_List,Product_Cost_List,Product_Sales_Argentina,Product_Sales_Bangladesh,Product_Sales_Brazil,Product_Sales_Cambodia,Product_Sales_China,Product_Sales_India,Product_Sales_Morocco,Product_Sales_Pakistan,Product_Sales_Portugal,Product_Sales_Spain,Product_Sales_Turkey,Product_Sales_Vietnam,Product_Price_Argentina,Product_Price_Bangladesh,Product_Price_Brazil,Product_Price_Cambodia,Product_Price_China,Product_Price_India,Product_Price_Morocco,Product_Price_Pakistan,Product_Price_Portugal,Product_Price_Spain,Product_Price_Turkey,Product_Price_Vietnam,Product_Cost_Argentina,Product_Cost_Bangladesh,Product_Cost_Brazil,Product_Cost_Cambodia,Product_Cost_China,Product_Cost_India,Product_Cost_Morocco,Product_Cost_Pakistan,Product_Cost_Portugal,Product_Cost_Spain,Product_Cost_Turkey,Product_Cost_Vietnam,i)[0][2];
      Product_Sales_Brazil = self.Region_Clothing_Sales(Product_Sales_File,Product_Sales_List,Product_Price_List,Product_Cost_List,Product_Sales_Argentina,Product_Sales_Bangladesh,Product_Sales_Brazil,Product_Sales_Cambodia,Product_Sales_China,Product_Sales_India,Product_Sales_Morocco,Product_Sales_Pakistan,Product_Sales_Portugal,Product_Sales_Spain,Product_Sales_Turkey,Product_Sales_Vietnam,Product_Price_Argentina,Product_Price_Bangladesh,Product_Price_Brazil,Product_Price_Cambodia,Product_Price_China,Product_Price_India,Product_Price_Morocco,Product_Price_Pakistan,Product_Price_Portugal,Product_Price_Spain,Product_Price_Turkey,Product_Price_Vietnam,Product_Cost_Argentina,Product_Cost_Bangladesh,Product_Cost_Brazil,Product_Cost_Cambodia,Product_Cost_China,Product_Cost_India,Product_Cost_Morocco,Product_Cost_Pakistan,Product_Cost_Portugal,Product_Cost_Spain,Product_Cost_Turkey,Product_Cost_Vietnam,i)[0][3];
      Product_Sales_Cambodia = self.Region_Clothing_Sales(Product_Sales_File,Product_Sales_List,Product_Price_List,Product_Cost_List,Product_Sales_Argentina,Product_Sales_Bangladesh,Product_Sales_Brazil,Product_Sales_Cambodia,Product_Sales_China,Product_Sales_India,Product_Sales_Morocco,Product_Sales_Pakistan,Product_Sales_Portugal,Product_Sales_Spain,Product_Sales_Turkey,Product_Sales_Vietnam,Product_Price_Argentina,Product_Price_Bangladesh,Product_Price_Brazil,Product_Price_Cambodia,Product_Price_China,Product_Price_India,Product_Price_Morocco,Product_Price_Pakistan,Product_Price_Portugal,Product_Price_Spain,Product_Price_Turkey,Product_Price_Vietnam,Product_Cost_Argentina,Product_Cost_Bangladesh,Product_Cost_Brazil,Product_Cost_Cambodia,Product_Cost_China,Product_Cost_India,Product_Cost_Morocco,Product_Cost_Pakistan,Product_Cost_Portugal,Product_Cost_Spain,Product_Cost_Turkey,Product_Cost_Vietnam,i)[0][4];
      Product_Sales_China = self.Region_Clothing_Sales(Product_Sales_File,Product_Sales_List,Product_Price_List,Product_Cost_List,Product_Sales_Argentina,Product_Sales_Bangladesh,Product_Sales_Brazil,Product_Sales_Cambodia,Product_Sales_China,Product_Sales_India,Product_Sales_Morocco,Product_Sales_Pakistan,Product_Sales_Portugal,Product_Sales_Spain,Product_Sales_Turkey,Product_Sales_Vietnam,Product_Price_Argentina,Product_Price_Bangladesh,Product_Price_Brazil,Product_Price_Cambodia,Product_Price_China,Product_Price_India,Product_Price_Morocco,Product_Price_Pakistan,Product_Price_Portugal,Product_Price_Spain,Product_Price_Turkey,Product_Price_Vietnam,Product_Cost_Argentina,Product_Cost_Bangladesh,Product_Cost_Brazil,Product_Cost_Cambodia,Product_Cost_China,Product_Cost_India,Product_Cost_Morocco,Product_Cost_Pakistan,Product_Cost_Portugal,Product_Cost_Spain,Product_Cost_Turkey,Product_Cost_Vietnam,i)[0][5];
      Product_Sales_India = self.Region_Clothing_Sales(Product_Sales_File,Product_Sales_List,Product_Price_List,Product_Cost_List,Product_Sales_Argentina,Product_Sales_Bangladesh,Product_Sales_Brazil,Product_Sales_Cambodia,Product_Sales_China,Product_Sales_India,Product_Sales_Morocco,Product_Sales_Pakistan,Product_Sales_Portugal,Product_Sales_Spain,Product_Sales_Turkey,Product_Sales_Vietnam,Product_Price_Argentina,Product_Price_Bangladesh,Product_Price_Brazil,Product_Price_Cambodia,Product_Price_China,Product_Price_India,Product_Price_Morocco,Product_Price_Pakistan,Product_Price_Portugal,Product_Price_Spain,Product_Price_Turkey,Product_Price_Vietnam,Product_Cost_Argentina,Product_Cost_Bangladesh,Product_Cost_Brazil,Product_Cost_Cambodia,Product_Cost_China,Product_Cost_India,Product_Cost_Morocco,Product_Cost_Pakistan,Product_Cost_Portugal,Product_Cost_Spain,Product_Cost_Turkey,Product_Cost_Vietnam,i)[0][6];
      Product_Sales_Morocco = self.Region_Clothing_Sales(Product_Sales_File,Product_Sales_List,Product_Price_List,Product_Cost_List,Product_Sales_Argentina,Product_Sales_Bangladesh,Product_Sales_Brazil,Product_Sales_Cambodia,Product_Sales_China,Product_Sales_India,Product_Sales_Morocco,Product_Sales_Pakistan,Product_Sales_Portugal,Product_Sales_Spain,Product_Sales_Turkey,Product_Sales_Vietnam,Product_Price_Argentina,Product_Price_Bangladesh,Product_Price_Brazil,Product_Price_Cambodia,Product_Price_China,Product_Price_India,Product_Price_Morocco,Product_Price_Pakistan,Product_Price_Portugal,Product_Price_Spain,Product_Price_Turkey,Product_Price_Vietnam,Product_Cost_Argentina,Product_Cost_Bangladesh,Product_Cost_Brazil,Product_Cost_Cambodia,Product_Cost_China,Product_Cost_India,Product_Cost_Morocco,Product_Cost_Pakistan,Product_Cost_Portugal,Product_Cost_Spain,Product_Cost_Turkey,Product_Cost_Vietnam,i)[0][7];
      Product_Sales_Pakistan = self.Region_Clothing_Sales(Product_Sales_File,Product_Sales_List,Product_Price_List,Product_Cost_List,Product_Sales_Argentina,Product_Sales_Bangladesh,Product_Sales_Brazil,Product_Sales_Cambodia,Product_Sales_China,Product_Sales_India,Product_Sales_Morocco,Product_Sales_Pakistan,Product_Sales_Portugal,Product_Sales_Spain,Product_Sales_Turkey,Product_Sales_Vietnam,Product_Price_Argentina,Product_Price_Bangladesh,Product_Price_Brazil,Product_Price_Cambodia,Product_Price_China,Product_Price_India,Product_Price_Morocco,Product_Price_Pakistan,Product_Price_Portugal,Product_Price_Spain,Product_Price_Turkey,Product_Price_Vietnam,Product_Cost_Argentina,Product_Cost_Bangladesh,Product_Cost_Brazil,Product_Cost_Cambodia,Product_Cost_China,Product_Cost_India,Product_Cost_Morocco,Product_Cost_Pakistan,Product_Cost_Portugal,Product_Cost_Spain,Product_Cost_Turkey,Product_Cost_Vietnam,i)[0][8];
      Product_Sales_Portugal = self.Region_Clothing_Sales(Product_Sales_File,Product_Sales_List,Product_Price_List,Product_Cost_List,Product_Sales_Argentina,Product_Sales_Bangladesh,Product_Sales_Brazil,Product_Sales_Cambodia,Product_Sales_China,Product_Sales_India,Product_Sales_Morocco,Product_Sales_Pakistan,Product_Sales_Portugal,Product_Sales_Spain,Product_Sales_Turkey,Product_Sales_Vietnam,Product_Price_Argentina,Product_Price_Bangladesh,Product_Price_Brazil,Product_Price_Cambodia,Product_Price_China,Product_Price_India,Product_Price_Morocco,Product_Price_Pakistan,Product_Price_Portugal,Product_Price_Spain,Product_Price_Turkey,Product_Price_Vietnam,Product_Cost_Argentina,Product_Cost_Bangladesh,Product_Cost_Brazil,Product_Cost_Cambodia,Product_Cost_China,Product_Cost_India,Product_Cost_Morocco,Product_Cost_Pakistan,Product_Cost_Portugal,Product_Cost_Spain,Product_Cost_Turkey,Product_Cost_Vietnam,i)[0][9];
      Product_Sales_Spain = self.Region_Clothing_Sales(Product_Sales_File,Product_Sales_List,Product_Price_List,Product_Cost_List,Product_Sales_Argentina,Product_Sales_Bangladesh,Product_Sales_Brazil,Product_Sales_Cambodia,Product_Sales_China,Product_Sales_India,Product_Sales_Morocco,Product_Sales_Pakistan,Product_Sales_Portugal,Product_Sales_Spain,Product_Sales_Turkey,Product_Sales_Vietnam,Product_Price_Argentina,Product_Price_Bangladesh,Product_Price_Brazil,Product_Price_Cambodia,Product_Price_China,Product_Price_India,Product_Price_Morocco,Product_Price_Pakistan,Product_Price_Portugal,Product_Price_Spain,Product_Price_Turkey,Product_Price_Vietnam,Product_Cost_Argentina,Product_Cost_Bangladesh,Product_Cost_Brazil,Product_Cost_Cambodia,Product_Cost_China,Product_Cost_India,Product_Cost_Morocco,Product_Cost_Pakistan,Product_Cost_Portugal,Product_Cost_Spain,Product_Cost_Turkey,Product_Cost_Vietnam,i)[0][10];
      Product_Sales_Turkey = self.Region_Clothing_Sales(Product_Sales_File,Product_Sales_List,Product_Price_List,Product_Cost_List,Product_Sales_Argentina,Product_Sales_Bangladesh,Product_Sales_Brazil,Product_Sales_Cambodia,Product_Sales_China,Product_Sales_India,Product_Sales_Morocco,Product_Sales_Pakistan,Product_Sales_Portugal,Product_Sales_Spain,Product_Sales_Turkey,Product_Sales_Vietnam,Product_Price_Argentina,Product_Price_Bangladesh,Product_Price_Brazil,Product_Price_Cambodia,Product_Price_China,Product_Price_India,Product_Price_Morocco,Product_Price_Pakistan,Product_Price_Portugal,Product_Price_Spain,Product_Price_Turkey,Product_Price_Vietnam,Product_Cost_Argentina,Product_Cost_Bangladesh,Product_Cost_Brazil,Product_Cost_Cambodia,Product_Cost_China,Product_Cost_India,Product_Cost_Morocco,Product_Cost_Pakistan,Product_Cost_Portugal,Product_Cost_Spain,Product_Cost_Turkey,Product_Cost_Vietnam,i)[0][11];
      Product_Sales_Vietnam = self.Region_Clothing_Sales(Product_Sales_File,Product_Sales_List,Product_Price_List,Product_Cost_List,Product_Sales_Argentina,Product_Sales_Bangladesh,Product_Sales_Brazil,Product_Sales_Cambodia,Product_Sales_China,Product_Sales_India,Product_Sales_Morocco,Product_Sales_Pakistan,Product_Sales_Portugal,Product_Sales_Spain,Product_Sales_Turkey,Product_Sales_Vietnam,Product_Price_Argentina,Product_Price_Bangladesh,Product_Price_Brazil,Product_Price_Cambodia,Product_Price_China,Product_Price_India,Product_Price_Morocco,Product_Price_Pakistan,Product_Price_Portugal,Product_Price_Spain,Product_Price_Turkey,Product_Price_Vietnam,Product_Cost_Argentina,Product_Cost_Bangladesh,Product_Cost_Brazil,Product_Cost_Cambodia,Product_Cost_China,Product_Cost_India,Product_Cost_Morocco,Product_Cost_Pakistan,Product_Cost_Portugal,Product_Cost_Spain,Product_Cost_Turkey,Product_Cost_Vietnam,i)[0][12];

      Product_Price_List = self.Region_Clothing_Sales(Product_Sales_File,Product_Sales_List,Product_Price_List,Product_Cost_List,Product_Sales_Argentina,Product_Sales_Bangladesh,Product_Sales_Brazil,Product_Sales_Cambodia,Product_Sales_China,Product_Sales_India,Product_Sales_Morocco,Product_Sales_Pakistan,Product_Sales_Portugal,Product_Sales_Spain,Product_Sales_Turkey,Product_Sales_Vietnam,Product_Price_Argentina,Product_Price_Bangladesh,Product_Price_Brazil,Product_Price_Cambodia,Product_Price_China,Product_Price_India,Product_Price_Morocco,Product_Price_Pakistan,Product_Price_Portugal,Product_Price_Spain,Product_Price_Turkey,Product_Price_Vietnam,Product_Cost_Argentina,Product_Cost_Bangladesh,Product_Cost_Brazil,Product_Cost_Cambodia,Product_Cost_China,Product_Cost_India,Product_Cost_Morocco,Product_Cost_Pakistan,Product_Cost_Portugal,Product_Cost_Spain,Product_Cost_Turkey,Product_Cost_Vietnam,i)[1][0];
      Product_Price_Argentina = self.Region_Clothing_Sales(Product_Sales_File,Product_Sales_List,Product_Price_List,Product_Cost_List,Product_Sales_Argentina,Product_Sales_Bangladesh,Product_Sales_Brazil,Product_Sales_Cambodia,Product_Sales_China,Product_Sales_India,Product_Sales_Morocco,Product_Sales_Pakistan,Product_Sales_Portugal,Product_Sales_Spain,Product_Sales_Turkey,Product_Sales_Vietnam,Product_Price_Argentina,Product_Price_Bangladesh,Product_Price_Brazil,Product_Price_Cambodia,Product_Price_China,Product_Price_India,Product_Price_Morocco,Product_Price_Pakistan,Product_Price_Portugal,Product_Price_Spain,Product_Price_Turkey,Product_Price_Vietnam,Product_Cost_Argentina,Product_Cost_Bangladesh,Product_Cost_Brazil,Product_Cost_Cambodia,Product_Cost_China,Product_Cost_India,Product_Cost_Morocco,Product_Cost_Pakistan,Product_Cost_Portugal,Product_Cost_Spain,Product_Cost_Turkey,Product_Cost_Vietnam,i)[1][1];
      Product_Price_Bangladesh = self.Region_Clothing_Sales(Product_Sales_File,Product_Sales_List,Product_Price_List,Product_Cost_List,Product_Sales_Argentina,Product_Sales_Bangladesh,Product_Sales_Brazil,Product_Sales_Cambodia,Product_Sales_China,Product_Sales_India,Product_Sales_Morocco,Product_Sales_Pakistan,Product_Sales_Portugal,Product_Sales_Spain,Product_Sales_Turkey,Product_Sales_Vietnam,Product_Price_Argentina,Product_Price_Bangladesh,Product_Price_Brazil,Product_Price_Cambodia,Product_Price_China,Product_Price_India,Product_Price_Morocco,Product_Price_Pakistan,Product_Price_Portugal,Product_Price_Spain,Product_Price_Turkey,Product_Price_Vietnam,Product_Cost_Argentina,Product_Cost_Bangladesh,Product_Cost_Brazil,Product_Cost_Cambodia,Product_Cost_China,Product_Cost_India,Product_Cost_Morocco,Product_Cost_Pakistan,Product_Cost_Portugal,Product_Cost_Spain,Product_Cost_Turkey,Product_Cost_Vietnam,i)[1][2];
      Product_Price_Brazil = self.Region_Clothing_Sales(Product_Sales_File,Product_Sales_List,Product_Price_List,Product_Cost_List,Product_Sales_Argentina,Product_Sales_Bangladesh,Product_Sales_Brazil,Product_Sales_Cambodia,Product_Sales_China,Product_Sales_India,Product_Sales_Morocco,Product_Sales_Pakistan,Product_Sales_Portugal,Product_Sales_Spain,Product_Sales_Turkey,Product_Sales_Vietnam,Product_Price_Argentina,Product_Price_Bangladesh,Product_Price_Brazil,Product_Price_Cambodia,Product_Price_China,Product_Price_India,Product_Price_Morocco,Product_Price_Pakistan,Product_Price_Portugal,Product_Price_Spain,Product_Price_Turkey,Product_Price_Vietnam,Product_Cost_Argentina,Product_Cost_Bangladesh,Product_Cost_Brazil,Product_Cost_Cambodia,Product_Cost_China,Product_Cost_India,Product_Cost_Morocco,Product_Cost_Pakistan,Product_Cost_Portugal,Product_Cost_Spain,Product_Cost_Turkey,Product_Cost_Vietnam,i)[1][3];
      Product_Price_Cambodia = self.Region_Clothing_Sales(Product_Sales_File,Product_Sales_List,Product_Price_List,Product_Cost_List,Product_Sales_Argentina,Product_Sales_Bangladesh,Product_Sales_Brazil,Product_Sales_Cambodia,Product_Sales_China,Product_Sales_India,Product_Sales_Morocco,Product_Sales_Pakistan,Product_Sales_Portugal,Product_Sales_Spain,Product_Sales_Turkey,Product_Sales_Vietnam,Product_Price_Argentina,Product_Price_Bangladesh,Product_Price_Brazil,Product_Price_Cambodia,Product_Price_China,Product_Price_India,Product_Price_Morocco,Product_Price_Pakistan,Product_Price_Portugal,Product_Price_Spain,Product_Price_Turkey,Product_Price_Vietnam,Product_Cost_Argentina,Product_Cost_Bangladesh,Product_Cost_Brazil,Product_Cost_Cambodia,Product_Cost_China,Product_Cost_India,Product_Cost_Morocco,Product_Cost_Pakistan,Product_Cost_Portugal,Product_Cost_Spain,Product_Cost_Turkey,Product_Cost_Vietnam,i)[1][4];
      Product_Price_China = self.Region_Clothing_Sales(Product_Sales_File,Product_Sales_List,Product_Price_List,Product_Cost_List,Product_Sales_Argentina,Product_Sales_Bangladesh,Product_Sales_Brazil,Product_Sales_Cambodia,Product_Sales_China,Product_Sales_India,Product_Sales_Morocco,Product_Sales_Pakistan,Product_Sales_Portugal,Product_Sales_Spain,Product_Sales_Turkey,Product_Sales_Vietnam,Product_Price_Argentina,Product_Price_Bangladesh,Product_Price_Brazil,Product_Price_Cambodia,Product_Price_China,Product_Price_India,Product_Price_Morocco,Product_Price_Pakistan,Product_Price_Portugal,Product_Price_Spain,Product_Price_Turkey,Product_Price_Vietnam,Product_Cost_Argentina,Product_Cost_Bangladesh,Product_Cost_Brazil,Product_Cost_Cambodia,Product_Cost_China,Product_Cost_India,Product_Cost_Morocco,Product_Cost_Pakistan,Product_Cost_Portugal,Product_Cost_Spain,Product_Cost_Turkey,Product_Cost_Vietnam,i)[1][5];
      Product_Price_India = self.Region_Clothing_Sales(Product_Sales_File,Product_Sales_List,Product_Price_List,Product_Cost_List,Product_Sales_Argentina,Product_Sales_Bangladesh,Product_Sales_Brazil,Product_Sales_Cambodia,Product_Sales_China,Product_Sales_India,Product_Sales_Morocco,Product_Sales_Pakistan,Product_Sales_Portugal,Product_Sales_Spain,Product_Sales_Turkey,Product_Sales_Vietnam,Product_Price_Argentina,Product_Price_Bangladesh,Product_Price_Brazil,Product_Price_Cambodia,Product_Price_China,Product_Price_India,Product_Price_Morocco,Product_Price_Pakistan,Product_Price_Portugal,Product_Price_Spain,Product_Price_Turkey,Product_Price_Vietnam,Product_Cost_Argentina,Product_Cost_Bangladesh,Product_Cost_Brazil,Product_Cost_Cambodia,Product_Cost_China,Product_Cost_India,Product_Cost_Morocco,Product_Cost_Pakistan,Product_Cost_Portugal,Product_Cost_Spain,Product_Cost_Turkey,Product_Cost_Vietnam,i)[1][6];
      Product_Price_Morocco = self.Region_Clothing_Sales(Product_Sales_File,Product_Sales_List,Product_Price_List,Product_Cost_List,Product_Sales_Argentina,Product_Sales_Bangladesh,Product_Sales_Brazil,Product_Sales_Cambodia,Product_Sales_China,Product_Sales_India,Product_Sales_Morocco,Product_Sales_Pakistan,Product_Sales_Portugal,Product_Sales_Spain,Product_Sales_Turkey,Product_Sales_Vietnam,Product_Price_Argentina,Product_Price_Bangladesh,Product_Price_Brazil,Product_Price_Cambodia,Product_Price_China,Product_Price_India,Product_Price_Morocco,Product_Price_Pakistan,Product_Price_Portugal,Product_Price_Spain,Product_Price_Turkey,Product_Price_Vietnam,Product_Cost_Argentina,Product_Cost_Bangladesh,Product_Cost_Brazil,Product_Cost_Cambodia,Product_Cost_China,Product_Cost_India,Product_Cost_Morocco,Product_Cost_Pakistan,Product_Cost_Portugal,Product_Cost_Spain,Product_Cost_Turkey,Product_Cost_Vietnam,i)[1][7];
      Product_Price_Pakistan = self.Region_Clothing_Sales(Product_Sales_File,Product_Sales_List,Product_Price_List,Product_Cost_List,Product_Sales_Argentina,Product_Sales_Bangladesh,Product_Sales_Brazil,Product_Sales_Cambodia,Product_Sales_China,Product_Sales_India,Product_Sales_Morocco,Product_Sales_Pakistan,Product_Sales_Portugal,Product_Sales_Spain,Product_Sales_Turkey,Product_Sales_Vietnam,Product_Price_Argentina,Product_Price_Bangladesh,Product_Price_Brazil,Product_Price_Cambodia,Product_Price_China,Product_Price_India,Product_Price_Morocco,Product_Price_Pakistan,Product_Price_Portugal,Product_Price_Spain,Product_Price_Turkey,Product_Price_Vietnam,Product_Cost_Argentina,Product_Cost_Bangladesh,Product_Cost_Brazil,Product_Cost_Cambodia,Product_Cost_China,Product_Cost_India,Product_Cost_Morocco,Product_Cost_Pakistan,Product_Cost_Portugal,Product_Cost_Spain,Product_Cost_Turkey,Product_Cost_Vietnam,i)[1][8];
      Product_Price_Portugal = self.Region_Clothing_Sales(Product_Sales_File,Product_Sales_List,Product_Price_List,Product_Cost_List,Product_Sales_Argentina,Product_Sales_Bangladesh,Product_Sales_Brazil,Product_Sales_Cambodia,Product_Sales_China,Product_Sales_India,Product_Sales_Morocco,Product_Sales_Pakistan,Product_Sales_Portugal,Product_Sales_Spain,Product_Sales_Turkey,Product_Sales_Vietnam,Product_Price_Argentina,Product_Price_Bangladesh,Product_Price_Brazil,Product_Price_Cambodia,Product_Price_China,Product_Price_India,Product_Price_Morocco,Product_Price_Pakistan,Product_Price_Portugal,Product_Price_Spain,Product_Price_Turkey,Product_Price_Vietnam,Product_Cost_Argentina,Product_Cost_Bangladesh,Product_Cost_Brazil,Product_Cost_Cambodia,Product_Cost_China,Product_Cost_India,Product_Cost_Morocco,Product_Cost_Pakistan,Product_Cost_Portugal,Product_Cost_Spain,Product_Cost_Turkey,Product_Cost_Vietnam,i)[1][9];
      Product_Price_Spain = self.Region_Clothing_Sales(Product_Sales_File,Product_Sales_List,Product_Price_List,Product_Cost_List,Product_Sales_Argentina,Product_Sales_Bangladesh,Product_Sales_Brazil,Product_Sales_Cambodia,Product_Sales_China,Product_Sales_India,Product_Sales_Morocco,Product_Sales_Pakistan,Product_Sales_Portugal,Product_Sales_Spain,Product_Sales_Turkey,Product_Sales_Vietnam,Product_Price_Argentina,Product_Price_Bangladesh,Product_Price_Brazil,Product_Price_Cambodia,Product_Price_China,Product_Price_India,Product_Price_Morocco,Product_Price_Pakistan,Product_Price_Portugal,Product_Price_Spain,Product_Price_Turkey,Product_Price_Vietnam,Product_Cost_Argentina,Product_Cost_Bangladesh,Product_Cost_Brazil,Product_Cost_Cambodia,Product_Cost_China,Product_Cost_India,Product_Cost_Morocco,Product_Cost_Pakistan,Product_Cost_Portugal,Product_Cost_Spain,Product_Cost_Turkey,Product_Cost_Vietnam,i)[1][10];
      Product_Price_Turkey = self.Region_Clothing_Sales(Product_Sales_File,Product_Sales_List,Product_Price_List,Product_Cost_List,Product_Sales_Argentina,Product_Sales_Bangladesh,Product_Sales_Brazil,Product_Sales_Cambodia,Product_Sales_China,Product_Sales_India,Product_Sales_Morocco,Product_Sales_Pakistan,Product_Sales_Portugal,Product_Sales_Spain,Product_Sales_Turkey,Product_Sales_Vietnam,Product_Price_Argentina,Product_Price_Bangladesh,Product_Price_Brazil,Product_Price_Cambodia,Product_Price_China,Product_Price_India,Product_Price_Morocco,Product_Price_Pakistan,Product_Price_Portugal,Product_Price_Spain,Product_Price_Turkey,Product_Price_Vietnam,Product_Cost_Argentina,Product_Cost_Bangladesh,Product_Cost_Brazil,Product_Cost_Cambodia,Product_Cost_China,Product_Cost_India,Product_Cost_Morocco,Product_Cost_Pakistan,Product_Cost_Portugal,Product_Cost_Spain,Product_Cost_Turkey,Product_Cost_Vietnam,i)[1][11];
      Product_Price_Vietnam = self.Region_Clothing_Sales(Product_Sales_File,Product_Sales_List,Product_Price_List,Product_Cost_List,Product_Sales_Argentina,Product_Sales_Bangladesh,Product_Sales_Brazil,Product_Sales_Cambodia,Product_Sales_China,Product_Sales_India,Product_Sales_Morocco,Product_Sales_Pakistan,Product_Sales_Portugal,Product_Sales_Spain,Product_Sales_Turkey,Product_Sales_Vietnam,Product_Price_Argentina,Product_Price_Bangladesh,Product_Price_Brazil,Product_Price_Cambodia,Product_Price_China,Product_Price_India,Product_Price_Morocco,Product_Price_Pakistan,Product_Price_Portugal,Product_Price_Spain,Product_Price_Turkey,Product_Price_Vietnam,Product_Cost_Argentina,Product_Cost_Bangladesh,Product_Cost_Brazil,Product_Cost_Cambodia,Product_Cost_China,Product_Cost_India,Product_Cost_Morocco,Product_Cost_Pakistan,Product_Cost_Portugal,Product_Cost_Spain,Product_Cost_Turkey,Product_Cost_Vietnam,i)[1][12];

      Product_Cost_List = self.Region_Clothing_Sales(Product_Sales_File,Product_Sales_List,Product_Price_List,Product_Cost_List,Product_Sales_Argentina,Product_Sales_Bangladesh,Product_Sales_Brazil,Product_Sales_Cambodia,Product_Sales_China,Product_Sales_India,Product_Sales_Morocco,Product_Sales_Pakistan,Product_Sales_Portugal,Product_Sales_Spain,Product_Sales_Turkey,Product_Sales_Vietnam,Product_Price_Argentina,Product_Price_Bangladesh,Product_Price_Brazil,Product_Price_Cambodia,Product_Price_China,Product_Price_India,Product_Price_Morocco,Product_Price_Pakistan,Product_Price_Portugal,Product_Price_Spain,Product_Price_Turkey,Product_Price_Vietnam,Product_Cost_Argentina,Product_Cost_Bangladesh,Product_Cost_Brazil,Product_Cost_Cambodia,Product_Cost_China,Product_Cost_India,Product_Cost_Morocco,Product_Cost_Pakistan,Product_Cost_Portugal,Product_Cost_Spain,Product_Cost_Turkey,Product_Cost_Vietnam,i)[2][0];
      Product_Cost_Argentina = self.Region_Clothing_Sales(Product_Sales_File,Product_Sales_List,Product_Price_List,Product_Cost_List,Product_Sales_Argentina,Product_Sales_Bangladesh,Product_Sales_Brazil,Product_Sales_Cambodia,Product_Sales_China,Product_Sales_India,Product_Sales_Morocco,Product_Sales_Pakistan,Product_Sales_Portugal,Product_Sales_Spain,Product_Sales_Turkey,Product_Sales_Vietnam,Product_Price_Argentina,Product_Price_Bangladesh,Product_Price_Brazil,Product_Price_Cambodia,Product_Price_China,Product_Price_India,Product_Price_Morocco,Product_Price_Pakistan,Product_Price_Portugal,Product_Price_Spain,Product_Price_Turkey,Product_Price_Vietnam,Product_Cost_Argentina,Product_Cost_Bangladesh,Product_Cost_Brazil,Product_Cost_Cambodia,Product_Cost_China,Product_Cost_India,Product_Cost_Morocco,Product_Cost_Pakistan,Product_Cost_Portugal,Product_Cost_Spain,Product_Cost_Turkey,Product_Cost_Vietnam,i)[2][1];
      Product_Cost_Bangladesh = self.Region_Clothing_Sales(Product_Sales_File,Product_Sales_List,Product_Price_List,Product_Cost_List,Product_Sales_Argentina,Product_Sales_Bangladesh,Product_Sales_Brazil,Product_Sales_Cambodia,Product_Sales_China,Product_Sales_India,Product_Sales_Morocco,Product_Sales_Pakistan,Product_Sales_Portugal,Product_Sales_Spain,Product_Sales_Turkey,Product_Sales_Vietnam,Product_Price_Argentina,Product_Price_Bangladesh,Product_Price_Brazil,Product_Price_Cambodia,Product_Price_China,Product_Price_India,Product_Price_Morocco,Product_Price_Pakistan,Product_Price_Portugal,Product_Price_Spain,Product_Price_Turkey,Product_Price_Vietnam,Product_Cost_Argentina,Product_Cost_Bangladesh,Product_Cost_Brazil,Product_Cost_Cambodia,Product_Cost_China,Product_Cost_India,Product_Cost_Morocco,Product_Cost_Pakistan,Product_Cost_Portugal,Product_Cost_Spain,Product_Cost_Turkey,Product_Cost_Vietnam,i)[2][2];
      Product_Cost_Brazil = self.Region_Clothing_Sales(Product_Sales_File,Product_Sales_List,Product_Price_List,Product_Cost_List,Product_Sales_Argentina,Product_Sales_Bangladesh,Product_Sales_Brazil,Product_Sales_Cambodia,Product_Sales_China,Product_Sales_India,Product_Sales_Morocco,Product_Sales_Pakistan,Product_Sales_Portugal,Product_Sales_Spain,Product_Sales_Turkey,Product_Sales_Vietnam,Product_Price_Argentina,Product_Price_Bangladesh,Product_Price_Brazil,Product_Price_Cambodia,Product_Price_China,Product_Price_India,Product_Price_Morocco,Product_Price_Pakistan,Product_Price_Portugal,Product_Price_Spain,Product_Price_Turkey,Product_Price_Vietnam,Product_Cost_Argentina,Product_Cost_Bangladesh,Product_Cost_Brazil,Product_Cost_Cambodia,Product_Cost_China,Product_Cost_India,Product_Cost_Morocco,Product_Cost_Pakistan,Product_Cost_Portugal,Product_Cost_Spain,Product_Cost_Turkey,Product_Cost_Vietnam,i)[2][3];
      Product_Cost_Cambodia = self.Region_Clothing_Sales(Product_Sales_File,Product_Sales_List,Product_Price_List,Product_Cost_List,Product_Sales_Argentina,Product_Sales_Bangladesh,Product_Sales_Brazil,Product_Sales_Cambodia,Product_Sales_China,Product_Sales_India,Product_Sales_Morocco,Product_Sales_Pakistan,Product_Sales_Portugal,Product_Sales_Spain,Product_Sales_Turkey,Product_Sales_Vietnam,Product_Price_Argentina,Product_Price_Bangladesh,Product_Price_Brazil,Product_Price_Cambodia,Product_Price_China,Product_Price_India,Product_Price_Morocco,Product_Price_Pakistan,Product_Price_Portugal,Product_Price_Spain,Product_Price_Turkey,Product_Price_Vietnam,Product_Cost_Argentina,Product_Cost_Bangladesh,Product_Cost_Brazil,Product_Cost_Cambodia,Product_Cost_China,Product_Cost_India,Product_Cost_Morocco,Product_Cost_Pakistan,Product_Cost_Portugal,Product_Cost_Spain,Product_Cost_Turkey,Product_Cost_Vietnam,i)[2][4];
      Product_Cost_China = self.Region_Clothing_Sales(Product_Sales_File,Product_Sales_List,Product_Price_List,Product_Cost_List,Product_Sales_Argentina,Product_Sales_Bangladesh,Product_Sales_Brazil,Product_Sales_Cambodia,Product_Sales_China,Product_Sales_India,Product_Sales_Morocco,Product_Sales_Pakistan,Product_Sales_Portugal,Product_Sales_Spain,Product_Sales_Turkey,Product_Sales_Vietnam,Product_Price_Argentina,Product_Price_Bangladesh,Product_Price_Brazil,Product_Price_Cambodia,Product_Price_China,Product_Price_India,Product_Price_Morocco,Product_Price_Pakistan,Product_Price_Portugal,Product_Price_Spain,Product_Price_Turkey,Product_Price_Vietnam,Product_Cost_Argentina,Product_Cost_Bangladesh,Product_Cost_Brazil,Product_Cost_Cambodia,Product_Cost_China,Product_Cost_India,Product_Cost_Morocco,Product_Cost_Pakistan,Product_Cost_Portugal,Product_Cost_Spain,Product_Cost_Turkey,Product_Cost_Vietnam,i)[2][5];
      Product_Cost_India = self.Region_Clothing_Sales(Product_Sales_File,Product_Sales_List,Product_Price_List,Product_Cost_List,Product_Sales_Argentina,Product_Sales_Bangladesh,Product_Sales_Brazil,Product_Sales_Cambodia,Product_Sales_China,Product_Sales_India,Product_Sales_Morocco,Product_Sales_Pakistan,Product_Sales_Portugal,Product_Sales_Spain,Product_Sales_Turkey,Product_Sales_Vietnam,Product_Price_Argentina,Product_Price_Bangladesh,Product_Price_Brazil,Product_Price_Cambodia,Product_Price_China,Product_Price_India,Product_Price_Morocco,Product_Price_Pakistan,Product_Price_Portugal,Product_Price_Spain,Product_Price_Turkey,Product_Price_Vietnam,Product_Cost_Argentina,Product_Cost_Bangladesh,Product_Cost_Brazil,Product_Cost_Cambodia,Product_Cost_China,Product_Cost_India,Product_Cost_Morocco,Product_Cost_Pakistan,Product_Cost_Portugal,Product_Cost_Spain,Product_Cost_Turkey,Product_Cost_Vietnam,i)[2][6];
      Product_Cost_Morocco = self.Region_Clothing_Sales(Product_Sales_File,Product_Sales_List,Product_Price_List,Product_Cost_List,Product_Sales_Argentina,Product_Sales_Bangladesh,Product_Sales_Brazil,Product_Sales_Cambodia,Product_Sales_China,Product_Sales_India,Product_Sales_Morocco,Product_Sales_Pakistan,Product_Sales_Portugal,Product_Sales_Spain,Product_Sales_Turkey,Product_Sales_Vietnam,Product_Price_Argentina,Product_Price_Bangladesh,Product_Price_Brazil,Product_Price_Cambodia,Product_Price_China,Product_Price_India,Product_Price_Morocco,Product_Price_Pakistan,Product_Price_Portugal,Product_Price_Spain,Product_Price_Turkey,Product_Price_Vietnam,Product_Cost_Argentina,Product_Cost_Bangladesh,Product_Cost_Brazil,Product_Cost_Cambodia,Product_Cost_China,Product_Cost_India,Product_Cost_Morocco,Product_Cost_Pakistan,Product_Cost_Portugal,Product_Cost_Spain,Product_Cost_Turkey,Product_Cost_Vietnam,i)[2][7];
      Product_Cost_Pakistan = self.Region_Clothing_Sales(Product_Sales_File,Product_Sales_List,Product_Price_List,Product_Cost_List,Product_Sales_Argentina,Product_Sales_Bangladesh,Product_Sales_Brazil,Product_Sales_Cambodia,Product_Sales_China,Product_Sales_India,Product_Sales_Morocco,Product_Sales_Pakistan,Product_Sales_Portugal,Product_Sales_Spain,Product_Sales_Turkey,Product_Sales_Vietnam,Product_Price_Argentina,Product_Price_Bangladesh,Product_Price_Brazil,Product_Price_Cambodia,Product_Price_China,Product_Price_India,Product_Price_Morocco,Product_Price_Pakistan,Product_Price_Portugal,Product_Price_Spain,Product_Price_Turkey,Product_Price_Vietnam,Product_Cost_Argentina,Product_Cost_Bangladesh,Product_Cost_Brazil,Product_Cost_Cambodia,Product_Cost_China,Product_Cost_India,Product_Cost_Morocco,Product_Cost_Pakistan,Product_Cost_Portugal,Product_Cost_Spain,Product_Cost_Turkey,Product_Cost_Vietnam,i)[2][8];
      Product_Cost_Portugal = self.Region_Clothing_Sales(Product_Sales_File,Product_Sales_List,Product_Price_List,Product_Cost_List,Product_Sales_Argentina,Product_Sales_Bangladesh,Product_Sales_Brazil,Product_Sales_Cambodia,Product_Sales_China,Product_Sales_India,Product_Sales_Morocco,Product_Sales_Pakistan,Product_Sales_Portugal,Product_Sales_Spain,Product_Sales_Turkey,Product_Sales_Vietnam,Product_Price_Argentina,Product_Price_Bangladesh,Product_Price_Brazil,Product_Price_Cambodia,Product_Price_China,Product_Price_India,Product_Price_Morocco,Product_Price_Pakistan,Product_Price_Portugal,Product_Price_Spain,Product_Price_Turkey,Product_Price_Vietnam,Product_Cost_Argentina,Product_Cost_Bangladesh,Product_Cost_Brazil,Product_Cost_Cambodia,Product_Cost_China,Product_Cost_India,Product_Cost_Morocco,Product_Cost_Pakistan,Product_Cost_Portugal,Product_Cost_Spain,Product_Cost_Turkey,Product_Cost_Vietnam,i)[2][9];
      Product_Cost_Spain = self.Region_Clothing_Sales(Product_Sales_File,Product_Sales_List,Product_Price_List,Product_Cost_List,Product_Sales_Argentina,Product_Sales_Bangladesh,Product_Sales_Brazil,Product_Sales_Cambodia,Product_Sales_China,Product_Sales_India,Product_Sales_Morocco,Product_Sales_Pakistan,Product_Sales_Portugal,Product_Sales_Spain,Product_Sales_Turkey,Product_Sales_Vietnam,Product_Price_Argentina,Product_Price_Bangladesh,Product_Price_Brazil,Product_Price_Cambodia,Product_Price_China,Product_Price_India,Product_Price_Morocco,Product_Price_Pakistan,Product_Price_Portugal,Product_Price_Spain,Product_Price_Turkey,Product_Price_Vietnam,Product_Cost_Argentina,Product_Cost_Bangladesh,Product_Cost_Brazil,Product_Cost_Cambodia,Product_Cost_China,Product_Cost_India,Product_Cost_Morocco,Product_Cost_Pakistan,Product_Cost_Portugal,Product_Cost_Spain,Product_Cost_Turkey,Product_Cost_Vietnam,i)[2][10];
      Product_Cost_Turkey = self.Region_Clothing_Sales(Product_Sales_File,Product_Sales_List,Product_Price_List,Product_Cost_List,Product_Sales_Argentina,Product_Sales_Bangladesh,Product_Sales_Brazil,Product_Sales_Cambodia,Product_Sales_China,Product_Sales_India,Product_Sales_Morocco,Product_Sales_Pakistan,Product_Sales_Portugal,Product_Sales_Spain,Product_Sales_Turkey,Product_Sales_Vietnam,Product_Price_Argentina,Product_Price_Bangladesh,Product_Price_Brazil,Product_Price_Cambodia,Product_Price_China,Product_Price_India,Product_Price_Morocco,Product_Price_Pakistan,Product_Price_Portugal,Product_Price_Spain,Product_Price_Turkey,Product_Price_Vietnam,Product_Cost_Argentina,Product_Cost_Bangladesh,Product_Cost_Brazil,Product_Cost_Cambodia,Product_Cost_China,Product_Cost_India,Product_Cost_Morocco,Product_Cost_Pakistan,Product_Cost_Portugal,Product_Cost_Spain,Product_Cost_Turkey,Product_Cost_Vietnam,i)[2][11];
      Product_Cost_Vietnam = self.Region_Clothing_Sales(Product_Sales_File,Product_Sales_List,Product_Price_List,Product_Cost_List,Product_Sales_Argentina,Product_Sales_Bangladesh,Product_Sales_Brazil,Product_Sales_Cambodia,Product_Sales_China,Product_Sales_India,Product_Sales_Morocco,Product_Sales_Pakistan,Product_Sales_Portugal,Product_Sales_Spain,Product_Sales_Turkey,Product_Sales_Vietnam,Product_Price_Argentina,Product_Price_Bangladesh,Product_Price_Brazil,Product_Price_Cambodia,Product_Price_China,Product_Price_India,Product_Price_Morocco,Product_Price_Pakistan,Product_Price_Portugal,Product_Price_Spain,Product_Price_Turkey,Product_Price_Vietnam,Product_Cost_Argentina,Product_Cost_Bangladesh,Product_Cost_Brazil,Product_Cost_Cambodia,Product_Cost_China,Product_Cost_India,Product_Cost_Morocco,Product_Cost_Pakistan,Product_Cost_Portugal,Product_Cost_Spain,Product_Cost_Turkey,Product_Cost_Vietnam,i)[2][12];

      Country_Name = str(input("Enter the Country name for sending Arguments to the Definition of Plotting Sales, Price and Cost of the Clothing products."));
      Sales_List_Country = [];
      Price_List_Country = [];
      Cost_List_Country = [];

      if(Country_Name == 'Argentina'):
         Sales_List_Country = Product_Sales_Argentina;        
         Price_List_Country = Product_Price_Argentina;
         Cost_List_Country = Product_Cost_Argentina;
         self.Scatter_Plot_Sales_Price_Cost(Sales_List_Country,Price_List_Country,Cost_List_Country);
      elif(Country_Name == 'Bangladesh'):
         Sales_List_Country = Product_Sales_Bangladesh;        
         Price_List_Country = Product_Price_Bangladesh;
         Cost_List_Country = Product_Cost_Bangladesh;
         self.Scatter_Plot_Sales_Price_Cost(Sales_List_Country,Price_List_Country,Cost_List_Country);
      elif(Country_Name == 'Brazil'):
         Sales_List_Country = Product_Sales_Brazil;        
         Price_List_Country = Product_Price_Brazil;
         Cost_List_Country = Product_Cost_Brazil;
         self.Scatter_Plot_Sales_Price_Cost(Sales_List_Country,Price_List_Country,Cost_List_Country);
      elif(Country_Name == 'Cambodia'):
         Sales_List_Country = Product_Sales_Cambodia;        
         Price_List_Country = Product_Price_Cambodia;
         Cost_List_Country = Product_Cost_Cambodia;
         self.Scatter_Plot_Sales_Price_Cost(Sales_List_Country,Price_List_Country,Cost_List_Country);
      elif(Country_Name == 'China'):
         Sales_List_Country = Product_Sales_China;        
         Price_List_Country = Product_Price_China;
         Cost_List_Country = Product_Cost_China;
         self.Scatter_Plot_Sales_Price_Cost(Sales_List_Country,Price_List_Country,Cost_List_Country);
      elif(Country_Name == 'India'):
         Sales_List_Country = Product_Sales_India;        
         Price_List_Country = Product_Price_India;
         Cost_List_Country = Product_Cost_India;
         self.Scatter_Plot_Sales_Price_Cost(Sales_List_Country,Price_List_Country,Cost_List_Country);
      elif(Country_Name == 'Morocco'):
         Sales_List_Country = Product_Sales_Morocco;        
         Price_List_Country = Product_Price_Morocco;
         Cost_List_Country = Product_Cost_Morocco;
         self.Scatter_Plot_Sales_Price_Cost(Sales_List_Country,Price_List_Country,Cost_List_Country);
      elif(Country_Name == 'Pakistan'):
         Sales_List_Country = Product_Sales_Pakistan;        
         Price_List_Country = Product_Price_Pakistan;
         Cost_List_Country = Product_Cost_Pakistan;
         self.Scatter_Plot_Sales_Price_Cost(Sales_List_Country,Price_List_Country,Cost_List_Country);
      elif(Country_Name == 'Portugal'):
         Sales_List_Country = Product_Sales_Portugal;        
         Price_List_Country = Product_Price_Portugal;
         Cost_List_Country = Product_Cost_Portugal;
         self.Scatter_Plot_Sales_Price_Cost(Sales_List_Country,Price_List_Country,Cost_List_Country);
      elif(Country_Name == 'Spain'):
         Sales_List_Country = Product_Sales_Spain;        
         Price_List_Country = Product_Price_Spain;
         Cost_List_Country = Product_Cost_Spain;
         self.Scatter_Plot_Sales_Price_Cost(Sales_List_Country,Price_List_Country,Cost_List_Country);
      elif(Country_Name == 'Turkey'):
         Sales_List_Country = Product_Sales_Turkey;        
         Price_List_Country = Product_Price_Turkey;
         Cost_List_Country = Product_Cost_Turkey;
         self.Scatter_Plot_Sales_Price_Cost(Sales_List_Country,Price_List_Country,Cost_List_Country);
      elif(Country_Name == 'Vietnam'):
         Sales_List_Country = Product_Sales_Vietnam;        
         Price_List_Country = Product_Price_Vietnam;
         Cost_List_Country = Product_Cost_Vietnam;
         self.Scatter_Plot_Sales_Price_Cost(Sales_List_Country,Price_List_Country,Cost_List_Country);
      else:
         print("The above Diagram illustrates the Regression behaviour between Sales, Revenue and Price of Products.");
      return(None);
Region_Promotion_Imp = Regional_Promotion_Impact();