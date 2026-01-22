import numpy as np;
import pandas as pd;
import matplotlib.pyplot as plt;
import math;

class Analyse_Business_Revenue:
   #def Analyse_Business_Sales_Cost(self,Product_Sales_File,Product_ID,Product_Sales_Volume,Product_Cost,i):
   #def Analyse_Business_Sales_Cost(self,Product_Sales_File,Product_ID,list(Product_Sales_Volume),list(Product_Cost),i,list(Product_Sales_List),list(Product_Cost_List),list(Product_Sales_Argentina),list(Product_Cost_Argentina),list(Product_Sales_Bangladesh),list(Product_Cost_Bangladesh),list(Product_Sales_Brazil),list(Product_Cost_Brazil),list(Product_Sales_Cambodia),list(Product_Cost_Cambodia),list(Product_Sales_China),list(Product_Cost_China),list(Product_Sales_India),list(Product_Cost_India),list(Product_Sales_Morocco),list(Product_Cost_Morocco),list(Product_Sales_Pakistan),list(Product_Cost_Pakistan),list(Product_Sales_Portugal),list(Product_Cost_Portugal),list(Product_Sales_Spain),list(Product_Cost_Spain),list(Product_Sales_Turkey),list(Product_Cost_Turkey),list(Product_Sales_Vietnam),list(Product_Cost_Vietnam)):
   #def Analyse_Business_Sales_Cost(self,Product_Sales_File,list(Product_ID),list(Product_Sales_Volume),list(Product_Cost),i,list(Product_Sales_List),list(Product_Cost_List),list(Product_Sales_Argentina),list(Product_Cost_Argentina),list(Product_Sales_Bangladesh),list(Product_Cost_Bangladesh),list(Product_Sales_Brazil),list(Product_Cost_Brazil),list(Product_Sales_Cambodia),list(Product_Cost_Cambodia),list(Product_Sales_China),list(Product_Cost_China),list(Product_Sales_India),list(Product_Cost_India),list(Product_Sales_Morocco),list(Product_Cost_Morocco),list(Product_Sales_Pakistan),list(Product_Cost_Pakistan),list(Product_Sales_Portugal),list(Product_Cost_Portugal),list(Product_Sales_Spain),list(Product_Cost_Spain),list(Product_Sales_Turkey),list(Product_Cost_Turkey),list(Product_Sales_Vietnam),list(Product_Cost_Vietnam)):
   def Analyse_Business_Sales_Cost(self,Product_Sales_File,Product_ID,Product_Sales_Volume,Product_Cost,i,Product_Sales_List,Product_Cost_List,Product_Sales_Argentina,Product_Cost_Argentina,Product_Sales_Bangladesh,Product_Cost_Bangladesh,Product_Sales_Brazil,Product_Cost_Brazil,Product_Sales_Cambodia,Product_Cost_Cambodia,Product_Sales_China,Product_Cost_China,Product_Sales_India,Product_Cost_India,Product_Sales_Morocco,Product_Cost_Morocco,Product_Sales_Pakistan,Product_Cost_Pakistan,Product_Sales_Portugal,Product_Cost_Portugal,Product_Sales_Spain,Product_Cost_Spain,Product_Sales_Turkey,Product_Cost_Turkey,Product_Sales_Vietnam,Product_Cost_Vietnam):
      Product_ID = list(Product_Sales_File[0]);
      Product_Position = list(Product_Sales_File[1]);
      Product_Promotion = list(Product_Sales_File[2]);
      Product_Category = list(Product_Sales_File[3]);
      Product_Seasonal = list(Product_Sales_File[4]);
      Product_Sales_Volume = list(Product_Sales_File[5]);
      Product_Brand = list(Product_Sales_File[6]);
      Product_URL = list(Product_Sales_File[7]);
      Product_Name = list(Product_Sales_File[8]);
      Product_Description = list(Product_Sales_File[9]);
      Product_Cost = list(Product_Sales_File[10]);
      Product_Currency = list(Product_Sales_File[11]);
      Product_Terms = list(Product_Sales_File[12]);
      Product_Section = list(Product_Sales_File[13]);
      Product_Season = list(Product_Sales_File[14]);
      Product_Material = list(Product_Sales_File[15]);
      Product_Origin = list(Product_Sales_File[16]);

      list(Product_Sales_Argentina);
      list(Product_Sales_Bangladesh);
      list(Product_Sales_Brazil);
      list(Product_Sales_Cambodia);
      list(Product_Sales_China);
      list(Product_Sales_India);
      list(Product_Sales_Morocco);
      list(Product_Sales_Pakistan);
      list(Product_Sales_Portugal);
      list(Product_Sales_Spain);
      list(Product_Sales_Turkey);
      list(Product_Sales_Vietnam);
      '''for i in range(len(Product_ID)):
         if((i < len(Product_ID)) and (float(Product_Sales_Volume[i]) != 'Nan')):
            #Product_Sales_Volume.update(i,0.0);#insert(i,0.0);
            #Product_Sales_Volume[i] = 0.0;
            Product_Sales_Volume.insert(i,0);
         elif((i < len(Product_ID) and (float(Product_Cost[i] != 'Nan')))):
            #Product_Cost.insert(i,0.0);
            Product_Cost.insert(i,0);
         elif(i < len(Product_ID) and (float(Product_ID[i]) != 'Nan')):
            Product_ID.insert(i,333333);
            #Product_ID.insert(i,333333);
         elif((i < len(Product_ID)) and (Product_Sales_Volume[i] != float('Nan')) and (Product_Cost[i] == float('Nan'))):
            Product_Cost.insert(i,0)
            #Product_Cost.insert(i,0.0);
         elif((i < len(Product_ID)) and (Product_Sales_Volume[i] == float('Nan')) and (Product_Cost[i] != float('Nan'))):
            Product_Sales_Volume.insert(i,0);
            #Product_Sales_Volume.insert(i,0.0);
         else:
            print("Sales and Cost Values are fixed for Nan and Null values from CSV data file");'''

      for i in range(len(Product_ID)):
         if((i < len(Product_ID)) and (Product_Origin[i] == 'Argentina')):
            #print("Inside the loop of Argentina",i);
            Product_Sales_Argentina.append(Product_Sales_Volume[i]);
            Product_Cost_Argentina.append(Product_Cost[i]);
         elif((i < len(Product_ID)) and (Product_Origin[i] == 'Bangladesh')):
            Product_Sales_Bangladesh.append(Product_Sales_Volume[i]);
            Product_Cost_Bangladesh.append(Product_Cost[i]);
         elif((i < len(Product_ID)) and (Product_Origin[i] == 'Brazil')):
            Product_Sales_Brazil.append(Product_Sales_Volume[i]);
            Product_Cost_Brazil.append(Product_Cost[i]);
         elif((i < len(Product_ID)) and (Product_Origin[i] == 'Cambodia')):
            Product_Sales_Cambodia.append(Product_Sales_Volume[i]);
            Product_Cost_Cambodia.append(Product_Cost[i]);
         elif((i < len(Product_ID)) and (Product_Origin[i] == 'China')):
            Product_Sales_China.append(Product_Sales_Volume[i]);
            Product_Cost_China.append(Product_Cost[i]);
         elif((i < len(Product_ID)) and (Product_Origin[i] == 'India')):
            Product_Sales_India.append(Product_Sales_Volume[i]);
            Product_Cost_India.append(Product_Cost[i]);
         elif((i < len(Product_ID)) and (Product_Origin[i] == 'Morocco')):
            Product_Sales_Morocco.append(Product_Sales_Volume[i]);
            Product_Cost_Morocco.append(Product_Cost[i]);
         elif((i < len(Product_ID)) and (Product_Origin[i] == 'Pakistan')):
            Product_Sales_Pakistan.append(Product_Sales_Volume[i]);
            Product_Cost_Pakistan.append(Product_Cost[i]);
         elif((i < len(Product_ID)) and (Product_Origin[i] == 'Portugal')):
            Product_Sales_Portugal.append(Product_Sales_Volume[i]);
            Product_Cost_Portugal.append(Product_Cost[i]);
         elif((i < len(Product_ID)) and (Product_Origin[i] == 'Spain')):
            Product_Sales_Spain.append(Product_Sales_Volume[i]);
            Product_Cost_Spain.append(Product_Cost[i]);
         elif((i < len(Product_ID)) and (Product_Origin[i] == 'Turkey')):
            Product_Sales_Turkey.append(Product_Sales_Volume[i]);
            Product_Cost_Turkey.append(Product_Cost[i]);
         elif((i < len(Product_ID)) and (Product_Origin[i] == 'Vietnam')):
            Product_Sales_Vietnam.append(Product_Sales_Volume[i]);
            Product_Cost_Vietnam.append(Product_Cost[i]);
         elif(i == len(Product_ID)):
            break;
      Product_Sales_List = [Product_Sales_Volume,Product_Sales_Argentina,Product_Sales_Bangladesh,Product_Sales_Brazil,Product_Sales_Cambodia,Product_Sales_China,Product_Sales_India,Product_Sales_Morocco,Product_Sales_Pakistan,Product_Sales_Portugal,Product_Sales_Spain,Product_Sales_Turkey,Product_Sales_Vietnam];
      Product_Cost_List = [Product_Cost,Product_Cost_Argentina,Product_Cost_Bangladesh,Product_Cost_Brazil,Product_Cost_Cambodia,Product_Cost_China,Product_Cost_India,Product_Cost_Morocco,Product_Cost_Pakistan,Product_Cost_Portugal,Product_Cost_Spain,Product_Cost_Turkey,Product_Cost_Vietnam];
      #return([Product_Sales_List,Product_Cost_List]);
      #Product_Sales_Argentina = #float(np.sum(Product_Sales_Argentina))/float(np.sum(Product_Sales_Volume));
      ##Product_Cost_Argentina = #float(np.sum(Product_Cost_Argentina))/float(np.sum(Product_Cost));
      #Product_Sales_Brazil =  #float(np.sum(Product_Sales_Brazil))/float(np.sum(Product_Sales_Volume));
      #Product_Cost_Brazil = #float(np.sum(Product_Cost_Brazil))/float(np.sum(Product_Cost));
      #Product_Sales_Bangladesh =  #float(np.sum(Product_Sales_Bangladesh))/float(np.sum(Product_Sales_Volume));
      #Product_Cost_Bangladesh = #float(np.sum(Product_Cost_Bangladesh))/float(np.sum(Product_Cost));
      #Product_Sales_Cambodia =  #float(np.sum(Product_Sales_Cambodia))/float(np.sum(Product_Sales_Volume));
      #Product_Cost_Cambodia = #float(np.sum(Product_Cost_Cambodia))/float(np.sum(Product_Cost));
      #Product_Sales_China =  #float(np.sum(Product_Sales_China))/float(np.sum(Product_Sales_Volume));
      #Product_Cost_China = #float(np.sum(Product_Cost_China))/float(np.sum(Product_Cost));
      #Product_Sales_India =  #float(np.sum(Product_Sales_India))/float(np.sum(Product_Sales_Volume));
      #Product_Cost_India = #float(np.sum(Product_Cost_India))/float(np.sum(Product_Cost));
      #Product_Sales_Morocco =  #float(np.sum(Product_Sales_Morocco))/float(np.sum(Product_Sales_Volume));
      #Product_Cost_Morocco = #float(np.sum(Product_Cost_Morocco))/float(np.sum(Product_Cost));
      #Product_Sales_Pakistan =  #float(np.sum(Product_Sales_Pakistan))/float(np.sum(Product_Sales_Volume));
      #Product_Cost_Pakistan = #float(np.sum(Product_Cost_Pakistan))/float(np.sum(Product_Cost));
      #Product_Sales_Portugal =  #float(np.sum(Product_Sales_Portugal))/float(np.sum(Product_Sales_Volume));
      #Product_Cost_Portugal = #float(np.sum(Product_Cost_Portugal))/float(np.sum(Product_Cost));
      #Product_Sales_Spain =  #float(np.sum(Product_Sales_Spain))/float(np.sum(Product_Sales_Volume));
      #Product_Cost_Spain = #float(np.sum(Product_Cost_Spain))/float(np.sum(Product_Cost));
      #Product_Sales_Turkey =  #float(np.sum(Product_Sales_Turkey))/float(np.sum(Product_Sales_Volume));
      #Product_Cost_Turkey = #float(np.sum(Product_Cost_Turkey))/float(np.sum(Product_Cost));
      #Product_Sales_Vietnam =  #float(np.sum(Product_Sales_Vietnam))/float(np.sum(Product_Sales_Volume));
      #Product_Cost_Vietnam = #float(np.sum(Product_Cost_Vietnam))/float(np.sum(Product_Cost));

      
      return([Product_Sales_List,Product_Cost_List]);

   def Adjust_Product_Price(self,Product_Price,Product_Sales_Volume,Product_ID,i,Product_Cost):
      for i in range(len(Product_ID)):
         if(i < len(Product_ID)):
            Product_Cost.append((Product_Sales_Volume[i]* Product_Price[i]));

         elif(i == len(Product_ID)):
            continue;
         else:
            return(Product_Cost);
      return(Product_Cost);
   
   '''def pie_chart_origins(self,Product_Sales,Product_Sales_Argentina,Product_Sales_Bangladesh,Product_Sales_Brazil,Product_Sales_Cambodia,Product_Sales_China,Product_Sales_India,Product_Sales_Morocco,Product_Sales_Pakistan,Product_Sales_Portugal,Product_Sales_Spain,Product_Sales_Turkey,Product_Sales_Vietnam):
      plt.style.use('_mpl-gallery-nogrid');
      labels = ['Argentina','Bangladesh','Brazil','Cambodia','China','India','Morocco','Pakistan','Portugal','Spain','Turkey','Vietnam'];
      #label = ["Sales"];
      #Sales_Value = [];
      Sales_Regions = (int(np.sum(Product_Sales_Argentina))/int(np.sum(Product_Sales)),int(np.sum(Product_Sales_Bangladesh))/int(np.sum(Product_Sales)),int(np.sum(Product_Sales_Brazil))/int(np.sum(Product_Sales)),int(np.sum(Product_Sales_Cambodia))/int(np.sum(Product_Sales)),int(np.sum(Product_Sales_China))/int(np.sum(Product_Sales)),int(np.sum(Product_Sales_India))/int(np.sum(Product_Sales)),int(np.sum(Product_Sales_Morocco))/int(np.sum(Product_Sales)),int(np.sum(Product_Sales_Pakistan))/int(np.sum(Product_Sales)),int(np.sum(Product_Sales_Portugal))/int(np.sum(Product_Sales)),int(np.sum(Product_Sales_Spain))/int(np.sum(Product_Sales)),int(np.sum(Product_Sales_Turkey))/int(np.sum(Product_Sales)),int(np.sum(Product_Sales_Vietnam))/int(np.sum(Product_Sales)));
      #Sales_Value.insert(0,[int(np.sum(Product_Sales))]);
      fig, ax = plt.subplots();
      ax.pie(Sales_Regions,labels);
      #ax.pie([Sales_Value,20,30],label);
      #plt.xlabel("Product Sales");
      #plt.ylabel("Region of Sales");
      plt.show();
      return(None);'''

   def Scatter_Visualization(self,Product_Sales,Product_Sales_Argentina,Product_Sales_Bangladesh,Product_Sales_Brazil,Product_Sales_Cambodia,Product_Sales_China,Product_Sales_India,Product_Sales_Morocco,Product_Sales_Pakistan,Product_Sales_Portugal,Product_Sales_Spain,Product_Sales_Turkey,Product_Sales_Vietnam):    
      #plt.style.use('_mpl-gallery-nogrid');
      #Sales_Origins = [int(np.sum(Product_Sales_Argentina))/int(np.sum(Product_Sales)),int(np.sum(Product_Sales_Bangladesh))/int(np.sum(Product_Sales)),int(np.sum(Product_Sales_Brazil))/int(np.sum(Product_Sales)),int(np.sum(Product_Sales_Cambodia))/int(np.sum(Product_Sales)),int(np.sum(Product_Sales_China))/int(np.sum(Product_Sales)),int(np.sum(Product_Sales_India))/int(np.sum(Product_Sales)),int(np.sum(Product_Sales_Morocco))/int(np.sum(Product_Sales)),int(np.sum(Product_Sales_Pakistan))/int(np.sum(Product_Sales)),int(np.sum(Product_Sales_Portugal))/int(np.sum(Product_Sales)),int(np.sum(Product_Sales_Spain))/int(np.sum(Product_Sales)),int(np.sum(Product_Sales_Turkey))/int(np.sum(Product_Sales)),int(np.sum(Product_Sales_Vietnam))/int(np.sum(Product_Sales))];
      #Sales_Origins = [Product_Sales_Argentina,Product_Sales_Bangladesh,Product_Sales_Brazil,Product_Sales_Cambodia,Product_Sales_China,Product_Sales_India,Product_Sales_Morocco,Product_Sales_Pakistan,Product_Sales_Portugal,Product_Sales_Spain,Product_Sales_Turkey,Product_Sales_Vietnam];
      Sales_Origins = [int(np.sum(Product_Sales_Argentina)),int(np.sum(Product_Sales_Bangladesh)),int(np.sum(Product_Sales_Brazil)),int(np.sum(Product_Sales_Cambodia)),int(np.sum(Product_Sales_China)),int(np.sum(Product_Sales_India)),int(np.sum(Product_Sales_Morocco)),int(np.sum(Product_Sales_Pakistan)),int(np.sum(Product_Sales_Portugal)),int(np.sum(Product_Sales_Spain)),int(np.sum(Product_Sales_Turkey)),int(np.sum(Product_Sales_Vietnam))];
      labels = ['Argentina','Bangladesh','Brazil','Cambodia','China','India','Morocco','Pakistan','Portugal','Spain','Turkey','Vietnam'];
      colours = ['blue','green','orange','brown','yellow','white','black','Red','Cyan','Pink','Violet','Indigo'];
      fig, ax = plt.subplots();
      ax.scatter(Sales_Origins,labels);
      ax.set(xlim=(0,60),ylim=(0,12),xticks=np.arange(1,60),yticks=np.arange(1,12));
      #ax.set(xticklabels=[],yticklabels=[]);
      #ax.set(xlabel="Product Sales",ylabel="Revenue from Distinct Regions in $: ")
      #ax.xlabel("Product Sales");
      #ax.ylabel("Revenue from Distinct Regions in $:"); 
      plt.show();
      return();

   def Pie_Chart_Visuals(self,Product_Sales_List,Product_Cost_List):
      #Pie chart styles to update the gallery with nogrid.
      plt.style.use('_mpl-gallery-nogrid');
      # make data
      #x = Product_Section_Output; #[1, 2, 3, 4]
      #x = Product_Season_Output;
      #x = Product_Position_Output;
      #x = Product_Material_Output;
      #x = Product_Origin_Output;
      # Plot colour addition to shell pie charts.
      x = [];
      y = [];
      z = [];
      w = [];
      Product_Sales = [];
      Product_Cost = [];
      Product_Sales = float(np.sum(Product_Sales_List));
      Product_Cost = float(np.sum(Product_Cost_List));

      #x = #[1,2,3,4];#[1,2,3,4,5,6,7,8,10,50,25,45,32,98,76]
      x = Product_Sales_List;
      y = Product_Cost_List;
      z = Product_Sales;
      w = Product_Cost;
      #y = Product_Cost_List;
      #colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len(x)))
      # ploting
      fig, ax = plt.subplots();
      #ax.pie(x, colors=colors, radius=3, center=(1527, 1527),wedgeprops={"linewidth": 1, "edgecolor": "green"}, frame=True);
      #s = x**2;#math.pow(x,2);
      s = x;
      plt.scatter(x,y,marker = r"$\diamond$",label="Product Sales VS Revenue in $");
      #color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']);
      plt.xlabel("Product Sales");
      plt.ylabel("Product Revenue in $");
      plt.show();
      #plt.plot(x,y);
      fig, ax = plt.subplots();
      plt.scatter(z,w,marker = r"$\$$",label="Product Sales Vs Net Revenue in $");
      plt.xlabel("Product Sales");
      plt.ylabel("Product Net Revenue in $");
      #ax.set(xlim=(950, 2000), xticks=np.arange(957, 2000),
      #ylim=(950, 2000), yticks=np.arange(957, 2000));
      plt.show();
      return(None);

   def __init__(self):
      Business_Sales_File = pd.read_csv("/content/Product_Sales/Business_sales_EDA.csv",delimiter=';');

      Product_ID = [];
      Product_Name = [];
      Product_Category = [];
      Product_Description = [];
      Product_Position = [];
      Product_Promotion = [];
      Product_Sales_Volume = [];
      Product_URL = [];
      Product_Price = [];
      Product_Brand = [];
      Product_Material = [];
      Product_Seasonal = [];
      Product_Season = [];
      Product_Terms = [];
      Product_Section = [];
      Product_Currency = [];
      Product_Origin = [];

      Product_ID = Business_Sales_File['Product ID'];
      Product_Name = Business_Sales_File['name'];
      Product_Category = Business_Sales_File['Product Category'];
      Product_Position = Business_Sales_File['Product Position'];
      Product_Promotion = Business_Sales_File['Promotion'];
      Product_Sales_Volume = Business_Sales_File['Sales Volume'];
      Product_Price = Business_Sales_File['price'];
      Product_Brand = Business_Sales_File['brand'];
      Product_Seasonal = Business_Sales_File['Seasonal'];
      Product_URL = Business_Sales_File['url'];
      Product_Description = Business_Sales_File['description'];
      Product_Season = Business_Sales_File['season'];
      Product_Material = Business_Sales_File['material'];
      Product_Currency = Business_Sales_File['currency'];
      Product_Section = Business_Sales_File['section'];
      Product_Terms = Business_Sales_File['terms'];
      Product_Origin = Business_Sales_File['origin'];
      i = 0;
      Product_Cost = [];

      Product_Sales_File = [Product_ID,Product_Position,Product_Promotion,Product_Category,Product_Seasonal,Product_Sales_Volume,Product_Brand,Product_URL,Product_Name,Product_Description,Product_Cost,Product_Currency,Product_Terms,Product_Section,Product_Season,Product_Material,Product_Origin];
      Product_Cost = self.Adjust_Product_Price(Product_Price,Product_Sales_Volume,Product_ID,i,Product_Cost);

      print("Sales Revenue for Zara Brand in all Regions for the Fiscal Year 2024 is:",int(np.sum(Product_Sales_Volume)));
      self.Pie_Chart_Visuals(Product_Sales_Volume,Product_Cost);

      Product_Sales_Argentina = [];
      Product_Cost_Argentina = [];
      Product_Sales_Bangladesh = [];
      Product_Cost_Bangladesh = [];
      Product_Sales_Brazil = [];
      Product_Cost_Brazil = [];
      Product_Sales_Cambodia = [];
      Product_Cost_Cambodia = [];
      Product_Sales_China = [];
      Product_Cost_China =[];
      Product_Sales_India = [];
      Product_Cost_India = [];
      Product_Sales_Morocco = [];
      Product_Cost_Morocco = [];
      Product_Sales_Pakistan = [];
      Product_Cost_Pakistan = [];
      Product_Sales_Portugal = [];
      Product_Cost_Portugal = [];
      Product_Sales_Spain = [];
      Product_Cost_Spain = [];
      Product_Sales_Turkey = [];
      Product_Cost_Turkey = [];
      Product_Sales_Vietnam = [];
      Product_Cost_Vietnam = [];
      Product_Sales_List = [];
      Product_Cost_List = [];
      i = 0;
      Product_Analysis = [];
      Product_Sales = [];
      Product_Revenue = [];
      Product_Sales = self.Analyse_Business_Sales_Cost(Product_Sales_File,Product_ID,Product_Sales_Volume,Product_Cost,i,Product_Sales_List,Product_Cost_List,Product_Sales_Argentina,Product_Cost_Argentina,Product_Sales_Bangladesh,Product_Cost_Bangladesh,Product_Sales_Brazil,Product_Cost_Brazil,Product_Sales_Cambodia,Product_Cost_Cambodia,Product_Sales_China,Product_Cost_China,Product_Sales_India,Product_Cost_India,Product_Sales_Morocco,Product_Cost_Morocco,Product_Sales_Pakistan,Product_Cost_Pakistan,Product_Sales_Portugal,Product_Cost_Portugal,Product_Sales_Spain,Product_Cost_Spain,Product_Sales_Turkey,Product_Cost_Turkey,Product_Sales_Vietnam,Product_Cost_Vietnam)[0][0];
      #x = len(Product_Sales[0][0])/13;
      #Product_Sales = Product_Sales[:x];
      #Product_Sales_Argentina = Product_Sales[(len(Product_Sales[0][0])/13)+1:(len(Product_Sales[0][0])/26)];
      #print(int(len(Product_Sales)/13));
      #print(Product_Sales_Argentina);
      Product_Sales_Argentina = self.Analyse_Business_Sales_Cost(Product_Sales_File,Product_ID,Product_Sales_Volume,Product_Cost,i,Product_Sales_List,Product_Cost_List,Product_Sales_Argentina,Product_Cost_Argentina,Product_Sales_Bangladesh,Product_Cost_Bangladesh,Product_Sales_Brazil,Product_Cost_Brazil,Product_Sales_Cambodia,Product_Cost_Cambodia,Product_Sales_China,Product_Cost_China,Product_Sales_India,Product_Cost_India,Product_Sales_Morocco,Product_Cost_Morocco,Product_Sales_Pakistan,Product_Cost_Pakistan,Product_Sales_Portugal,Product_Cost_Portugal,Product_Sales_Spain,Product_Cost_Spain,Product_Sales_Turkey,Product_Cost_Turkey,Product_Sales_Vietnam,Product_Cost_Vietnam)[0][1];
      
      Product_Sales_Bangladesh = self.Analyse_Business_Sales_Cost(Product_Sales_File,Product_ID,Product_Sales_Volume,Product_Cost,i,Product_Sales_List,Product_Cost_List,Product_Sales_Argentina,Product_Cost_Argentina,Product_Sales_Bangladesh,Product_Cost_Bangladesh,Product_Sales_Brazil,Product_Cost_Brazil,Product_Sales_Cambodia,Product_Cost_Cambodia,Product_Sales_China,Product_Cost_China,Product_Sales_India,Product_Cost_India,Product_Sales_Morocco,Product_Cost_Morocco,Product_Sales_Pakistan,Product_Cost_Pakistan,Product_Sales_Portugal,Product_Cost_Portugal,Product_Sales_Spain,Product_Cost_Spain,Product_Sales_Turkey,Product_Cost_Turkey,Product_Sales_Vietnam,Product_Cost_Vietnam)[0][2];
      Product_Sales_Brazil = self.Analyse_Business_Sales_Cost(Product_Sales_File,Product_ID,Product_Sales_Volume,Product_Cost,i,Product_Sales_List,Product_Cost_List,Product_Sales_Argentina,Product_Cost_Argentina,Product_Sales_Bangladesh,Product_Cost_Bangladesh,Product_Sales_Brazil,Product_Cost_Brazil,Product_Sales_Cambodia,Product_Cost_Cambodia,Product_Sales_China,Product_Cost_China,Product_Sales_India,Product_Cost_India,Product_Sales_Morocco,Product_Cost_Morocco,Product_Sales_Pakistan,Product_Cost_Pakistan,Product_Sales_Portugal,Product_Cost_Portugal,Product_Sales_Spain,Product_Cost_Spain,Product_Sales_Turkey,Product_Cost_Turkey,Product_Sales_Vietnam,Product_Cost_Vietnam)[0][3];
      Product_Sales_Cambodia = self.Analyse_Business_Sales_Cost(Product_Sales_File,Product_ID,Product_Sales_Volume,Product_Cost,i,Product_Sales_List,Product_Cost_List,Product_Sales_Argentina,Product_Cost_Argentina,Product_Sales_Bangladesh,Product_Cost_Bangladesh,Product_Sales_Brazil,Product_Cost_Brazil,Product_Sales_Cambodia,Product_Cost_Cambodia,Product_Sales_China,Product_Cost_China,Product_Sales_India,Product_Cost_India,Product_Sales_Morocco,Product_Cost_Morocco,Product_Sales_Pakistan,Product_Cost_Pakistan,Product_Sales_Portugal,Product_Cost_Portugal,Product_Sales_Spain,Product_Cost_Spain,Product_Sales_Turkey,Product_Cost_Turkey,Product_Sales_Vietnam,Product_Cost_Vietnam)[0][4];
      Product_Sales_China = self.Analyse_Business_Sales_Cost(Product_Sales_File,Product_ID,Product_Sales_Volume,Product_Cost,i,Product_Sales_List,Product_Cost_List,Product_Sales_Argentina,Product_Cost_Argentina,Product_Sales_Bangladesh,Product_Cost_Bangladesh,Product_Sales_Brazil,Product_Cost_Brazil,Product_Sales_Cambodia,Product_Cost_Cambodia,Product_Sales_China,Product_Cost_China,Product_Sales_India,Product_Cost_India,Product_Sales_Morocco,Product_Cost_Morocco,Product_Sales_Pakistan,Product_Cost_Pakistan,Product_Sales_Portugal,Product_Cost_Portugal,Product_Sales_Spain,Product_Cost_Spain,Product_Sales_Turkey,Product_Cost_Turkey,Product_Sales_Vietnam,Product_Cost_Vietnam)[0][5];
      Product_Sales_India = self.Analyse_Business_Sales_Cost(Product_Sales_File,Product_ID,Product_Sales_Volume,Product_Cost,i,Product_Sales_List,Product_Cost_List,Product_Sales_Argentina,Product_Cost_Argentina,Product_Sales_Bangladesh,Product_Cost_Bangladesh,Product_Sales_Brazil,Product_Cost_Brazil,Product_Sales_Cambodia,Product_Cost_Cambodia,Product_Sales_China,Product_Cost_China,Product_Sales_India,Product_Cost_India,Product_Sales_Morocco,Product_Cost_Morocco,Product_Sales_Pakistan,Product_Cost_Pakistan,Product_Sales_Portugal,Product_Cost_Portugal,Product_Sales_Spain,Product_Cost_Spain,Product_Sales_Turkey,Product_Cost_Turkey,Product_Sales_Vietnam,Product_Cost_Vietnam)[0][6];
      Product_Sales_Morocco = self.Analyse_Business_Sales_Cost(Product_Sales_File,Product_ID,Product_Sales_Volume,Product_Cost,i,Product_Sales_List,Product_Cost_List,Product_Sales_Argentina,Product_Cost_Argentina,Product_Sales_Bangladesh,Product_Cost_Bangladesh,Product_Sales_Brazil,Product_Cost_Brazil,Product_Sales_Cambodia,Product_Cost_Cambodia,Product_Sales_China,Product_Cost_China,Product_Sales_India,Product_Cost_India,Product_Sales_Morocco,Product_Cost_Morocco,Product_Sales_Pakistan,Product_Cost_Pakistan,Product_Sales_Portugal,Product_Cost_Portugal,Product_Sales_Spain,Product_Cost_Spain,Product_Sales_Turkey,Product_Cost_Turkey,Product_Sales_Vietnam,Product_Cost_Vietnam)[0][7];
      Product_Sales_Pakistan = self.Analyse_Business_Sales_Cost(Product_Sales_File,Product_ID,Product_Sales_Volume,Product_Cost,i,Product_Sales_List,Product_Cost_List,Product_Sales_Argentina,Product_Cost_Argentina,Product_Sales_Bangladesh,Product_Cost_Bangladesh,Product_Sales_Brazil,Product_Cost_Brazil,Product_Sales_Cambodia,Product_Cost_Cambodia,Product_Sales_China,Product_Cost_China,Product_Sales_India,Product_Cost_India,Product_Sales_Morocco,Product_Cost_Morocco,Product_Sales_Pakistan,Product_Cost_Pakistan,Product_Sales_Portugal,Product_Cost_Portugal,Product_Sales_Spain,Product_Cost_Spain,Product_Sales_Turkey,Product_Cost_Turkey,Product_Sales_Vietnam,Product_Cost_Vietnam)[0][8];
      Product_Sales_Portugal = self.Analyse_Business_Sales_Cost(Product_Sales_File,Product_ID,Product_Sales_Volume,Product_Cost,i,Product_Sales_List,Product_Cost_List,Product_Sales_Argentina,Product_Cost_Argentina,Product_Sales_Bangladesh,Product_Cost_Bangladesh,Product_Sales_Brazil,Product_Cost_Brazil,Product_Sales_Cambodia,Product_Cost_Cambodia,Product_Sales_China,Product_Cost_China,Product_Sales_India,Product_Cost_India,Product_Sales_Morocco,Product_Cost_Morocco,Product_Sales_Pakistan,Product_Cost_Pakistan,Product_Sales_Portugal,Product_Cost_Portugal,Product_Sales_Spain,Product_Cost_Spain,Product_Sales_Turkey,Product_Cost_Turkey,Product_Sales_Vietnam,Product_Cost_Vietnam)[0][9];
      Product_Sales_Spain = self.Analyse_Business_Sales_Cost(Product_Sales_File,Product_ID,Product_Sales_Volume,Product_Cost,i,Product_Sales_List,Product_Cost_List,Product_Sales_Argentina,Product_Cost_Argentina,Product_Sales_Bangladesh,Product_Cost_Bangladesh,Product_Sales_Brazil,Product_Cost_Brazil,Product_Sales_Cambodia,Product_Cost_Cambodia,Product_Sales_China,Product_Cost_China,Product_Sales_India,Product_Cost_India,Product_Sales_Morocco,Product_Cost_Morocco,Product_Sales_Pakistan,Product_Cost_Pakistan,Product_Sales_Portugal,Product_Cost_Portugal,Product_Sales_Spain,Product_Cost_Spain,Product_Sales_Turkey,Product_Cost_Turkey,Product_Sales_Vietnam,Product_Cost_Vietnam)[0][10];
      Product_Sales_Turkey = self.Analyse_Business_Sales_Cost(Product_Sales_File,Product_ID,Product_Sales_Volume,Product_Cost,i,Product_Sales_List,Product_Cost_List,Product_Sales_Argentina,Product_Cost_Argentina,Product_Sales_Bangladesh,Product_Cost_Bangladesh,Product_Sales_Brazil,Product_Cost_Brazil,Product_Sales_Cambodia,Product_Cost_Cambodia,Product_Sales_China,Product_Cost_China,Product_Sales_India,Product_Cost_India,Product_Sales_Morocco,Product_Cost_Morocco,Product_Sales_Pakistan,Product_Cost_Pakistan,Product_Sales_Portugal,Product_Cost_Portugal,Product_Sales_Spain,Product_Cost_Spain,Product_Sales_Turkey,Product_Cost_Turkey,Product_Sales_Vietnam,Product_Cost_Vietnam)[0][11];
      Product_Sales_Vietnam = self.Analyse_Business_Sales_Cost(Product_Sales_File,Product_ID,Product_Sales_Volume,Product_Cost,i,Product_Sales_List,Product_Cost_List,Product_Sales_Argentina,Product_Cost_Argentina,Product_Sales_Bangladesh,Product_Cost_Bangladesh,Product_Sales_Brazil,Product_Cost_Brazil,Product_Sales_Cambodia,Product_Cost_Cambodia,Product_Sales_China,Product_Cost_China,Product_Sales_India,Product_Cost_India,Product_Sales_Morocco,Product_Cost_Morocco,Product_Sales_Pakistan,Product_Cost_Pakistan,Product_Sales_Portugal,Product_Cost_Portugal,Product_Sales_Spain,Product_Cost_Spain,Product_Sales_Turkey,Product_Cost_Turkey,Product_Sales_Vietnam,Product_Cost_Vietnam)[0][12];
      
      print(Product_Sales);
      print(Product_Sales_Argentina);
      print(Product_Sales_Bangladesh)
      print(Product_Sales_Brazil);
      print(Product_Sales_Cambodia);
      print(Product_Sales_China);
      print(Product_Sales_India);
      print(Product_Sales_Morocco);
      print(Product_Sales_Pakistan);
      print(Product_Sales_Portugal);
      print(Product_Sales_Spain);
      print(Product_Sales_Turkey);
      print(Product_Sales_Vietnam);
      
      print(float(np.sum(Product_Sales)));
      print(float(np.sum(Product_Sales_Argentina)));
      print(float(np.sum(Product_Sales_Bangladesh)));
      print(float(np.sum(Product_Sales_Brazil)));
      print(float(np.sum(Product_Sales_Cambodia)));
      print(float(np.sum(Product_Sales_China)));
      print(float(np.sum(Product_Sales_India)));
      print(float(np.sum(Product_Sales_Morocco)));
      print(float(np.sum(Product_Sales_Pakistan)));
      print(float(np.sum(Product_Sales_Portugal)));
      print(float(np.sum(Product_Sales_Spain)));
      print(float(np.sum(Product_Sales_Turkey)));
      print(float(np.sum(Product_Sales_Vietnam)));
      print(float(np.sum(Product_Sales)));
      #print(Product_Sales_Bangladesh);
      #self.pie_chart_origins(Product_Sales,Product_Sales_Argentina,Product_Sales_Bangladesh,Product_Sales_Brazil,Product_Sales_Cambodia,Product_Sales_China,Product_Sales_India,Product_Sales_Morocco,Product_Sales_Pakistan,Product_Sales_Portugal,Product_Sales_Spain,Product_Sales_Turkey,Product_Sales_Vietnam);
      self.Scatter_Visualization(Product_Sales,Product_Sales_Argentina,Product_Sales_Bangladesh,Product_Sales_Brazil,Product_Sales_Cambodia,Product_Sales_China,Product_Sales_India,Product_Sales_Morocco,Product_Sales_Pakistan,Product_Sales_Portugal,Product_Sales_Spain,Product_Sales_Turkey,Product_Sales_Vietnam);
      #Product_Revenue = self.Analyse_Business_Sales_Cost(Product_Sales_File,Product_ID,Product_Sales_Volume,Product_Cost,i)[1];
      #print(np.sum(Product_Sales));
      #print(np.sum(Product_Revenue));
      #self.Pie_Chart_Visuals(Product_Sales,Product_Revenue);
      return(None);
Analyse_Business = Analyse_Business_Revenue();

