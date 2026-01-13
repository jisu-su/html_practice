
tag_name = "h1"
content = "고양이"



def make_tag(isOpen):
    angle_bracket = ["<", ">"]
    slash = "/"

    if isOpen == True:
        open = angle_bracket[0] + tag_name + angle_bracket[1]
        return open
    else:
        close = angle_bracket[0] + slash + tag_name + angle_bracket[1]
        return close


result = make_tag(True) + content + make_tag(False)
print(result)

