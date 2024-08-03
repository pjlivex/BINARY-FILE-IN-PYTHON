import pickle
with open("pjlivex.dat","wb") as f:
        n=int(input("how many records to store into binary file"))
        for i in range(n):
            bid=int(input("enter bookid"))
            bn=input("enter bookname")
            au=input("enter author name")
            s=[bid,bn,au]
            pickle.dump(s,f)
