# Two Way Communication R <-> Python
 
"""
Instructions to use:
1. Run this line in terminal:
   $ python3 2_Way_Py_R.py
"""
 
"""
(User) Problem
  We know / We have:
        script execution from R in python
 
  We need / We don't have:
       The output (return)
       of functions from R accessible to python
 
  We must:
      Try to do this, in python, without special libraries
      (which can be fragile, slow, break, conflict, etc.)
      or limitations on which OS this solution can run on.
 
Solution (Product)
   There are two parts we need:
   1. One part for python to be able to run an R script
   2. A second part for the output of the R script to be
   output in a way that python can access it.
 
   Here are those two parts:
 
   1. For Python to call an R script:
   import subprocess
   return_code = subprocess.call(['/usr/bin/Rscript','convert.r'])
 
   or
   return_code = subprocess.call([ where R is on your computer, the r script])
 
   Note: You don't need 'return_code =' unless you want to know if
   the script returned something.
 
   2. R can produce output as a readable file
   instead of printing to a console
   by using the sink() function (no special libraries needed)
   just call sink twice, before and after the function call:
 
   e.g.
   sink(file = "ouput_file_name.txt")
   funtion_with_ouput()
   sink(file = NULL)
 
 
Note:
For python, you enter a python environment by typing:
$ python
 
And you run a script by typing:
$ python script_name.py
 
But for R,
You enter the R command line enviroment by typing:
$ R
 
And you run an R script by typing:
$ Rscript script_name.r
 
So that is why subprocess is calling "Rscript"
 
"""
 
import subprocess
 
# a function to write a custom R script that produces an readable output
def write_R_output_script(function_text,
                         script_name = "script.r",
                         output_file_name = "r_output.txt"):
 
   script_text = f'sink("{output_file_name}")\n{function_text}\nsink(file = NULL)'
  
   # create, write-to, save .txt file, & close
   file_to_create = open(script_name, "w")
   file_to_create.write(script_text)
   file_to_create.close()
 
   return None
 
#########
## Set Up
#########
 
# Write your function as raw text:
function_input = r"""my_fun <- function(x) {
z <- x * x
return(z)
}
my_fun(x = 2)"""
 
# Default Script Name =
script_name = "script.r"
 
 
#######################
## Write & Run R Script
#######################
 
# Make R Script (which return output as a file)
write_R_output_script(function_input, script_name)
 
# Run the R Script
subprocess.call(['/usr/bin/Rscript',script_name])
 
# Optional Clean Up Trash: remove the R script
# os.remove(script_name)
 
 
###########################
## READ R-Ouput With Python
###########################
 
# e.g. using default file name
output_file_name = 'r_output.txt'
 
# open it
file_to_create = open(output_file_name, "r")
# print it
print("This is what R says!:\n", file_to_create.read())
# close it
file_to_create.close()
 


