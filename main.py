def pick_one(num):
    with open(f"story{num}.txt" , "r", encoding="utf-8") as f:
        stored_data = f.read()
        return stored_data

while True:
    story_number = input("Enter story number(1-3) : ")
    if story_number.isdigit():
        story_number = int(story_number)
        if 1<= story_number <= 3:
            break
        else:
            print("Enter number between 1-2! ")
    else:
        print("Enter a valid number !")

story_data = pick_one(story_number)

def display(story):
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

    print("WELCOME TO MADLIB GEN")
    dic={}
    for word in (words):
        if '_' in word:
            i=word.index('_')
            s=word[1:i]+" "+word[i+1:-1]
        else:
            s=word[1:-1]
        dic[word]= input("Enter a word for "+s+": ")

    for word in words:
        story = story.replace(word , dic[word])
    print("\nHERE IS YOUR STORY\n\n",story)

display(story_data)  

