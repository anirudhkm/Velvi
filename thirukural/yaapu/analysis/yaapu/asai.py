import numpy as np
import pandas as pd
from utils import *
from tamil.utf8 import *


class Asai(object):
    """
    Find the asai pattern of a poem in tamil.
    """

    def __init__(self, seyyul):

        self.seyyul = seyyul

    def get_asai_type(self, word_lst, asai="", i=0):
    
        if i >= len(word_lst):
            return asai
        
        if is_ottru(word_lst[i]):
            i+=1
        
        elif i+2 < len(word_lst) and is_kuril(word_lst[i]) and is_nedil(word_lst[i+1]) and is_ottru(word_lst[i+2]):
            asai += "நிரை"
            i = i+3
            
        elif i+1 < len(word_lst) and is_kuril(word_lst[i]) and is_nedil(word_lst[i+1]):
            asai += "நிரை"
            i = i+2
        
        elif i+2 < len(word_lst) and is_kuril(word_lst[i]) and is_kuril(word_lst[i+1]) and is_ottru(word_lst[i+2]):
            asai += "நிரை"
            i = i+3
            
        elif i+1 < len(word_lst) and is_kuril(word_lst[i]) and is_kuril(word_lst[i+1]):
            asai += "நிரை"
            i = i+2
        
        elif i+1 < len(word_lst) and is_kuril(word_lst[i]) and is_ottru(word_lst[i+1]):
            asai += "நேர்"
            i = i+2
            
        elif i+1 < len(word_lst) and is_nedil(word_lst[i]) and is_ottru(word_lst[i+1]):
            asai += "நேர்"
            i = i+2
            
        elif i < len(word_lst) and (is_nedil(word_lst[i]) or is_kuril(word_lst[i])):
            asai += "நேர்"
            i = i+1
        return self.get_asai_type(word_lst, asai, i)

    def vaipaadu_map(self, )