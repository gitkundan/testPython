#TODO : split on / and then combine parent, child into flatten and then run a loop using while count } >0
import re
from time import sleep
data=r'Financials or External Disclosure /{Financial Statement/{Balance Sheet,Cash Flow Statement},Trading Profit and Loss}'
# data=r'Financials or External Disclosure /{Financial Statement/Balance Sheet,Financial Statement/Cash Flow Statement,Trading Profit and Loss}'
 
pattern_inner=r'[\w ]*\/{[\w ,]*}'
pattern_outer=r'[\w -]*\/{[^}]*}'

def parse_text_inner(pattern:str,full_text:str)->str:
    """for nested inner blocks regex match pattern on text and output a string"""

    result=re.findall(pattern,full_text) #=> Financial Statement/{Balance Sheet,Cash Flow Statement}
    result=result[0] if isinstance(result,list) and len(result)>0 else None

    if result is not None:
        text=result.split('/{') #delimiter for parent-child boundary
        parent=text[0]
        children=text[1:][0].split(',') #children will be delimited with comma

        final=[]
        for child in children:
            if child != '' :
                child=child.removesuffix('}')
                element=f'{parent}/{child}'
                final.append(element.strip())

        x=','.join(final)
        x=x.removeprefix('{')
        new_text=full_text.replace(result,x)
        return new_text
    else:
        return None

final_inner=''

while data is not None:
    print(f'data at start : {data}')
    #nested parsing for inner block
    data=parse_text_inner(pattern=pattern_inner,full_text=data)
    final_inner=data if data is not None else final_inner #catch the value of data at the last correct match
    print(f'data at end : {data}')
    sleep (10)

print(f'inner is {final_inner}')
final_outer=parse_text_inner(pattern_outer,final_inner)
print(f'outer is {final_outer}')
