from mdt.mdt_init import *

def round_by_minutes(arg, minutes = 1):
    ns5min=minutes*60*1000000000   # 5 minutes in nanoseconds 
    return pd.DatetimeIndex(((arg.astype(np.int64) // ns5min + 1 ) * ns5min))

def flattenCols(col,sep = '_'):
    if not type(col) is tuple:
        return col
    else:
        new_col = ''
        for leveli,level in enumerate(col):
            if not level == '':
                if not leveli == 0:
                    new_col += sep
                new_col += level
        return new_col
