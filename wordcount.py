def word_count(filename):
    word_count_dict = {}
    text_file = open(filename)
    for line in text_file:
        list_of_words = line.split()
        for word in list_of_words:
            if word in word_count_dict:
                word_count_dict[word] += 1
            else:   
                word_count_dict[word] = 1
    text_file.close()

    for tup in word_count_dict.iteritems():
        print "{} {}".format(tup[0], tup[1])
    return None

    # alternative way to tuple and print:
    # for counted_word in word_count_dict:
    #     quantity = word_count_dict[counted_word]
    #     print "{} {}".format(counted_word, quantity)

word_count("twain.txt")
