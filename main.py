with open("story1.txt" , "r", encoding="utf-8") as f:
    story = f.read()
    words = set()
    word_start = -1
    target_start = '<'
    target_end = '>'
    for i,char in  enumerate(story):
        if char == target_start :
            word_start = i
        if char == target_end and word_start != -1 :
            word = story[word_start:i+1]
            words.add(word)
            word_start=-1
    print(words)