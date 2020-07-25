import os
audio = os.path.join(os.getcwd(), 'audio')
overall_count = 0
for folder in os.listdir(audio):
    count = 0
    for file in os.listdir(os.path.join(audio,folder)):
        #print(folder, file)
        count+=1
        overall_count +=1
    print(folder, ":", count)
print("total no of audio/frames pairs or videos is:",overall_count)
