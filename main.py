import random


def demograhics():
    g = random.randint(0, 2)
    if g == 1:
        return 'Male'
    else:
        return "Female"


gen = demograhics()



age = random.randint(18,90)

Tcc = ['fall', 'assault', 'stabbed', 'burned', 'object fell on head', 'gun shot wound']
Mcc = ['seizure', 'suicidal ideation',
       'Bleeding', 'pregnancy', 'Diabetic issues', 'generalized weakness', 'cold and flu like symptoms', 'fainting',
       'stroke']
PainMcc = ['Chest pain', 'Headache', 'Abdominal pain', 'Leg pain']
Respiratory = ['shortness of breath', 'difficulty in breathing', 'asthma attack']


def cc():
    global x
    global d
    x = random.randint(0,4)



    if x <4:
        x = 'Medical'
        rand = random.randint(0, 2)
        if rand == 1:
            p = random.randint(0, 8)
            d = Mcc[p]
            print(f'This will be a {d} call')
            return Mcc[p]
        elif rand == 2:
            p = random.randint(0, 8)
            d = Respiratory[p]
            print(f'This will be a {d} call')
            return Respiratory[p]
        else:
            p = random.randint(0, 3)
            d = PainMcc[p]
            print(f'This will be a {d} call')
            return PainMcc[p]
    else:
        x = 'Trauma'
        p = random.randint(0, 5)
        d = Tcc[p]
        print(f'This will be a {d} call')
        return f'with {d}'


cc = cc()


def O():
    w = random.randint(0, 1)
    if w == 1:
        return 'described as a gradual onset'
    else:
        return 'described as a sudden onset'


provv = 'standing walking jumping breathing stretching palpating'
prov = provv.split()


def P():
    q = random.randint(0, 5)
    w = random.randint(0, 8)
    if q > 1:
        return 'is unprovokable'
    else:
        return 'and ' + prov[q] + ' worsens it.'


Qual = 'stabbing pressure dull aching burning tightness'
qual = Qual.split()


def Q():
    q = random.randint(0, 5)
    return 'They describe it as ' + qual[q]


radi = 'back left-arm right-arm neck'
Radi = radi.split()


def R():
    RadChance = random.randint(0, 10)
    if RadChance > 3:
        return 'that does not radiate'
    else:
        RadChoice = random.randint(0, 3)
        return 'that radiates to the ' + Radi[RadChance]


def S():
    return 'that is a ' + str(random.randint(0, 10)) + '/10 pain.'


Time = 'hours days'
time = Time.split()


def T():
    TimeInc = random.randint(0, 1)
    TimeValue = str(random.randint(1, 5))
    return 'for ' + TimeValue + ' ' + time[TimeInc]


def pain():
    global O, P, Q, R, S, T

    O = O()
    P = P()
    Q = Q()
    R = R()
    S = S()
    T = T()


pain()

Allers = 'Sulfa aspirin codeine contrast penicillin haldol amoxicillin tylenol ibuprofen omeprazole'

# contains list of allergies
All = Allers.split()


def Allergies():
    AllergyPoss = random.randint(0, 2)
    # creates list of allergies selected at random starting as blank
    AllChoice = []
    # decides whether or not patient has allergies
    if AllergyPoss == 1:
        # patient has allergies
        # how many allergies will they have
        Allchoiceamount = random.randint(1, 10)
        # for each instance up to the amount of allergies randomly generated
        for char in range(0, Allchoiceamount):
            # which allergy is selected
            o = random.randint(0, 9)
            # empty list is appended with instances from 'All' allergy master list
            AllChoice.append(All[o])
        # remove duplicates by creating new list to store non duplicates
        AllChoiceFinal = list(set(AllChoice))
        AllChoiceFinal = ', '.join(AllChoiceFinal)

        return 'Patient has allergies to ' + AllChoiceFinal

    else:
        return 'Patient has NKDA'


Allergy = Allergies()

Histories = 'CHF Diabetes HTN Hyperlipidemia CAD Renal-Disease migraines depression atrial-fibrillation schiophrenia'

