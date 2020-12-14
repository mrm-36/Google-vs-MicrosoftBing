from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

def Subjectivity(lst):
    st = str()
    for x in lst:
        st += x + ' '
    ans = TextBlob(st).sentiment
    sent = TextBlob(st, analyzer=NaiveBayesAnalyzer()).sentiment
    return ans.subjectivity, ans.polarity, sent.p_pos, sent.p_neg, sent.classification