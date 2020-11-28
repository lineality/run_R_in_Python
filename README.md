# run_R_in_Python
#### An Approach to run R scripts inside Python scripts, to get the best of both worlds.

# Goals
#### 1. Run an R-script from python (Simple call)
#### 2. Get the output of a function (run in R) back into python (Two Way Communication)

# Spirit of Approach
- small is good
- fewer libraries and dependencies are better
- cross-system compatibility is good
#### This uses no special libraries so it can be used without any need to configure environments.


## Approach:
#### The strategy is to use python to make and then call R scripts.


## Google Colab Notebooks:

#### Amazingly, most of this works in Colab (so Colab includes R as well as Python...wow...)


## Sample Summary:
#### There are only 2 lines of code to be run in R
```
df <- readRDS("{doc_name}.rds")
write.csv(df, "{doc_name}.csv")
```
#### The challenge is to automate the R code. The automation and file management is easier in Python (and in some cases the required code-stack is python, not R)
 
#### What we need is the ability to call an R script inside Python:
#### We can do this with these ~two lines (including the import), which wonderfully does not require any special installs or pip-installed libraries, just 'subprocess' which is standard:
```
import subprocess
 
subprocess.call(['/usr/bin/Rscript','convert.r'])
or
subprocess.call([ where R is on your computer , the r script])
```
## Script Factory
#### With python we can make and remake and run R scripts very easily as we need them. This may be a little verbose, but it is not fragile, OS dependent, or a black box. 



# Example Code, Notebooks, Scripts:

#### Calling an R function, automated with Python
[python script](https://github.com/lineality/run_R_in_Python/blob/main/py_r_csv.py)  
[Notebook](https://github.com/lineality/run_R_in_Python/blob/main/colab_py_r_csv_test.ipynb) 
[Colab Online](https://colab.research.google.com/drive/1AI3a2gWrKikqaS6HKDvKqFbn-WZkdmYU?usp=sharing#scrollTo=eQ1ExjI0erk_) 

#### Sending output back and forth between R and Python
[python script](https://github.com/lineality/run_R_in_Python/blob/main/two_way_py_r.py)  
[notebook](https://github.com/lineality/run_R_in_Python/blob/main/2_Way_Py_R.ipynb) 
[Colab Online](https://colab.research.google.com/drive/1D3A6btJgyhJ0VH7j6oqQC6SSUkK4xBAT?usp=sharing) 