HistMeds = {'Diabetes':['Metformin','Insulin','Glipizide'],
            'CHF':[],
            'HTN':['Lasix','Atenolol','HCTZ','Metoprolol','Spirinolactone'],
            'Hyperlipidemia':['Atorvastatin','Crestor'],
            'CAD':[''],
            'Renal-Disease':[''],
            'migraines':['Tylenol','Motrin'],
            'depression':['Wellbutrin','Lexapro',''],
            'atrial-fibrillation':[]}
# contains list of histories
History = Histories.split()


def MedHx():
    HistoryPoss = random.randint(0, 2)

    # creates list of Historis selected at random starting as blank
    HxChoice = []
    # decides whether or not patient has allergies
    if HistoryPoss == 1:
        # patient has History
        # how many Histories will they have
        HxChoiceamount = random.randint(1, 9)
        # for each instance up to the amount of allergies randomly generated
        for char in range(0, HxChoiceamount):
            # which history is selected
            o = random.randint(0, 8)
            # empty list is appended with instances from 'History' History master list
            HxChoice.append(History[o])
        # remove duplicates by creating new list to store non duplicates
        HxChoiceFinal = list(set(HxChoice))
        HxChoiceFinal = ', '.join(HxChoiceFinal)

        return 'Patient has a history of ' + HxChoiceFinal

    else:
        return 'Patient insists they have no medical history,'


Hx = MedHx()

Medis = 'lisinopril amlodipine zoloft atorvastatin eliquis wellbutrin HCTZ lasix tramadol metformin aspirin albuterol'

# contains list of histories
Medicines = Medis.split()


def Med():
    MedsPoss = random.randint(0, 2)

    # creates list of meds selected at random starting as blank
    MedChoice = []
    # decides whether or not patient has meds
    if MedsPoss == 1:
        # patient has meds
        # how many meds will they have
        MedChoiceamount = random.randint(1, 12)
        # for each instance up to the amount of meds randomly generated
        for char in range(0, MedChoiceamount):
            # which med is selected
            o = random.randint(0, 11)

            # empty list is appended with instances from 'meds' master list
            MedChoice.append(Medicines[o])
        # remove duplicates by creating new list to store non duplicates
        MedChoiceFinal = list(set(MedChoice))
        MedChoiceFinal = ', '.join(MedChoiceFinal)

        return 'Patient takes ' + MedChoiceFinal

    else:
        return 'Patient takes no medicines'


Meds = Med()

PossEvents = ['walking', 'standing', 'sitting', 'sleeping', 'relaxing']


def Event():
    e = random.randint(0, 4)
    return 'that started while ' + PossEvents[e]


Events = Event()




def pertneg():
    o = input(
        'Can you name some pertinent negaitves, or symptoms that the patient does not have that can rule out other related illnesses?').capitalize()
    while o not in ('Yes', 'No', 'Y', "N"):
        print("please choose yes or no.")

        o = input('Can you name some pertinent negaitves?').capitalize()
    else:
        if o == "No" or o == 'N':
            return ''
        # Yes to pert negs
        else:
            if cc in Tcc:
                return 'Patient has no deformity, instability, uncontrolled bleeding, LOC, DIB, Chest pain.'
            elif cc in PainMcc:
                return 'Patient denies LOC, DIB, Chest pain, Nausea vomiting diarrhea, weakness/fatigue.'
            elif cc in Mcc:
                return 'Patient denies SI/HI, weakness, pain, DIB, dizziness, lOC.'
            else:
                return 'Patient denies LOC, Chest pain, Nausea vomiting diarrhea, weakness/fatigue, dizziness.'



pertneg = pertneg()


def Misc():
    print('Do you have any miscellaneous details to add in to the subjective findings?')
    m = input().capitalize()
    while m not in ('Yes', 'No', 'Y', 'N'):
        print('Yes or No (Y or N)')
        m = input('Do you have any miscellaneous details to add in for the subjective report?').capitalize()
    else:
        if m in ('Y', "Yes"):
            m = input(
                "Type in complete sentences what else you would like to add about the patient's subjective findings.")
            return m
        else:
            return ""


Misc = Misc()


