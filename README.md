ChinesePinyin
=============

Translate chinese hanzi to pinyin by python.

inspired by flyerhzm's <https://github.com/flyerhzm/chinese_pinyin>

The dict is borrowed from <http://github.com/fayland/perl-lingua-han/tree/master/Lingua-Han-PinYin/>

Install
-------

    sudo python setup.py install 

Usage
-----
    
    from chinese_pinyin import Pinyin

    Pinyin.t('中国')  => "zhong guo"
    Pinyin.t('中国', '-') => "zhong-guo"
    Pinyin.t('中国', '') => "zhongguo"
    Pinyin.t('你好world') => "ni hao world"
