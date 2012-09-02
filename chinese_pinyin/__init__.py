#!/usr/bin/env python
#encoding: utf-8

import os.path

__version__ = "0.1"

class Pinyin(object):
    """ translate chinese hanzi to pinyin

        usage
        -----
        ::
            In [1]: from ChinesePinyin import Pinyin
            In [2]: Pinyin.t("汉字")
            Out[3]: 'han zi'
    """

    p = None
    table = {}

    def to_unicode(self, value):
        """Converts a string argument to a unicode string.

        If the argument is already a unicode string or None, it is returned
        unchanged.  Otherwise it must be a byte string and is decoded as utf8.
        """
        if isinstance(value, (unicode, type(None))):
            return value
        assert isinstance(value, bytes)
        try:
            return unicode(value, "utf8")
        except:
            return value.encode("utf8").decode("utf8")

    def init_table(self):
        """docstring for init_table"""

        if self.table:
            return
        
        self.table = {}

        data_path = os.path.join(os.path.dirname(__file__), "Mandarin.dat")
        for line in open(data_path):
            key, value = line.split("\t", 1)
            self.table[key] = value
    
    def translate(self, chars, splitter = ' '):
        """docstring for translate"""
        
        self.init_table()
        results = []
        is_english = False

        chars = self.to_unicode(chars)
        for char in chars:
            key = repr(char)[4:-1].upper()
            if key in self.table:
                if is_english:
                    results.append(splitter)
                    
                results.append(self.table[key].strip().split(" ", 1)[0][0:-1].lower())
                results.append(splitter)
                
                is_english = False
            else:
                results.append(char)
                is_english = True
        
        return "".join(results).strip(splitter)
    
    @classmethod
    def t(self, chars, splitter = ' '):
        """docstring for t"""

        cls = Pinyin

        if not cls.p:
            cls.p = Pinyin()

        return cls.p.translate(chars, splitter)
    
if __name__ == "__main__":
    print Pinyin.t("hi 中国汉字")