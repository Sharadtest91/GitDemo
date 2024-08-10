itemincart = 0
if itemincart != 2:
    #raise Exception("item not found")
    pass

assert (itemincart == 0)

try:
    with open('text', 'r') as reader:
        reader.read()

except Exception as e:
    print(e)

finally:
    print("automation done")


