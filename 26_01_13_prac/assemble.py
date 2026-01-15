# 미션: "<p>Python is fun!</p>" 만들기
# Stage 1부터 Stage 7까지 직접 작성해보세요

# Stage 1: 변수 분해
tag_name = "p"
content = "Python is fun!"
angle_bracket = ["<", ">"]
slash = "/"

result = "<" + tag_name + ">" + content + "<" + slash + tag_name + ">"

# Stage 2: 패턴 발견
tag_name = "p"
content = "Python is fun!"
angle_bracket = ["<", ">"]
slash = "/"

open = angle_bracket[0] + tag_name + angle_bracket[1]
close = angle_bracket[0] + slash + tag_name + angle_bracket[1]

result = open + content + close

# Stage 3: 함수화 시도
tag_name = "p"
content = "Python is fun!"
angle_bracket = ["<", ">"]
slash = "/"

open = angle_bracket[0] + tag_name + angle_bracket[1]
close = angle_bracket[0] + slash + tag_name + angle_bracket[1]

def make_line(isOpen):
    if isOpen == True:
        return open
    else:
        return close

result = make_line(True) + content + make_line(False)

# Stage 7까지 진화시켜보세요!
