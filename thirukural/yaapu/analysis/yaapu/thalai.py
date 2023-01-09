import numpy as np
import pandas as pd
from utils import *
from tamil.utf8 import *


class Thalai(object):
    """
    Thalai pattern.
    """

    def __init__(self, seer_lst, seer_vaaipaadu):
        self.seer_lst = seer_lst
        self.seer_vaaipaadu = seer_vaaipaadu

    def get_thalai_pattern(self):
        """
        """

        thalai_lst = []
        for i in range(len(self.seer_lst)-1):
            if self.seer_vaaipaadu[i].endswith("மா") and self.seer_lst[i+1].startswith("நேர்"):
                thalai = "நேரொன்றிய ஆசிரியத்தளை"
            elif self.seer_vaaipaadu[i].endswith("விளம்") and self.seer_lst[i+1].startswith("நிரை"):
                thalai = "நிரையொன்றிய ஆசிரியத்தளை"
            elif (self.seer_vaaipaadu[i].endswith("மா") and self.seer_lst[i+1].startswith("நிரை")) or (self.seer_vaaipaadu[i].endswith("விளம்") and self.seer_lst[i+1].startswith("நேர்")):
                thalai = "இயற்சீர் வெண்டளை"
            elif self.seer_vaaipaadu[i].endswith("காய்") and self.seer_lst[i+1].startswith("நேர்"):
                thalai = "வெண்சீர் வெண்டளை"
            elif self.seer_vaaipaadu[i].endswith("காய்") and self.seer_lst[i+1].startswith("நிரை"):
                thalai = "கலித்தளை"
            elif self.seer_vaaipaadu[i].endswith("கனி") and self.seer_lst[i+1].startswith("நிரை"):
                thalai = "ஒன்றிய வஞ்சித்தளை"
            elif self.seer_vaaipaadu[i].endswith("கனி") and self.seer_lst[i+1].startswith("நேர்"):
                thalai = "ஒன்றாத வஞ்சித்தளை"
            else:
                thalai = "error"
            thalai_lst.append(thalai)
        thalai_lst.append("-")
        return thalai_lst