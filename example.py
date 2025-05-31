def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = [] # create the list that you're going to fill
    for old_node in old_nodes: # look at each node in the list of nodes
        if old_node.text_type != TextType.TEXT: # if it's already formatted, then just append it
            new_nodes.append(old_node)
            continue # move to the next iteration of the loop
        split_nodes = [] # create a list to fill with the split sections of this current nodes text
        sections = old_node.text.split(delimiter) # create sections of text
        if len(sections) % 2 == 0: # check if there are matching delimiters
            raise ValueError("invalid markdown, formatted section not closed") # raise error if not
        for i in range(len(sections)): # loop through each section
            if sections[i] == "": # if this index of the section is empty
                continue # move to the next iteration of the loop
            if i % 2 == 0: # if this index is an even index then
                split_nodes.append(TextNode(sections[i], TextType.TEXT)) # append the text. it doesn't need to be formatted because it's not inside a delimiter
            else: # otherwise
                split_nodes.append(TextNode(sections[i], text_type)) # append the text to the list with the text_type passed
        new_nodes.extend(split_nodes) # add the current node to the list of new nodes
    return new_nodes
