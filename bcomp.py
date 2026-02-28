import sys
from os import path
import hashlib
import binascii
from colorama import Back

lfile = ""
rfile = ""
region = [0, -1]
argCounter = 0


def reading(FilePath):
	try:
		with open(FilePath, "rb") as File:
			File.read(region[0] * 16)
			if region[1] < 0:
				return bytearray(File.read(path.getsize(FilePath)))
			return bytearray(File.read((region[1] - region[0] + 1) * 16))
	except Exception as e:
		exit(f"{Back.RED}Error{Back.BLACK}:{e}")

for arg in sys.argv:
	if arg == "-h" or "-help":
		exit(f"ByteCompare - Compare files, see difference\n" +
		"Usage: python3 bcomp.py -region 0xFROM-0xTO -lf path/to/first_file -rf path/to/second_file\n" + 
		"\nFLAGS:\n-region(OPTIONAL): Script uses 16byte lines, -region flag sets region(in lines), which"+
		" script will compare in files. if -region is not presented, script compares both files completly"+
		"\n-lf: first file to compare\n-rf: second file to compare")
	if arg == "-lf":
		lfile = reading(sys.argv[argCounter + 1])
	if arg == "-rf":
		rfile = reading(sys.argv[argCounter + 1])
	if arg == "-region":
		map = sys.argv[argCounter + 1].split("-")
		region[0] = int(map[0], 16)
		region[1] = int(map[1], 16)
		if region[1] - region[0] < 0:
			exit(f"{Back.RED}WRONG REGION{Back.BLACK}: set region FROM-TO.")
	argCounter = argCounter + 1

llen = len(lfile)
if llen != len(rfile):
	exit("files should be same size!")
lhsh = hashlib.md5(lfile).hexdigest()
if lhsh == hashlib.md5(rfile).hexdigest():
	exit(f"files hash is the same, files are {Back.GREEN}EQUAL TO EACH OTHER{Back.BLACK}: {lhsh}")

i=0
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
			print(f"{(i + region[0])*16:08x} \t {''.join(l_form)} \t {''.join(r_form)}")
		i = i+1

except Exception as e:
	print(e)
exit("Done comparing.")

