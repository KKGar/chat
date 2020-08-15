def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f: 
        for line in f:
            lines.append(line.strip())
    return lines


def convert(lines):
    person = None
    Gary_word_count = 0
    Iris_word_count = 0
    Gary_sticker_count = 0
    Iris_sticker_count = 0
    Gary_image_count = 0
    Iris_image_count = 0
    for line in lines:
        s = line.split(' ')
        time = s[0]
        name = s[1]
        if name == '郭小郭。':
            if s[2] == '貼圖':
                Gary_sticker_count += 1
            elif s[2] == '圖片':
                Gary_image_count += 1
            else:
                for m in s[2:]:
                    Gary_word_count += len(m)
        elif name == 'Babe':
            if s[2] == '貼圖':
                Iris_sticker_count += 1
            elif s[2] == '圖片':
                Iris_image_count += 1
            else:
                for m in s[2:]:
                    Iris_word_count += len(m)
    print('Gary said', Gary_word_count, 'word(s)')
    print('Gary sent', Gary_sticker_count, 'sticker(s)')
    print('Gary sent', Gary_image_count, 'image(s)')
    print('Iris said', Iris_word_count, 'word(s)')
    print('Iris sent', Iris_sticker_count, 'sticker(s)')
    print('Iris sent', Iris_image_count, 'image(s)')


def write_file(filename, lines):
    with open(filename, 'w') as f:
    	for line in lines:
    		f.write(line + '\n')


def main():
    lines = read_file('[LINE]Babe.txt')
    lines = convert(lines)
    # write_file('output.txt', lines)
    

main()

