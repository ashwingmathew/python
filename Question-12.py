l = ['Hi','How','are','you?']
with open('text.txt', 'w+') as f:
    for items in l:
        f.write('%s\n' %items)
f.close()
