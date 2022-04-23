import wikipedia
import numpy as np
n = 16*2
result = wikipedia.search("Neural Networks")
Global_Count = 0
for keyword in result:
    temp = wikipedia.summary(keyword)
    split_string = [temp[i:i + n] for i in range(0, len(temp), n)]
    final_split_string = split_string[:len(split_string) - 1]
    Array = np.array(final_split_string)
    for content in Array:
        filename = "plain-" + str(Global_Count) + ".txt"
        Global_Count = Global_Count + 1
        file = open(filename, "w+")
        file.write(content)
        file.close()



