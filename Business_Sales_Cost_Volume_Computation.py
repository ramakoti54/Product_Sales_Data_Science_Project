# The file is in progress to build for Future reference Follow the process changes are required to update dynamic components. If needed to execute and compile contact me on my email or Github commentary. Strictly prohibited for external
# usecases unless it is verified and modified by the Senior Developers and Architect reviews.
import numpy as np;
import pandas as pd;
import math;
import matplotlib.pyplot as plt;
import Analyse_Business_Revenue as ABR;

class Business_Sales_Cost_Volume_Computation:
   def Business_Sales_Cost_Volume_Compute(self,Data_File,Product_Sales,Product_Cost,i):
      Product_ID = Data_File[0];
      Product_Name = Data_File[1];
      Product_Description = Data_File[2];
      Product_Terms = Data_File[3];
      Product_Promotion = Data_File[3];
      Product_Position = Data_File[4];
      Product_URL = Data_File[5];
      Product_Category = Data_File[6];
      Product_Sales_Volume = Data_File[7];
      Product_Section = Data_File[8];
      Product_Price = Data_File[9];
      Product_Seasonal = Data_File[10];
      Product_Season = Data_File[11];
      Product_Currency = Data_File[12];
      Product_Material = Data_File[13];
      Product_Origin = Data_File[14];
      Product_Brand = Data_File[15];

      for i in range(len(Product_ID)):
         if((i < len(Product_ID)) and (Product_Promotion[i] =='Yes') and (Product_Origin[i] == 'India' or Product_Origin[i] == 'Spain' or Product_Origin[i] == 'China') and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Silk' or Product_Material[i] == 'Cotton') and (Product_Section == 'WOMAN')):
            Product_Sales.append(Product_Sales_Volume[i]);
            Product_Cost.append(Product_Price[i]);
            i = i + 1;
            self.Business_Sales_Cost_Volume_Compute(Data_File,Product_Sales[i:],Product_Cost[i:],i);
         elif(i <= len(Product_ID)):
            i = i +1;
            self.Business_Sales_Cost_Volume_Compute(Data_File,Product_Sales[i:],Product_Cost[i:],i);
         else:
            print("Product Sales value and Amount in Dollars:",Product_Sales,Product_Cost);
            return([Product_Sales,Product_Cost]);
         print("Product Sales Value and Amount in Dollars:",Product_Sales,Product_Cost);
      return([Product_Sales,Product_Cost]);

   def Product_Sales_Cost_Compute(self,Product_Sales_Computation,Product_Cost_Computation,Porduct_Sales_Number,Product_Cost_Dollars):
      Product_Sales_Number = int(np.sum(Product_Sales_Computation));
      Product_Cost_Dollars = float(np.sum(Product_Cost_Computation));
      return([Product_Sales_Number,Product_Cost_Dollars]);

   def Product_Section_Compute(self,Product_Section,Product_Sales_Volume,Product_Section_Output,Product_Section_Man,Product_Section_Woman,i):
      if(i < len(Product_Section)):
         if(Product_Section[i] == 'MAN'):
            Product_Section_Output.append(Product_Sales_Volume[i]);
            i = i+1;
            Product_Section_Man = np.sum(Product_Section_Output);
            self.Product_Section_Compute(Product_Section,Product_Sales_Volume,Product_Section_Output[i:],Product_Section_Man,Product_Section_Woman,i);
         elif(Product_Section[i] == 'WOMAN'):
            Product_Section_Output.append(Product_Sales_Volume[i]);
            i = i+1;
            Product_Section_Woman = np.sum(Product_Section_Output);
            self.Product_Section_Compute(Product_Section,Product_Sales_Volume,Product_Section_Output[i:],Product_Section_Man,Product_Section_Woman,i);
      elif(i== len(Product_Section)):
         i = i+1;
         self.Product_Section_Compute(Product_Section,Product_Sales_Volume,Product_Section_Output[i:],Product_Section_Man,Product_Section_Woman,i);
      else:
         return([Product_Section_Man,Product_Section_Woman]);
      return([Product_Section_Man,Product_Section_Woman]);

   def Product_Position_Compute(self,Product_Position,Product_Sales_Volume,Product_Position_Output,Product_Position_Aisle,Product_Position_Front_Of_Store,Product_Position_End_Cap,i):
      if(i < len(Product_Position)):
         if(Product_Position[i] == 'Aisle'):
            Product_Position_Output.append(Product_Sales_Volume[i]);
            i = i+1;
            Product_Position_Aisle = np.sum(Product_Position_Output);
            self.Product_Position_Compute(Product_Position,Product_Sales_Volume,Product_Position_Output[i:],Product_Position_Aisle[i:],Product_Front_Of_Store[i:],Product_Position_End_Cap[i:],i);
         elif(Product_Position[i] == 'Front_Of_Store'):
            Product_Position_Output.append(Product_Sales_Volume[i]);
            i = i+1;
            Product_Position_Front_Of_Store = np.sum(Product_Position_Output);
            self.Product_Position_Compute(Product_Position,Product_Sales_Volume,Product_Position_Output[i:],Product_Position_Aisle[i:],Product_Front_Of_Store[i:],Product_Position_End_Cap[i:],i);
         elif(Product_Position[i] == 'End-Cap'):
            Product_Position_Output.append(Product_Sales_Volume[i]);
            i = i+1;
            Product_Position_End_Cap = np.sum(Product_Position_Output);
            self.Product_Position_Compute(Product_Position,Product_Sales_Volume,Product_Position_Output[i:],Product_Position_Aisle[i:],Product_Front_Of_Store[i:],Product_Position_End_Cap[i:],i);
      elif(i == len(Product_Position)):
         i = i+1;
         self.Product_Position_Compute(Product_Position,Product_Sales_Volume,Product_Position_Output[i:],Product_Position_Aisle[i:],Product_Front_Of_Store[i:],Product_Position_End_Cap[i:],i);
      else:
         return([Product_Position_Aisle,Product_Position_Front_Of_Store,Product_Position_End_Cap]);
      return([Product_Position_Aisle,Product_Position_Front_Of_Store,Product_Position_End_Cap]);

   def Product_Season_Compute(self,Product_Season,Product_Sales_Volume,Product_Season_Output,Product_Season_Winter,Product_Season_Autumn,Product_Season_Summar,Product_Season_Spring,i):
      if(i < len(Product_Season)):
         if(Product_Season[i] == 'Winter'):
            Product_Season_Output.append(Product_Sales_Volume[i]);
            i = i+1;
            Product_Season_Winter = np.sum(Product_Season_Output);
            self.Product_Season_Compute(Product_Season,Product_Sales_Volume,Product_Season_Output[i:],Product_Season_Winter,Product_Season_Autumn,Product_Season_Summar,Product_Season_Spring,i);
         elif(Product_Season[i] == 'Autumn'):
            Product_Season_Output.append(Product_Sales_Volume[i]);
            i = i+1;
            Product_Season_Autumn = np.sum(Product_Season_Output);
            self.Product_Season_Compute(Product_Season,Product_Sales_Volume,Product_Season_Output[i:],Product_Season_Winter,Product_Season_Autumn,Product_Season_Summar,Product_Season_Spring,i);
         elif(Product_Season[i] == 'Summar'):
            Product_Season_Output.append(Product_Sales_Volume[i]);
            i = i+1;
            Product_Season_Summar = np.sum(Product_Season_Output);
            self.Product_Season_Compute(Product_Season,Product_Sales_Volume,Product_Season_Output[i:],Product_Season_Winter,Product_Season_Autumn,Product_Season_Summar,Product_Season_Spring,i);
         elif(Product_Season[i] == 'Spring'):
            Product_Season_Output.append(Product_Sales_Volume[i]);
            i = i+1;
            Product_Season_Spring = np.sum(Product_Season_Output);
            self.Product_Season_Compute(Product_Season,Product_Sales_Volume,Product_Season_Output[i:],Product_Season_Winter,Product_Season_Autumn,Product_Season_Summar,Product_Season_Spring,i);
      elif(i == len(Product_Season)):
         i = i+1;
         self.Product_Season_Compute(Product_Season,Product_Sales_Volume,Product_Season_Output[i:],Product_Season_Winter,Product_Season_Autumn,Product_Season_Summar,Product_Season_Spring,i);
      else:
         return([Product_Season_Winter,Product_Season_Autumn,Product_Season_Summar,Product_Season_Spring]);
      return([Product_Season_Winter,Product_Season_Autumn,Product_Season_Summar,Product_Season_Spring]);

   def Product_Material_Compute(self,Product_Material,Product_Sales_Volume,Product_Material_Output,Product_Material_Wool,Product_Material_Wool_Blend,Product_Material_Linen,Product_Material_Linen_Blend,Product_Material_Cotton,Product_Material_Silk,Product_Material_Viscose,Product_Material_Denim,Product_Material_Acrylic,Product_Material_Polyester):
      if(i < len(Product_Material)):
         if(Product_Material[i] == 'Wool'):
            Product_Material_Output.append(Product_Sales_Volume[i]);
            i = i+1;
            Product_Material_Wool = float(math.round(np.sum(Product_Material_Output),2));
            self.Product_Material_Compute(Product_Material,Product_Sales_Volume,Product_Material_Output[i:],Product_Material_Wool,Product_Material_Wool_Blend,Product_Material_Linen,Product_Material_Linen_Blend,Product_Material_Cotton,Product_Material_Silk,Product_Material_Viscose,Product_Material_Denim,Product_Material_Acrylic,Product_Material_Polyester);
         elif(Product_Material[i] == 'Wool Blend'):
            Product_Material_Output.append(Product_Sales_Volume[i]);
            i = i+1;
            Product_Material_Wool_Blend = float(math.round(np.sum(Product_Material_Output),2));
            self.Product_Material_Compute(Product_Material,Product_Sales_Volume,Product_Material_Output[i:],Product_Material_Wool,Product_Material_Wool_Blend,Product_Material_Linen,Product_Material_Linen_Blend,Product_Material_Cotton,Product_Material_Silk,Product_Material_Viscose,Product_Material_Denim,Product_Material_Acrylic,Product_Material_Polyester);
         elif(Product_Material[i] == 'Linen'):
            Product_Material_Output.append(Product_Sales_Volume[i]);
            i = i+1;
            Product_Material_Linen = float(math.round(np.sum(Product_Material_Output),2));
            self.Product_Material_Compute(Product_Material,Product_Sales_Volume,Product_Material_Output[i:],Product_Material_Wool,Product_Material_Wool_Blend,Product_Material_Linen,Product_Material_Linen_Blend,Product_Material_Cotton,Product_Material_Silk,Product_Material_Viscose,Product_Material_Denim,Product_Material_Acrylic,Product_Material_Polyester);
         elif(Product_Material[i] == 'Linen Blend'):
            Product_Material_Output.append(Product_Sales_Volume[i]);
            i = i+1;
            Product_Material_Linen_Blend = float(math.round(np.sum(Product_Material_Output),2));
            self.Product_Material_Compute(Product_Material,Product_Sales_Volume,Product_Material_Output[i:],Product_Material_Wool,Product_Material_Wool_Blend,Product_Material_Linen,Product_Material_Linen_Blend,Product_Material_Cotton,Product_Material_Silk,Product_Material_Viscose,Product_Material_Denim,Product_Material_Acrylic,Product_Material_Polyester);
         elif(Product_Material[i] == 'Cotton'):
            Product_Material_Output.append(Product_Sales_Volume[i]);
            i = i+1;
            Product_Material_Cotton = float(math.round(np.sum(Product_Material_Output),2));
            self.Product_Material_Compute(Product_Material,Product_Sales_Volume,Product_Material_Output[i:],Product_Material_Wool,Product_Material_Wool_Blend,Product_Material_Linen,Product_Material_Linen_Blend,Product_Material_Cotton,Product_Material_Silk,Product_Material_Viscose,Product_Material_Denim,Product_Material_Acrylic,Product_Material_Polyester);
         elif(Product_Material[i] == 'Silk'):
            Product_Material_Output.append(Product_Sales_Volume[i]);
            i = i+1;
            Product_Material_Silk = float(math.round(np.sum(Product_Material_Output),2));
            self.Product_Material_Compute(Product_Material,Product_Sales_Volume,Product_Material_Output[i:],Product_Material_Wool,Product_Material_Wool_Blend,Product_Material_Linen,Product_Material_Linen_Blend,Product_Material_Cotton,Product_Material_Silk,Product_Material_Viscose,Product_Material_Denim,Product_Material_Acrylic,Product_Material_Polyester);
         elif(Product_Material[i] == 'Viscose'):
            Product_Material_Output.append(Product_Sales_Volume[i]);
            i = i+1;
            Product_Material_Viscose = float(math.round(np.sum(Product_Material_Output),2));
            self.Product_Material_Compute(Product_Material,Product_Sales_Volume,Product_Material_Output[i:],Product_Material_Wool,Product_Material_Wool_Blend,Product_Material_Linen,Product_Material_Linen_Blend,Product_Material_Cotton,Product_Material_Silk,Product_Material_Viscose,Product_Material_Denim,Product_Material_Acrylic,Product_Material_Polyester);
         elif(Product_Material[i] == 'Polyester'):
            Product_Material_Output.append(Product_Sales_Volume[i]);
            i = i+1;
            Product_Material_Polyester = float(math.round(np.sum(Product_Material_Output),2));
            self.Product_Material_Compute(Product_Material,Product_Sales_Volume,Product_Material_Output[i:],Product_Material_Wool,Product_Material_Wool_Blend,Product_Material_Linen,Product_Material_Linen_Blend,Product_Material_Cotton,Product_Material_Silk,Product_Material_Viscose,Product_Material_Denim,Product_Material_Acrylic,Product_Material_Polyester);
         elif(Product_Material[i] == 'Acrylic'):
            Product_Material_Output.append(Product_Sales_Volume[i]);
            i = i+1;
            Product_Material_Acrylic = float(math.round(np.sum(Product_Material_Output),2));
            self.Product_Material_Compute(Product_Material,Product_Sales_Volume,Product_Material_Output[i:],Product_Material_Wool,Product_Material_Wool_Blend,Product_Material_Linen,Product_Material_Linen_Blend,Product_Material_Cotton,Product_Material_Silk,Product_Material_Viscose,Product_Material_Denim,Product_Material_Acrylic,Product_Material_Polyester);
         elif(Product_Material[i] == 'Denim'):
            Product_Material_Output.append(Product_Sales_Volume[i]);
            i = i+1;
            Product_Material_Denim = float(math.round(np.sum(Product_Material_Output),2));
            self.Product_Material_Compute(Product_Material,Product_Sales_Volume,Product_Material_Output[i:],Product_Material_Wool,Product_Material_Wool_Blend,Product_Material_Linen,Product_Material_Linen_Blend,Product_Material_Cotton,Product_Material_Silk,Product_Material_Viscose,Product_Material_Denim,Product_Material_Acrylic,Product_Material_Polyester);
      elif(i == len(Product_Material)):
         i = i+1;
         self.Product_Material_Compute(Product_Material,Product_Sales_Volume,Product_Material_Output[i:],Product_Material_Wool,Product_Material_Wool_Blend,Product_Material_Linen,Product_Material_Linen_Blend,Product_Material_Cotton,Product_Material_Silk,Product_Material_Viscose,Product_Material_Denim,Product_Material_Acrylic,Product_Material_Polyester);
      else:
         return([Product_Material_Wool,Product_Material_Wool_Blend,Product_Material_Linen,Product_Material_Linen_Blend,Product_Material_Cotton,Product_Material_Silk,Product_Material_Viscose,Product_Material_Polyester,Product_Material_Acrylic,Product_Material_Denim]);

      return([Product_Material_Wool,Product_Material_Wool_Blend,Product_Material_Linen,Product_Material_Linen_Blend,Product_Material_Cotton,Product_Material_Silk,Product_Material_Viscose,Product_Material_Polyester,Product_Material_Acrylic,Product_Material_Denim]);

   def Product_Origin_Compute(self,Product_Origin,Product_Sales_Volume,Product_Origin_Output,Product_Origin_Argentina,Product_Origin_Bangladesh,Product_Origin_Brazil,Product_Origin_Cambodia,Product_Origin_China,Product_Origin_India,Product_Origin_Moraco,Product_Origin_Pakistan,Product_Origin_Portugal,Product_Origin_Spain,Origin_Turkey,Product_Origin_Vietnam):
      if(i < len(Product_Origin)):
         if(Product_Origin[i] == 'Argentina'):
            Product_Origin_Output.append(Product_Sales_Volume[i]);
            i = i+1;
            self.Product_Origin_Compute(Product_Origin,Product_Sales_Volume,Product_Origin_Output[i:],Product_Origin_Argentina,Product_Origin_Bangladesh,Product_Origin_Brazil,Product_Origin_Cambodia,Product_Origin_China,Product_Origin_India,Product_Origin_Moraco,Product_Origin_Pakistan,Product_Origin_Portugal,Product_Origin_Spain,Origin_Turkey,Product_Origin_Vietnam);
         elif(Product_Origin[i] == 'Bangladesh'):
            Product_Origin_Output.append(Product_Sales_Volume[i]);
            i = i+1;
            self.Product_Origin_Compute(Product_Origin,Product_Sales_Volume,Product_Origin_Output[i:],Product_Origin_Argentina,Product_Origin_Bangladesh,Product_Origin_Brazil,Product_Origin_Cambodia,Product_Origin_China,Product_Origin_India,Product_Origin_Moraco,Product_Origin_Pakistan,Product_Origin_Portugal,Product_Origin_Spain,Origin_Turkey,Product_Origin_Vietnam);
         elif(Product_Origin[i] == 'Brazil'):
            Product_Origin_Output.append(Product_Sales_Volume[i]);
            i = i+1;
            self.Product_Origin_Compute(Product_Origin,Product_Sales_Volume,Product_Origin_Output[i:],Product_Origin_Argentina,Product_Origin_Bangladesh,Product_Origin_Brazil,Product_Origin_Cambodia,Product_Origin_China,Product_Origin_India,Product_Origin_Moraco,Product_Origin_Pakistan,Product_Origin_Portugal,Product_Origin_Spain,Origin_Turkey,Product_Origin_Vietnam);
         elif(Product_Origin[i] == 'Cambodia'):
            Product_Origin_Output.append(Product_Sales_Volume[i]);
            i = i+1;
            self.Product_Origin_Compute(Product_Origin,Product_Sales_Volume,Product_Origin_Output[i:],Product_Origin_Argentina,Product_Origin_Bangladesh,Product_Origin_Brazil,Product_Origin_Cambodia,Product_Origin_China,Product_Origin_India,Product_Origin_Moraco,Product_Origin_Pakistan,Product_Origin_Portugal,Product_Origin_Spain,Origin_Turkey,Product_Origin_Vietnam);
         elif(Product_Origin[i] == 'China'):
            Product_Origin_Output.append(Product_Sales_Volume[i]);
            i = i+1;
            self.Product_Origin_Compute(Product_Origin,Product_Sales_Volume,Product_Origin_Output[i:],Product_Origin_Argentina,Product_Origin_Bangladesh,Product_Origin_Brazil,Product_Origin_Cambodia,Product_Origin_China,Product_Origin_India,Product_Origin_Moraco,Product_Origin_Pakistan,Product_Origin_Portugal,Product_Origin_Spain,Origin_Turkey,Product_Origin_Vietnam);
         elif(Product_Origin[i] == 'India'):
            Product_Origin_Output.append(Product_Sales_Volume[i]);
            i = i+1;
            self.Product_Origin_Compute(Product_Origin,Product_Sales_Volume,Product_Origin_Output[i:],Product_Origin_Argentina,Product_Origin_Bangladesh,Product_Origin_Brazil,Product_Origin_Cambodia,Product_Origin_China,Product_Origin_India,Product_Origin_Moraco,Product_Origin_Pakistan,Product_Origin_Portugal,Product_Origin_Spain,Origin_Turkey,Product_Origin_Vietnam);
         elif(Product_Origin[i] == 'Moracco'):
            Product_Origin_Output.append(Product_Sales_Volume[i]);
            i = i+1;
            self.Product_Origin_Compute(Product_Origin,Product_Sales_Volume,Product_Origin_Output[i:],Product_Origin_Argentina,Product_Origin_Bangladesh,Product_Origin_Brazil,Product_Origin_Cambodia,Product_Origin_China,Product_Origin_India,Product_Origin_Moraco,Product_Origin_Pakistan,Product_Origin_Portugal,Product_Origin_Spain,Origin_Turkey,Product_Origin_Vietnam);
         elif(Product_Origin[i] == 'Pakistan'):
            Product_Origin_Output.append(Product_Sales_Volume[i]);
            i = i+1;
            self.Product_Origin_Compute(Product_Origin,Product_Sales_Volume,Product_Origin_Output[i:],Product_Origin_Argentina,Product_Origin_Bangladesh,Product_Origin_Brazil,Product_Origin_Cambodia,Product_Origin_China,Product_Origin_India,Product_Origin_Moraco,Product_Origin_Pakistan,Product_Origin_Portugal,Product_Origin_Spain,Origin_Turkey,Product_Origin_Vietnam);
         elif(Product_Origin[i] == 'Portugal'):
            Product_Origin_Output.append(Product_Sales_Volume[i]);
            i = i+1;
            self.Product_Origin_Compute(Product_Origin,Product_Sales_Volume,Product_Origin_Output[i:],Product_Origin_Argentina,Product_Origin_Bangladesh,Product_Origin_Brazil,Product_Origin_Cambodia,Product_Origin_China,Product_Origin_India,Product_Origin_Moraco,Product_Origin_Pakistan,Product_Origin_Portugal,Product_Origin_Spain,Origin_Turkey,Product_Origin_Vietnam);
         elif(Product_Origin[i] == 'Spain'):
            Product_Origin_Output.append(Product_Sales_Volume[i]);
            i = i+1;
            self.Product_Origin_Compute(Product_Origin,Product_Sales_Volume,Product_Origin_Output[i:],Product_Origin_Argentina,Product_Origin_Bangladesh,Product_Origin_Brazil,Product_Origin_Cambodia,Product_Origin_China,Product_Origin_India,Product_Origin_Moraco,Product_Origin_Pakistan,Product_Origin_Portugal,Product_Origin_Spain,Origin_Turkey,Product_Origin_Vietnam);
         elif(Product_Origin[i] == 'Turkey'):
            Product_Origin_Output.append(Product_Sales_Volume[i]);
            i = i+1;
            self.Product_Origin_Compute(Product_Origin,Product_Sales_Volume,Product_Origin_Output[i:],Product_Origin_Argentina,Product_Origin_Bangladesh,Product_Origin_Brazil,Product_Origin_Cambodia,Product_Origin_China,Product_Origin_India,Product_Origin_Moraco,Product_Origin_Pakistan,Product_Origin_Portugal,Product_Origin_Spain,Origin_Turkey,Product_Origin_Vietnam);
         elif(Product_Origin[i] == 'Vietnam'):
            Product_Origin_Output.append(Product_Sales_Volume[i]);
            i = i+1;
            self.Product_Origin_Compute(Product_Origin,Product_Sales_Volume,Product_Origin_Output[i:],Product_Origin_Argentina,Product_Origin_Bangladesh,Product_Origin_Brazil,Product_Origin_Cambodia,Product_Origin_China,Product_Origin_India,Product_Origin_Moraco,Product_Origin_Pakistan,Product_Origin_Portugal,Product_Origin_Spain,Origin_Turkey,Product_Origin_Vietnam);
      elif(i == len(Product_Origin)):
         i = i+1;
         self.Product_Origin_Compute(Product_Origin,Product_Sales_Volume,Product_Origin_Output[i:],Product_Origin_Argentina,Product_Origin_Bangladesh,Product_Origin_Brazil,Product_Origin_Cambodia,Product_Origin_China,Product_Origin_India,Product_Origin_Moraco,Product_Origin_Pakistan,Product_Origin_Portugal,Product_Origin_Spain,Origin_Turkey,Product_Origin_Vietnam);
      else:
         return([Product_Origin_Argentina,Product_Origin_Bangladesh,Product_Origin_Brazil,Product_Origin_Cambodia,Product_Origin_China,Product_Origin_India,Product_Origin_Moraco,Product_Origin_Pakistan,Product_Origin_Portugal,Product_Origin_Spain,Origin_Turkey,Product_Origin_Vietnam]);
      return([Product_Origin_Argentina,Product_Origin_Bangladesh,Product_Origin_Brazil,Product_Origin_Cambodia,Product_Origin_China,Product_Origin_India,Product_Origin_Moraco,Product_Origin_Pakistan,Product_Origin_Portugal,Product_Origin_Spain,Origin_Turkey,Product_Origin_Vietnam]);

   def Pie_Chart_Visuals(self,Product_Section_Output,Product_Position_Output,Product_Season_Output,Product_Material_Output,Product_Origin_Output):
      #Pie chart styles to update the gallery with nogrid.
      plt.style.use('_mpl-gallery-nogrid')
      # make data
      x = Product_Section_Output; #[1, 2, 3, 4]
      x = Product_Season_Output;
      x = Product_Position_Output;
      x = Product_Material_Output;
      x = Product_Origin_Output;
      # Plot colour addition to shell pie charts.
      colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len(x)))
      # ploting
      fig, ax = plt.subplots()
      ax.pie(x, colors=colors, radius=3, center=(6, 6),
      wedgeprops={"linewidth": 1, "edgecolor": "green"}, frame=True)
      ax.set(xlim=(0, 12), xticks=np.arange(1, 12),
      ylim=(0, 12), yticks=np.arange(1, 12))
      plt.show()
      return(None);

   def __Init__(self):
      Product_Sales = pd.read_csv('/content/Product_Sales/Business_sales_EDA.csv',delimiter=';');
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
      i = 0;
      Product_Sales_Computation = [];
      Product_Cost_Computation = [];
      Product_Sales_Number = 0;
      Product_Cost_Dollars = 0.0;
      Product_Sales_Cost_Output = [];
      Product_Sales_Model_Output = [];
      Product_Sales_Train = Product_Sales_Volume[:20000];
      Product_Sales_Test =  Product_Sales_Volume[20001:];

      Product_Train_Data = [];
      Product_Test_Data  = [];
      Product_Section_Output = [];
      Product_Section_Man = 0.0;
      Product_Section_Woman = 0.0;
      Product_Position_Aisle = 0.0;
      Product_Postion_Front_Of_Store = 0.0;
      Product_Postion_End_Cap = 0.0;
      Product_Postion_Output = [];
      Product_Season_Winter = 0.0;
      Product_Season_Autumn = 0.0;
      Product_Season_Summar = 0.0;
      Product_Season_Spring = 0.0;
      Product_Season_Output = [];
      Product_Material_Wool = 0.0;
      Product_Material_Wool_Blend = 0.0;
      Product_Material_Linen = 0.0;
      Product_Material_Linen_Blend = 0.0;
      Product_Material_Cotton = 0.0;
      Product_Material_Silk = 0.0;
      Product_Material_Polyester = 0.0;
      Product_Material_Denim = 0.0;
      Product_Material_Acrylic = 0.0;
      Product_Material_Viscose = 0.0;
      Product_Material_Output = [];
      Product_Origin_Argentina = 0.0;
      Product_Origin_Bangladesh = 0.0;
      Product_Origin_Brazil = 0.0;
      Product_Origin_Cambodia = 0.0;
      Product_Origin_China = 0.0;
      Product_India = 0.0;
      Product_Origin_Moracco = 0.0;
      Product_Origin_Pakistan = 0.0;
      Product_Origin_Portugal = 0.0;
      Product_Origin_Spain = 0.0;
      Product_Origin_Turkey = 0.0;
      Product_Origin_Vietnam = 0.0;
      Product_Origin_Output = [];
      Product_Train_Sample = pd.dataframe(Product_Sales_Train,Product_Cost_Train);
      Product_Train_Mean = 0.0;
      Product_Train_Std = 0.0;
      Product_Cost_List = [];
      Product_Cost = [];

      Product_Cost_List = ABR.__init__().Adjust_Product_Price(Product_Price,Product_Sales_Volume,Product_ID,i,Product_Cost);
      
      Product_Cost_Train = Product_Cost[:20000];
      Product_Cost_Test =  Product_Cost[20001:];      

      Product_Sales_Computation.append(self.Business_Sales_Cost_Volume_Compute(Product_Sales_File,Product_Sales_List,Product_Cost_List,i))[0];
      Product_Cost_Computation.append(self.Business_Sales_Cost_Volume_Compute(Product_Sales_File,Product_Sales_List,Product_Cost_List,i))[1];
      #Product_Sales_Computation = Product_Sales_Cost_Output[0];
      #Product_Cost_Computation  =  Product_Sales_Cost_Output[1];
      Product_Sales_Number = self.Product_Sales_Cost_Compute(Product_Sales_Computation,Product_Cost_Computation,Product_Sales_Number,Product_Cost_Dollars);
      Product_Cost_Dollars  = self.Product_Sales_Cost_Compute(Product_Sales_Computation,Product_Cost_Computation,Product_Sales_Number,Product_Cost_Dollars);
      Product_Section_Output = self.Product_Section_Compute(Product_Section,Product_Sales_Volume,Product_Section_Output,Product_Section_Man,Product_Section_Woman,i);
      Product_Section_Man = Product_Section_Output[0];
      Product_Section_Woman = Product_Section_Output[1];
      Product_Position_Output = self.Product_Position_Compute(Product_Position,Product_Sales_Volume,Product_Position_Output,Product_Position_Aisle,Product_Position_Front_Of_Store,Product_Position_End_Cap,i);
      Product_Position_Aisle = Product_Position_Output[0];
      Product_Postion_Front_Of_Store = Product_Position_Output[1];
      Product_Postion_End_Cap = Product_Position_Output[2];

      Product_Season_Output = self.Product_Season_Compute(Product_Season,Product_Sales_Volume,Product_Season_Output,Product_Season_Winter,Product_Season_Autumn,Product_Season_Summar,Product_Season_Spring,i);
      Product_Season_Winter = Product_Season_Output[0];
      Product_Season_Autumn = Product_Season_Output[1];
      Product_Season_Summar = Product_Season_Output[2];
      Product_Season_Spring = Product_Season_Output[3];

      Product_Material_Output = self.Product_Material_Compute(Product_Material,Product_Sales_Volume,Product_Material_Output,Product_Material_Wool,Product_Material_Wool_Blend,Product_Material_Linen,Product_Material_Linen_Blend,Product_Material_Cotton,Product_Material_Silk,Product_Material_Viscose,Product_Material_Denim,Product_Material_Acrylic,Product_Material_Polyester);
      Product_Material_Wool = Product_Material_Output[0];
      Product_Material_Wool_Blend = Product_Material_Output[1];
      Product_Material_Linen = Product_Material_Output[2];
      Product_Material_Linen_Blend = Product_Material_Output[3];
      Product_Material_Cotton = Product_Material_Output[4];
      Product_Material_Silk = Product_Material_Output[5];
      Product_Material_Polyester = Product_Material_Output[7];
      Product_Material_Denim = Product_Material_Output[9];
      Product_Material_Acrylic = Product_Material_Output[8];
      Product_Material_Viscose = Product_Material_Output[6];

      Product_Origin_Output = self.Product_Origin_Compute(Product_Origin,Product_Sales_Volume,Product_Origin_Output,Product_Origin_Argentina,Product_Origin_Bangladesh,Product_Origin_Brazil,Product_Origin_Cambodia,Product_Origin_China,Product_Origin_India,Product_Origin_Moracco,Product_Origin_Pakistan,Product_Origin_Portugal,Product_Origin_Spain,Product_Origin_Turkey,Product_Origin_Vietnam);
      Product_Origin_Argentina = Product_Origin_Output[0];
      Product_Origin_Bangladesh = Product_Origin_Output[1];
      Product_Origin_Brazil = Product_Origin_Output[2];
      Product_Origin_Cambodia = Product_Origin_Output[3];
      Product_Origin_China = Product_Origin_Output[4];
      Product_India = Product_Origin_Output[5];
      Product_Origin_Moracco = Product_Origin_Output[6];
      Product_Origin_Pakistan = Product_Origin_Output[7];
      Product_Origin_Portugal = Product_Origin_Output[8];
      Product_Origin_Spain = Product_Origin_Output[9];
      Product_Origin_Turkey = Product_Origin_Output[10];
      Product_Origin_Vietnam = Product_Origin_Output[11];

      #ABR.__init__().Pie_Chart_Visuals(Product_Section_Man,Product_Section_Woman);
      #print("The Sales volume of Clothing for Zara brand :",Product_Sales_Number,"- sold for the Amount $",Product_Cost_Dollars);
      #Product_Sales_Number = Product_Sales_Cost_Compute(Product_Sales_Computation,Product_Cost_Computation,Product_Sales_Number,Product_Cost_Dollars)[0];
      #Product_Cost_Dollars = Product_Sales_Cost_Compute(Product_Sales_Computation,Product_Cost_Computation,Product_Sales_Number,Product_Cost_Dollars)[1];
      #print("Total Product Sales of Jackets and Sweaters for Woman in India, Spain and China are: ",Product_Sales_Number);
      #print("Total Product Cost of Jackets | Sweaters for Woman in India, Spain and China in $ ",Product_Cost_Dollars);
      print("Product Section Sales for Man includes:",Product_Section_Output[0],"Product Section for Woman includes: ",Product_Section_Output[1]);
      #print("Product Position Output for Aisle: ", Product_Position_Output[0],"Product Postion Output for Front of store includes: ", Product_Postion_Output[1],"Cloths displayed at the End of the store are: ",Product_Position_Output[2]);
      #print("Product Season Sales for Winter: ", Product_Season_Output[0],"Product Sales for Autumn: ", Product_Season_Output[1],"Cloths displayed at the End of the Summar: ",Product_Season_Output[2],"Cloths sold by end of Spring are: ",Product_Season_Output[3]);
      #print("Wool Volume sold: ",Product_Material_Output[0],"Wool Blend of the Product sold: ",Product_Material_Output[1],"Linen for Zara sold in all seasons: ",Product_Material_Output[2],"Linen Blend sales: ",Product_Material_Output[3],"Cotton Products sold in clothing: ",Product_Material_Output[4],"Silk product sales: ",Product_Material_Output[5],"Product Viscose volume of sales: ",Product_Material_Output[6],"Clothing of Polyester for Zara Volume: ",Product_Material_Output[7],"Product Denim Sales: ",Product_Material_Output[8]);
      #print("Sales of the Zara brand across Argentina: ",Product_Origin_Output[0],"Sales of Clothing for Bangladesh: ",Product_Origin_Output[1],"Sales of Zara brand Clothing over Brazil: ",Product_Origin_Output[2],"Product Sales over Cambodia: ",Product_Origin_Output[3],"Product Sales over China: ",Product_Origin_Output[4],"Zara brand sales in India: ",Product_Origin_Output[5],"Product Sales Over Moracco: ",Product_Origin_Output[6],"Product Sales Over Pakistan: ",Product_Origin_Output[7],"Product Sales Over Portugal: ",Product_Origin_Output[8],"Sales of Spain: ",Product_Origin_Output[9],"Sales of Turkey: ",Product_Origin_Output[10],"Vietnam Sales volume:",Product_Origin_Output[11]);
      #Product_Sales_Model_Output = Model_Generation(Product_Train_Sample[0],Product_Train_Sample[1],Product_Train_Data,Product_Test_Data,Product_Train_Mean,Product_Train_Std);
      #Pie_Chart_Visuals(Product_Section_Output,Product_Position_Output,Product_Season_Output,Product_Material_Output,Product_Origin_Output);
      return(None);
      
Business_Sales_Comp = Business_Sales_Compute();
Business_Comp = Business_Sales_Cost_Volume_Computation();
