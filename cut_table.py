import sys
# 切詞用
import jieba
import jieba.posseg as pseg
import jieba.analyse
from optparse import OptionParser
import pprint
from prettytable import PrettyTable


import mainprogram
def cutting2(filename):
  
  mainprogram.loadjieba()
  content = open(filename, 'rb').read()
  input_file = open(filename, 'r', encoding = 'utf-8-sig')
  
  dicbig = {}
  dicbig['time'] = []
  dicbig['user'] = []
  dicbig['con'] = []

  word_count = {}
  for line in input_file :
    words = line.split(' ',2)
    if line == '\n':
      print("found an end of line")
      continue
      
    print('colume1:',words[0])
    dicbig['time'].append(words[0])

    if len(words)>1:
      dicbig['user'].append(words[1])
      print('colume2:',words[1])
    #有些日期只會分割成兩個物件
    #對話通常能分成三個
    if len(words)>2:
      print('colume3:',words[2])
      dicbig['con'].append(words[2])
  
    # for word in words:
    #   word = word.lower()
    #   # Special case if we're seeing this word for the first time.
    #   if not word in word_count:
    #     word_count[word] = 1
    #   else:
    #     word_count[word] = word_count[word] + 1

  # print(word_count.items())
  pp = pprint.PrettyPrinter(indent=4)
  pp.pprint(dicbig)
  

def cutting3(filename):
  
  mainprogram.loadjieba()
  content = open(filename, 'rb').read()
  input_file = open(filename, 'r', encoding = 'utf-8-sig')

  t = PrettyTable()
  t.field_names = ["Name", "Conversation"]

  for line in input_file :
    words = line.split(' ',2)
    if line == '\n':
      print("found an end of line")
      continue
    
    if len(words) == 3:
      # print('colume1:',words[0])
      # print('colume2:',words[1])
      # print('colume3:',words[2])
      cutdone = jieba.cut(words[2], cut_all=False)
      t.add_row([words[1], '/'.join(cutdone)])
      

  print(t)  
  # pp = pprint.PrettyPrinter(indent=4)
  # pp.pprint(dicbig)