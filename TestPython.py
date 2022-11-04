from functools import reduce
import operator
import numpy as np

text='Boris' #case 1
text='{Boris,Rishi}' #case 2
text='{UK/{Boris,Rishi},US/{Biden,Trump}}' #case 3
# text='{UK/{Boris,Rishi}}' #case 3


text=text.strip("'").removesuffix('}').removeprefix('{')
if text.find('/') >0 :
    #identifier for case 3
    text=text.split('}') #=> ('UK', '/{', 'Boris,Rishi')
    for i in text:
        #start of each parent block with associated childs
        if len(i)>0:
            value=i.partition('/{')
            concept_parent=value[0]
            concept_childs=value[2].split(',') #=> list : ['Boris', 'Rishi']
            # out = reduce(operator.concat, concept_childs)
            # out=list(np.array(concept_childs).flat)
            result=[f'{concept_parent}/{i}' for i in concept_childs]
            print(result)
            # print(concept_childs)
            # print(concept_parent)
            # concept_childs #=> ['Boris,Rishi']
            # print(concept_childs) #=> ['Boris,Rishi']
            # for i in concept_childs:
            #     x=f'{concept_parent}/{i}'
            #     print(i)



