import sys
import jieba
import jieba.posseg as pseg
import jieba.analyse

import word_count as wc
import cut
import weight
import cut_table

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

def print_words(filename):
  """Prints one per line '<word> <count>' sorted by word for the given file."""
  word_count = wc.word_count_dict(filename)
  words = sorted(word_count.keys())
  for word in words:
    print(word,word_count[word])


def print_top(filename):
  """Prints the top count listing for the given file."""
  word_count = wc.word_count_dict(filename)
  print(type(word_count))
  # Each item is a (word, count) tuple.
  # Sort them so the big counts are first using key=get_count() to extract count.
  items = sorted(word_count.items(), key=cut.get_count, reverse=False)

  # Print the first 20
  for item in items[:20]:
    print(item[0], item[1])



def main():
  if len(sys.argv) != 3:
    print('usage: ./mainprogram.py {--count | --topcount | --weight | --cut} filename.txt')
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  #看關鍵詞
  elif option == '--weight':
    weight.weight_func(filename)
  elif option == '--cut':
    cut.cutting(filename)  
  elif option == '--cut2':
    cut_table.cutting3(filename) 
  else:
    print('unknown option: ' + option)
    sys.exit(1)

if __name__ == '__main__':
  main()
