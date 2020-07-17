import chatterREF

def nume(text):
    discutie = 'Îmi pare bine, ' + text + '. Despre ce dorești să discuți cu mine?'
    return discutie

def convorbireIT(userText):
    if userText.lower() == "da":
        raspuns = "Păi, let's begin! Inroduceți un cuvant cheie în limba engleză. Pentru a termina discuția în limba engleză, tastează exit"
    elif userText.lower() == "nu":
        raspuns = "Înteleg, însa chiar aș dori să mai exersez limba engleză. Știai că în fiecare țară (nu pitică) din lume există măcar un vorbitor? Deci, ce zici? Dacă mă respingi și acum, va trebui să încheiem conversația."
    else:
        raspuns = "Scuze, nu înțeleg! Credeam că am fost destul de clar când ți-am dat opțiunile cu DA sau NU. Mai încearcă odată. Dacă nici acum nu accepți, va trebui să încheiem conversația."
    return raspuns

def convorbireREF(userText):
    if userText.lower() == "da":
        raspuns = "Să începem atunci! Inroduceți un cuvânt cheie în limba engleză (deoarece textul este în limba engleză). Pentru a termina căutarea de referințe după cuvântul introdus, tastează Q"
    elif userText.lower() == "nu":
        raspuns = "Înteleg, însa chiar aș dori să detectez referințe. Deci, ce zici? Dacă mă respingi și acum, va trebui să încheiem conversația."
    else:
        raspuns = "Scuze, nu înțeleg! Credeam că am fost destul de clar când ți-am dat opțiunile cu DA sau NU. Mai încearcă odată. Dacă nici acum nu accepți, va trebui să încheiem conversația."
    return raspuns

def referinte(userText):
    return chatterREF.response(userText)
