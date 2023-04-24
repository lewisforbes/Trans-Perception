file = open("output.csv", "r")
total = 0
m = 0 
f = 0
both = 0
none = 0
first = True
for line in file:
    if first:
        first=False
        continue
    
    total +=1
    gender = line.strip().split(",")[0]
    if gender=="M":
        m+=1
    elif gender=="F":
        f+=1
    elif gender=="Both":
        both+=1
    elif gender=="None":
        none+=1
    else:
        raise Exception("gender invalid: {}".format(gender))

file.close()

output = "-- Overview of Data --"
output += "\ntotal = {}".format(total)
output += "\nM = {} ({}%)".format(m, round(100*m/total, 1))
output += "\nF = {} ({}%)".format(f, round(100*f/total, 1))
output += "\nBoth = {} ({}%)".format(both, round(100*both/total, 1))
output += "\nNone = {} ({}%)".format(none, round(100*none/total, 1))
assert (m+f+both+none)==total
file = open("overview.txt", "w")
file.write(output)
file.close()
print(output)
