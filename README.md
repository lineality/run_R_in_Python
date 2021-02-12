# run_R_in_Python
### An Approach to run R scripts inside Python scripts, to get the best of both worlds.


# Goals
#### 1. Run an R-script from python (Simple Call)
#### 2. Get the output of a function (run in R) back into python (Two Way Communication)


# Spirit of Approach
- small is good
- fewer libraries and dependencies are better
- cross-system compatibility is good
- less special environment configuration is good


## Approach:
#### The strategy is to use python to make and then call R scripts.


## R in Colab:
#### Amazingly, most of this works in Colab (so Colab includes R as well as Python...wow...)


# Summary 1. Run an R-script from python (Simple call)
#### There are only 2 lines of code to be run in R
```
df <- readRDS("{doc_name}.rds")
write.csv(df, "{doc_name}.csv")
```
#### The challenge is to automate the R code. The automation and file management is easier in Python (and in some cases the required code-stack is python, not R)
 
#### What we need is the ability to call an R script inside Python:
#### We can do this with this one line (not including the import), which wonderfully does not require any special installs or pip-installed libraries, just 'subprocess' which comes standard:
```
import subprocess
 
subprocess.call(['/usr/bin/Rscript','convert.r'])
or
subprocess.call([ where R is on your computer , the r script])
```
## Script Factory
#### With python we can make and remake and run R scripts very easily as we need them. This may be a little verbose, but it is not fragile, OS dependent, or a black box. 

# Summary 2. Output from R back into Python (Two Way Communication)

#### Just two lines of R code will direct the output into a file (rather than a console print). The function needed is sink(). 
 
#### A "Sink Sandwich":
#### The structure of the R code you create should look like the following so that the output is accessible to python (e.g. so that the output is a file accessible to another program and not just a print to the terminal). Sandwich your R function between two calls to the sink() function, and the output is then readable to python (in the file you name in that call).    
e.g.
```
   sink(file = "ouput_file_name.txt")
   funtion_with_ouput()
   sink(file = NULL)
```
#### This can output individual values or even the converted contents of dataframes (e.g. converted into .csv format). 
 

# Example Code, Notebooks, Scripts:

#### Calling an R function, automated with Python
[python script](https://github.com/lineality/run_R_in_Python/blob/main/py_r_csv.py)  
[Notebook](https://github.com/lineality/run_R_in_Python/blob/main/colab_py_r_csv_test.ipynb)  
[Colab Online](https://colab.research.google.com/drive/1AI3a2gWrKikqaS6HKDvKqFbn-WZkdmYU?usp=sharing#scrollTo=eQ1ExjI0erk_) 

#### Sending output back and forth between R and Python
[python script](https://github.com/lineality/run_R_in_Python/blob/main/two_way_py_r.py)  
[notebook](https://github.com/lineality/run_R_in_Python/blob/main/2_Way_Py_R.ipynb)  
[Colab Online](https://colab.research.google.com/drive/1D3A6btJgyhJ0VH7j6oqQC6SSUkK4xBAT?usp=sharing) 




