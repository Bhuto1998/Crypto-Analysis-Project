import wikipedia
import numpy as np
n = 16*64
result = wikipedia.search("Neural Networks")
Global_Count = 0
for keyword in result:
    page = wikipedia.page(keyword)
    temp = page.content
    split_string = [temp[i:i + n] for i in range(0, len(temp), n)]
    final_split_string = split_string[:len(split_string) - 1]
    Array = np.array(final_split_string)
    for content in Array:
        filename = "plainLarge-" + str(Global_Count) + ".txt"
        Global_Count = Global_Count + 1
        file = open(filename, "w+")
        file.write(content)
        file.close()