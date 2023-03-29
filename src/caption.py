file_path = './data/베드로성당.txt'
file = open(file_path, "r", encoding='UTF8')
data = file.read()
captions = list(data.split('\n'))

[captions.remove('V3, 1') for caption in captions if caption == 'V3, 1']

for i in range(len(captions)):
    caption = captions[i]
    if caption.startswith("00;"):
        start_time, end_time = caption.split(' - ')
        start_time = start_time.replace(';', ':')
        start_time_seconds = sum(x * int(t) for x, t in zip([3600, 60, 1, 1 / 30], start_time[-2]))
        start_time_str = start_time[:-3] + '.' + str(round(start_time_seconds, 3))

        end_time = end_time.replace(';', ':')
        end_time_seconds = sum(x * int(t) for x, t in zip([3600, 60, 1, 1 / 30], end_time[-2]))
        end_time_str = end_time[:-3] + '.' + str(round(end_time_seconds, 3))

        temp = f'{start_time_str} --> {end_time_str}'
        captions[i] = temp

[captions.insert(i*4, f'{i+1}') for i in range(len(captions)//3)]

print(captions)

with open(file_path[-4] + '.str', "w", encoding='UTF8') as f:
    [f.write(f'{caption}\n') for caption in captions]