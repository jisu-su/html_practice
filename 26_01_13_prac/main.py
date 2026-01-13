
tag_name = "h1"
angle_bracket = ["<", ">"]
content = "고양이"

tag_assemble_open = angle_bracket[0] + tag_name + angle_bracket[1]
tag_assemble_close = angle_bracket[0] + "/" + tag_name + angle_bracket[1]

result = tag_assemble_open + content + tag_assemble_close

