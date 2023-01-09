import numpy as np
import pandas as pd
from utils import *
from tamil.utf8 import *


class Seer(object):
    """
    Find the asai pattern of a poem in tamil.
    """

    def __init__(self, seyyul):

        self.seyyul = seyyul

    def get_seer_type(self, word_lst, seer="", i=0):
    
        if i >= len(word_lst):
            return seer
        
        if is_ottru(word_lst[i]):
            i+=1
        
        elif i+2 < len(word_lst) and is_kuril(word_lst[i]) and is_nedil(word_lst[i+1]) and is_ottru(word_lst[i+2]):
            seer += "நிரை"
            i = i+3
            
        elif i+1 < len(word_lst) and is_kuril(word_lst[i]) and is_nedil(word_lst[i+1]):
            seer += "நிரை"
            i = i+2
        
        elif i+2 < len(word_lst) and is_kuril(word_lst[i]) and is_kuril(word_lst[i+1]) and is_ottru(word_lst[i+2]):
            seer += "நிரை"
            i = i+3
            
        elif i+1 < len(word_lst) and is_kuril(word_lst[i]) and is_kuril(word_lst[i+1]):
            seer += "நிரை"
            i = i+2
        
        elif i+1 < len(word_lst) and is_kuril(word_lst[i]) and is_ottru(word_lst[i+1]):
            seer += "நேர்"
            i = i+2
            
        elif i+1 < len(word_lst) and is_nedil(word_lst[i]) and is_ottru(word_lst[i+1]):
            seer += "நேர்"
            i = i+2
            
        elif i < len(word_lst) and (is_nedil(word_lst[i]) or is_kuril(word_lst[i])):
            seer += "நேர்"
            i = i+1
        return self.get_seer_type(word_lst, seer, i)

    def vaaipaadu_map(self, seer_lst):
    
        seer_vaaipaadu = [[] for _ in range(len(seer_lst))]
        for i in range(len(seer_lst)):
            for j in range(len(seer_lst[i])):
                if seer_lst[i][j] == "நேர்":
                    seer = "நேர்"
                elif seer_lst[i][j] == "நிரை":
                    seer = "நிரை"
                elif seer_lst[i][j] == "நேர்நேர்":
                    seer = "தேமா"
                elif seer_lst[i][j] == "நிரைநேர்":
                    seer = "புளிமா"
                elif seer_lst[i][j] == "நேர்நிரை":
                    seer = "கூவிளம்"
                elif seer_lst[i][j] == "நிரைநிரை":
                    seer = "கருவிளம்"
                elif seer_lst[i][j] == "நேர்நேர்நேர்":
                    seer = "தேமாங்காய்"
                elif seer_lst[i][j] == "நிரைநேர்நேர்":
                    seer = "புளிமாங்காய்"
                elif seer_lst[i][j] == "நேர்நிரைநேர்":
                    seer = "கூவிளங்காய்"
                elif seer_lst[i][j] == "நிரைநிரைநேர்":
                    seer = "கருவிளங்காய்"
                elif seer_lst[i][j] == "நேர்நேர்நிரை":
                    seer = "தேமாங்கனி"
                elif seer_lst[i][j] == "நிரைநேர்நிரை":
                    seer = "புளிமாங்கனி"
                elif seer_lst[i][j] == "நேர்நிரைநிரை":
                    seer = "கூவிளங்கனி"
                elif seer_lst[i][j] == "நிரைநிரைநிரை":
                    seer = "கருவிளங்கனி"
                else:
                    seer = "error"
                seer_vaaipaadu[i].insert(j, seer)
        return seer_vaaipaadu

    def get_seer_pattern(self):
        """
        Get Seer pattern for a given seyyul.
        """

        seyyul_lst = split_seyyul(self.seyyul)
        seer_lst = [[] for _ in range(len(seyyul_lst))]
        for i in range(len(seyyul_lst)):
            for j in range(len(seyyul_lst[i])):
                word_lst = get_letters(seyyul_lst[i][j])
                seer = self.get_seer_type(word_lst)
                seer_lst[i].insert(j, seer)
        seer_vaaipaadu = self.vaaipaadu_map(seer_lst)
        return seer_lst, seer_vaaipaadu