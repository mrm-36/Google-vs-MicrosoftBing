# Google-vs-MicrosoftBing

1. Description

1.1 Main Idea
Study the bias, positivity, negativity, objectivity, and subjectivity of the two search engines Google and Microsoft Bing individually and then in comparison with each other, using a series of controversial queries.

1.2 Motive
I believe that this project is one way of emphasizing the claim that AI has still a lot to achieve, especially when it comes to ethics and bias.

1.3 Objective
My objective is to show that even two of the giants in the world of technology haven’t figured out yet how to make a completely unbiased and objective algorithm.

2. Project

2.1 Part I
Build a tool that takes a controversial query as input and returns an analysis of the sentiments, classification, polarity, objectivity, and subjectivity in the top 10 results in each of Google and Microsoft Bing, and a comparison of these parameters in the results of each against the other.

2.2 Part II - Case Study
Using the same tool, iterate over 50 controversial pre-defined queries and return an overview of the analysis of sentiments, classification, polarity, objectivity and subjectivity done on each query in each of Google and Microsoft Bing, and then in comparison with each other.

3. Metrics

3.1 Kendall Tau

In statistics, the Kendall Tau is a metric used to measure the ordinal association between two measured quantities.
It is a measure of rank correlation: the similarity of the orderings of the data.
The result is a floating number within the range [-1.0, 1.0] where 1.0 is an identical correlation and -1.0 is a fully different correlation.
In this project, we used the ranks of the links as they appear on the search page in each browser.
The Kendall $\tau$ coefficient is defined as:
$$\tau = ((number of concordant pairs) - (number of discordant pairs)) / (n \choose 2)$$
Any pair of observation (x_i, y_i) and (x_j, y_j), where i < j, are said to be concordant if the sort order of (x_i, x_j) and (y_i, y_j) agrees:
that is, if either both x_i > x_j and y_i > y_j hold or both x_i < x_j and y_i < y_j hold; otherwise thay are said to be discordant.
Where {n \choose 2} = (n(n\ -\ 1)) / 2$ is the binomial coefficient for the number of ways to choose two items from n items.

3.2 Jaccard Coefficient

The Jaccard coefficient is a statistic used for calculating the similarity and diversity of sample sets. The Jaccard Coefficient measures the similarity between finite sample sets.
The result is a floating number within the range [0.0, 1.0] where 0.0 is no intersection at all and 1.0 is the two sets are the same.
In this project, we used the links in the result page of each query.
$$J(A, B)\ =\ (A inter B) / (A union B)$$

3.3 Subjectivity

A measure of the subjectivity of the text.
The subjectivity is a floating number within the range [0.0, 1.0] where 0.0 is very objective and 1.0 is very subjective.
In this project, we calculated the average subjectivity of all the links for each query for each browser.

3.4 Polarity

A measure of the negativity, the neutralness, or the positivity of the text.
The polarity score is a floating number within the range [-1.0, 1.0] where -1.0 is negative, 0.0 is neutral, and 1.0 is positive.
In this project, we calculated the average polarity of all the links for each query for each browser.

3.5 Classification (Positivity, Negativity)

Classification - Either 'pos' or 'neg' indicating if the text has a positive effect or negative one.
Positivity - a measure of how positive the text is.
Negativity - a measure of how negative the text is.
In this project, we calculated the average positivity and negativity of all the links for each query for each browser, and based on these results we determined the classification of the query in each browser.
The average of the Classification was calculated as 1 for 'pos' and 0 for 'neg'.
