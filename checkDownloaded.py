def checkDownloaded():
    downloaded = set()
    file_object = open('mj.txt', 'r')
    for line in file_object:
        downloaded.add(line[:-1])
    #print(downloaded)
    return downloaded
