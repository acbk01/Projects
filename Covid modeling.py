import pylab
import random
import numpy as np

N = input("Wprowadź populacje Polski:")
N = float(N)
S = []                                                          # Osoby podatne na infekcjie
E = []                                                          # Osony narażone
I1 = []                                                          # Osoby zarażone
I2 = []
H = []                                                          # Osoby w szpitalu
V = []                                                          # Osoby na intensywnej terapi
Vo = []
D = []                                                          # Osoby zmarłe
R = []                                                          # Osoby zdrowe
G1 = []                                                          # Całkowita liczba zachorowań
G2 = [] 
Ho = []
w_1 = 0.28  
w_2 = 0.125  
w_3 = 0.125  
e_1 = 0.066  
e_2 = 0.3  
e_3 = 0.57  
R_0 = 2                                                    # Bazowy wsp. reprodukcji
R_0 = float(R_0)
k = float(input("Podaj współczynnik kappa (liczba od 0 do 1):"))# wsp. izolacji
if k < 0 or k > 1:
    k = float(input("Wprowadziłeś złą liczbę, spróbuj ponownie:"))
y = 0.53                                                        # Współczynnik gamma   

s = 1 / 4.6                                                     # Współczynnik sigma    
b = (float(R_0) * float(y)) / float(N)
S.insert(0, N - 1) 
I1.insert(0, 1)  
E.insert(0, 0)
H.insert(0, 0)  
Ho.insert(0, 0)
V.insert(0, 0)
D.insert(0, 0)
R.insert(0, 0)
G1.insert(0, 1)
l = 0.76

i = 1 #Bez Gaussa
while i < 7:
    S.insert(i, N - G1[i - 1])
    E.insert(i, G1[i - 1] * b * S[i])
    I1.insert(i, E[i] * s)
    G1.insert(i, G1[i - 1] + I1[i])
    R.insert(i, 0)
    V.insert(i, 0)
    Vo.insert(i, 0)
    H.insert(i, 0)
    Ho.insert(i, 0)
    D.insert(i, 0)
    i += 1

i = 7  #pojawia się szpital
while i < 10:
    S.insert(i, N - G1[i - 1])
    E.insert(i, ((G1[i - 1] - G1[i - 7]) * b * S[i]))  
    I1.insert(i, E[i] * s)
    G1.insert(i, G1[i - 1] + I1[i])
    R.insert(i, I1[i - 7] * (1 - e_1) * l)  
    V.insert(i, 0)
    Vo.insert(i, 0)
    H.insert(i, I1[i - 7] * e_1 * l)
    Ho.insert(i, Ho[i - 1] + H[i] - H[i - 7])
    D.insert(i, 0)
    i += 1

i = 10  #pojawiają się obostrzenia
while i < 14:
    S.insert(i, N - G1[i - 1])
    E.insert(i, ((G1[i - 1] - G1[i - 7]) * b * k * S[i]))  
    I1.insert(i, E[i] * s)
    G1.insert(i, G1[i - 1] + I1[i])
    R.insert(i, I1[i - 7] * (1 - e_1) * l)  
    V.insert(i, 0)
    Vo.insert(i, 0)
    H.insert(i, I1[i - 7] * e_1 * l)
    Ho.insert(i, Ho[i - 1] + H[i] - H[i - 7])
    D.insert(i, 0)
    i += 1

i = 14  #pojawia się intensywna terapia
while i < 21:
    S.insert(i, N - G1[i - 1])
    E.insert(i, ((G1[i - 1] - G1[i - 7]) * b * k * S[i]))  
    I1.insert(i, E[i] * s)
    H.insert(i, I1[i - 7] * e_1 * l)
    Ho.insert(i, Ho[i - 1] + H[i] - H[i - 7])
    D.insert(i, 0)
    R.insert(i, I1[i - 7] * (1 - e_1) * l + H[i - 7] * (1 - e_2) * w_1)
    G1.insert(i, G1[i - 1] + I1[i])
    V.insert(i, H[i - 7] * e_2 * w_1)
    Vo.insert(i, Ho[i - 7] * e_2 * w_1)
    i += 1

i = 21
while i < 100:
    S.insert(i, N - G1[i - 1])
    E.insert(i, ((G1[i - 1] - G1[i - 7]) * b * k * S[i]))  
    I1.insert(i, E[i] * s)
    H.insert(i, I1[i - 7] * e_1 * l)
    Ho.insert(i, Ho[i - 1] + H[i] - H[i - 7])
    R.insert(i, I1[i - 7] * (1 - e_1) * l + H[i - 7] * (1 - e_2) * w_1 + V[i - 7] * (1 - e_3) * w_2)
    G1.insert(i, G1[i - 1] + I1[i])
    V.insert(i, H[i - 7] * e_2 * w_1)
    Vo.insert(i, Ho[i - 7] * e_2 * w_1)
    D.insert(i, V[i - 7] * e_3 * w_2)
    i += 1
G1_a = [round(n) for n in G1]
R_a = [round(m) for m in R]

#print("I",I)
#print("E",E)
##print("G",G)
#print("G_a",G_a)
#print("Ho", Ho)
#print("Vo", Vo)
#print("D", D)

j = range(0, 100)
pylab.plot(j, G1, label="Całkowita liczba chorych")
pylab.axvline(x=10, color='r', linestyle='dotted')
pylab.title('Wykres G')
pylab.legend(loc="upper left")
pylab.show()

j = range(0, 100)
pylab.plot(j, G1_a, label="Całkowita liczba chorych")
pylab.axvline(x=10, color='r', linestyle='dotted')
pylab.title(' Wykres G_a')
pylab.show()

