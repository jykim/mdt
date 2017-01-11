from mdt.mdt_init import *
import mdt.mdt_parse as mp
    
def create_key(tbl):
    #pdb.set_trace()
    res = Series([""] * len(tbl), index=range(len(tbl)))
    for col in tbl.columns:
        res += (tbl[col].fillna("")+"/")
    return res

def diff_tbls(tbl1, tbl2):
    try:
        tbl1['key'] = create_key(tbl1[["T1","T2","T3","TXT"]])
        tbl2['key'] = create_key(tbl2[["T1","T2","T3","TXT"]])
        tbl_del = tbl1[~tbl1.key.isin(tbl2.key)]; tbl_del.insert(0,'Type', "DEL")
        tbl_add = tbl2[~tbl2.key.isin(tbl1.key)]; tbl_add.insert(0,'Type', "ADD")
        dtm = pd.concat([tbl_del, tbl_add], axis=0)
        del dtm['key'], tbl1['key'], tbl2['key']
        dtm.insert(0, 'Time', strftime("%Y-%m-%d %H:%M:%S", localtime()))
    except Exception:
        dtm = DataFrame()
    return dtm

def diff_md_files(file1, file2):
    return diff_tbls(mp.parse_md_file(file1), mp.parse_md_file(file2))

# Process infile (file pattern)
# Output latest file into outfile
# Keep changelog in logfile
def track_md_file(infile, outfile, logfile):
    dta2 = mp.parse_md_files(infile)
    if not os.path.exists(outfile):
        dta2.to_csv(outfile, sep="\t", index=False)
        return 0
    lf = open(logfile, "a")
    if os.path.getsize(logfile) == 0:
        lf.write("\t".join(["Time", "Type", "ID", "T1", "T2", "T3", "TXT"])+"\n")
    dta1 = pd.read_csv(outfile, sep="\t")
    dtm = diff_tbls(dta1, dta2)
    if len(dtm) > 0:
        dta2.to_csv(outfile, sep="\t", index=False)
        dtm.to_csv(lf, sep="\t", header=False, index=False)
        print(dtm)
        lf.flush()
        return 1
    else:
        return 0
