from pandas.tseries.offsets import QuarterBegin
import numpy as np;
import pandas as pd;
import matplotlib.pyplot as pyplt;
import math;
import scipy;
import scipy.stats as stats;
#import scikit-learn as skl;
import Sequential_Number_Generation as SNG;

class Wine_Quality_Red:
   def Wine_Quality_Red(self,Red_Wine,Quality_Metrics,i):
      Red_Wine_Fixed_Acidity = Red_Wine[0];
      Red_Wine_Volatile_Acidity = Red_Wine[1];
      Red_Wine_Citric_Acid = Red_Wine[2];
      Red_Wine_Residual_Sugar = Red_Wine[3];
      Red_Wine_Chlorides = Red_Wine[4];
      Red_Wine_Free_Sulfur_Dioxide = Red_Wine[5];
      Red_Wine_Total_Sulfur_Dioxide = Red_Wine[6];
      Red_Wine_Density = Red_Wine[7];
      Red_Wine_pH = Red_Wine[8];
      Red_Wine_Sulphates = Red_Wine[9];
      Red_Wine_Alcohol = Red_Wine[10];
      Red_Wine_Quality = Red_Wine[11];
      
      for i in range(len(Red_Wine_Quality)):
         #print(i);
         if((Red_Wine_Fixed_Acidity[i] <= 7.45 and Red_Wine_Fixed_Acidity[i] >= 7.35) and (Red_Wine_Volatile_Acidity[i] <= 1.4) and (Red_Wine_Citric_Acid[i] >=0.32 and Red_Wine_Citric_Acid[i] <= 1.24)):
            print("In the first loop");
            if((Red_Wine_Residual_Sugar[i] <= 35)):
               print("In second Condition")
               if(Red_Wine_Chlorides[i] >= 0.096 and Red_Wine_Chlorides[i] <= 0.106):
                  print("Conditional loop 3")
                  if((Red_Wine_Free_Sulfur_Dioxide[i] <= 120 and Red_Wine_Free_Sulfur_Dioxide[i] >=20) and (Red_Wine_Total_Sulfur_Dioxide[i] <= 165 and Red_Wine_Total_Sulfur_Dioxide[i] >= 0.075)):
                     print("Next loop with in the conditional statement 4")
                     if(Red_Wine_Density[i] >= 0.981 and Red_Wine_Density[i] <= 1.013):
                        print("Within the Conditional loop 5")
                        if(Red_Wine_pH[i] <=3.8 and Red_Wine_pH [i]>= 3.3):
                           print("Conditional loop statement exist 6")
                           if((Red_Wine_Alcohol[i] <= 15 and Red_Wine_Alcohol[i] >= 12) and (Red_Wine_Sulphates[i] <= 350)):
                              print("Within Conditional statement 7")
                              if(Red_Wine_Quality[i] > 7):
                                 Quality_Metrics.append('Devinely sourbread');
                              else:
                                 Quality_Metrics.append('consumable at sweet shop');
         #elif(Red_Wine_Fixed_Acidity) 
      return(Quality_Metrics);

   def Wine_Quality_Metrics_Computation(self,Red_Wine,Quality_Metrics,Quality_Metrics_UnHealthy,i):
      Red_Wine_SNO = Red_Wine[0];
      Red_Wine_Fixed_Acidity = Red_Wine[1];
      Red_Wine_Volatile_Acidity = Red_Wine[2];
      Red_Wine_Citric_Acid = Red_Wine[3];
      Red_Wine_Residual_Sugar = Red_Wine[4];
      Red_Wine_Chlorides = Red_Wine[5];
      Red_Wine_Free_Sulfur_Dioxide = Red_Wine[6];
      Red_Wine_Total_Sulfur_Dioxide = Red_Wine[7];
      Red_Wine_Density = Red_Wine[8];
      Red_Wine_pH = Red_Wine[9];
      Red_Wine_Sulphates = Red_Wine[10];
      Red_Wine_Alcohol = Red_Wine[11];
      Red_Wine_Quality = Red_Wine[12];
   
      for i in range(len(Red_Wine_Quality)):
         #print(i);
         if((Red_Wine_Fixed_Acidity[i] <= 7.45 and Red_Wine_Fixed_Acidity[i] >= 7.35) and (Red_Wine_Volatile_Acidity[i] <= 1.4) and (Red_Wine_Citric_Acid[i] >=0.32 and Red_Wine_Citric_Acid[i] <= 1.24)):
            print("In the first loop");
            if((Red_Wine_Residual_Sugar[i] <= 35)):
               Quality_Metrics.append(Red_Wine_SNO[i]+1);
            else:
               Quality_Metrics_UnHealthy.append(Red_Wine_SNO[i]+1);   
      return([Quality_Metrics,Quality_Metrics_UnHealthy]);

   def Scatter_Plot(self,Quality_Metrics,Devinely_Sourbread,Sweet_Shop):

      X = Devinely_Sourbread;
      N = len(X);
      #Y = Sweet_Shop;
      #Y = Quality_Metrics;
      Y = []; 
      colours = ['Green','Black'];
      fig, ax = pyplt.subplots();
      ax.scatter(X,Y);
      pyplt.xlabel("Devinely Sourbread");
      pyplt.ylabel("Quality Metrics");
      pyplt.show();
      return(None)   
   
   def Hist_Plot(self,Devinely_Sourbread,Sweet_Shop):
      print(len(Devinely_Sourbread))
      fig, ax = pyplt.subplots();
      ax.hist(Devinely_Sourbread,int(len(Devinely_Sourbread)),label='Red wine Quality');
      pyplt.show();
      return(None)

   def __init__(self):  
      Bevarage = pd.read_csv('/content/Wine_Features/wineequality-red.csv',delimiter=',');
      Red_Wine_Fixed_Acidity = Bevarage['fixed acidity'];
      Red_Wine_Volatile_Acidity = Bevarage['volatile acidity'];
      Red_Wine_Citric_Acid = Bevarage['citric acid'];
      Red_Wine_Residual_Sugar = Bevarage['residual sugar'];
      Red_Wine_Chlorides = Bevarage['chlorides'];
      Red_Wine_Free_Sulfur_Dioxide = Bevarage['free sulfur dioxide'];
      Red_Wine_Total_Sulfur_Dioxide = Bevarage['total sulfur dioxide'];
      Red_Wine_Density = Bevarage['density'];
      Red_Wine_pH = Bevarage['pH'];
      Red_Wine_Sulphates = Bevarage['sulphates'];
      Red_Wine_Alcohol = Bevarage['alcohol'];
      Red_Wine_Quality = Bevarage['quality'];
      Red_Wine_SNO = [];
      Red_Wine_SNO = SNG.Sequential_Number_Generation();
      #Bevarage['SNO'];
      
      Red_Wine = [Red_Wine_SNO,Red_Wine_Fixed_Acidity,Red_Wine_Volatile_Acidity,Red_Wine_Citric_Acid,Red_Wine_Residual_Sugar,Red_Wine_Chlorides,Red_Wine_Free_Sulfur_Dioxide,Red_Wine_Total_Sulfur_Dioxide,Red_Wine_Density,Red_Wine_pH,Red_Wine_Sulphates,Red_Wine_Alcohol,Red_Wine_Quality];
      #print(Red_Wine)
      Quality_Metrics = [];
      Quality_Metrics_UnHealthy  = [];
      Devinely_Sourbread = [];
      Sweet_Shop =[];
      i = 0;
      #Quality_Metrics = self.Wine_Quality_Red(Red_Wine,Quality_Metrics,i);
      Quality_Metrics = self.Wine_Quality_Metrics_Computation(Red_Wine,Quality_Metrics,Quality_Metrics_UnHealthy,i)[0];
      Quality_Metrics_UnHealthy = self.Wine_Quality_Metrics_Computation(Red_Wine,Quality_Metrics,Quality_Metrics_UnHealthy,i)[1];
      #for i in range(len(Quality_Metrics)):
      #  if(Quality_Metrics[i] == 'Devinely sourbread'):
      #      Devinely_Sourbread.append(Quality_Metrics[i]);
      #   else:
      #      Sweet_Shop.append(Quality_Metrics[i]);
      
      print(Quality_Metrics);
      print(Quality_Metrics_UnHealthy);
      #print(Sweet_Shop)
      #self.Scatter_Plot(Quality_Metrics,Devinely_Sourbread,Sweet_Shop); 
      #self.Hist_Plot(Devinely_Sourbread,Sweet_Shop);
      return(None);

Wine_Quality_R = Wine_Quality_Red();
