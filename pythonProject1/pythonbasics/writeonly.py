with open('text', 'r') as reader:
    content = reader.readlines()
    reversed(content)
    with open('text', 'w') as writer:
        for line in reversed(content):
            writer.write(line)