j = range(0, 100)
pylab.plot(j, I1, label="Liczba nowych dziennych zachowowań")
pylab.axvline(x=10, color='r', linestyle='dotted')
pylab.title('Wykres I1')
pylab.show()








                                                # Współczynnik gamma   
                                                    # Współczynnik sigma    
S.insert(0, N - 1) 
I2.insert(0, 1)  
E.insert(0, 0)
H.insert(0, 0)  
Ho.insert(0, 0)
V.insert(0, 0)
D.insert(0, 0)
R.insert(0, 0)
G2.insert(0, 1)
l = 0.76

i = 1 #Z Gaussem
while i < 7:
    S.insert(i, N - G2[i - 1])
    E.insert(i, G2[i - 1] * b * S[i])
    I2.insert(i, E[i] * s)
    G2.insert(i, G2[i - 1] + I2[i])
    R.insert(i, 0)
    V.insert(i, 0)
    Vo.insert(i, 0)
    H.insert(i, 0)
    Ho.insert(i, 0)
    D.insert(i, 0)
    i += 1

i = 7  #pojawia się szpital
while i < 10:
    S.insert(i, N - G2[i - 1])
    E.insert(i, ((G2[i - 1] - G2[i - 7]) * b * S[i]))  
    I2.insert(i, E[i] * s)
    G2.insert(i, G2[i - 1] + I2[i])
    R.insert(i, I2[i - 7] * (1 - e_1) * l)  
    V.insert(i, 0)
    Vo.insert(i, 0)
    H.insert(i, I2[i - 7] * e_1 * l)
    Ho.insert(i, Ho[i - 1] + H[i] - H[i - 7])
    D.insert(i, 0)
    i += 1

i = 10  #pojawiają się obostrzenia
while i < 14:
    S.insert(i, N - G2[i - 1])
    E.insert(i, ((G2[i - 1] - G2[i - 7]) * b * k * S[i]))  
    I2.insert(i, E[i] * s)
    G2.insert(i, G2[i - 1] + I2[i])
    R.insert(i, I2[i - 7] * (1 - e_1) * l)  
    V.insert(i, 0)
    Vo.insert(i, 0)
    H.insert(i, I2[i - 7] * e_1 * l)
    Ho.insert(i, Ho[i - 1] + H[i] - H[i - 7])
    D.insert(i, 0)
    i += 1

i = 14  #pojawia się intensywna terapia
while i < 21:
    u = random.randint(1, 7)
    if u == 5:
        z = np.abs(round(random.gauss(0,np.sqrt(G2[i-1]))))
    else:
        z = 0
    S.insert(i, N - G2[i - 1])
    E.insert(i, ((G2[i - 1] - G2[i - 7]) * b * k * S[i]))  
    I2.insert(i, E[i] * s + z)
    H.insert(i, I2[i - 7] * e_1 * l)
    Ho.insert(i, Ho[i - 1] + H[i] - H[i - 7])
    D.insert(i, 0)
    R.insert(i, I2[i - 7] * (1 - e_1) * l + H[i - 7] * (1 - e_2) * w_1)
    G2.insert(i, G2[i - 1] + I2[i])
    V.insert(i, H[i - 7] * e_2 * w_1)
    Vo.insert(i, Ho[i - 7] * e_2 * w_1)
    i += 1

i = 21
while i < 100:
    u = random.randint(1, 7)
    if u == 5:
        z = np.abs(round(random.gauss(0,np.sqrt(G2[i-1]))))
    else:
        z = 0
    S.insert(i, N - G2[i - 1])
    E.insert(i, ((G2[i - 1] - G2[i - 7]) * b * k * S[i]))  
    I2.insert(i, E[i] * s + z)
    H.insert(i, I2[i - 7] * e_1 * l)
    Ho.insert(i, Ho[i - 1] + H[i] - H[i - 7])
    R.insert(i, I2[i - 7] * (1 - e_1) * l + H[i - 7] * (1 - e_2) * w_1 + V[i - 7] * (1 - e_3) * w_2)
    G2.insert(i, G2[i - 1] + I2[i])
    V.insert(i, H[i - 7] * e_2 * w_1)
    Vo.insert(i, Ho[i - 7] * e_2 * w_1)
    D.insert(i, V[i - 7] * e_3 * w_2)
    i += 1
G2_a = [round(n) for n in G2]
R_a = [round(m) for m in R]

#print("I",I)
#print("E",E)
##print("G",G)
#print("G_a",G_a)
#print("Ho", Ho)
#print("Vo", Vo)
#print("D", D)

j = range(0, 100)
pylab.plot(j, G1, label="Całkowita liczba zachorowań bez szumu")
pylab.axvline(x=10, color='r', linestyle='dotted')
pylab.plot(j, G2, '-r', label="Całkowita liczba zachorowań z szumem")
pylab.title('Wykres całkowitej liczby zachorowań')
pylab.legend(loc="upper left")
pylab.show()

j = range(0, 100)
pylab.plot(j, G2_a, label="Całkowita liczba chorych")
pylab.axvline(x=10, color='r', linestyle='dotted')
pylab.title(' Wykres G2_a')
pylab.show()

j = range(0, 100)
pylab.plot(j, I1, label="Liczba dziennej liczby zachowowań bez szumu")
pylab.axvline(x=10, color='r', linestyle='dotted')
pylab.plot(j, I2, '-r', label="Liczba dziennej liczby zachowowań z szumem")
pylab.title('Wykres dziennej liczby zachorowań')
pylab.legend(loc="upper left")
pylab.show()