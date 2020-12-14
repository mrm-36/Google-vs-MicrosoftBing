import scraper

def read_file(filename):
    with open(filename, 'r') as fs:
        lst = [x[:-1] for x in fs.readlines()]
    return lst

def accumulate(lst):
    ans = str()
    for x in lst:
        ans += x + ' '
    return ans

def compare(lst):
    g_links = open('G_links.txt', 'a')
    b_links = open('B_links.txt', 'a')

    for query in lst:
        Bing_Results = scraper.q_Bing(query)
        Google_Results = scraper.q_Google(query)

        b_links.write(query + ' ' + accumulate(Bing_Results))
        g_links.write(query + ' ' + accumulate(Google_Results))

    b_links.close()
    g_links.close()

if __name__ == "__main__":
    compare(read_file("queries.txt"))
    print("DONE")