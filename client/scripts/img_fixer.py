import os
from .const import CYNDAQUILL_PATH

# animations = set()

# # get individual names for animations
# for img in os.listdir(PATH):
#     string = img.split('.')[0]
#     for char in string:
#         if char.isdigit():
#             string = string.replace(char, '')
#     if string[-2] == '-f':
#         string = string.replace(char, '')
        
#     if string not in animations:
#         animations.add(string)
            
# print(animations)

# convert names into numbers (excluding idle and walk)
# for folder in os.listdir(CYNDAQUILL_PATH):
#     if folder not in ['idle', 'walk']:
#         for file in os.listdir(CYNDAQUILL_PATH + '/' + folder):
#             num = file.split(folder)[-1].split('.')[0]
#             src = os.path.join(CYNDAQUILL_PATH, folder, file)
#             dst = os.path.join(CYNDAQUILL_PATH, folder, f'{str(int(num) -1)}.png')
#             print(src, dst)
#             os.rename(src, dst)



