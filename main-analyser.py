file = open("output.csv", "r",  encoding="utf-8")
total = [0,0,0]
m = [0,0,0] 
f = [0,0,0]
both = [0,0,0]
first = True
for line in file:
    if first:
        first=False
        continue
    
    parsed = line.strip().split(",")
    parsed[3] = int(parsed[3])
    parsed[4] = int(parsed[4])
    
    total[0] += 1
    total[1] += parsed[3]
    total[2] += parsed[4]

    if parsed[0]=="M":
        m[0]+=1
        m[1] += parsed[3]
        m[2] += parsed[4]
    elif parsed[0]=="F":
        f[0]+=1
        f[1] += parsed[3]
        f[2] += parsed[4]
    elif parsed[0]=="Both":
        both[0]+=1
        both[1] += parsed[3]
        both[2] += parsed[4]
    else:
        raise Exception("gender invalid: {}".format(parsed[0]))

file.close()

output = "-- Overview of Data --"
headers = ["prevalence", "likes", "retweets"]
for i in range(len(headers)):
    assert (m[i]+f[i]+both[i])==total[i]

    output += "\n- {} -".format(headers[i])
    output += "\ntotal = {}".format(total[i])
    output += "\nM = {} ({}%)".format(m[i], round(100*m[i]/total[i], 1))
    output += "\nF = {} ({}%)".format(f[i], round(100*f[i]/total[i], 1))
    output += "\nBoth = {} ({}%)\n".format(both[i], round(100*both[i]/total[i], 1))

file = open("overview.txt", "w")
file.write(output)
file.close()
print(output)
