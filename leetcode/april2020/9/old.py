import math
from typing import List

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        #  import pdb; pdb.set_trace()
        slowS, fastS = len(S) - 1, len(S) - 1
        slowT, fastT = len(T) - 1, len(T) - 1
        # iterate over both, checking the values they would have when they get written
        both_exhausted = False
        exhaustedS = False
        exhaustedT = False
        while not both_exhausted:
            #  import pdb; pdb.set_trace()
            print(S, slowS, fastS)
            print(T, slowT, fastT)
            to_compareS = None
            to_compareT = None

            # slow stops at # and fast finds what to delete

            if slowS == fastS and S[slowS] != "#":
                # We're at a comparison point
                to_compareS = S[slowS]
            else:
                # Get S to a comparison point
                while S[slowS] == "#" or S[fastS] == "#":
                    while S[fastS] == "#":
                        fastS -= 1
                        if fastS < 0:
                            exhaustedS = True
                            break
                    slowS -= 1
                    fastS -= 1
                    if fastS < 0:
                        exhaustedS = True
                        break
                # Advance slow until it gets to a "#"
                while S[slowS] != "#" and slowS > fastS:
                    slowS -= 1
                #slowS = fastS
                
            if slowT == fastT and T[slowT] != "#":
                # We're at a comparison point
                to_compareT = T[slowT]
            else:
                # Get T to a comparison point
                while T[slowT] == "#" or T[fastT] == "#":
                    while T[fastT] == "#":
                        fastT -= 1
                        if fastT < 0:
                            exhaustedT = True
                            break
                    slowT -= 1
                    fastT -= 1
                    if fastT < 0:
                        exhaustedT = True
                        break
                # Advance slow until it gets to a "#"
                while T[slowT] != "#" and slowT > fastT:
                    slowT -= 1
                #slowT = fastT

            if to_compareS is not None and to_compareT is not None:
                import pdb; pdb.set_trace()
                print("COMPARING", to_compareS, to_compareT)
                if to_compareS != to_compareT:
                    return False
                slowS -= 1
                fastS -= 1
                slowT -= 1
                fastT -= 1
                exhaustedS = fastS < 0
                exhaustedT = fastT < 0

            both_exhausted = exhaustedS and exhaustedT
            if both_exhausted:
                return True
            #  if exhaustedS ^ exhaustedT:
            #      return False
                
        return True

    def __call__(self, str1, str2):
        return self.backspaceCompare(str1, str2)
