path = 'newlines_to_spaces.txt'
fr = open(path, 'r')
body = fr.read()
fr.close()
body = body.replace('\n', ' ')
fw = open(path, 'w')
fw.write(body)
fw.close()