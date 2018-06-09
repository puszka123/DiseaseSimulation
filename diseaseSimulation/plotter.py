import matplotlib.pyplot as plt
import datetime
import matplotlib


def main():
    healthy = list()
    infected = list()
    dead = list()
    time = list()
    with open('result/result.txt', 'r', encoding="utf8") as f:
        content = f.readlines()
        for line in content:
            data = line.split(';')
            healthy.append(int(data[0]))
            infected.append(int(data[1]))
            dead.append(int(data[2]))
            time.append(datetime.timedelta(seconds=int(data[3])).total_seconds()/60)

    fig, ax = plt.subplots()
    ax.set_color_cycle(['red', 'blue', 'black'])
    plt.plot(time, infected, label="zainfekowani")
    plt.plot(time, healthy, label="zdrowi")
    plt.plot(time, dead, label="zmarli")
    plt.legend(loc='best')
    plt.gcf().autofmt_xdate()
    plt.show()


main()
