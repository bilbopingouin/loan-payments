# Short description

Calculate the loan and yearly payments in Germany

# Help

### Run the python script

Simply run

    python calculate_debt.py
    
which would provide something like

    $ python calculate_debt.py                                                                                                                                                                       
    Enter debt [1] or calculate debt [2]? Please enter 1 or 2: 
    Please enter the choice: 2
    Please enter the price: 300000
    Please enter the capital: 30000
    Please enter the commission (3.57): 3.57
    Please enter the interest rate: 1
    Please enter the monthly paiement: 600
    Please enter the fixed years: 15
    Please enter the yearly extra transfer: 1000
    
    ---
    Current status:
     original debt: 295710.00
     current year: 0.00
     yearly extra transfer: 1000.00
     interest rate: 1.00
     monthly paiement: 600.00
     fixed years: 15.00
     current debt: 295710.00
    
    ---
      Year |       Pay/month     Reimb/month     Inter/month |     Irreg reimb |       Rest debt
    --------------------------------------------------------------------------------------------
         1 |          600.00          353.58          246.42 |         1000.00 |       290467.10
         2 |          600.00          357.94          242.06 |         1000.00 |       285171.77
         3 |          600.00          362.36          237.64 |         1000.00 |       279823.49
         4 |          600.00          366.81          233.19 |         1000.00 |       274421.72
         5 |          600.00          371.32          228.68 |         1000.00 |       268965.94
         6 |          600.00          375.86          224.14 |         1000.00 |       263455.60
         7 |          600.00          380.45          219.55 |         1000.00 |       257890.16
         8 |          600.00          385.09          214.91 |         1000.00 |       252269.06
         9 |          600.00          389.78          210.22 |         1000.00 |       246591.75
        10 |          600.00          394.51          205.49 |         1000.00 |       240857.67
        11 |          600.00          399.29          200.71 |         1000.00 |       235066.24
        12 |          600.00          404.11          195.89 |         1000.00 |       229216.90
        13 |          600.00          408.99          191.01 |         1000.00 |       223309.07
        14 |          600.00          413.91          186.09 |         1000.00 |       217342.16
        15 |          600.00          418.88          181.12 |         1000.00 |       211315.59
    
    ---
    Current status:
     original debt: 295710.00
     current year: 15.00
     yearly extra transfer: 1000.00
     interest rate: 1.00
     monthly paiement: 600.00
     fixed years: 15.00
     current debt: 211315.59

    Press enter...
    

### Generate an exe and run it

Generate the exe by running

    python setup.py

This will generate the file `dist/calculate_debt.exe` which can either be run in a command line or simply by double-clicking on the file.
