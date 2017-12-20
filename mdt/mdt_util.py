import io
import dropbox
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


def import_from_dropbox(auth_token, tmp_path = "tmp/"):
    dbx = dropbox.Dropbox(auth_token)
    if not os.path.exists(tmp_path):
        os.mkdir(tmp_path)   
    for entry in dbx.files_list_folder('').entries:
        #print(entry.name)
        md, res = dbx.files_download('/'+entry.name)
        with io.open(os.path.join(tmp_path, md.name), "w", encoding='utf-8') as of:
            of.write(res.content.decode('utf-8'))
