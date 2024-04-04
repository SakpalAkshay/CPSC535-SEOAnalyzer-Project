import DataScraper
from algorithms import KMPAlgo, NaiveStringMatching, RabinKarpAlgo, SuffixArray, SuffixTree
import time


def getProcessTimeAndWordCount(scrapped_data, algorithmselected):

    wordCount = {}
    process_time = {}

    # run algorithms
    if "Naive String Matching" in algorithmselected:
        start = time.process_time()
        
        text_data = scrapped_data.split()
        # print(text_data)
        for word in text_data:
            if word in wordCount:
                continue
            else:
                count = NaiveStringMatching.naive_string_matching(scrapped_data, word)
                wordCount[word] = count

        end = time.process_time()
        process_time["NaiveString"] = (end - start)
        print("time to run NaiveStringMatching algorithm", (end - start) , "secs")


    if "KMP Algorithm" in algorithmselected:
        start = time.process_time()
        wordCount = {}
        text_data = scrapped_data.split()
        # print(text_data)
        for word in text_data:
            if word in wordCount:
                continue
            else:
                count = KMPAlgo.kmp_search(scrapped_data, word)
                wordCount[word] = count
        end = time.process_time()
        process_time["KMP"] = (end - start) 
        print("time to run KMP algorithm", (end - start),  "secs")
        

    if "Rabin Karp" in algorithmselected:
        start = time.process_time()
        wordCount = {}
        text_data = scrapped_data.split()
        # print(text_data)
        for word in text_data:
            if word in wordCount:
                continue
            else:
                rk_search = RabinKarpAlgo.RabinKarp(scrapped_data, word)

                count = rk_search.search_pattern()
                wordCount[word] = count

        end = time.process_time()
        process_time["RabinKarb"] = (end - start)
        print("Time to run Rabin Karp algorithm", (end - start), "secs")

    if "Suffix Array" in algorithmselected:
        start = time.process_time()
        wordCount = {}
        text_data = scrapped_data.split()
        # print(text_data)
        for word in text_data:
            if word in wordCount:
                continue
            else:
                count = SuffixArray.count_pattern_occurrences(scrapped_data, word)

                wordCount[word] = count

        end = time.process_time()
        process_time["SuffixArray"] = (end - start)
        print("Time to run Suffix Array algorithm", (end - start), "secs")

    if "Suffix Tree" in algorithmselected:
        start = time.process_time()
        wordCount = {}
        text_data = scrapped_data.split()
        # print(text_data)
        for word in text_data:
            if word in wordCount:
                continue
            else:
                count = SuffixTree.count_pattern_occurrences(scrapped_data, word)
                
                wordCount[word] = count

        end = time.process_time()
        process_time["SuffixTree"] = (end - start)
        print("Time to run Suffix Tree algorithm", (end - start), "secs")

    return wordCount, process_time
