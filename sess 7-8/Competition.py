def alphabet_position(text):
    vowels=('a','e','i','o','u')
    dict = {0:' ',1:'a','2':'b','c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
    new_text = text.lower()
    counter=0
    line=''
    for line in new_text:
        for char in line:
            if char in vowels:
                counter+=1


    return (new_text)





