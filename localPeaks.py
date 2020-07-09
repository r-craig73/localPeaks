import os, csv

def peaks(file, yLimit):
    times, peaks = [], []

    openFile = open(file, 'r')
    read = csv.reader(openFile, delimiter='\t')

    # store x and y columns into a string-fomratted list
    data = list(read)

    # change data list to float format
    data = [list(map(float, sublist)) for sublist in data]

    # determine neighboring peak values conditions (first 3 elements)
    for i in range(0, 3, 1):
        if data[i + 1][1] > float(yLimit) and data[i + 1][1] > data[i - 4][1] and data[i + 1][1] > data[i - 3][1]:
            if data[i + 1][1] > data[i - 2][1] and data[i + 1][1] > data[i - 1][1] and data[i + 1][1] > data[4][1]:
                if data[i + 1][1] > data[5][1] and data[i + 1][1] > data[6][1] and data[i + 1][1] > data[7][1] and data[i + 1][1] > data[8][1]:
                    times.append(data[i + 1][0])
                    peaks.append(data[i + 1][1])

    # determine neighboring peak values conditions (middle region)
    for i in range(4, len(data) - 4, 1):
        if data[i][1] > float(yLimit) and data[i][1] > data[i - 4][1] and data[i][1] > data[i - 3][1]:
            if data[i][1] > data[i - 2][1] and data[i][1] > data[i - 1][1] and data[i][1] > data[i + 1][1]:
                if data[i][1] > data[i + 2][1] and data[i][1] > data[i + 3][1] and data[i][1] > data[i + 4][1]:
                    times.append(data[i][0])
                    peaks.append(data[i][1])

    # determine neighboring peak values conditions (last 3 elements)
    for i in range(len(data) - 4, len(data), 1):
        if data[i][1] > float(yLimit) and data[i][1] > data[len(data) - 1][1] and data[i][1] > data[i - 5][1]: 
            if data[i][1] > data[i - 4][1] and data[i][1] > data[i - 3][1] and data[i][1] > data[i - 2][1] and data[i][1] > data[i - 1][1]:
                if data[i][1] > data[i + 1][1] and data[i][1] > data[i + 2][1] and data[i][1] > data[i + 3][1]:
                    times.append(data[i][0])
                    peaks.append(data[i][1])
    print(f'Peaks detected: {str(len(peaks))}')

    f = open(file[0:-4] + '-LocalPeaks.txt', 'w')
    f.write('time\t' + 'value\n')
    for i in range(len(times)):
        f.write(str(times[i]) + '\t' + str(peaks[i]) + '\n')
    f.close

def main():
    filePath = os.sys.argv[1]
    head, tail = os.path.split(filePath)
    limit = os.sys.argv[2]
    # peaks(tail, limit)
    if  tail[-3:].lower().endswith(('txt', 'asc')) is True:
        peaks(tail, limit)
    else:
        print('File is not a txt or asc file type.')

if __name__ == "__main__":
    main()