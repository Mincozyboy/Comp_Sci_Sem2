# sentence = "whale hello there. Don't we all love whales? I absolutely love whales! whales are so huge!!!"
# for i in range(0, len(sentence)):
#     y=sentence[i:i+5]
#     if y == 'whale':
#         print("Found a Whale!")
      


count = 0 
with open('moby.txt') as f:
    for line in f:
        sentence = line.strip()
        for i in range(0, len(sentence)):
            if sentence[i:i+5].lower() == "whale":
                count = count + 1
                print("Found a Whale!")
                # print(str(i) + ":" + str(i+5))
print("The word Whale is said " + str(count) + " times.")

f.close()
