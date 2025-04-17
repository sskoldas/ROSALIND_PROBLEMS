
## ID : INI2
def square_of_hypothenuse(a,b):
    hypothenuse_squared = a**2 + b**2
    return hypothenuse_squared


## ID : INI3
def extract_and_combine(s,a,b,c,d):
    slice1 = s[a:b+1]
    slice2 = s[c:d+1]
    result = slice1 + " " + slice2
    return result


## ID : INI4
def sum_of_odds(a,b):
    collect = []
    for i in range(a,b+1):
        if i % 2 == 1:
            collect.append(i)
        
    return sum(collect)


## ID : INI5
def extract_lines(input_filename):
    f = open(input_filename, 'r')
    lines = f.readlines()

    
    # Iterate over the lines, enumerate starts counting from 1
    for index, line in enumerate(lines, start=1):
        if index % 2 == 0:
            print(line.strip())
    

## ID : INI6
def count_words_occurrence(x):
    words = x.split()
    word_count ={}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    for word, count in word_count.items():
        print(f"{word} {count}")

