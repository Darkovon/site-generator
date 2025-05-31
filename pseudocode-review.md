# Split Nodes Delimiter Function - Pseudocode Review

## Function Purpose
Split text nodes containing markdown delimiters into separate nodes for plain text and formatted text.

## Pseudocode Steps

### 1. Initialize Main Result List
- Create the list that you're going to fill

### 2. Process Each Input Node
- Look at each node in the list of nodes

### 3. Handle Already Formatted Nodes
- If it's already formatted, then just append it
- Move to the next iteration of the loop

### 4. Initialize Processing for Text Nodes
- Create a list to fill with the split sections of this current node's text
- Create sections of text by splitting on delimiter

### 5. Validate Delimiter Pairing
- Check if there are matching delimiters
- Raise error if not: "invalid markdown, formatted section not closed"

### 6. Process Each Text Section
- Loop through each section
- If this index of the section is empty:
  - Move to the next iteration of the loop
- If this index is an even index then:
  - Append the text. It doesn't need to be formatted because it's not inside a delimiter
- Otherwise:
  - Append the text to the list with the text_type passed

### 7. Add Results to Main List
- Add the current node to the list of new nodes

### 8. Return Results
- Return the complete list of processed nodes

## Key Logic Notes
- Even indices contain plain text (outside delimiters)
- Odd indices contain formatted text (inside delimiters)
- Empty sections are skipped (occur at string boundaries)
- Non-text nodes pass through unchanged
- Validation ensures delimiters are properly paired