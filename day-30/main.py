try:
    file = open('my_file.txt')
except FileNotFoundError:
    open('my_file.txt', 'w')
else:
    content = file.read()
    print('content: ' + content)
finally:
    file.close()
    print('File was closed')