if __name__ == '__main__':
    import os
    files=os.listdir()
    for file_name in files:
        tokens=file_name.split('.')
        if len(tokens)>1:
            file_type=tokens[len(tokens)-1]
        else:
            file_type=''
        argument=input(file_name + ' book name (d for discard, s for skip): ')
        if argument=='d':
            os.remove(file_name)
            print(file_name+' removed')
            continue
        elif argument=='s':
            print(file_name + ' skipped')
            continue
        else:
            author=input('author: ')
            year=input('year: ')

        new_name=argument
        if len(author) >=1:
            new_name=new_name+'_'+author
        if len(year) >=1:
            new_name=new_name+'_'+year

        if len(tokens)>1:
            os.rename(file_name, new_name+'.'+file_type)
        else:
            os.rename(file_name, new_name)
