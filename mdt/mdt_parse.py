"""
# Parse Markdown into TSV #
@author: jink
"""
from mdt.mdt_init import *
import dropbox
P_T1 = r"^# (.*)"
P_T2 = r"^## (.*)"
P_T3 = r"^### (.*)"
P_BLANK = r"^\s*$"
C_TITLE = "#"
VERSION = "0.1.2t"

def import_from_dropbox(auth_token, tmp_path = "tmp/"):
    dbx = dropbox.Dropbox(auth_token)
    if not os.path.exists(tmp_path):
        os.mkdir(tmp_path)   
    for entry in dbx.files_list_folder('').entries:
        #print(entry.name)
        md, res = dbx.files_download('/'+entry.name)
        of = open(os.path.join(tmp_path, md.name), "w")
        of.write(res.content.decode())

def parse_md_files(fileptn):
    mds = glob.glob(fileptn)
    mds.sort()
    return pd.concat([parse_md_file(fn) for fn in mds], axis=0)

def parse_md_file(filename):
    tbl = parse_md_text(read_md_file(filename))
    tbl.insert(0,'Filename', basename(filename).split(".")[0])
    return tbl

def read_md_file(filename):
    fc = open(filename,"rU").read()
    fn = re.sub(re.compile(r"\<\!--.*?--\>", re.DOTALL), "", fc)
    return fn

def parse_md_text(text):
    #import pdb; pdb.set_trace()
    lines = text.split("\n")
    #print(lines)
    res = DataFrame()
    t1 = t2 = t3 = None
    i1 = i2 = i3 = 0
    for l in lines:
        if re.search(P_T1, l):
            t1 = parse_title(l); i1+=1; i2=0; i3=0; t2 = None; t3 = None
        elif re.search(P_T2, l):
            t2 = parse_title(l); i2+=1; i3=0; t3 = None
        elif re.search(P_T3, l):
            t3 = parse_title(l); i3+=1
        elif re.search(P_BLANK, l):
            next
        else:
            lid = "%d.%d.%d" % (i1, i2, i3)
            sl = parse_line(lid, t1, t2, t3, l)
            res = pd.concat([res,sl], axis=0)
    res.index = range(len(res))
    return res

def parse_title(l):
    return l.replace(C_TITLE,"").strip()

def parse_line(lid, t1, t2, t3, l):
    #("Time",TIME_NOW),
    return DataFrame.from_items([("ID",[lid]), ("T1",[t1]), ("T2",[t2]), ("T3",[t3]) ,("TXT",[l.strip()])])
