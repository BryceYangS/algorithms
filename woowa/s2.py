def solution(S):
    # write your code in Python 3.6

    fileType = dict()
    fileType['music'] = ['.mp3', '.aac', '.flac']
    fileType['images'] = ['.jpg', '.bmp', '.gif']
    fileType['movies'] = ['.mp4', '.avi', '.mkv']
    fileType['other'] = []

    rtnStr = ''
    fileReport = dict.fromkeys(fileType.keys(), 0)

    files = S.split('\n')
    for file in files:
        tmp = file.split(' ')
        for key in fileType.keys():
            checked = False
            if key == 'other':
                fileReport[key] += int(tmp[1][:-1])
                break
            for ext in fileType[key]:
                if tmp[0].endswith(ext):
                    fileReport[key] += int(tmp[1][:-1])
                    checked = True
                    break
            if checked:
                break

    for i in range(len(fileReport.keys())):
        key = list(fileReport.keys())[i]
        rtnStr += key + ' ' + str(fileReport[key]) + 'b'
        if i != len(fileReport.keys()):
            rtnStr += '\n'

    return rtnStr

print(solution('my.song.mp3 11b\ngreatSong.flac 1000b\nnot3.txt 5b\nvideo.mp4 200b\ngame.exe 100b\nmov!e.mkv 10000b'))
