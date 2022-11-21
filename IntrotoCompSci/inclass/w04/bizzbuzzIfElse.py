"""
Trace through this program and predict the output.
"""

def main():
    for i in range(1,36):
        if i%5==0 and i%7==0:
            print("bizz buzz")
        elif i%5==0:
            print("bizz")
        elif i%7==0:
            print("buzz")
        else:
            print(i)

main()
