import base64
import sys

fr = open(sys.argv[1], 'rb');
b64 = base64.standard_b64encode(fr.read())
fr.close()
fw = open('base64_enc.txt', 'wb')
fw.write(b64)
fw.close()