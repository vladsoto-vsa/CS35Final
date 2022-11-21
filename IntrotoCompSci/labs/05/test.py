
def foo(val):
    val[0] = "b"
    print(val)
    return len(val)

def main():
    temp = ["l", "o", "l"]
    x = foo(temp)
    print(x, temp)

main()
