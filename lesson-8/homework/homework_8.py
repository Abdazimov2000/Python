with open('story.txt', 'w+') as text:
    text.write('Once upon the time there was a wolf.')
    text.seek(0)
    for x in text:
        print(len(x.split()))
