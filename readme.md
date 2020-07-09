# localPeaks.py

### by Ron Craig (ron.craig@comcast.net)
### GitHub repository: https://github.com/r-craig73/localPeaks

## Description
###  A Python script that detects and lists local maxima from an imported two column, tab-delimited ASC file.

### Peak detection method: The 'peaks' function takes one-dimensional array and threshold y value arguments. The function finds all local maxima by simple comparison of neighboring values (4 points left/right of center value).  The time (column A) and peak values (column B) results are saved to a tab delimited TXT file (file-LocalPeaks.txt).

### User can run the script by running...
* Input: (Powershell Terminal)

command | os.sys.argv[0] | os.sys.argv[1] | os.sys.argv[2]
------- | -------------- | -------------- | --------------
```>py``` | ```.\pathTo...\localPeaks.py``` | ```'C:\pathTo...\filename.asc'``` | ```thresholdValue```
* Output: A txt, tab delimited named "filename-LocalPeaks.txt" located in the "C:\pathTo...\file.asc" path (or where the filename path is located) with peaks sorted in time and value columns, tab delimited.
### Pros: The script works and fast results.
### Cons: Using brute for loops,  neighboring value is fixed to 4 (not adjustable), first and last data points are not considered, and smelly code (especially the for loops for first three elements and last three elements).

### Technologies Used
```
Application: Python 3.8.2 64-bit
Packages: os and csv
```

### Things to do..
- [ ] Raise an exception to verify Input's thresholdValue is inputted and a float number.

