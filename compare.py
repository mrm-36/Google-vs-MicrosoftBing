def compare(filename):
    with open(filename, 'r') as fs:
        fs.readline()
        print("%-64s | %-8s | %-8s | %-49s | %-49s |" % ("Query", "Kendall", "Jaccard", "Bing Results", "Google Results"))
        print("%-64s | %-8s | %-8s | %-8s | %-8s | %-8s | %-8s | %-5s | %-8s | %-8s | %-8s | %-8s | %-5s |"
                % ("", '', '', 'Subj', 'Pol', 'Pos', 'Neg', 'Class', 'Subj', 'Pol', 'Pos', 'Neg', 'Class'))
        print("%-64s | %-8s | %-8s | %-8s | %-8s | %-8s | %-8s | %-5s | %-8s | %-8s | %-8s | %-8s | %-5s |" % ("", '', '', '', '', '', '', '', '', '', '', '', ''))        
        print('-'*192)
        i = 1
        for x in fs.readlines():
            x = x.split()
            if x[0] == 'Average': print()
            print("%2i. %-60s | %-8s | %-8s | %-8s | %-8s | %-8s | %-8s | %-5s | %-8s | %-8s | %-8s | %-8s | %-5s |" 
                    % (i, ' '.join(x[:-12]), x[-12], x[-11], x[-10], x[-9], x[-8], x[-7], x[-6], x[-5], x[-4], x[-3], x[-2], x[-1]))
            print('-'*192)
            i += 1

if __name__ == "__main__":
    compare(r"Code\results.txt")
    input("\n\nPress Any Key...")