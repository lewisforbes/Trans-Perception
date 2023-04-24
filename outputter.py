def output(ts, init):
    headers = []
    for h in dir(ts[0]):
        if "__" in h:
            continue
        if h=="gen_user" or h=="about_who":
            continue
        headers.append(h)
    output = ""
    if init:
        output += str(headers)[1:-1].replace("\'", "") + "\n"
    for t in ts:
        line = ""
        for a in headers:
            line += str(getattr(t, a)).replace(",", "[[COMMMA]]") + ","
        line = line[:-1] + "\n"
        output += line
    
    f = open("raw_results.csv", "a", encoding="utf-8")
    f.write(output)
    f.close()