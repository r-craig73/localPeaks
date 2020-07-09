# localPeaks.py

### by Ron Craig (ron.craig@comcast.net)
### GitHub repository: https://github.com/r-craig73/localPeaks

## Description
###  A Python script that detects and lists local maxima from an imported two column, tab-delimited ASC or TXT file.

### Peak detection method: The 'peaks' function takes one-dimensional array and threshold y value arguments. The 'peaks' function determines all local maxima by comparison of neighboring values (4 points left/right of center value).  The time (column A) and peak values (column B) results are saved to a tab delimited TXT file (file-LocalPeaks.txt).

### User can run the script by running...
* Input: (Powershell Terminal)

command | os.sys.argv[0] | os.sys.argv[1] | os.sys.argv[2]
------- | -------------- | -------------- | --------------
```>py``` | ```.\pathTo...\localPeaks.py``` | ```'C:\pathTo...\filename.asc'``` | ```thresholdValue```
* Output #1: (Powershell Terminal) ```Peaks detected: 15```
* Output #2: A txt, tab delimited named "filename-LocalPeaks.txt" located in the "C:\pathTo...\file.asc" path (or folder where the imported filename is located) with peaks sorted in time and value columns.

### Pros: The script works and fast results.

### Cons: Using brute for loops,  neighboring value is fixed to 4 (not adjustable), first and last data points are not considered, and smelly code (especially for loops for first three elements [lines 16-21] and last three elements [lines 32-37]).

### Technologies Used
* ```Application: Python 3.8.2 64-bit```
* ```Packages: os and csv```

### Things to do..
- [ ] Raise an exception when the Input's thresholdValue is NOT inputted.
- [ ] Raise an exception when the Input's thresholdValue is NOT a float number.
