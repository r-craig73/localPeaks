# localPeaks.py

### by Ron Craig (ron.craig@comcast.net)
### GitHub repository: https://github.com/r-craig73/localPeaks

## Description
###  A Python script that detects and lists local maxima from an imported two column, tab-delimited ASC or TXT file.

### peaks method: The 'peaks' method opens an ASC or TXT file containing time and values columns (all numbers) ['open_asc' method]. The 'peaks' function determines all local maxima by comparing neighboring values (4 points left/right of center value).  The local maxima time (column A) and peak values (column B) results are saved to a tab delimited TXT file (file-LocalPeaks.txt) ['export_results_txt' method].

### User can run the script by running...
* (Powershell Terminal) ```>py .\pathTo...\localPeaks.py 'C:\pathTo...\filename.asc' thresholdValue```

command | os.sys.argv[0] | os.sys.argv[1] | os.sys.argv[2]
------- | -------------- | -------------- | --------------
```>py``` | ```.\pathTo...\localPeaks.py``` | ```'C:\pathTo...\filename.asc'``` | ```thresholdValue```
* Output #1: (Powershell Terminal) ```Peaks detected: 15```
* Output #2: A txt, tab delimited named "filename-LocalPeaks.txt" located in the "C:\pathTo...\file.asc" path (or folder where the imported filename is located) with peaks sorted in time and value columns.

### Pros:
* The script works.
* Fast results.

### Cons:
* Using multiple for loops.
* Neighboring value is fixed to 4 (not adjustable).
* First and last elements are not considered local peaks.
* Smelly code.

### Technologies Used
* ```Application: Python 3.8.2 64-bit```
* ```Packages: os and csv```

### Things to do..
- [ ] Add a method to open file and save values to a float formatted list [def open_asc].
- [ ] Add a method to save time and peak values to a TXT file [def export_results_txt].
- [ ] Raise an exception when the Input's thresholdValue is NOT inputted.
- [ ] Raise an exception when the Input's thresholdValue is NOT a float number.
