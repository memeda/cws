#coding=utf-8
TAG_B = 0
TAG_M = 1
TAG_E = 2
TAG_S = 3
TAG_NAME_TRANS={ TAG_B : "B" ,
                 TAG_M : "M" ,
                 TAG_E : "E" ,
                 TAG_S : "S"
                }
TAG_NUM = 4
TAG_LIST = [TAG_B , TAG_M , TAG_E , TAG_S]

BOS = u"<s>"
EOS = u"</s>"

BOT = u"TYPE_BOS"
EOT = u"TYPE_EOT"
ENG_TYPE = u"TYPE_ENG"

INF = float("inf")
NEG_INF = float("-inf")

LEXICON_MATCH_MAX_LENGTH = len(u"中华人民共和国")

OUTPUT_SEPARATOR = " " 

DEBUG = True
