import unittest
from mdt import *

class TestMDT(unittest.TestCase):

    def setUp(self):
        self.dt = mp.parse_md_file("demo/demo.md")

    def test_diff(self):
        dtm = md.diff_md_files("demo/demo.md", "demo/demo_new.md")
        #print dtm
        #pdb.set_trace()

    def test_diff_stat(self):
        dtm = ms.add_diff_stat( md.diff_md_files("demo/demo.md", "demo/demo_new.md"), "count")
        #print dtm

    def test_track(self):
        logfile = "demo/demo_log.tsv"
        outfile = "demo/demo.tsv"
        if os.path.exists(logfile): os.unlink(logfile)
        if os.path.exists(outfile): os.unlink(outfile)
        md.track_md_file("demo/demo_old.md", "demo/demo.tsv", "demo/demo_log.tsv")
        md.track_md_file("demo/demo.md", "demo/demo.tsv", "demo/demo_log.tsv")
        md.track_md_file("demo/demo_new.md", "demo/demo.tsv", "demo/demo_log.tsv")

    def test_stat_journal(self):
        dt = ms.add_stat(self.dt, "td_n,td_c,m,WC")
        #print dt
        #pdb.set_trace()

if __name__ == '__main__':
    unittest.main()
