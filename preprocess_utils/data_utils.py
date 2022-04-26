import pandas as pd

def load_data(filename, encoding = 'utf-8', sheet_name = 'sheet_name', sep = '\t'):
    
    """
    Load data into pandas dataframe.
    Data type: csv, xlsx, txt
    Parameter:
      - sheet: sheet name in xlsx file.
      - sep: columns separation index in txt file.
      - encoding: encoding type of file.
    """

    if filename.endswith('.csv'):
        data = pd.read_csv(filename, encoding = encoding)
    elif filename.endswith('.xlsx'):
        if sheet_name == 'sheet_name':
            data = pd.read_excel(filename)
        else:
            data = pd.read_excel(filename, sheet_name = sheet_name)    
    elif filename.endswith('.txt'):
        data = pd.read_csv(filename, sep = sep, engine='python', encoding = encoding)
    else:
        raise Exception("File extension must deviate from [csv, xlsx, txt].")
    
    return data
    
def datetime_convert(data, column, format = "%Y/%m/%d"):

    """
    Convert a Time-series column as datetime type.
    Parameter:
      - data: original data.
      - column: time-seires column name.
      - format: time-seires format. (default: "%Y/%m/%d")
    """

    data[column] = pd.to_datetime(data[column], format = format)
    return data

def data_split(data, column, by = 'time', time_sep = '2020-01-01', proportion = 0.7):

    """
    Convert a Time-series column as datetime type.
    Parameter:
      - data: original data.
      - column: time-seires column name.
      - by: split method. (time: 특정 시점 기준, proportion: 특정 비율 기준)
      - time_sep: 특정 시점 기준.
      - proportion: 특정 비율 기준.
    """

    if by == 'time':
        train = data.loc[data[column] <= time_sep, :].reset_index(drop = True)
        test = data.loc[data[column] > time_sep, :].reset_index(drop = True)
    elif by == 'proportion':
        index = int(len(data[column]) * proportion)
        train = data.iloc[:index, :].reset_index(drop = True)
        test = data.iloc[index:, :].reset_index(drop = True)
    else:
        raise Exception("Split method must be selected in ['time', 'proportion'].")
    
    return (train, test)

        
        


