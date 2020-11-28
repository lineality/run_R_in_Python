# Mix Python and R to convert files to .csv

"""
Instructions to use:
    1. open a terminal in the folder where your .rds files are
    2. Run this line in terminal:
       $ python3 py_r_csv.py
"""

"""
(User) Problem
We Have: many big .rds files (which can only be opened in R)
We Need: .csv files
We Must: Use python

Solution (Product)
The strategy is to use python to make and then call R scripts.

Use R to convert .rds R database files to .csv files,
in a why that is overall inside a python script
that can be called inside a directory and 
will then convert all applicable files inside that directory.

e.g. Let's convert the .rds files found here:
    https://hanlab.uth.edu/HeRA/download

There are only 2 lines of code to be run in R (converting .rds to .csv):
    df <- readRDS("{doc_name}.rds")
    write.csv(df, "{doc_name}.csv")

The challenge is to automate this.
The automation and file management is easier in Python.
(And in some cases the required code-stack is python, not R.)

What we need is the ability to call an R script inside Python:
We can do this with these one line (not including the import line):

    import subprocess
    return_code = subprocess.call(['/usr/bin/Rscript','convert.r'])

    or
    return_code = subprocess.call([ where R is on your computer , the r script])

(Note: "return_code = " may not be required, it just tell you 
whither the R script returned something or not: 0 means no, etc.)
"""


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

    return None


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

        # Run the R script:
        # (which converts the .rds to .csv!)
        # Note: requires import subprocess
        subprocess.call(['/usr/bin/Rscript','convert.r'])

    # Show Progress:
    progress_counter += 1
    print(progress_counter)


# Clean Up Trash
# remove the last R script
os.remove("convert.r")

# Yay!!
print("All Done!!")

