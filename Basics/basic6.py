

def multiply():
    go = True
    while go:
        a = input("\nEnter first number:\n")
        b = input("\nEnter second number:\n")
        try:
            c = float(a) * float(b)
            go = False
        except ValueError as e:
            print("\nError: You did not provide a numeric value. Specifically, ".format(e))
        finally:
            print("\nPlease try again...\n\n")
    print("{} * {} = {}".format(a,b,c))



if __name__ == "__main__":
    multiply()
