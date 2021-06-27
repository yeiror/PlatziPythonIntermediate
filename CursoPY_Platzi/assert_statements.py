def divisors(num):
    divisors= list(filter(lambda x: num%x ==0 , range(1,num+1)))
    return divisors

def run():
    num =input("Ingresa un número ")
    assert num.isnumeric(), "Debes ingresar un número"
    print(divisors(int(num)))

if __name__=="__main__":
    run()
