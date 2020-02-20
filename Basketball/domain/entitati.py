class Jucator():
    
    def __init__(self,nume,prenume,inaltime,post):
        self.__nume = nume
        self.__prenume = prenume
        self.__inaltime = inaltime
        self.__post = post

    def get_nume(self):
        return self.__nume


    def get_prenume(self):
        return self.__prenume


    def get_inaltime(self):
        return self.__inaltime


    def get_post(self):
        return self.__post


    def set_nume(self, value):
        self.__nume = value


    def set_prenume(self, value):
        self.__prenume = value


    def set_inaltime(self, value):
        self.__inaltime = value


    def set_post(self, value):
        self.__post = value

    @classmethod
    def read_entity(cls,line):
    #Functia transforma o linie dintr-un fisier intr-o entitate jucator
        line = line.split(' ')
        nume = line[0]
        prenume = line[1]
        inaltime = line[2]
        inaltime = int(inaltime)
        post = line[3]
        
        return Jucator(nume,prenume,inaltime,post)
    
    @classmethod
    def write_entity(cls,entitate):
    #Transforma o entitate intr-un string
    
        return (entitate.get_nume() + " " + entitate.get_prenume() + " " + str(entitate.get_inaltime()) + " " + entitate.get_post())

    def __str__(self):
        
         return (self.get_nume() + " " + self.get_prenume() + " " + str(self.get_inaltime()) + " " + self.get_post())


