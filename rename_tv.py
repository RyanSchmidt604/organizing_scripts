if __name__ == '__main__':
    import os
    files=os.listdir()
    show_name=input('show name: ')
    season=input('season: ')
    quality=input('quality (n for none): ')
    for file_name in files:
        tokens=file_name.split('.')
        if len(tokens)>1:
            file_type=tokens[len(tokens)-1]
        else:
            file_type=''
        argument=input(file_name + ' episode number (d for discard, s for skip): ')
        if argument=='d':
            os.remove(file_name)
            print(file_name+' removed')
            continue
        elif argument=='s':
            print(file_name + ' skipped')
            continue
        else:
            if quality =='n':
                new_name='{}_s{:0>2}e{:0>2}'.format(show_name, season, argument)
            else:
                new_name='{}_s{:0>2}e{:0>2}_{}'.format(show_name, season, argument, quality)

        if len(tokens)>1:
            os.rename(file_name, new_name+'.'+file_type)
        else:
            os.rename(file_name, new_name)
            print('file named: '+new_name)
