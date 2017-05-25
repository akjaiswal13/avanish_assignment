from django.shortcuts import render
import re

def getwords(text):
    tokens = text.split(' ')
    return tokens

if __name__ == '__main__':
    fyl = open('assignment/a.txt', 'r')
    text = fyl.read()
    fyl.close()

    print getwords(text)

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
        for ele in tokens:
            if word == ele:
                if word_count.has_key(word):
                    word_count[word] += 1
                else:
                    word_count[word] = 1
    return word_count


def wordfreq_without_noisewords(tokens):
    noise_word = open('assignment/noisewords.txt', 'r')
    noise_word_list = noise_word.read().replace('\n',' ').replace(' ','').split(',')
    filtered_tokens = filter(lambda x: False if x in noise_word_list else True, tokens)
    return wordfreq(filtered_tokens)



def home(request):
    return render(request,'home.html',{})

def assignment_task1(request):
    fyl = open('assignment/a.txt', 'r')
    text = fyl.read()
    fyl.close()
    text = text.replace('\n',' ').strip(' ')
    return render(request,'task1.html',{'data':getwords(text)})

def assignment_task2(request):
    fyl = open('assignment/a.txt', 'r')
    text = fyl.read()
    fyl.close()
    text = text.replace('\n',' ').strip(' ')
    return render(request,'task2.html',{'data':cleanwords(text)})

def assignment_task3(request):
    fyl = open('assignment/a.txt', 'r')
    text = fyl.read()
    fyl.close()
    text = text.replace('\n',' ').strip(' ')
    text = cleanwords(text)
    tokens = getwords(text)
    word_freq = wordfreq(tokens)
    return render(request,'task3.html',{'word_freq':word_freq})

def assignment_task4(request):
    fyl = open('assignment/a.txt', 'r')
    text = fyl.read()
    fyl.close()
    text = text.replace('\n',' ').strip(' ')
    text = cleanwords(text)
    tokens = getwords(text)
    word_freq = wordfreq_without_noisewords(tokens)

    return render(request,'task4.html',{'word_freq':word_freq})
    
def assignment_task5(request):
    fyl = open('assignment/a.txt', 'r')
    text = fyl.read()
    text = text.replace('\n',' ').strip(' ')
    text = cleanwords(text)
    tokens = getwords(text)
    word_count = wordfreq(tokens)
    return render(request,'task5.html',{'word_count':sorted(word_count.items())})

def assignment_task6(request, key=None):
    data = []
    fyl = open('assignment/a.txt', 'r')
    text = fyl.read()
    fyl.close()

    text = text.replace('\n',' ').strip(' ')
    text = cleanwords(text)
    tokens = list(set(getwords(text)))

    if key is not None:
        fyl = open('assignment/a.txt', 'r')
        content = fyl.readlines()
        fyl.close()
        for row in content:
            row = row.lower()
            if row.__contains__(key):
                data.append(row)

    return render(request,'task6.html',{'tokens':tokens , 'data':data})

