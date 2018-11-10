def filterKeywords(taggedText):
    filteredKeywords = []
    for taggedTextWord in taggedText:
        if taggedTextWord[1][0] == 'N':
            filteredKeywords.append(taggedTextWord[0])
    return filteredKeywords
