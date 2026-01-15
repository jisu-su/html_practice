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
print (result)

# Stage 4: 함수 내부로 로직 이동
tag_name = "p"
content = "Python is fun!"

def make_line(isOpen):
    #? 고정되는 값만 내부로 넣기
    angle_bracket = ["<", ">"]
    slash = "/"

    if isOpen == True:
        return angle_bracket[0] + tag_name + angle_bracket[1]
    else:
        return angle_bracket[0] + slash + tag_name + angle_bracket[1]

result = make_line(True) + content + make_line(False)
print (result)

# Stage 5: 매개변수로 확장
content = "Python is fun!"

def make_line(isOpen, tag_name):
    angle_bracket = ["<", ">"]
    slash = "/"

    if isOpen == True:
        return angle_bracket[0] + tag_name + angle_bracket[1]
    else:
        return angle_bracket[0] + slash + tag_name + angle_bracket[1]

result = make_line(True, "p") + content + make_line(False, "p")
print (result)

# Stage 6 : 고차 함수 만들기
content = "Python is fun!"

def make_sentence(isOpen, tag_name, content):
    def make_line(isOpen, tag_name):
        angle_bracket = ["<", ">"]
        slash = "/"

        if isOpen == True:
            return angle_bracket[0] + tag_name + angle_bracket[1]
        else:
            return angle_bracket[0] + slash + tag_name + angle_bracket[1]
    
    result = make_line(True, tag_name) + content + make_line(False, tag_name)
    return result

result_sentence = make_sentence(True, "p", content)
print(result)
