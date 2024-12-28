import pickle
def verify(sno):
    with open("NIT.data","rb") as fp:
        snos=[]
        while(True):
            try:
                record=pickle.load(fp)
                snos.append(record[0])
            except EOFError:
                break
        if sno in snos:
            return True
        else:
            return False
