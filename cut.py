import sys
# 切詞用
import jieba
import jieba.posseg as pseg
import jieba.analyse


import word_count as wc
import mainprogram


def get_count(word_count_tuple):
  """Returns the count from a dict word/count tuple  -- used for custom sort."""
  return word_count_tuple[1]

def cutting(filename):
  mainprogram.loadjieba()
  content = open(filename, 'rb').read()
  seglist = jieba.cut(content, cut_all=False)
  # print("/ ".join(seglist))

  word_count = {}

  for word in seglist:
    if not word in word_count:
      word_count[word] = 1
    else:
      word_count[word] = word_count[word] + 1

  items = sorted(word_count.items(), key=get_count, reverse=True)

  # words = sorted(word_count.keys())
  # for word in words:
  #   print(word,word_count[word])
  # Print the first 20
  for item in items[:20]:
    print(item[0], item[1])