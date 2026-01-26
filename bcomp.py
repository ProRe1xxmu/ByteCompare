import sys
import hashlib
import binascii
from colorama import Back

lfile=0
rfile = 0

try:
	with open(sys.argv[1], 'rb') as file:
		lfile = bytearray(file.read())
	with open(sys.argv[2], 'rb') as file:
		rfile = bytearray(file.read())
except Exception as e:
	exit(f"can't open file/s: {e}")
llen = len(lfile)
if llen != len(rfile):
	exit("files should be same size!")
lhsh = hashlib.md5(lfile).hexdigest()
if lhsh == hashlib.md5(rfile).hexdigest():
	exit(f"files hash is the same: {lhsh}")

i=0
diff = []
print(f"line\t\t {sys.argv[1].split("/")[-1]} \t\t\t\t\t\t {sys.argv[2].split("/")[-1]}")
try:
	while i < llen / 16:
		ls = i*16
		le = ls+16
		ll=lfile[ls:le]
		rl=rfile[ls:le]
		if ll != rl:
			l_form= []
			r_form= []
			j=0
			while j < len(ll):
				if ll[j] != rl[j]:
					l_form.append(Back.RED + format(ll[j], '04x')[2:].upper() + Back.BLACK + ' ')
					r_form.append(Back.RED + format(rl[j], '04x')[2:].upper()  + Back.BLACK + ' ')
				else:
					l_form.append(format(ll[j], '04x')[2:].upper() + ' ')
					r_form.append(format(rl[j], '04x')[2:].upper() + ' ')
				j = j+1
			print(f"{i:08x} \t {''.join(l_form)} \t {''.join(r_form)}")
		i = i+1

except Exception as e:
	print(e)
exit("Done comparing.")

