import pandas as pd
import openpyxl

def write(readfile, writefile):
    with open(readfile, 'r') as fs:
        fs.readline()
        fields = ["Query", "Kendall", "Jaccard", "Bing Results", "Google Results"]
        headers = ["", '', '', 'Subj', 'Pol', 'Pos', 'Neg', 'Class', 'Subj', 'Pol', 'Pos', 'Neg', 'Class']
        rows = []
        for x in fs.readlines():
            x = x.split()
            rows.append([' '.join(x[:-12]), float(x[-12]), float(x[-11]), float(x[-10]), float(x[-9]), float(x[-8]), 
                        float(x[-7]), x[-6], float(x[-5]), float(x[-4]), float(x[-3]), float(x[-2]), x[-1]])
    df = pd.DataFrame(rows, columns = headers)
    df.to_excel('results.xlsx', sheet_name = 'Results', index = False)

if __name__ == "__main__":
    write("results.txt", 'results.xlsx')
    input("\n\nPress Any Key...")