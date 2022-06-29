How to make a spreadsheet

Use following command:
    python gen_spread.py name_of_desired_output_file year month first_pay_period_length

It will generate a new csv file in this folder with scheduled information

Example: python spread_gen.py August 2022 8 15

This command would ask the scheduler to genrate a schdule for august 2022, with the first pay period ending on the 15th. 
It would then create a file called August.csv.