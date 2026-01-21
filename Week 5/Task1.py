line_count = 0
word_count = 0
with open("text.txt", "r") as source:
    content = source.read()
    source.seek(0)
    all_lines = source.readlines()
with open("analysis.txt", "w") as result:
    for _ in all_lines:
        line_count += 1
    result.write(f"Number of lines: {line_count}\n")
    word_list = []
    for line in all_lines:
        word_list += line.split()
    for _ in word_list:
        word_count += 1
    result.write(f"Number of words: {word_count}\n")
    for current_word in word_list:
        frequency = 0
        for w in word_list:
            if current_word == w:
                frequency += 1
        result.write(f"Frequency of {current_word}: {frequency}\n")
