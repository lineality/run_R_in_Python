# run_R_in_Python
#### An Approach to run R scripts inside Python scripts, to get the best of both worlds.


## Spirit of Approach
- small is good
- fewer libraries and dependencies are better
- cross-system compatibility is good
#### this uses no special libraries so it can be used without any need to configure environments


## Approach:
#### The strategy is to use python to make and then call R scripts


## Google Colab Notebooks:

#### Amazingly, this works in Colab (so Colab must include R as well as Python)

https://colab.research.google.com/drive/1AI3a2gWrKikqaS6HKDvKqFbn-WZkdmYU?usp=sharing

```
# Mix Python and R to convert files to .csv
 
# (User) Problem
# We know / We have: big .rds files (which can only be opened in R)
# We need / We don't have: .csv files
# We must: Use python,
# and convert a large number of files,
# too many to do individually manually
 
# Solution (Product)
#
# Use R to convert rds R database files to csv files,
# in a why that is overall inside a python script
# that can be called and will convert all applicable files
# inside a directory
 
 
# e.g. files https://hanlab.uth.edu/HeRA/download
# core code to run an r script in python
# https://stackoverflow.com/questions/24544190/calling-r-script-from-python-using-rpy2#24544362
 
# There are only 2 lines of code to be run in R
# df <- readRDS("{doc_name}.rds")
# write.csv(df, "{doc_name}.csv")
#
# The challenge is to automate this.
# The automation and file management is easier in Python
# (and in some cases the required code-stack is python, not R)
 
# What we need is the ability to call an R script inside Python:
# We can do this with these ~two lines (including the import):
 
# import subprocess
# retcode = subprocess.call(['/usr/bin/Rscript','convert.r'])
# or
# retcode = subprocess.call([ where R is on your computer , the r script])
 
# The strategy is to use python to make and then call R scripts
 
# Instructions to use:
# 1. open a terminal in the folder where your .rds files are
# 2. Run this line in terminal:
#    $ python3 py_r_csv.py
 
import os
import subprocess
 
# a function to write the temporary R script
def write_script(doc_name):
 
   # create file: readme_text
   readme_text = f'df <- readRDS("{doc_name}.rds")\nwrite.csv(df, "{doc_name}.csv")'
 
   # create, write-to, & save .txt file
   file_to_create1 = open("convert.r", "w")
   file_to_create1.write(readme_text)
   file_to_create1.close()
 
   pass
 
# in the case of a long wait, give the user some idea
# of the progress through the files (crude but works)
progress_counter = 0
print("progress Counter:")
 
# iterate through all .rds files in directory
the_path = "."
for filename in os.listdir(the_path):
 
   # check that each file is really an .rds file
   if filename[-4:] == ".rds":
 
 # save the file name minus the .suffix
       doc_name = filename[:-4]
 
       # write the R script
       write_script(doc_name)
 
       # run the R script:
       # which converts the .rds to .csv!
       # note: requires import subprocess
       retcode = subprocess.call(['/usr/bin/Rscript','convert.r'])
 
   # show progress:
   progress_counter += 1
   print(progress_counter)
 
 
# Clean up Trash
# remove the last R script
os.remove("convert.r")
 
# Yay!!
print("All Done!!")


```
