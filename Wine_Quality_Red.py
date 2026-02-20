import numpy as np;
import pandas as pd;
import matplotlib.pyplot as pyplt;
import math;
import scipy;
import scipy.stats as stats;
#import scikit-learn as skl;

class Wine_Quality_Red:
   def Wine_Quality_Red(self,Red_Wine,Quality_Metrics):
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
         if((Red_Wine_Fixed_Acidity[i] <= 7.45 and Red_Wine_Fixed_Acidity[i] >= 7.35) and (Red_Wine_Volatile_Acidity[i] <= 1.4) and (Red_Wine_Citric_Acid[i] >=0.32 and Red_Wine_Citric_Acid[i] <= 1.24)):
            if((Red_Wine_Residual_Sugar[i] <= 35)):
               if(Red_Wine_Chlorides[i] >= 96 and Red_Wine_Chlorides[i] <= 106):
                  if((Red_Wine_Free_Sulfur_Dioxide[i] <= 120 and Red_Wine_Free_Sulfur_Dioxide[i] >=20) and (Red_Wine_Total_Sulfur_Dioxide[i] <= 165 and Red_Wine_Total_Sulfur_Dioxide[i] >= 0.075)):
                     if(Red_Wine_Density[i] >= 0.981 and Red_Wine_Density[i] <= 1.013):
                        if(Red_Wine_pH[i] <=3.8 and Red_Wine_pH [i]>= 3.3):
                           if((Red_Wine_Alcohol[i] <= 15 and Red_Wine_Alcohol[i] >= 12) and (Red_Wine_Sulphates[i] <= 350)):
                              Quality_Metrics.append(Red_Wine_Quality[i]);
         #elif(Red_Wine_Fixed_Acidity)
         else:
            return(Quality_Metrics); 
      return(Quality_Metrics);
   
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

      Red_Wine = [Red_Wine_Fixed_Acidity,Red_Wine_Volatile_Acidity,Red_Wine_Citric_Acid,Red_Wine_Residual_Sugar,Red_Wine_Chlorides,Red_Wine_Free_Sulfur_Dioxide,Red_Wine_Total_Sulfur_Dioxide,Red_Wine_Density,Red_Wine_pH,Red_Wine_Sulphates,Red_Wine_Alcohol,Red_Wine_Quality];
      #print(Red_Wine)
      Quality_Metrics = [];
      self.Wine_Quality_Red(Red_Wine,Quality_Metrics);
      return(None);

Wine_Quality_R = Wine_Quality_Red();
