import re

def solution(files):
    answer = []
    for file in files:
        split_file=re.split(r'([0-9]+)',file)
        answer.append(split_file)
    
    answer=sorted(answer,key=lambda x:(x[0].lower(), int(x[1])))
        
        

    return [''.join(check) for check in answer]

print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]),["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"])
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]),["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"])