def Misc2():
    print('Do you have any miscellaneous details to add in to the objective findings?')
    m = input().capitalize()
    while m not in ('Yes', 'No', 'Y', 'N'):
        print('Yes or No (Y or N)')
        m = input('Do you have any miscellaneous details to add in for the objective report?').capitalize()
    else:
        if m in ('Y', "Yes"):
            m = input(
                "Type in complete sentences what else you would like to add about the patient's objective findings.")
            return m
        else:
            return ""


Misc2 = Misc2()


def LOC():
    o = random.randint(0,10)


    if o <7:
        return "Conscious, Alert, Breathing"
    elif o == 8:
        return "Alert only to verbal commands"
    elif o == 9:
        return "responsive to pain"
    else:
        return 'Unresponsive'


LOC = LOC()


def GCS():
    while LOC == str('Unresponsive') or LOC == str('Conscious, Alert, Breathing'):
        if LOC == str('Unresponsive'):
            return 3
        else:
            return 15
    else:
        print('''What is the patients eye GCS?
        4 - Eyes open spontaneously
        3 - Eyes react to verbal commands
        2 - Eyes react to painful stimuli
        1 - Eyes do not react to painful stimuli''')
        e = int(input())
        while e not in (1, 2, 3, 4) or type(e) != int:
            print("please choose one of the answers.")

            e = int(input())
        else:
            pass

        print('''What is the patients verbal GCS?
        5 - Answers questions appropriately
        4 - Answers questions with inaccurate or confused answers
        3 - Answers confused with words, not sentences
        2 - Responds with grunts or incomplete words
        1 - Does not responds verbally''')
        v = int(input())
        while e not in (1, 2, 3, 4, 5) or type(e) != int:
            print("please choose one of the answers.")

            e = int(input())
        else:
            pass

        print('''What is the patients Motor GCS?
        6 - Follows commands appropriately
        5 - Purposeful movement from painful stimuli
        4 - Simply withdraws from pain
        3 - Decorticate Posturing
        2 - Decerebrate Posturing
        1 - No response to pain''')
        m = int(input())
        while m not in (1, 2, 3, 4, 5, 6) or type(e) != int:
            print("please choose one of the answers.")

            m = int(input())
        else:
            pass
        return str(e + v + m) + ' (E' + str(e) + 'V' + str(v) + 'M' + str(m) + ')'


GCS = GCS()


def presentation():
    print('How did the patient?')
    C = {'1': 'flushed', '2': 'pink', '3': 'ashen/pale'}
    T1 = {'1': 'warm', '2': 'hot', '3': 'cool'}
    M = {'1': 'dry', '2': 'moist', '3': 'diaphoretic'}
    c = input('Skin color? 1 - flushed, 2 - pink, 3 - pale/ashen')
    t = input('Skin Temp? 1 - warm, 2 - hot, 3 - cool')
    m = input('Skin moisture? 1 - dry, 2 - moist, 3 - diaphoretic')
    while c not in ('1', '2', '3') and t not in ('1', '2', '3') and m not in ('1', '2', '3'):
        print('Please choose one of the options given')
        c = input('Skin color? 1 - flushed, 2 - pink, 3 - pale/ashen')
        t = input('Skin Temp? 1 - warm, 2 - hot, 3 - cool')
        m = input('Skin moisture? 1 - dry, 2 - moist, 3 - diaphoretic')
    else:
        return C[c] + ', ' + T1[t] + ', ' + M[m] + ' skin'


# press = presentation()
pres = 'warm, pink, and dry'


def amb():
    o = random.randint(0,5)
    if o != 5:
        return 'Patient was found to be ambulatory'
    else:
        return ''


amb = amb()


def How():
    if x in ('M', "Medical"):
        pass
    else:

        o = input('How did the patient become injured?  ')
        return o


How = How()


