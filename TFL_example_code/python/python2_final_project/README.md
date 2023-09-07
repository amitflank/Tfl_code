# How to make a spreadsheet

Use following command:
>python gen_spread.py name_of_desired_output_file year month first_pay_period_length[^1]

It will generate a new csv file in this folder with scheduled information

Example: 
>python spread_gen.py August 2022 8 15

This command would ask the scheduler to generate a schedule for august 2022, with the first pay period ending on the 15th. 
It would then create a file called August.csv.


#Assignment Goals

The goal of this assignment is for students to complete the scheduler. Some of the code has already been provided as well as the overall structure via pythons type hinting mechanic. Students should fill in the necessary methods. The spread_gen and mentor_db files have been provided to help students generate a csv file using the scheduler once it is complete. The oct_sched.csv file contains the expected schedule output of the given db file so students can check their work. 

[^1]: Note: Must by in scheduling directory for this command to work 