import streamlit as st
import random

alfabeto='abcdefghilmnopqrstuvwxyzABCDEFGHILMNOPQRSTUVWXYZ'
caratteriSpecial='?-_#*()![]&'
caratteriSpeciali=list(caratteriSpecial)
numeri='0123456789'
cifre=list(numeri)
alfabetoL=list(alfabeto)

def CreaPassword(lunghezza, s, c):
    password=[]
    if s+c < lunghezza:
        for a in range(0,s):
            s1=random.choice(caratteriSpeciali)
            password.append(s1)
        for b in range(0,c):
            s2=random.choice(cifre)
            password.append(s2)
    else:
        return 'caratteri speciali + cifre deve essere minore della lunghezza della password'
    while len(password)!=lunghezza:
        i=random.randint(0,len(alfabetoL))
        password.append(alfabetoL[i])
        random.shuffle(password)
    return ''.join(password)

st.title('Generatore di password')
lunghezza = st.slider('Indica la lunghezza della password', min_value=1, max_value=20, value=8)
s = st.slider('Quanti caratteri speciali vuoi?', min_value=0, max_value=lunghezza, value=2)
c = st.slider('Quanti cifre vuoi?', min_value=0, max_value=lunghezza-s, value=2)
password = CreaPassword(lunghezza, s, c)
st.write('La tua password è:', password)
