"""
This program demonstrates formatted printing.

Use %d as a placeholder for integers.
Use %f as a placeholder for floats.
Use %s as a placeholder for strings.

You can specify how many spaces to reserve for a value by
giving a width after the % and before the type code. For
example: %10s

You can specify how many decimal places to show for floats
by putting a period and number after the % and before the
f.  For example: %.2f

You can combine the width and number of decimal places
for a float like this: %5.2f

You can specify tabs by using \t in the format string.

"""

def main():
    val1 = int(input("Enter an integer: "))
    val2 = float(input("Enter a float: "))
    val3 = input("Enter a string: ")

    print()
    print("Integer: %d Float: %.2f String: %s" % (val1, val2, val3))

    print()
    print("%15s \t %15s \t %15s" % ("Integer", "Float", "String"))
    print("%15s \t %15s \t %15s" % ("-"*15, "-"*15, "-"*15))
    print("%15d \t %15.1f \t %15s" % (val1, val2, val3))

main()