def vitals():
    o = 'Y'
    while o not in ('Yes', 'No', 'N', 'Y'):
        print("please choose one of the answers.")

        o = input('Do you have vitals to enter?').capitalize()
    else:
        if o in ('No', 'N'):
            return ''
        else:
            Time = int(str(random.randint(0, 2)) + str(random.randint(0, 9)) + str(random.randint(0, 5)) + str(random.randint(0, 9)))
            SysBP = int(random.randint(92, 170))
            DiaBP = int(random.randint(40, 90))
            MAP = round(DiaBP + ((SysBP-DiaBP)/3),1)
            Pulse = int(random.randint(60, 125))
            Resp = int(random.randint(10, 23))
            SpO2 = int(random.randint(90, 100))
            O2 = 'RA'
            Temp1 = random.uniform(94.0, 101.0)
            Temp = float(round(Temp1, 1))
            CelTemp1 = (Temp * (5 / 9)) - 32
            CelTemp = float(round(CelTemp1, 1))
            Glu = int(random.randint(50, 170))
            Time2 = Time + 10
            SysBP2 = SysBP + 8
            DiaBP2 = DiaBP + 6
            MAP2 = round((DiaBP2 + ((SysBP2-DiaBP2)/3)),1)
            Pulse2 = Pulse + 8
            Resp2 = Resp + 2

            return f'''Vitals are as follows: Time = {Time}, {SysBP}/{DiaBP} ({MAP}), {Pulse} BPM, {Resp} Respirations per minute, {SpO2} % on {O2}, glucose of {Glu}, {Temp} degrees Farenheit.
            Second set of vitals are as follows: Time = {Time2}, {SysBP2}/{DiaBP2} ({MAP2}), {Pulse2} BPM, {Resp2} Respirations per minute, {SpO2} % on {O2}.'''


vitals = vitals()


def vitals2():
    o = 'Y'
    while o not in ('Yes', 'No', 'N', 'Y'):
        print("please choose one of the answers.")

        o = input('Do you have vitals to enter?').capitalize()
    else:
        if o in ('No', 'N'):
            return ''
        else:
            Time = str(random.randint(0, 23)) + str(random.randint(10, 49))
            SysBP = int(random.randint(92, 170))
            DiaBP = int(random.randint(40, 90))
            MAP = int(random.randint(60, 110))
            Pulse = int(random.randint(60, 125))
            Resp = int(random.randint(10, 23))
            SpO2 = int(random.randint(90, 100))
            O2 = 'RA'
            Glu = int(random.randint(50, 170))
            Temp1 = random.uniform(94.0, 101.0)
            Temp = float(round(Temp1, 1))
            CelTemp1 = (Temp * (5 / 9)) - 32
            CelTemp = float(round(CelTemp1, 1))
            return f'Vitals are as follows: Time = {Time}, {SysBP}/{DiaBP} ({MAP}), {Pulse} BPM, {Resp} Respirations per minute, {SpO2} % on {O2}, glucose of {Glu}, {Temp} degrees Farenheit ({CelTemp} degrees celcius).'


vitals2 = vitals2()


def refusal():
    o = input('Did the patient accept transport?').capitalize()
    while o not in ('Yes', 'No', 'N', 'Y'):
        print("please choose one of the answers.")

        o = input('Did the patient accept transport?').capitalize()
    else:
        if o in ('Y', "Yes"):
            return ""
        else:
            return 'Patient denied transport to facility.  Patient was advised that due to their condition, there is no definitive way to rule out a life threat on scene, and that transport to be evaluated by a physician is highly recommended.  Patient insisted that they do not want to be transported.  Patient was advised that their condition could worsen up to and including death and that rescue methods may not be effective due to EMS response time.  Patient acknowledged and signed refusal document.  Patient vital signs were reevaluated and patient mentation was deemed to be adequate for informed refusal of transport.  Patient was left at scene in position of comfort in no acute distress.'


refusal = refusal()


def narrative():
    if x == 'Medical' or x == 'M':

        print(f'''

        {age} year old {gen} patient presents with {cc} {T}, {O} {R} {Events}.  {Q} {S} {P}.  {Allergy}, {Meds}, and {Hx}. {pertneg} {Misc}

    Upon arrival patient was found to be {LOC} GCS of {GCS} with no outward signs of injury and {pres}, {amb}. {refusal} {Misc2} {vitals} ''')



    elif x == "Trauma" or x == "T":

        print(f'''

        {age} year old {gen} patient presents with {cc} that happened {T} ago that they describe as a {S}.  Patient has {Allergy}, {Meds}, and {Hx}. {pertneg} {Misc}

    Upon arrival patient was found to be {LOC} GCS of {GCS} with {pres}, {amb}.  {refusal} {Misc2} {vitals} ''')



narrative()

print('Treatment includes ')