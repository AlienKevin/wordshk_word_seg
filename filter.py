with open("jyutping_sentences.txt", "r") as f, open("sentences.txt", "w+") as output:
    lines = [line for line in f.readlines() if len(line.strip()) > 0]
    for i in range(0, len(lines), 2):
        yue = lines[i].strip()
        if len(yue) < 10 or " " in yue or "/" in yue:
            continue
        else:
            output.write(yue + "\n")
