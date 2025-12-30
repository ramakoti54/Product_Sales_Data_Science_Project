from typing import Sequence;
import numpy as np;
import pandas as pd;

class Even_Odd_Number_Generator:
   def Even_Odd_Gen(self,random_generator,i,j,counter,last_num_seq):
      #while counter < last_num_seq:
      if(counter < last_num_seq):
         if(counter%2 == 0):
            #i = 1; 
            #random_generator.append(i);
            counter = counter+1;
            random_generator.append(i);
            #insert(counter,i);     
            #print(random_generator);     
            self.Even_Odd_Gen(random_generator,i,j,counter,last_num_seq);
         elif(counter%2 == 1):
            #i = 0.5;
            #random_generator.append(i);
            #random_generator.insert(counter,i);
            counter = counter+1;
            random_generator.append(j);
            #random_generator.insert(counter,i);
            #print(random_generator);
            #print(counter,random_generator);
            self.Even_Odd_Gen(random_generator,i,j,counter,last_num_seq);
         else:
            self.Even_Odd_Gen(random_generator,i,j,counter,last_num_seq);            
      else:
         return(random_generator);
      return(random_generator);

   def __init__(self):
      last_num_seq = int(input("Enter length of the series to be computed"));
      i = float(input("Enter a first weight for storing as input value to vector"));
      counter = 0;
      j = float(input("Enter a weight for storing the values of it as incremental in a Weights vector"));      
      random_generator = [];
      random_generator = Random_Number_Gen.Even_Odd_Gen(random_generator,i,j,counter,last_num_seq);
      print(random_generator)      
      return(None);

Random_Number_Gen = Even_Odd_Number_Generator();
#print(random_generator);
