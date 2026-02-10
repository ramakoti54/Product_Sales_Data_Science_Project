import numpy as np;
import pandas as pd;
import matplotlib.pyplot as pyplt;
import math;
#import Even_Odd_Random_Number_Generator as eong;
import Analyse_Business_Revenue as ABR;
import Dynamic_Variable_Generator as DVG;

class Business_Sales_Price_Revenue_Report:

   def Business_Sales_Computation(Product_Sales_File,Product_Sales_List,i,Sales_Autumn_jackets_MAN,Sales_Autumn_jackets_WOMAN,Sales_Autumn_jeans_MAN,Sales_Autumn_jeans_WOMAN,Sales_Autumn_shoes_MAN,Sales_Autumn_shoes_WOMAN,Sales_Autumn_sweaters_MAN,Sales_Autumn_sweaters_WOMAN,Sales_Autumn_t_shirts_MAN,Sales_Autumn_t_shirts_WOMAN,Sales_Spring_jackets_MAN,Sales_Spring_jackets_WOMAN,Sales_Spring_jeans_MAN,Sales_Spring_jeans_WOMAN,Sales_Spring_shoes_MAN,Sales_Spring_shoes_WOMAN,Sales_Spring_sweaters_MAN,Sales_Spring_sweaters_WOMAN,Sales_Spring_t_shirts_MAN,Sales_Spring_t_shirts_WOMAN,Sales_Summer_jackets_MAN,Sales_Summer_jackets_WOMAN,Sales_Summer_jeans_MAN,Sales_Summer_jeans_WOMAN,Sales_Summer_shoes_MAN,Sales_Summer_shoes_WOMAN,Sales_Summer_sweaters_MAN,Sales_Summer_sweaters_WOMAN,Sales_Summer_t_shirts_MAN,Sales_Summer_t_shirts_WOMAN,Sales_Winter_jackets_MAN,Sales_Winter_jackets_WOMAN,Sales_Winter_jeans_MAN,Sales_Winter_jeans_WOMAN,Sales_Winter_shoes_MAN,Sales_Winter_shoes_WOMAN,Sales_Winter_sweaters_MAN,Sales_Winter_sweaters_WOMAN,Sales_Winter_t_shirts_MAN,Sales_Winter_t_shirts_WOMAN):
      
      Product_ID = Product_Sales_File[0];
      Product_Sales_Volume = Product_Sales_File[8];
      Product_Terms = Product_Sales_File[3];
      Product_Section = Product_Sales_File[9];
      Product_Price = Product_Sales_File[10];
      Product_Season = Product_Sales_File[12];
      Product_ Material = Product_Sales_File[14];
      
      for i in range(len(Product_ID)):
         if(i < len(Product_ID) and Product_Section[i] == 'MAN' and Product_Season[i] == 'Winter'):
            if(Product_Terms[i] == 'jackets' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):
               Sales_Winter_jackets_MAN.append(Product_Sales_Volume[i]);
            elif(Product_Terms[i] == 'jeans' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):   
               Sales_Winter_jeans_MAN.append(Product_Sales_Volume[i]);
            elif(Product_Terms[i] == 't-shirts' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):   
               Sales_Winter_t_shirts_MAN.append(Product_Sales_Volume[i]);
            elif(Product_Terms[i] == 'sweaters' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):   
               Sales_Winter_sweaters_MAN.append(Product_Sales_Volume[i]);
            elif(Product_Terms[i] == 'shoes' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):   
               Sales_Winter_shoes_MAN.append(Product_Sales_Volume[i]);
            else:
               continue;
         elif(i < len(Product_ID) and Product_Section[i] == 'MAN' and Product_Season[i] == 'Spring'):
            if(Product_Terms[i] == 'jackets' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):
               Sales_Spring_jackets_MAN.append(Product_Sales_Volume[i]);
            elif(Product_Terms[i] == 'jeans' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):   
               Sales_Spring_jeans_MAN.append(Product_Sales_Volume[i]);
            elif(Product_Terms[i] == 't-shirts' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):   
               Sales_Spring_t_shirts_MAN.append(Product_Sales_Volume[i]);
            elif(Product_Terms[i] == 'sweaters' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):   
               Sales_Spring_sweaters_MAN.append(Product_Sales_Volume[i]);
            elif(Product_Terms[i] == 'shoes' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):   
               Sales_Spring_shoes_MAN.append(Product_Sales_Volume[i]);
            else:
               continue;
         elif(i < len(Product_ID) and Product_Section[i] == 'MAN' and Product_Season[i] == 'Summer'):
            if(Product_Terms[i] == 'jackets' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):
               Sales_Summer_jackets_MAN.append(Product_Sales_Volume[i]);
            elif(Product_Terms[i] == 'jeans' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):   
               Sales_Summer_jeans_MAN.append(Product_Sales_Volume[i]);
            elif(Product_Terms[i] == 't-shirts' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):   
               Sales_Summer_t_shirts_MAN.append(Product_Sales_Volume[i]);
            elif(Product_Terms[i] == 'sweaters' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):   
               Sales_Summer_sweaters_MAN.append(Product_Sales_Volume[i]);
            elif(Product_Terms[i] == 'shoes' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):   
               Sales_Summer_shoes_MAN.append(Product_Sales_Volume[i]);
            else:
               continue;
         elif(i < len(Product_ID) and Product_Section[i] == 'MAN' and Product_Season[i] == 'Autumn'):
            if(Product_Terms[i] == 'jackets' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):
               Sales_Autumn_jackets_MAN.append(Product_Sales_Volume[i]);
            elif(Product_Terms[i] == 'jeans' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):   
               Sales_Autumn_jeans_MAN.append(Product_Sales_Volume[i]);
            elif(Product_Terms[i] == 't-shirts' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):   
               Sales_Autumn_t_shirts_MAN.append(Product_Sales_Volume[i]);
            elif(Product_Terms[i] == 'sweaters' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):   
               Sales_Autumn_sweaters_MAN.append(Product_Sales_Volume[i]);
            elif(Product_Terms[i] == 'shoes' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):   
               Sales_Autumn_shoes_MAN.append(Product_Sales_Volume[i]);
            else:
               continue;
         
         elif(i < len(Product_ID) and Product_Section[i] == 'WOMAN' and Product_Season[i] == 'Winter'):
            if(Product_Terms[i] == 'jackets' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):
               Sales_Winter_jackets_WOMAN.append(Product_Sales_Volume[i]);
            elif(Product_Terms[i] == 'jeans' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):   
               Sales_Winter_jeans_WOMAN.append(Product_Sales_Volume[i]);
            elif(Product_Terms[i] == 't-shirts' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):   
               Sales_Winter_t_shirts_WOMAN.append(Product_Sales_Volume[i]);
            elif(Product_Terms[i] == 'sweaters' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):   
               Sales_Winter_sweaters_WOMAN.append(Product_Sales_Volume[i]);
            elif(Product_Terms[i] == 'shoes' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):   
               Sales_Winter_shoes_WOMAN.append(Product_Sales_Volume[i]);
            else:
               continue;
         elif(i < len(Product_ID) and Product_Section[i] == 'WOMAN' and Product_Season[i] == 'Spring'):
            if(Product_Terms[i] == 'jackets' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):
               Sales_Spring_jackets_WOMAN.append(Product_Sales_Volume[i]);
            elif(Product_Terms[i] == 'jeans' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):   
               Sales_Spring_jeans_WOMAN.append(Product_Sales_Volume[i]);
            elif(Product_Terms[i] == 't-shirts' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):   
               Sales_Spring_t_shirts_WOMAN.append(Product_Sales_Volume[i]);
            elif(Product_Terms[i] == 'sweaters' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):   
               Sales_Spring_sweaters_WOMAN.append(Product_Sales_Volume[i]);
            elif(Product_Terms[i] == 'shoes' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):   
               Sales_Spring_shoes_WOMAN.append(Product_Sales_Volume[i]);
            else:
               continue;
         elif(i < len(Product_ID) and Product_Section[i] == 'WOMAN' and Product_Season[i] == 'Summer'):
            if(Product_Terms[i] == 'jackets' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):
               Sales_Summer_jackets_WOMAN.append(Product_Sales_Volume[i]);
            elif(Product_Terms[i] == 'jeans' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):   
               Sales_Summer_jeans_WOMAN.append(Product_Sales_Volume[i]);
            elif(Product_Terms[i] == 't-shirts' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):   
               Sales_Summer_t_shirts_WOMAN.append(Product_Sales_Volume[i]);
            elif(Product_Terms[i] == 'sweaters' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):   
               Sales_Summer_sweaters_WOMAN.append(Product_Sales_Volume[i]);
            elif(Product_Terms[i] == 'shoes' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):   
               Sales_Summer_shoes_WOMAN.append(Product_Sales_Volume[i]);
            else:
               continue;
         elif(i < len(Product_ID) and Product_Section[i] == 'WOMAN' and Product_Season[i] == 'Autumn'):
            if(Product_Terms[i] == 'jackets' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):
               Sales_Autumn_jackets_WOMAN.append(Product_Sales_Volume[i]);
            elif(Product_Terms[i] == 'jeans' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):   
               Sales_Autumn_jeans_WOMAN.append(Product_Sales_Volume[i]);
            elif(Product_Terms[i] == 't-shirts' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):   
               Sales_Autumn_t_shirts_WOMAN.append(Product_Sales_Volume[i]);
            elif(Product_Terms[i] == 'sweaters' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):   
               Sales_Autumn_sweaters_WOMAN.append(Product_Sales_Volume[i]);
            elif(Product_Terms[i] == 'shoes' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):   
               Sales_Autumn_shoes_WOMAN.append(Product_Sales_Volume[i]);
            else:
               continue;
         else:
            continue;
      Product_Sales_List = [Sales_Autumn_jackets_MAN,Sales_Autumn_jackets_WOMAN,Sales_Autumn_jeans_MAN,Sales_Autumn_jeans_WOMAN,Sales_Autumn_shoes_MAN,Sales_Autumn_shoes_WOMAN,Sales_Autumn_sweaters_MAN,Sales_Autumn_sweaters_WOMAN,Sales_Autumn_t_shirts_MAN,Sales_Autumn_t_shirts_WOMAN,Sales_Spring_jackets_MAN,Sales_Spring_jackets_WOMAN,Sales_Spring_jeans_MAN,Sales_Spring_jeans_WOMAN,Sales_Spring_shoes_MAN,Sales_Spring_shoes_WOMAN,Sales_Spring_sweaters_MAN,Sales_Spring_sweaters_WOMAN,Sales_Spring_t_shirts_MAN,Sales_Spring_t_shirts_WOMAN,Sales_Summer_jackets_MAN,Sales_Summer_jackets_WOMAN,Sales_Summer_jeans_MAN,Sales_Summer_jeans_WOMAN,Sales_Summer_shoes_MAN,Sales_Summer_shoes_WOMAN,Sales_Summer_sweaters_MAN,Sales_Summer_sweaters_WOMAN,Sales_Summer_t_shirts_MAN,Sales_Summer_t_shirts_WOMAN,Sales_Winter_jackets_MAN,Sales_Winter_jackets_WOMAN,Sales_Winter_jeans_MAN,Sales_Winter_jeans_WOMAN,Sales_Winter_shoes_MAN,Sales_Winter_shoes_WOMAN,Sales_Winter_sweaters_MAN,Sales_Winter_sweaters_WOMAN,Sales_Winter_t_shirts_MAN,Sales_Winter_t_shirts_WOMAN];      
      return(Product_Sales_List);

   def Business_Price_computation(Product_Sales_File,Product_Price_List,i,Price_Autumn_jackets_MAN,Price_Autumn_jackets_WOMAN,Price_Autumn_jeans_MAN,Price_Autumn_jeans_WOMAN,Price_Autumn_shoes_MAN,Price_Autumn_shoes_WOMAN,Price_Autumn_sweaters_MAN,Price_Autumn_sweaters_WOMAN,Price_Autumn_t_shirts_MAN,Price_Autumn_t_shirts_WOMAN,Price_Spring_jackets_MAN,Price_Spring_jackets_WOMAN,Price_Spring_jeans_MAN,Price_Spring_jeans_WOMAN,Price_Spring_shoes_MAN,Price_Spring_shoes_WOMAN,Price_Spring_sweaters_MAN,Price_Spring_sweaters_WOMAN,Price_Spring_t_shirts_MAN,Price_Spring_t_shirts_WOMAN,Price_Summer_jackets_MAN,Price_Summer_jackets_WOMAN,Price_Summer_jeans_MAN,Price_Summer_jeans_WOMAN,Price_Summer_shoes_MAN,Price_Summer_shoes_WOMAN,Price_Summer_sweaters_MAN,Price_Summer_sweaters_WOMAN,Price_Summer_t_shirts_MAN,Price_Summer_t_shirts_WOMAN,Price_Winter_jackets_MAN,Price_Winter_jackets_WOMAN,Price_Winter_jeans_MAN,Price_Winter_jeans_WOMAN,Price_Winter_shoes_MAN,Price_Winter_shoes_WOMAN,Price_Winter_sweaters_MAN,Price_Winter_sweaters_WOMAN,Price_Winter_t_shirts_MAN,Price_Winter_t_shirts_WOMAN):

      Product_ID = Product_Sales_File[0];
      Product_Sales_Volume = Product_Sales_File[8];
      Product_Terms = Product_Sales_File[3];
      Product_Section = Product_Sales_File[9];
      Product_Price = Product_Sales_File[10];
      Product_Season = Product_Sales_File[12];
      Product_ Material = Product_Sales_File[14];
      
      for i in range(len(Product_ID)):
         if(i < len(Product_ID) and Product_Section[i] == 'MAN' and Product_Season[i] == 'Winter'):
            if(Product_Terms[i] == 'jackets' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):
               Price_Winter_jackets_MAN.append(Product_Price[i]);
            elif(Product_Terms[i] == 'jeans' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):   
               Price_Winter_jeans_MAN.append(Product_Price[i]);
            elif(Product_Terms[i] == 't-shirts' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):   
               Price_Winter_t_shirts_MAN.append(Product_Price[i]);
            elif(Product_Terms[i] == 'sweaters' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):   
               Price_Winter_sweaters_MAN.append(Product_Price[i]);
            elif(Product_Terms[i] == 'shoes' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):   
               Price_Winter_shoes_MAN.append(Product_Price[i]);
            else:
               continue;
         elif(i < len(Product_ID) and Product_Section[i] == 'MAN' and Product_Season[i] == 'Spring'):
            if(Product_Terms[i] == 'jackets' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):
               Price_Spring_jackets_MAN.append(Product_Price[i]);
            elif(Product_Terms[i] == 'jeans' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):   
               Price_Spring_jeans_MAN.append(Product_Price[i]);
            elif(Product_Terms[i] == 't-shirts' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):   
               Price_Spring_t_shirts_MAN.append(Product_Price[i]);
            elif(Product_Terms[i] == 'sweaters' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):   
               Price_Spring_sweaters_MAN.append(Product_Price[i]);
            elif(Product_Terms[i] == 'shoes' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):   
               Price_Spring_shoes_MAN.append(Product_Price[i]);
            else:
               continue;
         elif(i < len(Product_ID) and Product_Section[i] == 'MAN' and Product_Season[i] == 'Summer'):
            if(Product_Terms[i] == 'jackets' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):
               Price_Summer_jackets_MAN.append(Product_Price[i]);
            elif(Product_Terms[i] == 'jeans' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):   
               Price_Summer_jeans_MAN.append(Product_Price[i]);
            elif(Product_Terms[i] == 't-shirts' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):   
               Price_Summer_t_shirts_MAN.append(Product_Price[i]);
            elif(Product_Terms[i] == 'sweaters' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):   
               Price_Summer_sweaters_MAN.append(Product_Price[i]);
            elif(Product_Terms[i] == 'shoes' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):   
               Price_Summer_shoes_MAN.append(Product_Price[i]);
            else:
               continue;
         elif(i < len(Product_ID) and Product_Section[i] == 'MAN' and Product_Season[i] == 'Autumn'):
            if(Product_Terms[i] == 'jackets' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):
               Price_Autumn_jackets_MAN.append(Product_Price[i]);
            elif(Product_Terms[i] == 'jeans' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):   
               Price_Autumn_jeans_MAN.append(Product_Price[i]);
            elif(Product_Terms[i] == 't-shirts' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):   
               Price_Autumn_t_shirts_MAN.append(Product_Price[i]);
            elif(Product_Terms[i] == 'sweaters' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):   
               Price_Autumn_sweaters_MAN.append(Product_Price[i]);
            elif(Product_Terms[i] == 'shoes' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):   
               Price_Autumn_shoes_MAN.append(Product_Price[i]);
            else:
               continue;
         
         elif(i < len(Product_ID) and Product_Section[i] == 'WOMAN' and Product_Season[i] == 'Winter'):
            if(Product_Terms[i] == 'jackets' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):
               Price_Winter_jackets_WOMAN.append(Product_Price[i]);
            elif(Product_Terms[i] == 'jeans' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):   
               Price_Winter_jeans_WOMAN.append(Product_Price[i]);
            elif(Product_Terms[i] == 't-shirts' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):   
               Price_Winter_t_shirts_WOMAN.append(Product_Price[i]);
            elif(Product_Terms[i] == 'sweaters' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):   
               Price_Winter_sweaters_WOMAN.append(Product_Price[i]);
            elif(Product_Terms[i] == 'shoes' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):   
               Price_Winter_shoes_WOMAN.append(Product_Price[i]);
            else:
               continue;
         elif(i < len(Product_ID) and Product_Section[i] == 'WOMAN' and Product_Season[i] == 'Spring'):
            if(Product_Terms[i] == 'jackets' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):
               Price_Spring_jackets_WOMAN.append(Product_Price[i]);
            elif(Product_Terms[i] == 'jeans' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):   
               Price_Spring_jeans_WOMAN.append(Product_Price[i]);
            elif(Product_Terms[i] == 't-shirts' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):   
               Price_Spring_t_shirts_WOMAN.append(Product_Price[i]);
            elif(Product_Terms[i] == 'sweaters' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):   
               Price_Spring_sweaters_WOMAN.append(Product_Price[i]);
            elif(Product_Terms[i] == 'shoes' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):   
               Price_Spring_shoes_WOMAN.append(Product_Price[i]);
            else:
               continue;
         elif(i < len(Product_ID) and Product_Section[i] == 'WOMAN' and Product_Season[i] == 'Summer'):
            if(Product_Terms[i] == 'jackets' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):
               Price_Summer_jackets_WOMAN.append(Product_Price[i]);
            elif(Product_Terms[i] == 'jeans' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):   
               Price_Summer_jeans_WOMAN.append(Product_Price[i]);
            elif(Product_Terms[i] == 't-shirts' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):   
               Price_Summer_t_shirts_WOMAN.append(Product_Price[i]);
            elif(Product_Terms[i] == 'sweaters' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):   
               Price_Summer_sweaters_WOMAN.append(Product_Price[i]);
            elif(Product_Terms[i] == 'shoes' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):   
               Price_Summer_shoes_WOMAN.append(Product_Price[i]);
            else:
               continue;
         elif(i < len(Product_ID) and Product_Section[i] == 'WOMAN' and Product_Season[i] == 'Autumn'):
            if(Product_Terms[i] == 'jackets' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):
               Price_Autumn_jackets_WOMAN.append(Product_Price[i]);
            elif(Product_Terms[i] == 'jeans' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):   
               Price_Autumn_jeans_WOMAN.append(Product_Price[i]);
            elif(Product_Terms[i] == 't-shirts' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):   
               Price_Autumn_t_shirts_WOMAN.append(Product_Price[i]);
            elif(Product_Terms[i] == 'sweaters' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):   
               Price_Autumn_sweaters_WOMAN.append(Product_Price[i]);
            elif(Product_Terms[i] == 'shoes' and (Product_Material[i] == 'Wool' or Product_Material[i] == 'Wool Blend' or Product_Material[i] == 'Linen' or Product_Material[i] == 'Linen Blend' or Product_Material[i] == 'Denim' or Product_Material[i] == 'Viscose')):   
               Price_Autumn_shoes_WOMAN.append(Product_Price[i]);
            else:
               continue;
      
      Product_Price_List = [Price_Autumn_jackets_MAN,Price_Autumn_jackets_WOMAN,Price_Autumn_jeans_MAN,Price_Autumn_jeans_WOMAN,Price_Autumn_shoes_MAN,Price_Autumn_shoes_WOMAN,Price_Autumn_sweaters_MAN,Price_Autumn_sweaters_WOMAN,Price_Autumn_t_shirts_MAN,Price_Autumn_t_shirts_WOMAN,Price_Spring_jackets_MAN,Price_Spring_jackets_WOMAN,Price_Spring_jeans_MAN,Price_Spring_jeans_WOMAN,Price_Spring_shoes_MAN,Price_Spring_shoes_WOMAN,Price_Spring_sweaters_MAN,Price_Spring_sweaters_WOMAN,Price_Spring_t_shirts_MAN,Price_Spring_t_shirts_WOMAN,Price_Summer_jackets_MAN,Price_Summer_jackets_WOMAN,Price_Summer_jeans_MAN,Price_Summer_jeans_WOMAN,Price_Summer_shoes_MAN,Price_Summer_shoes_WOMAN,Price_Summer_sweaters_MAN,Price_Summer_sweaters_WOMAN,Price_Summer_t_shirts_MAN,Price_Summer_t_shirts_WOMAN,Price_Winter_jackets_MAN,Price_Winter_jackets_WOMAN,Price_Winter_jeans_MAN,Price_Winter_jeans_WOMAN,Price_Winter_shoes_MAN,Price_Winter_shoes_WOMAN,Price_Winter_sweaters_MAN,Price_Winter_sweaters_WOMAN,Price_Winter_t_shirts_MAN,Price_Winter_t_shirts_WOMAN];   
      return(Product_Price_List);   

   def Business_Revenue_Computation(Product_Sales_List,Product_Price_List,i,j,Cost_Autumn_jackets_MAN,Cost_Autumn_jackets_WOMAN,Cost_Autumn_jeans_MAN,Cost_Autumn_jeans_WOMAN,Cost_Autumn_shoes_MAN,Cost_Autumn_shoes_WOMAN,Cost_Autumn_sweaters_MAN,Cost_Autumn_sweaters_WOMAN,Cost_Autumn_t_shirts_MAN,Cost_Autumn_t_shirts_WOMAN,Cost_Spring_jackets_MAN,Cost_Spring_jackets_WOMAN,Cost_Spring_jeans_MAN,Cost_Spring_jeans_WOMAN,Cost_Spring_shoes_MAN,Cost_Spring_shoes_WOMAN,Cost_Spring_sweaters_MAN,Cost_Spring_sweaters_WOMAN,Cost_Spring_t_shirts_MAN,Cost_Spring_t_shirts_WOMAN,Cost_Summer_jackets_MAN,Cost_Summer_jackets_WOMAN,Cost_Summer_jeans_MAN,Cost_Summer_jeans_WOMAN,Cost_Summer_shoes_MAN,Cost_Summer_shoes_WOMAN,Cost_Summer_sweaters_MAN,Cost_Summer_sweaters_WOMAN,Cost_Summer_t_shirts_MAN,Cost_Summer_t_shirts_WOMAN,Cost_Winter_jackets_MAN,Cost_Winter_jackets_WOMAN,Cost_Winter_jeans_MAN,Cost_Winter_jeans_WOMAN,Cost_Winter_shoes_MAN,Cost_Winter_shoes_WOMAN,Cost_Winter_sweaters_MAN,Cost_Winter_sweaters_WOMAN,Cost_Winter_t_shirts_MAN,Cost_Winter_t_shirts_WOMAN):
      
      Sales_Autumn_jackets_MAN = Product_Sales_List[0];
      Sales_Autumn_jackets_WOMAN = Product_Sales_List[1];
      Sales_Autumn_jeans_MAN = Product_Sales_List[2];
      Sales_Autumn_jeans_WOMAN = Product_Sales_List[3];
      Sales_Autumn_shoes_MAN = Product_Sales_List[4];
      Sales_Autumn_shoes_WOMAN = Product_Sales_List[5];
      Sales_Autumn__sweaters_MAN = Product_Sales_List[6];
      Sales_Autumn_sweaters_WOMAN = Product_Sales_List[7];
      Sales_Autumn_t_shirts_WOMAN = Product_Sales_List[8];
      Sales_Autumn_t_shirts_WOMAN = Product_Sales_List[9];
   
      Sales_Spring_jackets_MAN = Product_Sales_List[10];
      Sales_Spring_jackets_WOMAN = Product_Sales_List[11];
      Sales_Spring_jeans_MAN = Product_Sales_List[12];
      Sales_Spring_jeans_WOMAN = Product_Sales_List[13];
      Sales_Spring_shoes_MAN = Product_Sales_List[14];
      Sales_Spring_shoes_WOMAN = Product_Sales_List[15];
      Sales_Spring__sweaters_MAN = Product_Sales_List[16];
      Sales_Spring_sweaters_WOMAN = Product_Sales_List[17];
      Sales_Spring_t_shirts_WOMAN = Product_Sales_List[18];
      Sales_Spring_t_shirts_WOMAN = Product_Sales_List[19]; 

      Sales_Summer_jackets_MAN = Product_Sales_List[20];
      Sales_Summer_jackets_WOMAN = Product_Sales_List[21];
      Sales_Summer_jeans_MAN = Product_Sales_List[22];
      Sales_Summer_jeans_WOMAN = Product_Sales_List[23];
      Sales_Summer_shoes_MAN = Product_Sales_List[24];
      Sales_Summer_shoes_WOMAN = Product_Sales_List[25];
      Sales_Summer__sweaters_MAN = Product_Sales_List[26];
      Sales_Summer_sweaters_WOMAN = Product_Sales_List[27];
      Sales_Summer_t_shirts_WOMAN = Product_Sales_List[28];
      Sales_Summer_t_shirts_WOMAN = Product_Sales_List[29];

      Sales_Winter_jackets_MAN = Product_Sales_List[30];
      Sales_Winter_jackets_WOMAN = Product_Sales_List[31];
      Sales_Winter_jeans_MAN = Product_Sales_List[32];
      Sales_Winter_jeans_WOMAN = Product_Sales_List[33];
      Sales_Winter_shoes_MAN = Product_Sales_List[34];
      Sales_Winter_shoes_WOMAN = Product_Sales_List[35];
      Sales_Winter__sweaters_MAN = Product_Sales_List[36];
      Sales_Winter_sweaters_WOMAN = Product_Sales_List[37];
      Sales_Winter_t_shirts_WOMAN = Product_Sales_List[38];
      Sales_Winter_t_shirts_WOMAN = Product_Sales_List[39];      
      

      Price_Autumn_jackets_MAN = Product_Price_List[0];
      Price_Autumn_jackets_WOMAN = Product_Price_List[1];
      Price_Autumn_jeans_MAN = Product_Price_List[2];
      Price_Autumn_jeans_WOMAN = Product_Price_List[3];
      Price_Autumn_shoes_MAN = Product_Price_List[4];
      Price_Autumn_shoes_WOMAN = Product_Price_List[5];
      Price_Autumn__sweaters_MAN = Product_Price_List[6];
      Price_Autumn_sweaters_WOMAN = Product_Price_List[7];
      Price_Autumn_t_shirts_WOMAN = Product_Price_List[8];
      Price_Autumn_t_shirts_WOMAN = Product_Price_List[9];
   
      Price_Spring_jackets_MAN = Product_Price_List[10];
      Price_Spring_jackets_WOMAN = Product_Price_List[11];
      Price_Spring_jeans_MAN = Product_Price_List[12];
      Price_Spring_jeans_WOMAN = Product_Price_List[13];
      Price_Spring_shoes_MAN = Product_Price_List[14];
      Price_Spring_shoes_WOMAN = Product_Price_List[15];
      Price_Spring__sweaters_MAN = Product_Price_List[16];
      Price_Spring_sweaters_WOMAN = Product_Price_List[17];
      Price_Spring_t_shirts_WOMAN = Product_Price_List[18];
      Price_Spring_t_shirts_WOMAN = Product_Price_List[19];

      

      Price_Summer_jackets_MAN = Product_Price_List[20];
      Price_Summer_jackets_WOMAN = Product_Price_List[21];
      Price_Summer_jeans_MAN = Product_Price_List[22];
      Price_Summer_jeans_WOMAN = Product_Price_List[23];
      Price_Summer_shoes_MAN = Product_Price_List[24];
      Price_Summer_shoes_WOMAN = Product_Price_List[25];
      Price_Summer__sweaters_MAN = Product_Price_List[26];
      Price_Summer_sweaters_WOMAN = Product_Price_List[27];
      Price_Summer_t_shirts_WOMAN = Product_Price_List[28];
      Price_Summer_t_shirts_WOMAN = Product_Price_List[29];

      Price_Winter_jackets_MAN = Product_Price_List[30];
      Price_Winter_jackets_WOMAN = Product_Price_List[31];
      Price_Winter_jeans_MAN = Product_Price_List[32];
      Price_Winter_jeans_WOMAN = Product_Price_List[33];
      Price_Winter_shoes_MAN = Product_Price_List[34];
      Price_Winter_shoes_WOMAN = Product_Price_List[35];
      Price_Winter__sweaters_MAN = Product_Price_List[36];
      Price_Winter_sweaters_WOMAN = Product_Price_List[37];
      Price_Winter_t_shirts_WOMAN = Product_Price_List[38];
      Price_Winter_t_shirts_WOMAN = Product_Price_List[39];  

      #Product_Sales_List = 
      i = 0;

      for i in range(len(Product_Sales_List)):
         Sales_List = Product_Sales_List[i];
         Price_List = Product_Price_List[i];
         for j in range(len(Sales_List)):   
            if(j < len(Sales_List) and i == 0):
               Cost_Autumn_jackets_MAN.append(Sales_List[j] * Price_List[j]);
            elif(j < len(Sales_List) and i == 1):
               Cost_Autumn_jackets_WOMAN.append(Sales_List[j]* Price_List[j]);
            elif(j < len(Sales_List) and i == 2):
               Cost_Autumn_jeans_MAN.append(Sales_List[j] * Price_List[j]);
            elif(j < len(Sales_List) and i == 3):
               Cost_Autumn_jeans_WOMAN.append(Sales_List[j]* Price_List[j]);
            elif(j < len(Sales_List) and i == 4):
               Cost_Autumn_shoes_MAN.append(Sales_List[j] * Price_List[j]);
            elif(j < len(Sales_List) and i == 5):
               Cost_Autumn_shoes_WOMAN.append(Sales_List[j]* Price_List[j]);
            elif(j < len(Sales_List) and i == 6):
               Cost_Autumn_sweaters_MAN.append(Sales_List[j] * Price_List[j]);
            elif(j < len(Sales_List) and i == 7):
               Cost_Autumn_sweaters_WOMAN.append(Sales_List[j]* Price_List[j]); 
            elif(j < len(Sales_List) and i == 8):
               Cost_Autumn_t_shirts_MAN.append(Sales_List[j] * Price_List[j]);
            elif(j < len(Sales_List) and i == 9):
               Cost_Autumn_t_shirts_WOMAN.append(Sales_List[j]* Price_List[j]);
            
            elif(j < len(Sales_List) and i == 10):
               Cost_Spring_jackets_MAN.append(Sales_List[j] * Price_List[j]);
            elif(j < len(Sales_List) and i == 11):
               Cost_Spring_jackets_WOMAN.append(Sales_List[j]* Price_List[j]);
            elif(j < len(Sales_List) and i == 12):
               Cost_Spring_jeans_MAN.append(Sales_List[j] * Price_List[j]);
            elif(j < len(Sales_List) and i == 13):
               Cost_Spring_jeans_WOMAN.append(Sales_List[j]* Price_List[j]);
            elif(j < len(Sales_List) and i == 14):
               Cost_Spring_shoes_MAN.append(Sales_List[j] * Price_List[j]);
            elif(j < len(Sales_List) and i == 15):
               Cost_Spring_shoes_WOMAN.append(Sales_List[j]* Price_List[j]);
            elif(j < len(Sales_List) and i == 16):
               Cost_Spring_sweaters_MAN.append(Sales_List[j] * Price_List[j]);
            elif(j < len(Sales_List) and i == 17):
               Cost_Spring_sweaters_WOMAN.append(Sales_List[j]* Price_List[j]); 
            elif(j < len(Sales_List) and i == 18):
               Cost_Spring_t_shirts_MAN.append(Sales_List[j] * Price_List[j]);
            elif(j < len(Sales_List) and i == 19):
               Cost_Spring_t_shirts_WOMAN.append(Sales_List[j]* Price_List[j]);

            elif(j < len(Sales_List) and i == 20):
               Cost_Summer_jackets_MAN.append(Sales_List[j] * Price_List[j]);
            elif(j < len(Sales_List) and i == 21):
               Cost_Summer_jackets_WOMAN.append(Sales_List[j]* Price_List[j]);
            elif(j < len(Sales_List) and i == 22):
               Cost_Summer_jeans_MAN.append(Sales_List[j] * Price_List[j]);
            elif(j < len(Sales_List) and i == 23):
               Cost_Summer_jeans_WOMAN.append(Sales_List[j]* Price_List[j]);
            elif(j < len(Sales_List) and i == 24):
               Cost_Summer_shoes_MAN.append(Sales_List[j] * Price_List[j]);
            elif(j < len(Sales_List) and i == 25):
               Cost_Summer_shoes_WOMAN.append(Sales_List[j]* Price_List[j]);
            elif(j < len(Sales_List) and i == 26):
               Cost_Summer_sweaters_MAN.append(Sales_List[j] * Price_List[j]);
            elif(j < len(Sales_List) and i == 27):
               Cost_Summer_sweaters_WOMAN.append(Sales_List[j]* Price_List[j]); 
            elif(j < len(Sales_List) and i == 28):
               Cost_Summer_t_shirts_MAN.append(Sales_List[j] * Price_List[j]);
            elif(j < len(Sales_List) and i == 29):
               Cost_Summer_t_shirts_WOMAN.append(Sales_List[j]* Price_List[j]);

            elif(j < len(Sales_List) and i == 20):
               Cost_Winter_jackets_MAN.append(Sales_List[j] * Price_List[j]);
            elif(j < len(Sales_List) and i == 21):
               Cost_Winter_jackets_WOMAN.append(Sales_List[j]* Price_List[j]);
            elif(j < len(Sales_List) and i == 22):
               Cost_Winter_jeans_MAN.append(Sales_List[j] * Price_List[j]);
            elif(j < len(Sales_List) and i == 23):
               Cost_Winter_jeans_WOMAN.append(Sales_List[j]* Price_List[j]);
            elif(j < len(Sales_List) and i == 24):
               Cost_Winter_shoes_MAN.append(Sales_List[j] * Price_List[j]);
            elif(j < len(Sales_List) and i == 25):
               Cost_Winter_shoes_WOMAN.append(Sales_List[j]* Price_List[j]);
            elif(j < len(Sales_List) and i == 26):
               Cost_Winter_sweaters_MAN.append(Sales_List[j] * Price_List[j]);
            elif(j < len(Sales_List) and i == 27):
               Cost_Winter_sweaters_WOMAN.append(Sales_List[j]* Price_List[j]); 
            elif(j < len(Sales_List) and i == 28):
               Cost_Winter_t_shirts_MAN.append(Sales_List[j] * Price_List[j]);
            elif(j < len(Sales_List) and i == 29):
               Cost_Winter_t_shirts_WOMAN.append(Sales_List[j]* Price_List[j]);
            else:
               continue;

      Product_Cost_List = [Cost_Autumn_jackets_MAN,Cost_Autumn_jackets_WOMAN,Cost_Autumn_jeans_MAN,Cost_Autumn_jeans_WOMAN,Cost_Autumn_shoes_MAN,Cost_Autumn_shoes_WOMAN,Cost_Autumn_sweaters_MAN,Cost_Autumn_sweaters_WOMAN,Cost_Autumn_t_shirts_MAN,Cost_Autumn_t_shirts_WOMAN,Cost_Spring_jackets_MAN,Cost_Spring_jackets_WOMAN,Cost_Spring_jeans_MAN,Cost_Spring_jeans_WOMAN,Cost_Spring_shoes_MAN,Cost_Spring_shoes_WOMAN,Cost_Spring_sweaters_MAN,Cost_Spring_sweaters_WOMAN,Cost_Spring_t_shirts_MAN,Cost_Spring_t_shirts_WOMAN,Cost_Summer_jackets_MAN,Cost_Summer_jackets_WOMAN,Cost_Summer_jeans_MAN,Cost_Summer_jeans_WOMAN,Cost_Summer_shoes_MAN,Cost_Summer_shoes_WOMAN,Cost_Summer_sweaters_MAN,Cost_Summer_sweaters_WOMAN,Cost_Summer_t_shirts_MAN,Cost_Summer_t_shirts_WOMAN,Cost_Winter_jackets_MAN,Cost_Winter_jackets_WOMAN,Cost_Winter_jeans_MAN,Cost_Winter_jeans_WOMAN,Cost_Winter_shoes_MAN,Cost_Winter_shoes_WOMAN,Cost_Winter_sweaters_MAN,Cost_Winter_sweaters_WOMAN,Cost_Winter_t_shirts_MAN,Cost_Winter_t_shirts_WOMAN];      
      return(Product_Cost_List);   
   
   def Compute_Revenue(Net_Sales,Net_Revenue,Gross_Revenue):
      Gross_Revenue = np.sum(Net_Revenue);
      return([np.sum(Net_Sales),Gross_Revenue]);
   #def Scatterplot(Product_Sales_List,Product_Cost_List,Gross_Revenue):
      

   #   return(None);   
         
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
      Sales_Autumn_jackets_MAN =[];
      Sales_Autumn_jackets_WOMAN =[];
      Sales_Autumn_jeans_MAN =[];
      Sales_Autumn_jeans_WOMAN =[];
      Sales_Autumn_shoes_MAN =[];
      Sales_Autumn_shoes_WOMAN =[];
      Sales_Autumn_sweaters_MAN =[];
      Sales_Autumn_sweaters_WOMAN =[];
      Sales_Autumn_t_shirts_MAN =[];
      Sales_Autumn_t_shirts_WOMAN =[];
      Sales_Spring_jackets_MAN =[];
      Sales_Spring_jackets_WOMAN =[];
      Sales_Spring_jeans_MAN =[];
      Sales_Spring_jeans_WOMAN =[];
      Sales_Spring_shoes_MAN =[];
      Sales_Spring_shoes_WOMAN =[];
      Sales_Spring_sweaters_MAN =[];
      Sales_Spring_sweaters_WOMAN =[];
      Sales_Spring_t_shirts_MAN =[];
      Sales_Spring_t_shirts_WOMAN =[];
      Sales_Summer_jackets_MAN =[];
      Sales_Summer_jackets_WOMAN =[];
      Sales_Summer_jeans_MAN =[];
      Sales_Summer_jeans_WOMAN =[];
      Sales_Summer_shoes_MAN =[];
      Sales_Summer_shoes_WOMAN =[];
      Sales_Summer_sweaters_MAN =[];
      Sales_Summer_sweaters_WOMAN =[];
      Sales_Summer_t_shirts_MAN =[];
      Sales_Summer_t_shirts_WOMAN =[];
      Sales_Winter_jackets_MAN =[];
      Sales_Winter_jackets_WOMAN =[];
      Sales_Winter_jeans_MAN =[];
      Sales_Winter_jeans_WOMAN =[];
      Sales_Winter_shoes_MAN =[];
      Sales_Winter_shoes_WOMAN =[];
      Sales_Winter_sweaters_MAN =[];
      Sales_Winter_sweaters_WOMAN =[];
      Sales_Winter_t_shirts_MAN =[];
      Sales_Winter_t_shirts_WOMAN =[];
      Price_Autumn_jackets_MAN =[];
      Price_Autumn_jackets_WOMAN =[];
      Price_Autumn_jeans_MAN =[];
      Price_Autumn_jeans_WOMAN =[];
      Price_Autumn_shoes_MAN =[];
      Price_Autumn_shoes_WOMAN =[];
      Price_Autumn_sweaters_MAN =[];
      Price_Autumn_sweaters_WOMAN =[];
      Price_Autumn_t_shirts_MAN =[];
      Price_Autumn_t_shirts_WOMAN =[];
      Price_Spring_jackets_MAN =[];
      Price_Spring_jackets_WOMAN =[];
      Price_Spring_jeans_MAN =[];
      Price_Spring_jeans_WOMAN =[];
      Price_Spring_shoes_MAN =[];
      Price_Spring_shoes_WOMAN =[];
      Price_Spring_sweaters_MAN =[];
      Price_Spring_sweaters_WOMAN =[];
      Price_Spring_t_shirts_MAN = [];
      Price_Spring_t_shirts_WOMAN = [];
      Price_Summer_jackets_MAN = [];
      Price_Summer_jackets_WOMAN = [];
      Price_Summer_jeans_MAN = [];
      Price_Summer_jeans_WOMAN = [];
      Price_Summer_shoes_MAN = [];
      Price_Summer_shoes_WOMAN = [];
      Price_Summer_sweaters_MAN = [];
      Price_Summer_sweaters_WOMAN = [];
      Price_Summer_t_shirts_MAN = [];
      Price_Summer_t_shirts_WOMAN = [];
      Price_Winter_jackets_MAN = [];
      Price_Winter_jackets_WOMAN = [];
      Price_Winter_jeans_MAN = [];
      Price_Winter_jeans_WOMAN = [];
      Price_Winter_shoes_MAN = [];
      Price_Winter_shoes_WOMAN = [];
      Price_Winter_sweaters_MAN = [];
      Price_Winter_sweaters_WOMAN = [];
      Price_Winter_t_shirts_MAN = [];
      Price_Winter_t_shirts_WOMAN = [];
      Cost_Autumn_jackets_MAN = [];
      Cost_Autumn_jackets_WOMAN = [];
      Cost_Autumn_jeans_MAN = [];
      Cost_Autumn_jeans_WOMAN = [];
      Cost_Autumn_shoes_MAN = [];
      Cost_Autumn_shoes_WOMAN = [];
      Cost_Autumn_sweaters_MAN = [];
      Cost_Autumn_sweaters_WOMAN = [];
      Cost_Autumn_t_shirts_MAN = [];
      Cost_Autumn_t_shirts_WOMAN = [];
      Cost_Spring_jackets_MAN = [];
      Cost_Spring_jackets_WOMAN = [];
      Cost_Spring_jeans_MAN = [];
      Cost_Spring_jeans_WOMAN = [];
      Cost_Spring_shoes_MAN = [];
      Cost_Spring_shoes_WOMAN = [];
      Cost_Spring_sweaters_MAN = [];
      Cost_Spring_sweaters_WOMAN = [];
      Cost_Spring_t_shirts_MAN = [];
      Cost_Spring_t_shirts_WOMAN = [];
      Cost_Summer_jackets_MAN = [];
      Cost_Summer_jackets_WOMAN = [];
      Cost_Summer_jeans_MAN = [];
      Cost_Summer_jeans_WOMAN = [];
      Cost_Summer_shoes_MAN = [];
      Cost_Summer_shoes_WOMAN = [];
      Cost_Summer_sweaters_MAN = [];
      Cost_Summer_sweaters_WOMAN = [];
      Cost_Summer_t_shirts_MAN = [];
      Cost_Summer_t_shirts_WOMAN = [];
      Cost_Winter_jackets_MAN = [];
      Cost_Winter_jackets_WOMAN = [];
      Cost_Winter_jeans_MAN = [];
      Cost_Winter_jeans_WOMAN = [];
      Cost_Winter_shoes_MAN = [];
      Cost_Winter_shoes_WOMAN = [];
      Cost_Winter_sweaters_MAN = [];
      Cost_Winter_sweaters_WOMAN = [];
      Cost_Winter_t_shirts_MAN = [];
      Cost_Winter_t_shirts_WOMAN =[];
      
      i = 0;
      j = 0;
      Product_Sales_List = self.Business_Sales_Computation(Product_Sales_File,Product_Sales_List,i,Sales_Autumn_jackets_MAN,Sales_Autumn_jackets_WOMAN,Sales_Autumn_jeans_MAN,Sales_Autumn_jeans_WOMAN,Sales_Autumn_shoes_MAN,Sales_Autumn_shoes_WOMAN,Sales_Autumn_sweaters_MAN,Sales_Autumn_sweaters_WOMAN,Sales_Autumn_t_shirts_MAN,Sales_Autumn_t_shirts_WOMAN,Sales_Spring_jackets_MAN,Sales_Spring_jackets_WOMAN,Sales_Spring_jeans_MAN,Sales_Spring_jeans_WOMAN,Sales_Spring_shoes_MAN,Sales_Spring_shoes_WOMAN,Sales_Spring_sweaters_MAN,Sales_Spring_sweaters_WOMAN,Sales_Spring_t_shirts_MAN,Sales_Spring_t_shirts_WOMAN,Sales_Summer_jackets_MAN,Sales_Summer_jackets_WOMAN,Sales_Summer_jeans_MAN,Sales_Summer_jeans_WOMAN,Sales_Summer_shoes_MAN,Sales_Summer_shoes_WOMAN,Sales_Summer_sweaters_MAN,Sales_Summer_sweaters_WOMAN,Sales_Summer_t_shirts_MAN,Sales_Summer_t_shirts_WOMAN,Sales_Winter_jackets_MAN,Sales_Winter_jackets_WOMAN,Sales_Winter_jeans_MAN,Sales_Winter_jeans_WOMAN,Sales_Winter_shoes_MAN,Sales_Winter_shoes_WOMAN,Sales_Winter_sweaters_MAN,Sales_Winter_sweaters_WOMAN,Sales_Winter_t_shirts_MAN,Sales_Winter_t_shirts_WOMAN);
      Product_Price_List = self.Business_Price_computation(Product_Sales_File,Product_Price_List,i,Price_Autumn_jackets_MAN,Price_Autumn_jackets_WOMAN,Price_Autumn_jeans_MAN,Price_Autumn_jeans_WOMAN,Price_Autumn_shoes_MAN,Price_Autumn_shoes_WOMAN,Price_Autumn_sweaters_MAN,Price_Autumn_sweaters_WOMAN,Price_Autumn_t_shirts_MAN,Price_Autumn_t_shirts_WOMAN,Price_Spring_jackets_MAN,Price_Spring_jackets_WOMAN,Price_Spring_jeans_MAN,Price_Spring_jeans_WOMAN,Price_Spring_shoes_MAN,Price_Spring_shoes_WOMAN,Price_Spring_sweaters_MAN,Price_Spring_sweaters_WOMAN,Price_Spring_t_shirts_MAN,Price_Spring_t_shirts_WOMAN,Price_Summer_jackets_MAN,Price_Summer_jackets_WOMAN,Price_Summer_jeans_MAN,Price_Summer_jeans_WOMAN,Price_Summer_shoes_MAN,Price_Summer_shoes_WOMAN,Price_Summer_sweaters_MAN,Price_Summer_sweaters_WOMAN,Price_Summer_t_shirts_MAN,Price_Summer_t_shirts_WOMAN,Price_Winter_jackets_MAN,Price_Winter_jackets_WOMAN,Price_Winter_jeans_MAN,Price_Winter_jeans_WOMAN,Price_Winter_shoes_MAN,Price_Winter_shoes_WOMAN,Price_Winter_sweaters_MAN,Price_Winter_sweaters_WOMAN,Price_Winter_t_shirts_MAN,Price_Winter_t_shirts_WOMAN);
      Product_Cost_List = self.Business_Revenue_Computation(Product_Sales_List,Product_Price_List,i,j,Cost_Autumn_jackets_MAN,Cost_Autumn_jackets_WOMAN,Cost_Autumn_jeans_MAN,Cost_Autumn_jeans_WOMAN,Cost_Autumn_shoes_MAN,Cost_Autumn_shoes_WOMAN,Cost_Autumn_sweaters_MAN,Cost_Autumn_sweaters_WOMAN,Cost_Autumn_t_shirts_MAN,Cost_Autumn_t_shirts_WOMAN,Cost_Spring_jackets_MAN,Cost_Spring_jackets_WOMAN,Cost_Spring_jeans_MAN,Cost_Spring_jeans_WOMAN,Cost_Spring_shoes_MAN,Cost_Spring_shoes_WOMAN,Cost_Spring_sweaters_MAN,Cost_Spring_sweaters_WOMAN,Cost_Spring_t_shirts_MAN,Cost_Spring_t_shirts_WOMAN,Cost_Summer_jackets_MAN,Cost_Summer_jackets_WOMAN,Cost_Summer_jeans_MAN,Cost_Summer_jeans_WOMAN,Cost_Summer_shoes_MAN,Cost_Summer_shoes_WOMAN,Cost_Summer_sweaters_MAN,Cost_Summer_sweaters_WOMAN,Cost_Summer_t_shirts_MAN,Cost_Summer_t_shirts_WOMAN,Cost_Winter_jackets_MAN,Cost_Winter_jackets_WOMAN,Cost_Winter_jeans_MAN,Cost_Winter_jeans_WOMAN,Cost_Winter_shoes_MAN,Cost_Winter_shoes_WOMAN,Cost_Winter_sweaters_MAN,Cost_Winter_sweaters_WOMAN,Cost_Winter_t_shirts_MAN,Cost_Winter_t_shirts_WOMAN); 
      Gross_Revenue = 0.0;
      Sales = input("Enter the Sales List name for computing Net Sales of Conditional List");
      Net_Revenue = input("Enter the List name of Costs from the avialble lists based on it's Net Sales in the prior step: ");
      Net_Sales = 0;
      Net_Sales, Gross_Revenue = self.Compute_Revenue(Sales,Net_Revenue,Gross_Revenue);
      #self.Scatter_plot(Net_Sales,Gross_Revenue);
      print("Total Sales volume for f'{Sales} value is: ",Net_Sales,"\n Gross Revenue for the Fiscal year 2024 for given conditional sales volume stands at $",Gross_Revenue);
      ABR.__init__().self.Pie_Chart_Visuals(self,Product_Sales_List,Product_Cost_List);
      #Dynamic_Variables_List = [];
      #Dynamic_Variables_List = DVG.Dynamic_Variable_Generator();
      #print(type(Dynamic_Variables_List))
      #for i in Dynamic_Variables_List:
      #print(Dynamicariables_List[-1]);
      #list(Dynamic_Variables_List.ID());
      #print(Dynamic_Variables_List);
      #for i in range(120):
         #print(Dynamic_Variables_List[i]);
      return(None);

Business_SPR = Business_Sales_Price_Revenue_Report();
