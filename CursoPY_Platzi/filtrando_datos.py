DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():

    #Desarrolladores de  python
    all_python_devs= list(filter(lambda x:x["language"]=="python",DATA))
    all_python_devs= list(map(lambda x:x["name"],all_python_devs))
    #print(all_python_devs)

    #Desarrolladores de platzi
    all_Platzi_workers= list(filter(lambda x:x["organization"]=="Platzi",DATA))
    all_Platzi_workers= list(map(lambda x:x["name"],all_Platzi_workers))
    #print(all_Platzi_workers)


    #Obteniendo los mayores de 18
    adults= [x for x in DATA if x["age"]>18]
    adults= [x["name"] for x in adults]
    #for workers in adults:
    #    print(workers)

    #Mayores de 70, el operador pipe concatena nuevos items en un diccionario
    #old_people = list(map(lambda worker: worker |{"old":worker["age"]>70},DATA))
    old_people=[x | {"old": x["age"]>70} for x in DATA]
    for x in old_people:
        print(x["name"],x["old"])

if __name__=="__main__":
    run()
