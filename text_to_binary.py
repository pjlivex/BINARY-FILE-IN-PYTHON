import pickle
with open('pjlivex.dat','wb') as f:
    text=input('enter the text ')
    pickle.dump(text,f)
    
