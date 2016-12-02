import os

if __name__ == '__main__':
    files=os.listdir()
    for file_name in files:
        tokens=file_name.split('.')
        if len(tokens)>1:
            file_type=tokens[len(tokens)-1]
        else:
            file_type=''
        new_name= input('old: '+file_name[0:len(file_name)-(len(file_type)+1)]+' type: '+file_type +' new: ')
        if len(new_name) >= 1:
            if len(tokens)>1:
                os.rename(file_name, new_name+'.'+file_type)
            else:
                os.rename(file_name, new_name)
