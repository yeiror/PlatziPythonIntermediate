def run():
    #print([x**2 for x in range(101) if x%3!=0])
    print({i: round(i**(1/2),2) for i in range(1,1001)})

if __name__=="__main__":
    run()