import re
extension = "h"

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames 
# using as many lines of code as your chosen method requires.
newfilenames = []
finalfilenames = []
for v in filenames:
    data = re.findall(r"[\w]+\.", v)
    newfilenames.append(data)
    
for x in newfilenames:
    print(str(x[0]) + extension)
    finalfilenames.append(str(x[0] + extension))
    
print(finalfilenames)