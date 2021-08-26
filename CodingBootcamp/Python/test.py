def getInfo():
    var1 = input('Please provide the first numeric value: ')
    var2 = input('please provide the second numerfic value: ')
    compute(varr1, vars2)


def compute(var12, var2):
    try: 
        var3 = int(var1) + int(var2)
        print('{} + {} = {}'.format(var1, var2, var3))
    except:
        print('You did not provide a numeric value:')
        




if __name__ == "__main__":
    getInfo()

    
