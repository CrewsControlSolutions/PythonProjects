

def getInfo():
    var1 = input("\nPlease provide the first numeric value: ")
    var2 = input("\nPlease provide the second numeric value: ")
    return var1,var2


def compute():
    go = True
    while go:
        a, b = getInfo()
        try:
            var3 = int(a) + int(b)
            go = False
        except ValueError as e:
            print("{}: \n\nYou did not provide a numeric value.".format(e))
        except:
            print("\n\nOops, you provided invalid input. The program will close now.")
    print("{} + {} = {}".format(a,b,var3))



if __name__ == "__main__":
    compute()
