output = '\t'.join(['name', 'title', 'age', 'gender'])
with open('test.txt','a+') as f:
    f.write(output)
    f.close()