def divisor(num):
    #divisor=[x for x in range(1,num+1) if num%x==0]
    divisor=list(filter(lambda x : num%x==0, range(1,num)))
    return divisor

def run():
    try:
        num= int(input("Ingresa un numero "))
    except ValueError as ve:
        return print(ve)    
    print(divisor(num))
    print("Termina el programa")

if __name__ == "__main__":
    run()