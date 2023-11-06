import base64
import os

print (base64.encodebytes(os.urandom(32)))