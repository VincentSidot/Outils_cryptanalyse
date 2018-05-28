Alphabet = [chr(ord('A')+i) for i in range(26)]

## Crypto

def toUpper(car):
    if ord(car) >= ord('a') and ord(car) <= ord('z'):
        return chr(ord('A')+ord(car)-ord('a'))
    else:
        return car
 
def fixString(str):
    str_fix = ""
    for car in str:
        if (ord(car) >= ord('A') and ord(car) <= ord('Z')) or (ord(car) >= ord('a') and ord(car) <= ord('z')) or car == ' ':
            str_fix += toUpper(car);
    return str_fix;

def fixKey(str):
    str_fix = ""
    for car in str:
        if (ord(car) >= ord('A') and ord(car) <= ord('Z')) or (ord(car) >= ord('a') and ord(car) <= ord('z')):
            str_fix += toUpper(car);
    return str_fix;

def Indice(car):
    if ord(car) >= ord('A') and ord(car) <= ord('Z'):
        return ord(car)-ord('A')

def vignere(str,key,crypt = True):
    str = fixString(str)
    key = fixKey(key)
    new_str = ""
    for i in range(len(str)):
        if str[i] == ' ':
            new_str += str[i]
        else:
            if crypt:
                new_str += Alphabet[(Indice(str[i]) + Indice(key[i%len(key)]))%26]
            else:
                new_str += Alphabet[(Indice(str[i]) - Indice(key[i%len(key)]))%26]
    return new_str

    
## Chaine de test
    
    str1 = fixString("Ceci est un message de test il est ecrit en francais et il devrait donc suivre les règle de statistique propre a la langue francaise")
    
    message = fixString("Qu'elles soient Florentines ou d'Argentines, petites Françaises aux bonnes manières, qu'elles viennent des mers de Chine ou du fond des Angleterres, qu'elles aient le cheveu roux ou la peau noire, qu'elles soient indiennes ou filles d'un soir quand elles ont du christ à l'âme, quand elles sont belles à se pendre. Qu'elles soient riches de l'âme ou pauvres de l'esprit de bonne famille ou bien des rues, qu'elles s'appellent Philomène ou Églantine, qu'elles aient des allures d'ombres de Marilyn. Quand elles sont seule au bar qu'on dirait des nonnes qui ont perdu leur église, qui ont plus rien que des hommes pour espérer rencontrer Dieu, pour éponger la bruine à leurs yeux . Moi j'aime bien regarder, regarder les filles pleurer ça me rend gai. Qu'elles aient le cerveau de pas grand chose, qu'elles soient littéraires, philosophes à leurs heures, quand elles prennent l'orage, qu'elles me ressemblent un peu, quand elles sont toutes fragiles comme une eau qui dort. Quand elles vendent leur corps pour quelques sous, quand tu mets la forme qu'elles disent oui à tout, quand elles croient qu'elles sont libres, quand elles se donnent dans les bras du Malin, quand elles s'abandonnent. Qu'elles soient de Bizance ou de Syracuse, de Belgrade qu'elles soient de celles qui ne pleurent plus, qu'el4les traînent au soleil de Moscou, qu'elles jouent les marquises des nuits, les filles prêtent à tout. Qu'elles soient paysannes ou fille de ministre, ouvrière éperdue dans la fourmilière, qu'elles travaillent à l'usine, qu'elles soient filles de l'air, qu'elles aient les mêmes allures de putes que leur mère . Moi j'aime bien regarder, regarder les filles pleurer ça me rend gai. Dans les villes, dans les campagnes moi je vais comme un assassin en campagne et je taille au couteau des sourires sur les joues des princesses. Moi je suis qu'un pauvre gars, ils m'appellent l'idiot ,celui qui fait peur aux betes, qui fait mal aux oiseaux. Mais faut pas croire, tu sais moi j' suis pas mechant j'ai juste l'air maladroit, je sais juste pas comment faut leur parler aux filles, faut leur parler aux filles . Moi quand je vois les larmes leur tomber la joue, moi quand je vois les larmes leur tomber la joue, moi j' voudrais leur dire qu 'elles sont belles, et qu' il faut pas qu'elles pleurent pour un idiot puis faut qu'elles arretent d'etres connes et de tomber toujours amoureuses de celui qu' il faut pas et que moi, si elles voulaient, moi, moi j 'serais toujours gentil avec elles mais les filles elles aiment pas qu' on soit gentil, elles aiment pas. Alors moi dans les villes, dans les campagnes moi je vais comme un assassin en campagne et je taille au couteau des sourires sur les joues des princesses. Oui dans les villes, dans les campagnes moi je vais comme un assassin en campagne et je taille au couteau des sourires sur les joues des princesses. Quand elles sont seules au bar ou sur les trottoirs, crucifiees par des siecles d'histoires, quand on regarde un peu plus pres, c'est sûr qu'on peut se dire que c'est elles qui ont porte et qui portent la croix du monde. Sur leurs ailes.")
    
