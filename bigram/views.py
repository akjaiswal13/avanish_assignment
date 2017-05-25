from django.shortcuts import render
from django.http import HttpResponse
import re

# Create your views here.

def getwords(text):
    token_list = text.split(' ')
    tokens = []

    for n in range(len(token_list)-1):
       tokens.append(("%s %s")%(token_list[n],token_list[n+1]))
    return tokens

def cleanwords(text):
    text = text.replace('.','')
    text = text.lower()
    tokens = text.split(' ')
    pattern = r'[0-9]+'
    tally = lambda x: False if re.match(pattern,x) else True
    tokens = filter(tally, tokens)
    text = ' '.join(tokens)
    return text

def wordfreq(tokens):
    search_list = set(tokens)
    word_count = {}

    for word in search_list:
        #parse_word = word.replace('_',' ')
        for ele in tokens:
            if word == ele:
                if word_count.has_key(word):
                    word_count[word] += 1
                else:
                    word_count[word] = 1
    return word_count

def filter_noise_words(x):
    noise_word = open('assignment/noisewords.txt', 'r')
    noise_word_list = noise_word.read().replace('\n',' ').replace(' ','').split(',')

    x = x.split(' ')
    if x[0] not in noise_word_list and x[1] not in noise_word_list:
        return True
    else:
        return False

def wordfreq_without_noisewords(tokens):
    filtered_tokens = filter(filter_noise_words, tokens)
    return wordfreq(filtered_tokens)


if __name__ == '__main__':
    fyl = open('assignment/a.txt', 'r')
    text = fyl.read()
    fyl.close()
    text = text.replace('\n',' ').strip(' ')
    text = cleanwords(text)
    tokens = getwords(text)
    #print tokens
    print wordfreq(tokens)


def bigram(request):
    return render(request,'bigram.html',{})

def bigram_task1(request):
    fyl = open('assignment/a.txt', 'r')
    text = fyl.read()
    fyl.close()
    text = text.replace('\n',' ').strip(' ')
    return render(request,'bigram_task1.html',{'data':getwords(text)})

def bigram_task2(request):
    fyl = open('assignment/a.txt', 'r')
    text = fyl.read()
    fyl.close()
    text = text.replace('\n',' ').strip(' ')
    return render(request,'bigram_task2.html',{'data':cleanwords(text)})

def bigram_task3(request):
    fyl = open('assignment/a.txt', 'r')
    text = fyl.read()
    fyl.close()
    text = text.replace('\n',' ').strip(' ')
    text = cleanwords(text)
    tokens = getwords(text)
    word_freq = wordfreq(tokens)
    return render(request,'bigram_task3.html',{'word_freq':word_freq})

def bigram_task4(request):
    fyl = open('assignment/a.txt', 'r')
    text = fyl.read()
    fyl.close()
    text = text.replace('\n',' ').strip(' ')
    text = cleanwords(text)
    tokens = getwords(text)
    word_freq = wordfreq_without_noisewords(tokens)

    return render(request,'bigram_task4.html',{'word_freq':word_freq})


def bigram_task5(request):
    fyl = open('assignment/a.txt', 'r')
    text = fyl.read()
    fyl.close()
    text = text.replace('\n',' ').strip(' ')
    text = cleanwords(text)
    tokens = getwords(text)
    word_count = wordfreq(tokens)
    return render(request,'bigram_task5.html',{'word_count':sorted(word_count.items())})

def bigram_task6(request, key=None):
    data = []

    fyl = open('assignment/a.txt', 'r')
    text = fyl.read()
    fyl.close()

    text = text.replace('\n',' ').strip(' ')
    text = cleanwords(text)
    tokens = list(set(getwords(text)))

    if key is not None:
        print "clicked"
        fyl = open('assignment/a.txt', 'r')
        content = fyl.readlines()
        fyl.close()
        for row in content:
            row = row.lower()
            if row.__contains__(key):
                data.append(row)


    return render(request,'bigram_task6.html',{'tokens':tokens , 'data':data})

