import argparse
data=[{
    'file_path':'./data/dev.txt',
    'dev_text':'xxx',
    'prod_text':'yyy'},
     {
    'file_path':'./data/hardev.txt',
    'dev_text':'xxx',
    'prod_text':'yyy'}, 
    
]

def change_to_prod():
    for d in data:
        with open(d['file_path'],'r+') as f:
            source=f.readlines()
            f.seek(0) # Move file pointer to the beginning
            target=[s.replace(d['dev_text'],d['prod_text']) for s in source]
            f.writelines(target)
        

def change_to_dev():
    for d in data:
        with open(d['file_path'],'r+') as f:
            source=f.readlines()
            f.seek(0) # Move file pointer to the beginning
            target=[s.replace(d['prod_text'],d['dev_text']) for s in source]
            f.writelines(target)
            
def main():
    parser = argparse.ArgumentParser(description='Change text in files.')
    parser.add_argument('mode', choices=['prod', 'dev'], help='Choose between prod and dev modes.')

    args = parser.parse_args()

    if args.mode == 'prod':
        change_to_prod()
    elif args.mode == 'dev':
        change_to_dev()

if __name__ == '__main__':
    main()