## Stats français

def CalcDict():
    file = open('C:\\Users\\Vincent\\Documents\\Python\\Cryptanalyse\\Outils_cryptanalyse\\texte_français.txt','r')
    
    str = ""
    i = 1
    tmp = file.read(1)
    while tmp != '':
        str += fixString(tmp)
        tmp = file.read(1)
        i+=1
    file.close()
    return ProportionOccurence(CountOccurence(str)),i


frequence_apparition_france_wikipedia = { 'E': 0.121+0.0194+0.0031+0.0008+0.0001,'A':0.0711+0.0031+0.0003+0.0001,'I':0.0659+0.0003+0.0001+0.001,'S':0.0651,'N':0.0639,'R':0.0607,'T':0.0592,'O':0.0502+0.0004+0.0001,'L':0.0496,'U':0.0449+0.0002+0.0002+0.0001,'D':0.0367,'C':0.0318,'M':0.0262,'P':0.0249,'G':0.0123,'B':0.0114,'V':0.011,'H':0.011,'F':0.0111,'Q':0.0065,'Y':0.0046,'X':0.0038,'J':0.0034,'K':0.0029,'W':0.0017,'Z':0.0015 }

## Statistique



def moyenne(X):
    rep = 0;
    for i in X:
        rep += i
    return rep/len(X)

def ecart_type(X):
    m = moyenne(X)
    return moyenne([(i-m)*(i-m) for i in X])

def moyenne_carre_ecart(dict1,dict2):
    return moyenne([(dict1[i]-dict2[i])**2 for i in Alphabet])

def maxs_dict(X,number):
    maxs,cars = [0]*number,['0']*number
    for a in Alphabet:
        for j in range(number):
            if X[a] > maxs[j] and a not in cars:
                for i in range(j,number-1):
                    maxs[i+1],cars[i+1]=maxs[i],cars[i]
                maxs[j],cars[j] = X[a],a
    return cars
    
def Next(L,base):
    L[-1] += 1
    for i in range(1,len(L)):
        if L[-i]==base:
            L[-i] = 0
            L[-i-1]+=1
    return L
    
def ensemble_permutation(L):
    rep = [""] * (len(L[0])**len(L))
    P = [0] * len(L)
    for i in range(len(rep)):
        for j in range(len(L)):
            rep[i] += L[j][P[j]]
        Next(P,len(L[0]))
    return rep

def ListPossibleKey(message,keylen,n):
    dicts = ProportionMessageCode(message,keylen)
    keys = []
    for j in range(keylen):
        MAXS = maxs_dict(dicts[j],n)
        key = []
        for p in range(n):
            key += CalculClef(MAXS[p],"E")
        keys += [key.copy()]
    return keys

