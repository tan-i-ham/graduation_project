import sys
# 切詞用
import jieba
import jieba.posseg as pseg
import jieba.analyse
from optparse import OptionParser
import pprint
from prettytable import PrettyTable

# 結巴使用前的程序
def loadjieba():
  # 使用繁體中文詞庫
  jieba.set_dictionary('dict.txt.big.txt')
  # 將自定義詞庫加進來
  jieba.load_userdict("userdict.txt") 
  # 停用詞
  jieba.analyse.set_stop_words("stop_words.txt")
  jieba.analyse.set_idf_path("idf.txt.big.txt")

  # input_file = open(filename, 'r', encoding = utf8())

def cutandcount():
  filename = 'gogoro.txt'
  content = open(filename, 'rb').read()
  # input_file = open(filename, 'r', encoding = 'utf-8-sig')
  seglist = jieba.cut(content, cut_all=False)

  og_dict = {}
  chars = set(' 0123456789()$,:.。，/􀆿\r\n')


# 原本在字典裡的 斷詞 ＆ 頻率
# 讀入 og_dict
  with open('newdict.txt','rt') as f:
    for line in f:
      k = line.split('\t')[0]
      v = line.split('\t')[1][:-1]
      
      if k in og_dict.keys():
        og_dict[k] = v+1
      else:
        og_dict[k] = v


# 斷新的文字檔之後，把新的詞加入並把頻率設成 1
# 舊的詞在 value +1
  for word in seglist:
    if any((c in chars) for c in word):
      continue
    else:
      if not word in og_dict.keys():
        og_dict[word] = 1
      else:
        og_dict[word] = int(og_dict[word]) + 1

  print('it is NEW DATA !!!!!'+str(og_dict)+'!!!!')

  with open('newdict.txt','w') as f:
      for k,v in og_dict.items():
        f.write(k+'\t'+str(v)+'\n')

cutandcount()