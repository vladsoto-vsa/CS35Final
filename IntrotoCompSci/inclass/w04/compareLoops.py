"""
This program shows a for loop and a while loop that produce the same
output: printing the numbers from 0 to 3 a line at a time. 
"""

def main():
    end = 4

    ##### for loop
    for i in range(end):
        print(i)
    print("done for")

    ##### while loop
    j = 0               
    while j < end:      
        print(j)
        j = j+1         
    print("done while")

main()
