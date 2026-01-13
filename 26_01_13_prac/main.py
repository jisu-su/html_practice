
tag_name = "h1"
angle_bracket = ["<", ">"]
content = "고양이"

tag_assemble_open = angle_bracket[0] + tag_name + angle_bracket[1]
tag_assemble_close = angle_bracket[0] + "/" + tag_name + angle_bracket[1]

def make_tag(isOpen):
    if isOpen == True:
        open = tag_assemble_open
        return open + content + tag_assemble_close
    else:
        close = tag_assemble_close
        return tag_assemble_open + content + close


result = tag_assemble_open + content + tag_assemble_close

