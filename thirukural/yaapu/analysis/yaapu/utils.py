from tamil.utf8 import nedil_letters, uyir_mei_nedil, kuril_letters, uyir_mei_kuril, mei_letters, aytham_letter


def split_seyyul(val, sep="|"):
    
    val = val.replace(".", "").split(sep)
    for i in range(len(val)):
        val[i] = val[i].strip().split(" ")
    return val

def is_nedil(char):

    ai = ['கை', 'சை', 'டை', 'தை', 'பை', 'றை', 'ஞை', 'ஙை', 'ணை', 'நை',
        'மை', 'னை', 'யை', 'ரை', 'லை', 'வை', 'ழை', 'ளை']
    if char in nedil_letters or char in uyir_mei_nedil or char in ai:
        return True
    return False

def is_kuril(char):
    
    if char in kuril_letters or char in uyir_mei_kuril:
        return True
    return False

def is_ottru(char):
    
    if char in mei_letters or char in aytham_letter:
        return True
    return False
