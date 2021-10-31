# TODO: Create a letter using starting_letter.txt

# Open Stating letter file
with open(".\Input\Letters\starting_letter.txt") as f:
    content = f.readlines()

# open names file
with open(".\Input\\Names\invited_names.txt") as names:
    names_list = names.readlines()

# shallow copy of copy is needed
content_name = content.copy()

# go through names list and create a custom content for each name
for name in names_list:
    name = name.removesuffix("\n")
    content_name[0] = content[0].replace("[name]", name)
    file_name = f"{name}.txt"
    output_file = f".\\Output\\ReadyToSend\\{file_name}"
    with open(output_file, "w+") as f:
        for line in content_name:
            f.writelines(line)
