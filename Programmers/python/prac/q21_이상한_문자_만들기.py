def solution(s):
    answer = ""
    words = s.split(' ')
    for i in range(len(words)):
        for j in range(len(words[i])):
            if j % 2 == 0:
                answer += words[i][j].upper()
            else:
                answer += words[i][j].lower()
        answer += " "
    return answer[:-1]