def Decrypte_mauvaise_implementation(message,keylen,n=3):
    keys = ensemble_permutation(ListPossibleKey(message,keylen,n))
    messages = [ (vignere(message,key,False),key) for key in keys]
    min = 1
    for m in messages:
        freq = ProportionOccurence(CountOccurence(m[0]))
        n = moyenne_carre_ecart(freq,frequence_apparition_france)
        if n < min:
            min = n
            message = m
    return message

def FindBestKey(message,keys):
    messages = [ (vignere(message,key,False),key) for key in keys]
    min = 1
    for m in messages:
        freq = ProportionOccurence(CountOccurence(m[0]))
        n = moyenne_carre_ecart(freq,frequence_apparition_france)
        if n < min:
            min = n
            message = m
    return message

def Decrypte(message,keylen,n=3):
    key = ""
    rep = ['\0']*len(message)
    keys = ListPossibleKey(message,keylen,n)
    for i in range(keylen):
        m,k = FindBestKey(message[i::keylen],keys[i])
        key += k
        for j in range(len(m)):
            rep[i+keylen*j] = m[j]
    return ''.join(rep),key

## Calcul taille clé


def calcul_IC(message):
    if message == '':
        print("ERROR")
    ntot = len(fixKey(message))
    n = CountOccurence(message)
    ic = 0
    for c in Alphabet:
        ic += n[c]*(n[c]-1)/ntot/(ntot-1)
    return ic

def decoupe(message,n):
    rep= []
    for i in range(n):
        rep += [message[i::n]]
    return rep

def maximise_ic(message):
    nmax = len(message)
    n = 0
    ic_france = 0.0778
    e = 1
    while e > 0.01 and n < nmax:
        n+=1
        e = abs(moyenne([calcul_IC(m) for m in decoupe(message,n)])-ic_france)
    return n

## Decrypte

def decrypte(message):
    message = fixString(message)
    keylen = maximise_ic(message)
    return Decrypte(message,keylen,5)

## Analyse statistique

def IsGoodBoi(car):
    return ord(car) >= ord('A') and ord(car) <= ord('Z')

def CreateDict():
    dict = {}
    for car in Alphabet:
        dict[car] = 0
    return dict

def CountOccurence(str):
    dict = CreateDict()
    for car in str:
        if IsGoodBoi(car):
            dict[car] += 1
    return dict

def ProportionOccurence(dict):
    dtc = dict.copy()
    n = 0
    for a in Alphabet:
        n += dict[a]
    for a in Alphabet:
        dtc[a] /= n
    return dtc

def PrintProportion(prop):
    import matplotlib.pyplot as plt
    Prop = [prop[i] for i in Alphabet]
    for i in range(26):
        plt.plot([i,i],[0,Prop[i]],'r')
    plt.xticks(range(26),Alphabet)
    plt.show()

def ProportionMessageCode(str,keylen):
    dicts = [CreateDict()]*keylen
    for i in range(keylen):
        dicts[i] = ProportionOccurence(CountOccurence(str[i::keylen]))
    return dicts

def PrintProportionKeys(str,keylen):
    import matplotlib.pyplot as plt
    dicts = ProportionMessageCode(str,keylen)
    f,axarr = plt.subplots(keylen,sharex = True)
    f.suptitle('Analyse statistique du message codé séparer par differentes clé')
    for j in range(keylen):
        for i in range(26):
            axarr[j].plot([i,i],[0,dicts[j][Alphabet[i]]],'r')
    plt.xticks(range(26),Alphabet)
    plt.show()

def CalculClef(c1,c2):
    fixString(c1)
    fixString(c2)
    return Alphabet[(Indice(c1)-Indice(c2))%26]

def maxDict(dict):
    max,car = 0,'A'
    for i in Alphabet:
        if dict[i] > max:
            max,car = dict[i],i
    return car
    
def CrackKey_bad(str,keylen):
    dicts = ProportionMessageCode(str,keylen)
    key = ""
    for j in range(keylen):
        key += CalculClef(maxDict(dicts[j]),"E")
    return key
    

frequence_apparition_france = CalcDict()[0]