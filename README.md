# ByteCompare
simple python script which showing different bytes in files.
 
# Usage: 
  python3 bcomp.py -region 0xFROM-0xTO -lf path/to/first_file -rf path/to/second_file 

FLAGS:
- -region(OPTIONAL): Script uses 16byte lines, -region flag sets region(in lines), which script will compare in files. if -region is not presented, script compares both files completly
- -lf: first file to compare
- -rf: second file to compare

<img width="1698" height="596" alt="image" src="https://github.com/user-attachments/assets/368bf03b-88d7-4d9e-ae12-e3c79528f16f" />

# If you see...
- files should be same size! -> Causes when -region not presented. Compare files with same size, or set -region
- WRONG REGION: set region FROM-TO -> your region is flipped. start addr bigger than end address 
- files hash is the same, files are EQUAL TO EACH OTHER: <md5.hash> -> files are equal, no difference.
- can't open file/s -> script cannot find or access files you provide, check paths, rights.
- some other errors -> new issue

# In plans...
- ascii representation 
- chunk_size to work with non-2^x sized files


