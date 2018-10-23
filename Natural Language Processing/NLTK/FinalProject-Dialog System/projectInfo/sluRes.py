# sluRes.py
# Last Modified: April 12, 2018
# Author: Ronnie Smith
# Note: Modification of source code originally developed by former ECU
#       undergraduate and graduate student Ryan Dellana
# sluResult(turn,labelturn) compares the SLU hypothesis of highest probability
#      to "ground truth" and returns one of the following:
#      "U" : fully understood
#      "P" : partially understood
#      "N" : not understood
# turn - value for call["turns"] for a specific dialog turn from log.json
# labelturn - value for label["turns" for a specific dialog turn from label.json
#
# Usage: place source code in same directory as application code
# Add following two lines to application code
#  import sluRes
#  from sluRes import sluResult
#
import os
import json

def sluResult(turn,labelturn):
     dact = turn['output']['dialog-acts']
     slulist = turn['input']['live']['slu-hyps']
     first_sys_act = dact[0]
     match = False
     partial_match = False
     if first_sys_act is not None:   # check SLU
         sys_act = first_sys_act
         hyp = slulist[0]            # top hypothesis
         match = False
         partial_match = False

# NOTE:  using sorted in python version 2 yields more matches and less
#        partial matches --- needs further investigation
#        sorted for this data structure unavailable in python version 3

         #if sorted(hyp['slu-hyp']) == sorted(labelturn['semantics']['json']): 
         if (hyp['slu-hyp']) == (labelturn['semantics']['json']): 
             match = True
         else: # check for partial match.
             for lbl_part in labelturn['semantics']['json']:
                 for hyp_part in hyp['slu-hyp']:
                     if hyp_part == lbl_part:
                         partial_match = True

     if match == True:
          return "U"
     elif partial_match == True:
          return "P"
     else:
          return "N"
