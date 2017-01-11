from mdt.mdt_init import *
#P_TAG = r"\#([\w\:\,\_]+)"
#P_TAG = r"\@\w+(?:\([-\w]\))?"
P_TAG = r"\@\S+"
P_TAG2 = r"\@(\w+)\(([-\w]+)\)?"

def add_stat(tbl, stats, sign = 1):
    tbl_stat = pd.concat([tbl.apply(stat_count,axis=1), tbl.apply(stat_journal,axis=1)], axis=1)
    #pdb.set_trace()
    return pd.concat([tbl, sign * tbl_stat.reindex(columns=stats.split(","))], axis=1)

def agg_stat(tbl, verbose):
    gcols = ["T1","T2","T3"]
    return tbl.fillna(0).groupby(gcols[0:int(verbose)]).aggregate(sum)

def add_diff_stat(tbl, stats):
    tbla = tbl[tbl.Type == "ADD"] ; tbsa = add_stat(tbla.fillna(""), stats)
    tbld = tbl[tbl.Type == "DEL"] ; tbsd = add_stat(tbld.fillna(""), stats, -1)
    if len(tbsa) == 0:
        return tbsd
    elif len(tbsd) == 0:
        return tbsa
    else:
        return pd.concat([tbsa, tbsd], axis=0)

def agg_diff_stat(tbl, verbose):
    gcols = ["Time","T1","T2","T3"]
    return tbl.fillna("").groupby(gcols[0:int(verbose)+1]).aggregate(sum)

def stat_count(row):
    try:
        wc = len(str(row['TXT']).split(" "))
        return Series({"WC":wc, "CC":len(row['TXT']), "SC":1})
    except:
        print("[stat_count] ", row)
        return None

def stat_journal(row):
    try:
        text = str(row['TXT'])
        tags = parse_tags(extract_tags(text))
        #print(text, tags)
        return Series(tags)
    except e:
        print("[stat_journal] ", row, e)
        return None

def extract_tags(text):
    tags_all = re.findall(P_TAG, text)
    #print(text,tags_all)
    return "|".join(tags_all)

def parse_tags(text):
    res = {}
    if len(text) == 0:
        return res
    for tag in text.split("|"):
        if len(re.findall(P_TAG2, tag)) > 0:
            k, v = re.findall(P_TAG2, tag)[0]
            #import pdb; pdb.set_trace()
            #print(k,v)
            try:
                if "." in v:
                    v = float(v)
                else:
                    v = int(v)
            except:
                v = v
        else:
            k = tag ; v = 1
        k = k.lower()
        if k in res:
            res[k] += v
        else:
            res[k] = v
    return res
