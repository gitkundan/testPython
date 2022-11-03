'''
text="""
concept '{Account/{Financial Account, Transaction Account},Rate,Request/{Sales, Order}}'
"""
text=text.strip()
import re
# s = "Account\Trade"
pattern_1="^concept '([\w\W]+)'" #match all word and non-word multiple times
pattern_2="[^\/{},]+" #match all word and non-word multiple times


for record in re.findall(pattern_1, text):
    x=re.findall(pattern_2,record)
    print(x)
