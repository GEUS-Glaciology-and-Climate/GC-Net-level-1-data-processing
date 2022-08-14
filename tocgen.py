# -*- coding: utf-8 -*-
"""
@author: https://gist.github.com/chriscasola/4700426
"""
def processFile(inFile, outFile):
    mdFile = open(inFile, 'r')
    toc = []
    levels = [0,0,0,0]
    newFile = open(outFile, 'w')
    tempFile = []
    tocLoc = 0
    partOfToc = False
    
    for line in mdFile:
        if partOfToc and line != '\n':
            continue
        else:
            partOfToc = False
        if 'Table of Contents' in line:
            tocLoc = len(tempFile) + 1
            partOfToc = True
        elif line[0] == '#':
            secId = buildToc(line, toc, levels)
            line = addSectionTag(cleanLine(line), secId) + '\n'
        tempFile.append(line)

    for line in toc:
        tempFile.insert(tocLoc, line)
        tocLoc += 1

    for line in tempFile:
        newFile.write(line)

    mdFile.close()
    newFile.close()

def addSectionTag(line, secId):
    startIndex = line.find(' ')
    line = line[:startIndex + 1] + '<a id=\'' + secId + '\' />' + line[startIndex + 1:]
    return line

def buildToc(line, toc, levels):
    line = cleanLine(line)
    secId = 's'
    if line[:4] == '####':
        raise UserWarning('Header levels greater than 3 not supported')
    elif line[:3] == '###':
        levels[3] += 1
        secId += str(levels[1]) + '-' + str(levels[2]) + '-' + str(levels[3])
        toc.append('      * [' + line[4:] + '](#' + secId + ')\n')
    elif line[:2] == '##':
        levels[2] += 1
        levels[3] = 0
        secId += str(levels[1]) + '-' + str(levels[2])
        toc.append('  * [' + line[3:] + '](#' + secId + ')\n')
    elif line[:1] == '#':
        levels[1] += 1
        levels[3] = levels[2] = 0
        secId += str(levels[1])
        toc.append('* [' + line[2:] + '](#' + secId + ')\n')
    return secId

def cleanLine(text):
    text = stripNewline(text)
    text = removeAnchors(text)
    return text

def stripNewline(text):
    return text.replace('\n', '')

def removeAnchors(text):
    while ('<' in text and '>' in text):
        leftTag = text.index('<')
        rightTag = text.index('>')
        text = text[0:leftTag] + text[rightTag + 1:]
    return text

if __name__ == "__main__":
    import sys
    processFile(sys.argv[1], sys.argv[2])