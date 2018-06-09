

def save_stats(healthy, infected, dead, time):
    with open('result/result.txt', 'a', encoding="utf8") as f:
        line = str(healthy)+";"+str(infected)+";"+str(dead)+";"+str(time)+"\n"
        if line:
            f.write(line)
