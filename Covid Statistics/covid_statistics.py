import pandas as pd
import datetime


def get_date_format(dates):
    DATE_FORMATS = ["%Y-%m-%d", "%d.%m.%Y", "%d.%m.%y", "%d-%m-%Y", "%d/%m/%Y", "%m/%d/%Y"]
    for date_format in DATE_FORMATS:
        reject_format = False
        for date in dates:
            try:
                datetime.datetime.strptime(date, date_format)
            except ValueError:
                reject_format = True
                break
        if not reject_format:
            return date_format
    raise Exception('An error occurred: no valid date format found.')

def main():
    
    list_names = [0,0,0]
    names = [0,0,0]
    new_names = [0,0,0]
    i = 1
    while i < 4:
        filename = input("Enter the name of file #{}:\n".format(i))
        try:
            if filename in names:
                print('File {} is already included in this analysis. Please choose a different file.'.format(filename))
            else:
                names[i-1] = filename
                list_names[i-1] = pd.read_csv(filename, sep="\t", dtype=str)
                new_names[i-1] = 'cases_' + names[i-1].split('.')[0]
                list_names[i-1][new_names[i-1]] =  list_names[i-1]['cases']
                i = i + 1
            
        except OSError:
            print("Error in reading file {:s}. Closing program.".format(filename))
            break
        
    

    if i == 4:              
        for char in ['.', ',', ' ']:
            for i in range(3):
                list_names[i][new_names[i]]  =  list_names[i][new_names[i]].str.replace(char, "")
        
        for i in range(3):
            list_names[i][new_names[i]] = pd.to_numeric(list_names[i][new_names[i]], errors='coerce')
            date_format = get_date_format( list_names[i]['date'])
            list_names[i]['date'] = pd.to_datetime( list_names[i]["date"], format=date_format) 
            list_names[i]['date'] =  list_names[i]['date'].dt.date
            list_names[i] = list_names[i].drop(['cases'], axis=1)
            
            
        merged_dataframe = pd.merge(list_names[0], list_names[1], how='outer', on='date')
        described = pd.merge(merged_dataframe, list_names[2], how='outer', on='date')
        print('Printing summary statistics:')
        print(described.describe())
        
        merged_dataframe_new = pd.merge(list_names[0], list_names[1], how='outer', on='date')
        first_five = pd.merge(merged_dataframe_new, list_names[2], how='outer', on='date')
        print('Printing first five rows:')
        print(first_five.head())
    
        
main()
