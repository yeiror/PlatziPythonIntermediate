def read():
    
    with open("./archivos/numbers.txt", "r", encoding="utf-8") as f:
        numbers=[int(x) for x in f]
    
    return print(numbers)

def write():
    names= ["Facun", "Yair", "Mike", "Xalatiel", "Rocío"]
    with open("./archivos/names.txt","a",encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")

def run():
    write()

if __name__=="__main__":
    run()