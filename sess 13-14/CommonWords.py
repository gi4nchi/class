punctuation2=",.;:!?\"'()[]{}-*<>"
def common_words(file_name):
    Text=open(file_name,"r")
    d={}
    for line in Text:
        for c in punctuation2:
            line=line.replace(c," ")
        words=line.split()
        for word in words:
            if word in d:
                d[word]+=1
            else:
                d[word]=1

    values=list(d.values())
    values.sort(reverse=True)
    common=[]
    for numbers in values[:10]:
        for keys in d:
            if d[keys]==numbers:
                common.append((keys,numbers))
    print("the most common words are:")
    for i in common:
        print((i[0],i[1],"times"))

common_words("HarryPotter")


