def run():
    my_list=[1,4,5,6,9,13,19,21]
    square = list(map(lambda x:x**2,my_list))
    print(square)


if __name__=="__main__":
    run()