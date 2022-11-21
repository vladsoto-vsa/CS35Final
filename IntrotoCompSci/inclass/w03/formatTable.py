"""
This program produces a conversion table for meters to
yards (1 meter = 1.09361 yards).  It allows the user to
select the start, stop, and step size for the table.

It uses formatted printing to line up the columns of the
table.
"""

def main():
    print("This program produces a conversion table")
    print("for meters to yards")
    print()

    start = int(input("Enter starting meter: "))
    stop = int(input("Enter ending meter: "))
    step = int(input("Enter step size: "))
    print()

    print("%6s \t %6s" % ("Meters", "Yards"))
    print("%6s \t %6s" % ("-"*6, "-"*6))



    # Suppose the user chose 100 as the start, 400 as the stop, and
    # 100 as the step, then the table should look like this:
    #
    # Meters        Yards
    # ------        -----
    #    100	      109
    #    200	      218
    #    300	      328
    #    400	      437

main()
