def markdown_to_blocks(markdown):
    removed_doublelines = []
    stripped_list = []
    new_list = []
    removed_doublelines = markdown.split("\n\n")

    for i in removed_doublelines:
        stripped_list.append(i.strip())

    for line in stripped_list:
        if line != "":
            new_list.append(line)

    return new_list


# if __name__ == "__main__":
#     markdown = """
# This is **bolded** paragraph

# This is another paragraph with _italic_ text and `code` here
# This is the same paragraph on a new line

# - This is a list
# - with items
# """
#     markdown_to_blocks(markdown)