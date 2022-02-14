#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: rajeevkumar3322

Working wiith file methods assignment 

-This code :
1.Uses Python's built-in file functions and methods to open, read and write the contents of data files;
2.Writes a Python program that can convert a file from one format to another;
3.Writes a program that can merge separate files of the same format into a single larger file.
"""


#pathname for folder = /Users/rajeevkumar3322/Rstudio_csv/Courses_Spring_2021/Courses Fall2021/ABE/week_3_ENINF

#plann

#open(filename, access_mode) #open function template


import os # import required modules
import io 


#determining directory
input(os) #-> get cwd , make sure directory set 

os.getcwd()
#changing directory to correct location
os.chdir('/Users/rajeevkumar3322/Rstudio_csv/Courses_Spring_2021/Courses Fall2021/ABE/week_3_ENINF/datasets')


#defining input file and output file 
inFile = "ill-soilmoist-data-001.txt"
outFile = "ill-soilmoist-data-001.csv"


# define function
def process_data_file( inFile, outFile ):
    try:
        fin = open( inFile, 'r' ) #creating variable to read in inFile
    except IOError:
        print("ERROR: Unable to open the input file {}.".format(inFile))
        raise SystemExit
    print( "File opened!" )
    
    
    final = fin.readlines() #creating temporary variable for fin reading in data as list of strings

    print(process_data_file(final))

 
    Data = [0]*len(final)       #creating empty array length of final 
    for linx in range(len(final)):   #for every value in range of array values 
     Data[linx] = ",".join(final[linx].strip().split("\t"))+"\n" #write data to output file
        

    print(process_data_file(Data))
    
    
    

    if os.path.isfile(outFile) == False:       #if outfile exists
     
        print("The output file already exists!") #printing conditional to check
     
    
        try:
                fout = open( outFile, 'w')   #open outFile in wrting mode if exists
        except IOError:
                print("ERROR: Unable to open the input file {}.".format(outFile)) #printing error message if error occurs
                raise SystemExit
        print( "File opened!" )
        
fout.writelines(final [:2]) #writing header to outfile by indexing only top two rows
fout.writelines(Data [2:]) #writing body of file to outfile to all values except top two rows
   
    
 
    else: #if outfile exists
        fout = open( outFile, 'a' ) #opening outfile in append mode
        print("outfile poen and in append mode")   #determine if file is in a state to be modified

        fout.writelines(Data [3:])
        print("Outfile added body only")
   
    fin.close() 
    fout.close()     
             
        
        
        #confirming correct creation of outfile using line numbers
    count = 0
    for line in fout:
        count += 1
    
    if count == 4684:
        print("correct count")
    if count == 4711:
        print("Error: header duplicated")
    if count >= 4684:
        print("Error: file wasn't empty")
    else:
        print("Unknown Error")
        
   



if __name__ == '__main__':
    for i in os.listdir("datasets/"): #for loop calling each file from directory folder
        process_data_file( "datasets/"+i , "ill-soilmoist-data-Merge.csv" ) #merging all datasets in folder 
    print( "Function call complete!")
    


    
    
    
    
    
    