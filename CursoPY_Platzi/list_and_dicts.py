def run():
    my_list=[1,"Hello",True, 4.5]
    my_dict={"firstname":"Yair","lastname":"Riascos"}

    super_list=[
        {"firstname":"Yair","lastname":"Riascos"},
        {"firstname":"Mike","lastname":"Towers"},
        {"firstname":"Pepe","lastname":"Cuenca"},
        {"firstname":"Fabio","lastname":"Benitez"},
        {"firstname":"Luis","lastname":"Perenna"}
    ]
    super_dict={
        "natural_nums":[1,2,3,4,5],
        "integer_nums":[-1,0-2,1,2],
        "floating_nums":[1.1,4.5,6.43]
    }
    for x in super_list:
        for key, value in x.items():
            print( key, "->",value)
            
if __name__ == "__main__":
    run()