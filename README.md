# ByteCompare
simple python script which showing different bytes in files.

# Usage: 
  python3 bcomp.py /path/to/first/file /path/to/second/file
  
<img width="1698" height="596" alt="image" src="https://github.com/user-attachments/assets/368bf03b-88d7-4d9e-ae12-e3c79528f16f" />

# If you see...
- files should be same size! -> at this moment, the files you comparing should have same size in bytes.
- files hash is the same: <md5.hash> -> files are equal, no difference.
- can't open file/s -> script cannot find or access files you provide, check paths, rights.
- some other errors -> new issue

# In plans...
- ascii representation 
- working with -h -offset -length args
- chunk_size to work with non-2^x sized files

