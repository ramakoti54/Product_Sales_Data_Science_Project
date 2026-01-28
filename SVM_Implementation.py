import numpy as np;
import pandas as pd;
#import ndarray as nd;
#import scikit-learn as skl;
import tensorflow as tf;
import math;
import matplotlib as mtl;
import matplotlib.pyplot as plt;
import plotly.graph_objects as go;
import Visualize_Stock_Data as vsd;
from mlrefined_libraries import math_optimization_library as mopt;


# Support Vector Machine(SVM) Implementation process for Stock price prediction of Banking and Finance Organizations.
class SVM_Implementation:
   # Dataset Normalization procedure with Feature Engineering selection process. Using stat techniques Min, Max, Mean, Median, Std, IQR functions.
   def Dataset_Normalization(newprice):

      return(0);

   def Mean(self,x):
      sum = 0.0;
      for i in range(len(x)):
         sum = sum + x[i];
      mean = sum/len(x);
      return(mean);

   def Standard_Deviation(self,x):
      sum_std = 0.0;
      mean_x = self.Mean(x);
      print("Mean of the Distribution is:",mean_x);
      for i in range(len(x)):
         sum_std = sum_std + sum(pow((x[i] - mean_x),2));

      std_x = math.sqrt(sum_std/(len(x)-1));
      return(std_x);

   def Minimum(self,x):
      min_x = [];
      for i in range(len(x)):
         if(x[i] <= x[i+1]):
            min_x = x[i];
         else:
            min_x = x[i+1];
      return(min_x);

   def Maximum(self,x):
      max_x = [];
      for i in range(len(x)):
         if(x[i] >= x[i+1]):
            max_x = x[i];
         else:
            max_x = x[i+1];
      return(max_x);

   def Optimal_Range(self,x,range1,range2):
      for i in range(len(x)):
         range1 = range1 + x['Close']- x['Open'];
         range2 = range2 + x['High'] - x['Low'];
      return([range1,range2]);

   def Gaussian_Mean(self,x,Gaussian_Mean):
      mean_x = self.Mean(x);
      std_x = self.Standard_Deviation(x);
      sum_std = [];
      Gaussian_M = 0.0;
      for i in range(len(x)):
         sum_std.append(sum(pow((x[i]- mean_x),2)));
         Gaussian_Mean = (1/math.sqrt(2*math.pi)*std_x)*(math.exp((sum_std[i]*-1)/(2*pow(std_x,2))));
         Gaussian_Mean.append(Gaussian_M);
      return(Gaussian_Mean);

   def Gaussian_Median(self,x,Gaussian_Median):
      median_x = self.Median(x);
      std_x = self.Standard_Deviation(x);
      sum_std = [];
      Gaussian_Med = 0.0;
      for i in range(len(x)):
         sum_std.apeend(sum_std + sum(pow((x[i]-median_x),2)));
         Gaussian_Med = (1/math.sqrt(2*math.pi)*std_x)*(math.exp((sum_std[i]*-1)/(2*pow(std_x,2))));
         Gaussian_Median.append(Gaussian_Med);
      return(Gaussian_Median);

   def Gaussian_Standard_Deviation(self,x,Gaussian_Std):
      median_x = self.Median(x);
      std_x = self.Standard_Deviation(x);
      sum_std = [];
      Gaussian_Std = 0.0;
      for i in range(len(x)):
         sum_std.append(sum_std + sum(pow((x[i]-std_x),2)));
         Gaussian_Standard_Deviation = (1/math.sqrt(2*math.pi)*std_x)*(math.exp((sum_std[i]*-1)/(2*pow(std_x,2))));
         Gaussian_Std.append(Gaussian_Standard_Deviation);
      return(Gaussian_Std);

   def Gaussian_Minimum(self,x,Gaussian_Minimum):
      Min_x = self.Minimum(x);
      std_x = self.Standard_Deviation(x);
      sum_std = [];
      Gaussian_Min = 0.0;
      for i in range(len(x)):
         sum_std.append(sum_std + sum(pow((x[i]-Min_x),2)));

         Gaussian_Min = (1/math.sqrt(2*math.pi)*std_x)*(math.exp((sum_std[i]*-1)/(2*pow(std_x,2))));
         Gaussian_Minimum.append(Gaussian_Min);
      return(Gaussian_Minimum);

   def Gaussian_Maximum(self,x,Gaussian_Maximum):
      Max_x = self.Maximum(x);
      std_x = self.Standard_Deviation(x);
      sum_std = [];
      Gaussian_Max = 0.0;
      for i in range(len(x)):
         sum_std.append(sum_std + sum(pow((x[i]-Max_x),2)));
         Gaussian_Maximum = (1/math.sqrt(2*math.pi)*std_x)*(math.exp((sum_std[i]*-1)/(2*pow(std_x,2))));
         Gaussian_Maximum.append(Gaussian_Max);
      return(Gaussian_Maximum);

   # Find Dataset median for the Normalized price calculated from the Newprice computed from source files(Stock ticker csv files)
   # The method returns median value of the datasample to compute the samples of the dataset using median value comparision.
   def Median_Newprice(self,Newprice):
      median_Newprice = 0.0;
      if(int(len(Newprice))%2 == 0):
         median_Newprice = (Newprice[len(Newprice)] + Newprice[int(len(Newprice))+1])/2;
         return(median_Newprice);
      else:
         median_Newprice = math.floor(Newprice(len(Newprice[int(len(Newprice))])/2));
         return(median_Newprice);
      return(0);

   # A Sorting Algorithm for computing Sorted list of prices to compute median value of the sample.
   def sort_Newprice(self,Newprice,i,k,sorted_newprice):
      #print(type(Newprice))
      #sorted_newprice = [];
      if(i < len(Newprice)-1):
         if(Newprice[i] <= Newprice[i+1]):
            sorted_newprice.append(Newprice[i]);
            i = i+1;
            sorted_Newprice(Newprice[i:],i,k,sorted_newprice);
         elif(Newprice[i] > Newprice[i+1] & i < int(len(Newprice))):
            temp = Newprice[i];
            Newprice[i] = Newprice[i+1];
            Newprice[i+1] = temp;
            sorted_newprice.append(Newprice[i]);
            i = i+1;
            sorted_Newprice(Newprice[i:],i,k,sorted_newprice);
      elif(k < len(Newprice)):
         i = k;
         k = k+1;
         return(sorted_Newprice(Newprice[k:],i,k,sorted_newprice));
      elif(k == len(Newprice)):
         return(sorted_newprice);
      return(sorted_newprice);

   def standard_Normalizer(self,x):
      #for i in range(np.len)
      x_mean = self.Mean(x);
      x_std = self.Standard_Deviation(x);
      for i in len(range(x)):
         x_standard_normalizer = (x[i]-x_mean)/x_std;
      return(x_standard_normalizer);


   ''' Definitions for Model function, sine function and magnitude of weights vector '''

   def model(self,x,w):
      x_model = w[0]+np.dot(x.T,w[1:]);
      return(x_model);

   def sine_function(self,x,w):
      x_sine_function = np.sin(self.model(x,w));
      return(x_sine_function);

   '''def soft_max(w):
    x_softmax = np.log(1+np.exp(model(x,w)));
    return(x_softmax);    '''
   # Laplacian Distance between the point on Support vector machine/ the area above or below the rectangular plane to the support vector/Decision Boundary.
   # Formula for computing the Distance magnitude is in ||w|| and is equalent to sqrt(w1 2 + w2 2 + W3 2+ w4 2+w5 2+...+wn 2).
   def magnitude(w):
      w_mag = np.sqrt(w[1]**2+w[2]**2+w[3]**2+w[4]**2+w[5]**2+w[6]**2+w[7]**2+w[8]**2+w[9]**2+w[10]**2+w[11]**2+w[12]**2);
      print(w_mag)
      return(w_mag);
   ''' finding accuracy score to assign the value to +1 if the score is >=0.5
     and assigning the value to -1 if the score is < 0.5'''

   '''def accuracy_score(w):
         distance = sine_function(w)/magnitude(w);
         acc_score = 1/(1+np.exp(-distance));
         #acc1_score =soft_max(w)/magnitude(w);
         #print(acc1_score);
         return(acc_score);

   accuracy = accuracy_score(w);
   y_p = []
   y_p = accuracy;
   #print(np.round(accuracy,2))
   #print(accuracy.shape)
   #print(np.size(accuracy))
   '''

   ''' Logic to assign values for y_p either +1 or -1 as mentioned in the above comment'''
   '''i = 0;
   count_negative =0
   count_positive =0
   for i in range(np.size(accuracy)):
      if(accuracy[i]<= 0.50):
         y_p[i] = -1;
         count_negative +=1;
      elif(accuracy[i]>0.50):
         y_p[i] = +1;
         count_positive +=1;
   #print(np.size(y_p))'''

   ''' Least square cost function definition and logic'''
   '''def least_square_function(w):

    model_value = np.sum((model(x_p,w)-y_p)**2);
    #print(model_value)
    least_square_cost = model_value/float(np.size(y_p));
    return least_square_cost'''

   def SVM_Cost(self,sine_method_model,C):
      cost = sine_method_model*C;
      return(cost);

   def SVM_Extrapolation(self,present_ticker_price,w,predicted_output):
      for i in range(len(present_ticker_price)):
         for j in range(len(w)):
            predicted_output.append([(self.present_ticker_price[i] * w[j]+w[0])]);
      return(predicted_output);

   def SVM_Cost_Depiction(self,present_ticker_price,w):
      grad_descent = mopt.optimizers;
      grad_1 = self.SVM_Extrapolation(self.present_ticker_price,w);
      grad_2 = self.sine_function(present_ticker_price,w);

      alpha = pow(10,-1); alpha2 = pow(10,-2); alpha3 = pow(10,-5);
      max_iterations = 1000;

      svm_cost_function_weight_history1,svm_cost_function_cost_history1 = grad_descent.grad_descent(grad_1,alpha,max_iterations,w);
      svm_cost_function_weight_history2,svm_cost_function_cost_history2 = grad_descent.grad_descent(grad_1,alpha2,max_iterations,w);
      svm_cost_function_weight_history3,svm_cost_function_cost_history3 = grad_descent.grad_descent(grad_1,alpha3,max_iterations,w);

      cost_history =[svm_cost_function_cost_history1,svm_cost_function_cost_history2,svm_cost_function_cost_history3];
      #cost_history2 = [least_absolute_deviation_cost_history1,least_absolute_deviation_cost_history2,least_absolute_deviation_cost_history3];
      return(cost_history);

   def Plot_Cost_Histroy(self,cost_history,**kwargs):

      Plot_cost_history = Plot_Cost_Histories();
      ''' Calling plot function to show the diagrams for cost functions of both least square cost and least absolute deviation functions'''
      print("Comparision of Least squares cost vs Least Absolute Deviation")
      print("-------------------------------------------------------------")
      print("Least squares squares cost performs better while using Set-1 step length(alpha) values change to Set-2 in the code from previous code window to see results")
      print("Least squares Absolute performs better while using Set-2 step length(alpha) values change to Set-1 in the code from previous code window to see results")
      print("--------------------------------------------------------------")
      Plot_cost_history.plot_cost_histories(cost_history,0,labels=[r'Least squares cost function',r'alpha=10^-5',r'alpha=10^-2.5',r'alpha=10^-1.5']);
      #Plot_cost_history.plot_cost_histories(cost_history2,0,labels=[r'Least Absolute Deviation',r'alpha=10^-5',r'alpha=10^-2.5',r'alpha=10^-1.5']);
      return(0);

   def Implement_SVM(self,x,w):
      historical_ticker_price = self.x[1:70];
      present_ticker_price = self.x[71:];
      sine_method_model = self.sine_function(historical_ticker_price,w);
      magnitude_weights = self.magnitude(w);
      distance = sine_method_model/magnitude_weights;
      #acc_score = 1/(1+np.exp(-distance));
      C = 1/magnitude_weights;
      predicted_output = [];
      cost_SVM = self.SVM_Cost(sine_method_model,C);
      #Inference_price = self.SVM_Cost((self.sine_function(present_ticker_price,w)),C);
      predicted_output = self.SVM_Extrapolation(Inference_price,w,predicted_output);
      self.Candlestick_Graph_Price(predicted_output);
      cost_history = self.SVM_Cost_Depiction(predicted_output,w);
      self.Plot_Cost_History(cost_history);
      return(0);

   def Plot_Scatter(self,X,Y):
      plt.style.use('_mpl-gallery');
      #np.random.seed(3);
      number_days = len(X);
      #size and color
      sizes = np.random.uniform(0,200,len(X));
      colors = np.random.uniform(201,298,len(X));
      plt.plot(X,Y);
      fig, ax = plt.subplots();
      ax.scatter(X,Y,s=sizes,c=colors);
      ax.set(xlim=(0,200), xticks=np.arange(1,200),xlabel="Stock prices over last 98 days",
      ylim=(0,len(Y)), yticks=np.arange(1,len(Y)),ylabel="Volume of the stock over last 98 days");
      plt.show();
      return(0);

   def BoxPlotVisuals(Stock_File):
      mean = Stock_File['Mean_Price'];
      std = Stock_File['Std_Price'];
      min = Stock_File['Min_Price'];
      max = Stock_File['Max_Price'];
      median = Stock_File['Median_Price'];
      return(0);

   def Candlestick_Graph_File(Stock_File):
      fig = go.Figure(data = [go.Candlestick(
                    x = Stock_File['Date'],
                    Open = Stock_File['Open'],
                    Close = Stock_File['Close'],
                    Low = Stock_File['Low'],
                    High = Stock_File['High'],
                    Volume = Stock_File['Volume'],
                    Date = Stock_File['Date']
                        )]);
      fig.update_layout(xaxis_rangeslider_visible=False);
      # Set layout size
      fig.update_layout(autosize=False,width=700,height=500);
      fig.show();
      fig.write_html("/content/Stock_Files/candlestick-plotly-basic.html");
      return(0);

   '''def Candlestick_Graph_Price(Stock_Distribution_Price):

      fig = go.Figure(data = [go.Candlestick(
                    #x = Stock_File['Date'],
                    #Open = Stock_File['Open'],
                    #Close = Stock_File['Close'],
                    #Low = Stock_File['Low'],
                    #High = Stock_File['High'],
                    #Volume = Stock_File['Volume'],
                    #Date = Stock_File['Date']
                    Price_Data = Stock_Distribution_Price[0:len((Stock_Distribution_Price)-1)]
                       )]);
      fig.update_layout(xaxis_rangeslider_visible=False);
      # Set layout size
      fig.update_layout(autosize=False,width=700,height=500);
      fig.show();
      fig.write_html("/content/Stock_Files/candlestick-plotly-basic.html");
      return(0);
   '''
   def Statistical_Methods(self,x,volume,median_price,Stock_Files,i,k,sorted_newprice,range1,range2,calling):
      plot_scatter = self.Plot_Scatter(Newprice_Sample,Volume_Sample);
      if(calling == 'Mean'):
         x_mean = self.Mean(x);
         return(x_mean);
      elif(calling == 'Std'):
         x_std = self.Standard_Deviation(x);
         return(x_std);
      elif(calling == 'Min'):
         x_min = self.Minimum(x);
         return(x_min);
      elif(calling == 'Max'):
         x_max = self.Maximum(x);
         return(x_max);
      elif(calling == 'Median'):
         x_median = self.Median_Newprice(median_price);
         return(x_median);
      elif(calling == 'Optimal_Range'):
         x_optimal_range = self.Optimal_Range(x,range1,range2);
         return(x_optimal_range);
      elif(calling == 'Standard_Normalizer'):
         x_std_norm = self.standard_Normalizer(x);
         return(x_std_norm);
      elif(calling == 'Gaussian_Mean'):
         Gaussian_Mean = [];
         w = [1.0,2.0,3.0,4.0,2.0,2.0]
         x_gaussian_mean = self.Gaussian_Mean(x,Gaussian_Mean);
         #x_gaussian_med = self.Gaussian_Median(x,Gaussian_Median);
         #x_sine = self.sine_function(x_gaussian_mean,w);
         svm_gaussian_mean_cost = self.Implement_SVM(x_gaussian_mean,w);
         #svm_cost_gaussian_mean = self.SVM_Cost();
         return(svm_cost_gaussian_mean_cost);

      elif(calling == 'Gaussian_Median'):
         Gaussian_Median = [];
         x_sine = [];
         x_gaussian_median = self.Gaussian_Median(x,Gaussian_Median);
         x_sine = self.sine_function(x_gaussian_median,w);
         svm_gaussian_med = self.Implement_SVM(x_sine,w);
         svm_cost_gaussian_med = self.SVM_Cost();
         return(svm_cost_gaussian_med);
      elif(calling == 'Gaussian_Standard_Deviation'):
         Gaussian_Std = [];
         x_gaussian_std = self.Gaussian_Standard_Deviation(x,Gaussian_Std);
         #x_gaussian_median = self.Gaussian_Median(x,Gaussian_Median);
         x_sine = self.sine_function(x_gaussian_std,w);
         svm_gaussian_std = self.Implement_SVM(x_sine,w);
         svm_cost_gaussian_std = self.SVM_Cost();
         return(svm_cost_gaussian_std);
      elif(calling == 'Gaussian_Minimum'):
         Gaussian_Minimum = [];

         x_gaussian_min = self.Gaussian_Minimum(x,Gaussian_Minimum);
         #x_gaussian_median = self.Gaussian_Median(x,Gaussian_Median);
         x_sine = self.sine_function(x_gaussian_minimum,w);
         svm_gaussian_min = self.Implement_SVM(x_sine,w);
         svm_cost_gaussian_min = self.SVM_Cost();
         return(svm_cost_gaussian_min);

      elif(calling == 'Gaussian_Maximum'):
         Gaussian_Maximum = [];
         x_gaussian_max = self.Gaussian_Maximum(x,Gaussian_Maximum);
         #x_gaussian_median = self.Gaussian_Median(x,Gaussian_Median);
         x_sine = self.sine_function(x_gaussian_max,w);
         svm_gaussian_max = self.Implement_SVM(x_sine,w);
         svm_cost_gaussian_max = self.SVM_Cost();
         return(svm_cost_gaussian_max);

      elif(calling == 'Plot_Scatter'):
         plots = self.Plot_Scatter(x,volume);
         return(0);
      elif(calling == 'Candlestick_Graph_File'):
         Candlestick = self.Candlestick_Graph_File(Stock_File);
         return(0);
      elif(calling == 'Candlestick_Graph_Price'):
         Candlestick = self.Candlestick_Graph_Price(Stock_Distribution_Price);
         return(0);
      else:
         print("Enter the calling method for expected statistical method");
         return(0);
      return(0);

      #def scatter_plots():
      # Reading CSV files data for the source Stock Tickers include Banking and Finance Organizations.
      # Compute the simple average of Open,Close,High and Low prices of the file to find a frame of records representing the stock prices over couple of months from the sample.
      # initiate variables to calculate intermediate prices and performing required operations prior to normalization of dataset.
      # Instantiation of class SVM_Implementation to call required functions from the class.
      # Functional calls through required arguments.
   def __init__(self):
      #Stock_File_Name = pd.read_csv("/JPM.csv",delimiter=',');
      Sales_File = pd.read_csv("/content/Product_Sales_File/Business_sales_EDA.csv",delimiter=';');
      #Newprice = (Stock_File_Name['Open']+ Stock_File_Name['Close']+ Stock_File_Name['High']+ Stock_File_Name['Low'] + Stock_File_Name['Adj Close'])/5;
      Newprice_Sales_Volume = Sales_File['Sales Volume'];
      Newprice = Sales_File['price'];
      #volume = Stock_File_Name['Volume'];
      Newprice_sample = [];
      #Newprice_Sample = list[Newprice[10001:]];
      #Volume_Sample = list(volume[10001:]);
      i = 0;
      k = 1;
      sorted_Newprice = [];
      svm_implement = SVM_Implementation();
      range1 = [];
      range2 = [];
      calling = str(input("Enter one of the calling method as in ['Mean','Std','Min','Max','Median','Optimal_Range','Gaussian_Mean','Gaussian_Median','Gaussian_Standard_Deviation','Gaussian_Minimum','Gaussian_Maximum','Plot_Scatter','Candlestick_Graph_File','Candlestick_Graph_Price'] for Statistical Method"));
      #Standard_Normal_Price = svm_implement.standard_Normalizer(Newprice);
      Standard_Normal_Price = svm_implement.standard_Normalizer(Newprice_Sales_Volume);
      Standard_Normal_Price = svm_implement.standard_Normalizer(Newprice);
      #print("Input x_p after applying standard normalization function",x_p);

      #print(" Newprice\n","========\n",sum((Newprice[9001:]))/len(Newprice[9001:]));
      #print("Different numbers from 9000 to 10078 records for newprice\n",Newprice[9001:],"\n10000 beyond\n",Newprice[10001:])
      #print("\n Minimum of Newprice\n==============\n",min(Newprice[9000:]),min(Newprice[10001:]))
      #print("\n Max price\n========\n",max(Newprice[9001:]),max(Newprice[10001:]))
      #print("\n Volume of the stock with min and max",min(Newprice[10000:]),max(Newprice[10000:]));
      #Optimum_Range = Optimal_Range(Stock_File_Name,range1,range2);
      #print("\n Optimal Range of the price values over the intraday looks like\n",Optimum_Range[0],Optimum_Range[1]);
      #print("\n Median of the Newprice\n",svm_implement.median_Newprice(Newprice_sample),svm_implement.median_Newprice(Newprice_sample));
      #print(Newprice_sample)
      Sorted_Newprice = svm_implement.sort_Newprice(Newprice_Sample,i,k,sorted_Newprice);
      #print("Sorted prices of the Newprice list",sorted_Newprice);
      median_price = svm_implement.median_Newprice([Sorted_Newprice]);
      #print("\n Median value of Newprice is\n======================\n",median_price);
      #Normalized_Price = svm_implement.Dataset_Normalization(list(median_price));
      #print("\n Normalized prices for the Dataset is",Normalized_Price);
      #statistical_method_result = svm_implement.Statistical_Methods(Newprice,volume,median_price,Stock_File_Name,i,k,Sorted_Newprice,range1,range2,calling);
      statistical_method_result = svm_implement.Statistical_Methods(Newprice_Sales_Volume,volume,median_price,Stock_File_Name,i,k,Sorted_Newprice,range1,range2,calling);
      statistical_method_result = svm_implement.Statistical_Methods(Newprice,volume,median_price,Stock_File_Name,i,k,Sorted_Newprice,range1,range2,calling);
      Visualize_Data.Visualize_Stock_Results();

      return(None);

SVM_Imp = SVM_Implementation();

      
