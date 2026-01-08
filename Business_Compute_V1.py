import numpy as np;
import pandas as pd;
import math;
import matplotlib.pyplot as plt;
import random;
import stat;
import Even_Odd_Number_Generator as eong;

#from string import substr;
#from string import concat;
#import string;
#position_Aisle = [1,2,3,4,5];
#print(np.sum(position_Aisle))
#class Business_Compute:

class Business_Compute:
   def Business_Sales_Cost_Volume_Compute(self,Data_File,Product_Sales_List,Product_Cost_List,i):
      Product_ID = Data_File[0];
      Product_Name = Data_File[1];
      Product_Description = Data_File[2];
      Product_Terms = Data_File[3];
      Product_Promotion = Data_File[4];
      Product_Position = Data_File[5];
      Product_URL = Data_File[6];
      Product_Category = Data_File[7];
      Product_Sales_Volume = Data_File[8];
      Product_Section = Data_File[9];
      Product_Price = Data_File[10];
      Product_Seasonal = Data_File[11];
      Product_Season = Data_File[12];
      Product_Currency = Data_File[13];
      Product_Material = Data_File[14];
      Product_Origin = Data_File[15];
      Product_Brand = Data_File[16];
      counter_promotion = [];
      counter_origin = [];
      counter_material = [];
      counter_section = [];
      counter_id = [];
      Product_Sales_List = [];
      Product_Cost_List = [];
      #counter = 0;
      #print(Data_File[8])
      for i in range(len(Product_ID)):
         if((i < int(len(Product_ID)))):
            #counter_id.append([Product_ID[i]]);
            #print("Inside conditional statement at i value:",i);
            if((Product_Promotion[i] =='Yes') and (Product_Origin[i] == 'India' or Product_Origin[i] == 'Spain' or Product_Origin[i] == 'China') and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Silk' or Product_Material[i] == 'Cotton') and Product_Section[i] == 'WOMAN'):
               counter_id.append([Product_ID[i]]);
               counter_promotion.append(Product_Promotion[i]);
               counter_origin.append(Product_Origin[i]);
               counter_material.append(Product_Material[i])
               counter_section.append(Product_Section[i]);
               #print(Data_File[])
               #print(Product_Sales_Volume[i],Product_Price[i]);
               Product_Sales_List.append(Product_Sales_Volume[i]);
               Product_Cost_List.append(Product_Price[i]);
            elif((Product_Promotion[i] =='Yes') and (Product_Origin[i] == 'India' or Product_Origin[i] == 'Spain' or Product_Origin[i] == 'China') and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Silk' or Product_Material[i] == 'Cotton') and Product_Section[i] == 'MAN'):
               counter_id.append([Product_ID[i]]);
               counter_promotion.append(Product_Promotion[i]);
               counter_origin.append(Product_Origin[i]);
               counter_material.append(Product_Material[i])
               counter_section.append(Product_Section[i]);
               #print(Data_File[])
               #print(Product_Sales_Volume[i],Product_Price[i]);
               Product_Sales_List.append(Product_Sales_Volume[i]);
               Product_Cost_List.append(Product_Price[i]);
               #i = i + 1;
               #self.Business_Sales_Cost_Volume_Compute(Data_File,Product_Sales_List[i:],Product_Cost_List[i:],i);
               #elif(Product_Section[i] == 'MAN'):
               #print(Product_Sales_Volume[i],Product_Price[i]);
               #Product_Sales_List.append(Product_Sales_Volume[i]);
               #Product_Cost_List.append(Product_Price[i]);
               #i = i + 1;
               #self.Business_Sales_Cost_Volume_Compute(Data_File,Product_Sales_List[i:],Product_Cost_List[i:],i);
            #else:
               #i = i+1;
               #self.Business_Sales_Cost_Volume_Compute(Data_File,Product_Sales_List[i:],Product_Cost_List[i:],i);
         #elif(i < len(Product_ID)):
            #i = i +1;
            #self.Business_Sales_Cost_Volume_Compute(Data_File,Product_Sales_List[i:],Product_Cost_List[i:],i);
         else:
            #print("Product Sales value and Amount in Dollars:",Product_Sales_Lisst,Product_Cost);
            #return([np.round(np.float32(np.sum(Product_Sales)),2),np.round(np.float32(np.sum(Product_Cost),2))]);
            #return([np.sum(Product_Sales_List),np.sum(Product_Cost_List)]);
            #print("Product Sales Value and Amount in Dollars:",Product_Sales,Product_Cost);
            #return([np.round(np.float32(np.sum(Product_Sales)),2),np.round(np.float32(np.sum(Product_Cost),2))]);
            return([Product_Sales_List,Product_Cost_List,counter_id,counter_section,counter_promotion,counter_origin,counter_material]);
         #return([np.sum(Product_Sales_List),np.sum(Product_Cost_List)]);
      return([Product_Sales_List,Product_Cost_List,counter_id,counter_section,counter_promotion,counter_origin,counter_material]);

   def Product_Position_Compute(self,Data_File,Product_Sales_Aisle,Product_Cost_Aisle,Product_Sales_Front_Of_Store,Product_Cost_Front_Of_Store,Product_Sales_End_Cap,Product_Cost_End_Cap,Product_ID_Aisle_List,Product_ID_Front_Of_Store_List,Product_ID_End_Cap_List,i):
      Product_Sales_Aisle = [];
      Product_Cost_Aisle = [];
      Product_Sales_Front_Of_Store = [];
      Product_Cost_Front_Of_Store = [];
      Product_Sales_End_Cap = [];
      Product_Cost_End_Cap = [];
      Product_ID_Aisle_List = [];
      Product_ID_Front_Of_Store_List = [];
      Product_ID_End_Cap_List = [];
      #Product_Position_Output = [];
      #Product_Position_Aisle =
      Product_ID = Data_File[0];
      Product_Position = Data_File[5];
      Product_Sales_Volume = Data_File[8];
      Product_Price = Data_File[10];

      for i in range(len(Product_Position)):
         if(i < len(Product_Position)):
            if(Product_Position[i] == 'Aisle'):
               Product_Sales_Aisle.append(Product_Sales_Volume[i]);
               Product_Cost_Aisle.append(Product_Price[i]);
               Product_ID_Aisle_List.append(Product_ID[i]);
               #i = i+1;
               #Product_Position_Aisle = np.sum(Product_Position_Output);
               #Product_Position_Compute(Product_Position,Product_Sales_Volume,Product_Position_Output[i:],Product_Position_Aisle[i:],Product_Front_Of_Store[i:],Product_Position_End_Cap[i:],i);
            elif(Product_Position[i] == 'Front of Store'):
               Product_Sales_Front_Of_Store.append(Product_Sales_Volume[i]);
               Product_Cost_Front_Of_Store.append(Product_Price[i]);
               Product_ID_Front_Of_Store_List.append(Product_ID[i]);
               #Product_Position_Output.append(Product_Sales_Volume[i]);
               #i = i+1;
               #Product_Position_Front_Of_Store = np.sum(Product_Position_Output);
               #Product_Position_Compute(Product_Position,Product_Sales_Volume,Product_Position_Output[i:],Product_Position_Aisle[i:],Product_Front_Of_Store[i:],Product_Position_End_Cap[i:],i);
            elif(Product_Position[i] == 'End-cap'):
               Product_Sales_End_Cap.append(Product_Sales_Volume[i]);
               Product_Cost_End_Cap.append(Product_Price[i]);
               Product_ID_End_Cap_List.append(Product_ID[i]);
               #Product_Position_Output.append(Product_Sales_Volume[i]);
               #i = i+1;
               #Product_Position_End_Cap = np.sum(Product_Position_Output);
               #Product_Position_Compute(Product_Position,Product_Sales_Volume,Product_Position_Output[i:],Product_Position_Aisle[i:],Product_Front_Of_Store[i:],Product_Position_End_Cap[i:],i);
         else:
            return([Product_Sales_Aisle,Product_Sales_Front_Of_Store,Product_Sales_End_Cap,Product_Cost_Aisle,Product_Cost_Front_Of_Store,Product_Cost_End_Cap,Product_ID_Aisle_List,Product_ID_Front_Of_Store_List,Product_ID_End_Cap_List]);
      return([Product_Sales_Aisle,Product_Sales_Front_Of_Store,Product_Sales_End_Cap,Product_Cost_Aisle,Product_Cost_Front_Of_Store,Product_Cost_End_Cap,Product_ID_Aisle_List,Product_ID_Front_Of_Store_List,Product_ID_End_Cap_List]);

   def Standard_Normalized_Sales(self,Data_File,Product_Sales_List,Product_Cost_List,Product_Sales_Aisle,Product_Sales_Front_Of_Store,Product_Sales_End_Cap,Product_Cost_Aisle,Product_Cost_Front_Of_Store,Product_Cost_End_Cap,i):
      Product_ID = Data_File[0];
      Product_Sales_Volume = Data_File[8];
      Product_Price = Data_File[10];
      Sales_Mean = 0.0;
      Sales_Std = 0.0;
      Cost_Mean = 0.0;
      Cost_Std = 0.0;
      Aisle_Sales_Mean = 0.0;
      Aisle_Sales_Std = 0.0;
      Aisle_Cost_Mean = 0.0;
      Aisle_Cost_Std = 0.0;
      Front_Of_Store_Sales_Mean = 0.0;
      Front_Of_Store_Sales_Std = 0.0;
      Front_Of_Store_Cost_Mean = 0.0;
      Front_Of_Store_Cost_Std = 0.0;
      End_Cap_Sales_Mean = 0.0;
      End_Cap_Sales_Std = 0.0;
      End_Cap_Cost_Mean = 0.0;
      End_Cap_Cost_Std = 0.0;
      Gaussian_Sales = [];
      Gaussian_Cost = [];
      Gaussian_Aisle_Sales = [];
      Gaussian_Aisle_Cost = [];
      Gaussian_Front_Of_Store_Sales = [];
      Gaussian_Front_Of_Store_Cost = [];
      Gaussian_End_Cap_Sales = [];
      Gaussian_End_Cap_Cost = [];

      Sales_Mean = np.mean(Product_Sales_List);
      Sales_Std = np.std(Product_Sales_List);
      Cost_Mean = np.mean(Product_Cost_List);
      Cost_Std = np.std(Product_Cost_List);
      Aisle_Sales_Mean = np.mean(Product_Sales_Aisle);
      Aisle_Sales_Std = np.std(Product_Sales_Aisle);
      Aisle_Cost_Mean = np.mean(Product_Cost_Aisle);
      Aisle_Cost_Std = np.std(Product_Cost_Aisle);
      Front_Of_Store_Sales_Mean = np.mean(Product_Sales_Front_Of_Store);
      Front_Of_Store_Sales_Std = np.std(Product_Sales_Front_Of_Store);
      Front_Of_Store_Cost_Mean = np.mean(Product_Cost_Front_Of_Store);
      Front_Of_Store_Cost_Std = np.std(Product_Cost_Front_Of_Store);
      End_Cap_Sales_Mean = np.mean(Product_Sales_End_Cap);
      End_Cap_Sales_Std = np.std(Product_Sales_End_Cap);
      End_Cap_Cost_Mean = np.std(Product_Cost_End_Cap);
      End_Cap_Cost_Std = np.std(Product_Cost_End_Cap);

      for i in range(len(Product_ID)):
         if(i < len(Product_ID)):
            Gaussian_Sales.append((1/(math.sqrt(2*Sales_Std)))* math.exp((-1)*math.pow((Product_Sales_Volume[i]-Sales_Mean),2)/(2*math.pow(Sales_Std,2))));
            Gaussian_Cost.append((1/(math.sqrt(2*Cost_Std)))* math.exp((-1)*math.pow((Product_Price[i]-Cost_Mean),2)/(2*math.pow(Cost_Std,2))));
            Gaussian_Aisle_Sales.append((1/(math.sqrt(2*Aisle_Sales_Std)))* math.exp((-1)*math.pow((Product_Sales_Volume[i]-Aisle_Sales_Mean),2)/(2*math.pow(Aisle_Sales_Std,2))));
            Gaussian_Aisle_Cost.append((1/(math.sqrt(2*Aisle_Cost_Std)))* math.exp((-1)*math.pow((Product_Price[i]-Aisle_Cost_Mean),2)/(2*math.pow(Aisle_Cost_Std,2))));
            Gaussian_Front_Of_Store_Sales.append((1/(math.sqrt(2*Front_Of_Store_Sales_Std)))* math.exp((-1)*math.pow((Product_Sales_Volume[i]-Front_Of_Store_Sales_Mean),2)/(2*math.pow(Front_Of_Store_Sales_Std,2))));
            Gaussian_Front_Of_Store_Cost.append((1/(math.sqrt(2*Front_Of_Store_Cost_Std)))* math.exp((-1)*math.pow((Product_Price[i]-Front_Of_Store_Cost_Mean),2)/(2*math.pow(Front_Of_Store_Cost_Std,2))));
            Gaussian_End_Cap_Sales.append((1/(math.sqrt(2*End_Cap_Sales_Std)))* math.exp((-1)*math.pow((Product_Sales_Volume[i]-End_Cap_Sales_Mean),2)/(2*math.pow(End_Cap_Sales_Std,2))));
            Gaussian_End_Cap_Cost.append((1/(math.sqrt(2*End_Cap_Cost_Std)))* math.exp((-1)*math.pow((Product_Price[i]-End_Cap_Cost_Mean),2)/(2*math.pow(End_Cap_Cost_Std,2))));
         else:
            return([Gaussian_Sales,Gaussian_Cost,Gaussian_Aisle_Sales,Gaussian_Aisle_Cost,Gaussian_Front_Of_Store_Sales,Gaussian_Front_Of_Store_Cost,Gaussian_End_Cap_Sales,Gaussian_End_Cap_Cost]);
      return([Gaussian_Sales,Gaussian_Cost,Gaussian_Aisle_Sales,Gaussian_Aisle_Cost,Gaussian_Front_Of_Store_Sales,Gaussian_Front_Of_Store_Cost,Gaussian_End_Cap_Sales,Gaussian_End_Cap_Cost]);

   def Model(self,X,w):
      X = w[0]+np.dot(X,w[1:]);
      return(X);

   def Nonlinear_Sine_Model(self,X,w):
      X = np.sin(self.Model(X,w));
      return(X);

   def Model_Standard_Deviation_Softmax(self,X,W):
      X = self.Nonlinear_Sine_Model(X,W);
      X = np.log(1+np.exp((-1)*(self.Nonlinear_Sine_Model(X,W))));
      return(X);

   def Nonlinear_Transformational_Sales_Cost(self,Data_File,Product_Sales_List,Product_Cost_List,Product_ID_List,Product_Sales_Weights,Product_Cost_Weights,i):
      Product_ID = Data_File[0];
      Product_Sales_Volume = Data_File[8];
      Product_Price = Data_File[10];
      Product_Sales = [];
      Product_Cost = [];
      Product_Sales = self.Model_Standard_Deviation_Softmax(Product_Sales_Volume,Product_Sales_Weights);
      Product_Cost =  self.Model_Standard_Deviation_Softmax(Product_Price,Product_Cost_Weights);
      #Product_Sales_Weights = [1,1,2,1];
      #Product_Cost_Weights = [1,1,2,1];
      j = 0;
      for i in range(len(Product_ID)):
         if(i < len(Product_ID) and j < len(Product_Sales_Weights) and j < len(Product_Cost_Weights)):
            Product_Sales_List.append(Product_Sales[i]);
            Product_Cost_List.append(Product_Cost[i]);
            Product_ID_List.append(Product_ID[i]);
         elif(i < len(Product_ID) and ((j == len(Product_Sales_Weights)) or (j == len(Product_Cost_Weights)))):
            j = j+1;
         else:
            return([Product_Sales_List,Product_Cost_List,Product_ID_List]);
      return([Product_Sales_List,Product_Cost_List,Product_ID_List]);

   def Prediction_Inference_Model(self,Inference_Dataset,train_Dataset,test_Dataset,Product_ID,Prediction_Product_ID,weights,Prediction_Sales_List,Prediction_Cost_List):
      Inference_Dataset.append(Inference_Dataset[i]);
      for i in range(len(test_Dataset)):
         if(i < len(test_Dataset)):
            if((Inference_Dataset[i] - test_Dataset[i]) <=  0.95):
               Prediction_Sales_List.append(Inference_Dataset[i]);
               Prediction_Cost_List.append(Inference_Dataset[i]);
               Prediction_Product_ID.append(Product_ID[i]);
         else:
            return([[Prediction_Sales_List],[Prediction_Cost_List],[Prediction_Product_ID]]);
      return([[Prediction_Sales_List],[Prediction_Cost_List],[Prediction_Product_ID]]);

   def Model_Predictions(self,Product_Sales_List,Product_Cost_List,train_Dataset,test_Dataset,Product_ID,Prediction_Product_ID,Product_Sales_Weights,Product_Cost_Weights,Prediction_Sales_List,Prediction_Cost_List):
      train_Dataset = Product_Sales_List[:15000];
      test_Dataset = Product_Sales_List[15001:];
      #Inference_Dataset = Product_Sales_List[int(len(train_Dataset))+1:];
      Inference_Dataset = self.Nonlinear_Sine_Model(Inference_Dataset,Product_Sales_Weights[15001:]);
      Trained_Dataset = self.Nonlinear_Sine_Model(train_Dataset,Product_Sales_Weights[:15000]);
      Prediction_Sales_List = self.Prediction_Inference_Model(Inference_Dataset,train_Dataset,test_Dataset,Product_ID,Prediction_Product_ID,Product_Sales_Weights,Product_Cost_Weights,Prediction_Sales_List,Prediction_Cost_List)[0];
      Prediction_Cost_List =  self.Prediction_Inference_Model(Inference_Dataset,train_Dataset,test_Dataset,Product_ID,Prediction_Product_ID,Product_Sales_Weights,Product_Cost_Weights,Prediction_Sales_List,Prediction_Cost_List)[1];
      Prediction_Product_ID = self.Prediction_Inference_Model(Inference_Dataset,train_Dataset,test_Dataset,Product_ID,Prediction_Product_ID,Product_Sales_Weights,Product_Cost_Weights,Prediction_Sales_List,Prediction_Cost_List)[2];
      return([[Prediction_Sales_List],[Prediction_Cost_List],[Prediction_Product_ID]]);

   def Pie_Chart_Visuals(self,Product_Sales_List,Product_Cost_List):
      #Pie chart styles to update the gallery with nogrid.
      plt.style.use('_mpl-gallery-nogrid')
      # make data
      #x = Product_Section_Output; #[1, 2, 3, 4]
      #x = Product_Season_Output;
      #x = Product_Position_Output;
      #x = Product_Material_Output;
      #x = Product_Origin_Output;
      # Plot colour addition to shell pie charts.
      x=[];
      y = [];
      #x = #[1,2,3,4];#[1,2,3,4,5,6,7,8,10,50,25,45,32,98,76]
      x = Product_Sales_List;
      y = Product_Cost_List;
      #y = Product_Cost_List;
      #colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len(x)))
      # ploting
      fig, ax = plt.subplots();
      #ax.pie(x, colors=colors, radius=3, center=(1527, 1527),wedgeprops={"linewidth": 1, "edgecolor": "green"}, frame=True);
      #s = x**2;#math.pow(x,2);
      s = x;
      plt.scatter(x,y,marker = r'$\diamond$',label="Product Sales VS Price in $");
      #color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']);
      plt.xlabel("Product Sales");
      plt.ylabel("Product Price in $");
      #plt.plot(x,y);
      #ax.set(xlim=(950, 2000), xticks=np.arange(957, 2000),
      #ylim=(950, 2000), yticks=np.arange(957, 2000));
      plt.show();
      return(None);

   def Pie_Chart_Visuals_Position(self,Product_Sales_Aisle,Product_Cost_Aisle,Product_Sales_Front_Of_Store,Product_Cost_Front_Of_Store,Product_Sales_End_Cap,Product_Cost_End_Cap):
      plt.style.use('_mpl-gallery-nogrid');
      x = [];
      y =[];
      x = Product_Sales_Aisle; #Product_Sales_Front_Of_Store;#Product_Sales_End_Cap;
      y = Product_Cost_Aisle;  #Product_Cost_Front_Of_Store;#Product_Cost_End_Cap;
      fig, ax = plt.subplots();
      plt.scatter(x,y,marker = r'$\alpha$',label="Product Sales Vs Price at Aisle");
      plt.xlabel("Product Sales");
      plt.ylabel("Product Price in $");
      plt.show();
      print("\n\n\n")
      t = [];
      u = [];
      t = Product_Sales_Front_Of_Store;
      u = Product_Cost_Front_Of_Store;
      fig, ax = plt.subplots();
      plt.scatter(t,u,marker = r'$\alpha$',label="Product Sales vs Price at Front of Store");
      plt.xlabel("Product Sales from Front of Store");
      plt.ylabel("Front of store products sold for $");
      plt.show();
      print("\n\n\n")
      v = [];
      w = [];
      v = Product_Sales_End_Cap;
      w = Product_Cost_End_Cap;
      fig, ax = plt.subplots();
      plt.scatter(v,w,marker = r'$\alpha$',label="Product Sales vs Price at Rare side of store");
      plt.xlabel("Product Sales from Front of Store");
      plt.ylabel("Front of store products sold for $");
      plt.show();
      return(None)


   '''def Plot_Histograms(self,Product_Gaussian_Sales,Product_Gaussian_Sales_Aisle,Product_Gaussian_Sales_Front_Of_Store,Product_Gaussian_Sales_End_Cap,Product_Gaussian_Cost,Product_Gaussian_Cost_Aisle,Product_Gaussian_Cost_Front_Of_Store,Product_Gaussian_Cost_End_Cap):
      x = Product_Gaussian_Sales;
      y = Product_Gaussian_Sales_Aisle;
      z = Product_Gaussian_Sales_Front_Of_Store;
      t = Product_Gaussian_Sales_End_Cap;
      u = Product_Gaussian_Cost;
      v = Product_Gaussian_Cost_Aisle;
      w = Product_Gaussian_Cost_Front_Of_Store;
      x = Product_Gaussian_Cost_End_Cap;

      fig, ax = plt.subplots();

      bins = ax.hist(x,bins=40,density = True,label = "Product Gaussian Sales");
      ax.plot(x,bins,'--');
      plt.xlabel("Product Sales Volume");
      plt.ylabel("Product Sold for $");
      plt.show();
      return(None)'''

   def CSV_Reader(self):
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
      Product_Sales_File = [];
      Product_Sales_Computation = [];
      Product_Cost_Computation = [];
      i = 0;
      Product_Sales_List = [];
      Product_Cost_List = [];
      Product_Sales_Cost_Compute = [];
      Product_ID_List = [];
      Product_Sales_Number = 0.0;
      Product_Cost_Dollars = 0.0;
      Product_Sales_File = [Product_ID,Product_Name,Product_Description,Product_Terms,Product_Promotion,Product_Position,Product_URL,Product_Category,Product_Sales_Volume,Product_Section,Product_Price,Product_Seasonal,Product_Season,Product_Currency,Product_Material,Product_Origin,Product_Brand];
      #print("Product Column to demsonstrate Sales and price of each item bought during seasonal activity from the regional sales point.",Product_Sales_Volume,"with an amount of $",Product_Price);
      #print(Product_Sales_File);
      Product_Sales_List = self.Business_Sales_Cost_Volume_Compute(Product_Sales_File,Product_Sales_List,Product_Cost_List,i)[0];
      Product_Cost_List = self.Business_Sales_Cost_Volume_Compute(Product_Sales_File,Product_Sales_List,Product_Cost_List,i)[1];
      print("Sales of the Products:\n",np.sum(Product_Sales_List),"Products Sold for $:\n",np.sum(Product_Cost_List));
      self.Pie_Chart_Visuals(Product_Sales_List,Product_Cost_List);
      Product_Sales_Aisle = [];
      Product_Cost_Aisle = [];
      Product_Sales_Front_Of_Store = [];
      Product_Cost_Front_Of_Store = [];
      Product_Sales_End_Cap = [];
      Product_Cost_End_Cap = [];
      Product_ID_Aisle_List = [];
      Product_ID_Front_Of_Store_List = [];
      Product_ID_End_Cap_List = [];
      Product_Sales_Aisle = self.Product_Position_Compute(Product_Sales_File,Product_Sales_Aisle,Product_Cost_Aisle,Product_Sales_Front_Of_Store,Product_Cost_Front_Of_Store,Product_Sales_End_Cap,Product_Cost_End_Cap,Product_ID_Aisle_List,Product_ID_Front_Of_Store_List,Product_ID_End_Cap_List,i)[0];
      Product_Cost_Aisle = self.Product_Position_Compute(Product_Sales_File,Product_Sales_Aisle,Product_Cost_Aisle,Product_Sales_Front_Of_Store,Product_Cost_Front_Of_Store,Product_Sales_End_Cap,Product_Cost_End_Cap,Product_ID_Aisle_List,Product_ID_Front_Of_Store_List,Product_ID_End_Cap_List,i)[3];
      Product_Sales_Front_Of_Store = self.Product_Position_Compute(Product_Sales_File,Product_Sales_Aisle,Product_Cost_Aisle,Product_Sales_Front_Of_Store,Product_Cost_Front_Of_Store,Product_Sales_End_Cap,Product_Cost_End_Cap,Product_ID_Aisle_List,Product_ID_Front_Of_Store_List,Product_ID_End_Cap_List,i)[1];
      Product_Cost_Front_Of_Store = self.Product_Position_Compute(Product_Sales_File,Product_Sales_Aisle,Product_Cost_Aisle,Product_Sales_Front_Of_Store,Product_Cost_Front_Of_Store,Product_Sales_End_Cap,Product_Cost_End_Cap,Product_ID_Aisle_List,Product_ID_Front_Of_Store_List,Product_ID_End_Cap_List,i)[4];
      Product_Sales_End_Cap = self.Product_Position_Compute(Product_Sales_File,Product_Sales_Aisle,Product_Cost_Aisle,Product_Sales_Front_Of_Store,Product_Cost_Front_Of_Store,Product_Sales_End_Cap,Product_Cost_End_Cap,Product_ID_Aisle_List,Product_ID_Front_Of_Store_List,Product_ID_End_Cap_List,i)[2];
      Product_Cost_End_Cap = self.Product_Position_Compute(Product_Sales_File,Product_Sales_Aisle,Product_Cost_Aisle,Product_Sales_Front_Of_Store,Product_Cost_Front_Of_Store,Product_Sales_End_Cap,Product_Cost_End_Cap,Product_ID_Aisle_List,Product_ID_Front_Of_Store_List,Product_ID_End_Cap_List,i)[5];
      Product_ID_Aisle_List = self.Product_Position_Compute(Product_Sales_File,Product_Sales_Aisle,Product_Cost_Aisle,Product_Sales_Front_Of_Store,Product_Cost_Front_Of_Store,Product_Sales_End_Cap,Product_Cost_End_Cap,Product_ID_Aisle_List,Product_ID_Front_Of_Store_List,Product_ID_End_Cap_List,i)[6];
      Product_ID_Front_Of_Store_List = self.Product_Position_Compute(Product_Sales_File,Product_Sales_Aisle,Product_Cost_Aisle,Product_Sales_Front_Of_Store,Product_Cost_Front_Of_Store,Product_Sales_End_Cap,Product_Cost_End_Cap,Product_ID_Aisle_List,Product_ID_Front_Of_Store_List,Product_ID_End_Cap_List,i)[7];
      Product_ID_End_Cap_List = self.Product_Position_Compute(Product_Sales_File,Product_Sales_Aisle,Product_Cost_Aisle,Product_Sales_Front_Of_Store,Product_Cost_Front_Of_Store,Product_Sales_End_Cap,Product_Cost_End_Cap,Product_ID_Aisle_List,Product_ID_Front_Of_Store_List,Product_ID_End_Cap_List,i)[8];

      print("Sales Volume of the Products placed at Aisle stage of the store:\n",np.sum(Product_Sales_Aisle),"Aisle store cloths are Sold for $:\n",np.sum(Product_Cost_Aisle));
      print("Sales Volume of the Products placed at Front side of the store:\n",np.sum(Product_Sales_Front_Of_Store),"The clothes placed at Front side of the store Sold for $:\n",np.sum(Product_Cost_Front_Of_Store));
      print("Sales Volume of the Products placed at End of the store:\n",np.sum(Product_Sales_End_Cap),"The clothes placed at Rare side of the store sold for $:\n",np.sum(Product_Cost_End_Cap));
      self.Pie_Chart_Visuals_Position(Product_Sales_Aisle,Product_Cost_Aisle,Product_Sales_Front_Of_Store,Product_Cost_Front_Of_Store,Product_Sales_End_Cap,Product_Cost_End_Cap);

      Product_Gaussian_Sales = [];
      Product_Gaussian_Cost = [];
      Product_Gaussian_Sales_Aisle = [];
      Product_Gaussian_Cost_Aisle =[];
      Product_Gaussian_Sales_Front_Of_Store = [];
      Product_Gaussian_Cost_Front_Of_Store = [];
      Product_Gaussian_Sales_End_Cap = [];
      Product_Gaussian_Cost_End_Cap = [];

      Product_Gaussian_Sales = self.Standard_Normalized_Sales(Product_Sales_File,Product_Sales_List,Product_Cost_List,Product_Sales_Aisle,Product_Sales_Front_Of_Store,Product_Sales_End_Cap,Product_Cost_Aisle,Product_Cost_Front_Of_Store,Product_Cost_End_Cap,i)[0];
      Product_Gaussian_Cost = self.Standard_Normalized_Sales(Product_Sales_File,Product_Sales_List,Product_Cost_List,Product_Sales_Aisle,Product_Sales_Front_Of_Store,Product_Sales_End_Cap,Product_Cost_Aisle,Product_Cost_Front_Of_Store,Product_Cost_End_Cap,i)[1];
      Product_Gaussian_Sales_Aisle = self.Standard_Normalized_Sales(Product_Sales_File,Product_Sales_List,Product_Cost_List,Product_Sales_Aisle,Product_Sales_Front_Of_Store,Product_Sales_End_Cap,Product_Cost_Aisle,Product_Cost_Front_Of_Store,Product_Cost_End_Cap,i)[2];
      Product_Gaussian_Cost_Aisle = self.Standard_Normalized_Sales(Product_Sales_File,Product_Sales_List,Product_Cost_List,Product_Sales_Aisle,Product_Sales_Front_Of_Store,Product_Sales_End_Cap,Product_Cost_Aisle,Product_Cost_Front_Of_Store,Product_Cost_End_Cap,i)[3];
      Product_Gaussian_Sales_Front_Of_Store = self.Standard_Normalized_Sales(Product_Sales_File,Product_Sales_List,Product_Cost_List,Product_Sales_Aisle,Product_Sales_Front_Of_Store,Product_Sales_End_Cap,Product_Cost_Aisle,Product_Cost_Front_Of_Store,Product_Cost_End_Cap,i)[4];
      Product_Gaussian_Cost_Front_Of_Store = self.Standard_Normalized_Sales(Product_Sales_File,Product_Sales_List,Product_Cost_List,Product_Sales_Aisle,Product_Sales_Front_Of_Store,Product_Sales_End_Cap,Product_Cost_Aisle,Product_Cost_Front_Of_Store,Product_Cost_End_Cap,i)[5];
      Product_Gaussian_Sales_End_Cap = self.Standard_Normalized_Sales(Product_Sales_File,Product_Sales_List,Product_Cost_List,Product_Sales_Aisle,Product_Sales_Front_Of_Store,Product_Sales_End_Cap,Product_Cost_Aisle,Product_Cost_Front_Of_Store,Product_Cost_End_Cap,i)[6];
      Product_Gaussian_Cost_End_Cap = self.Standard_Normalized_Sales(Product_Sales_File,Product_Sales_List,Product_Cost_List,Product_Sales_Aisle,Product_Sales_Front_Of_Store,Product_Sales_End_Cap,Product_Cost_Aisle,Product_Cost_Front_Of_Store,Product_Cost_End_Cap,i)[7];

      print("Sales of Gaussian components Sales list, Aisle Sales, Front Of Store and End Cap Sales: \n",np.sum(Product_Gaussian_Sales),"\n",np.sum(Product_Gaussian_Sales_Aisle),"\n",np.sum(Product_Gaussian_Sales_Front_Of_Store),"\n",np.sum(Product_Gaussian_Sales_End_Cap),"\n");
      print("Cost of Gaussian components Cost list, Aisle Cost, Front Of Store and End Cap Cost: \n",np.sum(Product_Gaussian_Cost),"\n",np.sum(Product_Gaussian_Cost_Aisle),"\n",np.sum(Product_Gaussian_Cost_Front_Of_Store),"\n",np.sum(Product_Gaussian_Cost_End_Cap),"\n");

      #self.Plot_Histograms(Product_Gaussian_Sales,Product_Gaussian_Sales_Aisle,Product_Gaussian_Sales_Front_Of_Store,Product_Gaussian_Sales_End_Cap,Product_Gaussian_Cost,Product_Gaussian_Cost_Aisle,Product_Gaussian_Cost_Front_Of_Store,Product_Gaussian_Cost_End_Cap);
      Product_Sales_List = [];
      Product_Cost_List = [];
      Product_ID = [];
      i = 0;
      Product_Sales_Weigths = [];
      Product_Cost_Weights = [];
      #Product_Sales_Weights = Even_Odd_Gen_Weights;
      Product_Sales_Weights = eong.Even_Odd_Number_Generator().__initialization__();
      Product_Cost_Weights = eong.Even_Odd_Number_Generator().__initialization__();

      Product_Sales_List = self.Nonlinear_Transformational_Sales_Cost(Product_Sales_File,Product_Sales_List,Product_Cost_List,Product_ID,Product_Sales_Weights,Product_Cost_Weights,i)[0];
      Product_Cost_List = self.Nonlinear_Transformational_Sales_Cost(Product_Sales_File,Product_Sales_List,Product_Cost_List,Product_ID,Product_Sales_Weights,Product_Cost_Weights,i)[1];
      Product_ID_List = self.Nonlinear_Transformational_Sales_Cost(Product_Sales_File,Product_Sales_List,Product_Cost_List,Product_ID,Product_Sales_Weights,Product_Cost_Weights,i)[2];
      print("Product Sales List values: ",Product_Sales_List[20200:],"\n Product Price List: ",Product_Cost_List[20200:],"\n Product ID List values: ",Product_ID_List[20200:]);
      Prediction_Sales_List = [];
      Prediction_Cost_List = [];
      train_Dataset = [];
      test_Dataset = [];
      Product_ID = Product_Sales['Product ID'];
      Prediction_Product_ID = [];
      Prediction_Cost_Product_ID = [];
      Prediction_Sales_List = self.Model_Predictions(Product_Sales_List,train_Dataset,test_Dataset,Product_ID,Prediction_Product_ID,Product_Sales_Weights,Product_Cost_Weights,Prediction_Sales_List,Product_Cost_List)[0];
      Prediction_Product_ID  = self.Model_Predictions(Product_Sales_List,train_Dataset,test_Dataset,Product_ID,Prediction_Product_ID,Product_Sales_Weights,Product_Cost_Weights,Prediction_Sales_List,Product_Cost_List)[1];
      Prediction_Cost_List =  self.Model_Predictions(Product_Sales_List,train_Dataset,test_Dataset,Product_ID,Prediction_Product_ID,Product_Sales_Weights,Product_Cost_Weights,Prediction_Sales_List,Prediction_Cost_List)[0];
      Prediction_Cost_Product_ID =  self.Model_Predictions(Product_Sales_List,train_Dataset,test_Dataset,Product_ID,Prediction_Product_ID,Product_Sales_Weights,Product_Cost_Weights,Prediction_Sales_List,Prediction_Cost_List)[1];
      print("Prediction Sales List data consists of: ",Prediction_Sales_List,Prediction_Product_ID);
      print("Prediction Cost List data consists of: ",Prediction_Cost_List,Prediction_Cost_Product_ID);
      #print(self.Business_Sales_Cost_Volume_Compute(Product_Sales_File,Product_Sales_List,Product_Cost_List,i)[2],"\n");
      #print(self.Business_Sales_Cost_Volume_Compute(Product_Sales_File,Product_Sales_List,Product_Cost_List,i)[3],"\n");
      #print(self.Business_Sales_Cost_Volume_Compute(Product_Sales_File,Product_Sales_List,Product_Cost_List,i)[4],"\n");
      #print(self.Business_Sales_Cost_Volume_Compute(Product_Sales_File,Product_Sales_List,Product_Cost_List,i)[5],"\n");
      #print(self.Business_Sales_Cost_Volume_Compute(Product_Sales_File,Product_Sales_List,Product_Cost_List,i)[6]);
      #print("Sales Volume of Man in India, Spain and China for specified product terms are:",Product_Sales_Number,"Sold for $",Product_Cost_Dollars)
      #print("The precision values of the Sales volume:\n",self.Measures_Compute(Product_Sales_Number,Product_Dollars,Product_Sales_Cost_Compute)[0]);
      #print("Amount of Products sold for $",self.Measures_Compute(Product_Sales_Number,Product_Dollars,Product_Sales_Cost_Compute)[1]);
      #Product_Sales_Cost_Compute.append(Product_Sales_Computation,Product_Cost_Computation);
      #print("The Net Sales of Zabra for Woman on regions with specific Materials are: ",Product_Sales_Computation,"Sold for an amount of $",Product_Cost_Computation);
      return(0);

Buss_Comp = Business_Compute();
print(Buss_Comp.CSV_Reader());
