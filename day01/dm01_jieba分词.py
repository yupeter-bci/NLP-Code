from unittest import result

import jieba

def dm01():
    content = '传智教育是一家上市公司，旗下有黑马程序员品牌。我是在黑马这里学习人工智能'
    result1 = jieba.cut(content,cut_all=False)
    print(result1)
    print(next(result1))
    print(next(result1))
    for item in result1:
        print(item)
    list1 = list(result1)
    print(list1)
    list2 = jieba.lcut(content,cut_all=False)
    print(list2)

def dm02():
    content = '传智教育是一家上市公司，旗下有黑马程序员品牌。我是在黑马这里学习人工智能'
    result1 = jieba.cut(content, cut_all=True)
    print(result1)
    print(next(result1))
    print(next(result1))
    for item in result1:
        print(item)
    list1 = list(result1)
    print(list1)
    list2 = jieba.lcut(content, cut_all=True)
    print(list2)

def dm03():
    content = '传智教育是一家上市公司，旗下有黑马程序员品牌。我是在黑马这里学习人工智能'
    result1 = jieba.cut_for_search(content)
    print(result1)
    print(next(result1))
    print(next(result1))
    for item in result1:
        print(item)
    list1 = list(result1)
    print(list1)
    list2 = jieba.lcut_for_search(content)
    print(list2)

def dm04():
    content = '煩惱即是菩提，我暫且不提'
    result = jieba.lcut(content,cut_all=False)
    print(result)

def dm05():
    content = '传智教育是一家上市公司，旗下有黑马程序员品牌。我是在黑马这里学习人工智能'
    result1 = jieba.lcut(content)
    print(f"精确分词:{result1}")
    jieba.load_userdict('data/userdict.txt')
    result2 = jieba.lcut(content)
    print(result2)

if __name__ == '__main__':
    # dm01()
    # dm02()
    # dm03()
    # dm04()
    dm05()