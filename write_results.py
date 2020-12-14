import jaccard, kendall, subjectivity, scraper

def read_file(filename):
    mp = {}
    with open(filename, 'r') as fs:
        for x in fs.readlines():
            i, x = 0, x.split()
            for w in x:
                if w[:4] != 'http': i += 1
            mp[' '.join(x[:i])] = x[i:]
    return mp

def write(Bing_Results, Google_Results, Queries, n):
    results = open('results2.txt', 'a')
    results.write('Query Kendall Jaccard B_Sub B_Pol B_pos B_neg B_Class G_Sub G_Pol G_pos G_neg G_Class\n')

    kd, jc = 0, 0
    bs, bp, bpos, bneg, bcl = 0, 0, 0, 0, 0
    gs, gp, gpos, gneg, gcl = 0, 0, 0, 0, 0

    # Missed: 13, 14, 15, 16, 17, 18, 19

    for query in Queries[42:50]:
        query = query[:-1]
        curr_kd = kendall.Kendall(Bing_Results[query], Google_Results[query])
        curr_jc = jaccard.Jaccard(Bing_Results[query], Google_Results[query])
        curr_bs = subjectivity.Subjectivity([scraper.get_text(x) for x in Bing_Results[query]])
        curr_gs = subjectivity.Subjectivity([scraper.get_text(x) for x in Google_Results[query]])
        print(query)
        kd += curr_kd
        jc += curr_jc
        bs += curr_bs[0]
        bp += curr_bs[1]
        bpos += curr_bs[2]
        bneg += curr_bs[3]
        bcl += 1 if curr_bs[4] == 'pos' else 0 
        gs += curr_gs[0]
        gp += curr_gs[1]
        gpos += curr_gs[2]
        gneg += curr_gs[3]
        gcl += 1 if curr_gs[4] == 'pos' else 0
        msg = (query + ' ' + str(round(curr_kd, 4)) + ' ' + str(round(curr_jc, 4)) +  ' ' 
                + str(round(curr_bs[0], 4)) + ' ' + str(round(curr_bs[1], 4)) +  ' ' + str(round(curr_bs[2], 4)) 
                + ' ' + str(round(curr_bs[3], 4)) + ' ' + str(curr_bs[4]) + ' '
                + str(round(curr_gs[0], 4)) + ' ' + str(round(curr_gs[1], 4)) + ' '  + str(round(curr_gs[2], 4)) 
                + ' ' + str(round(curr_gs[3], 4)) + ' ' + str(curr_gs[4]) + '\n') 
        results.write(msg)

    msg = (f'Average {round(kd/n, 4)} {round(jc/n, 4)} {round(bs/n, 4)} {round(bp/n, 4)} {round(bpos/n, 4)} {round(bneg/n, 4)}'
            + f' {round(bcl/n, 4)} {round(gs/n, 4)} {round(gp/n, 4)} {round(gpos/n, 4)} {round(gneg/n, 4)} {round(gcl/n, 4)}')
    results.write(msg)


if __name__ == "__main__":
    Bing_Results = read_file('B_links.txt')
    Google_Results = read_file('G_links.txt')
    Queries = open('queries.txt', 'r').readlines()

    write(Bing_Results, Google_Results, Queries, len(Queries))

    print("DONE")   