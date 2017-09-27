import sys
import jieba
import jieba.posseg as pseg
import jieba.analyse

import mainprogram 

def weight_func(filename):
  mainprogram.loadjieba()
  content = open(filename, 'rb').read()
  
  tags = jieba.analyse.extract_tags(content, topK=10,withWeight=1)

  for tag in tags:
    print("tag: %s\t\t weight: %f" % (tag[0],tag[1]))