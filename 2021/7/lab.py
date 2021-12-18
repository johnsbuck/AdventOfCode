import matplotlib.pyplot as plt


def score(x, data):
    output = 0
    for num in data:
        diff = abs(num - x)
        output += (diff * diff + diff) / 2
    return output


def main():
    data = [0, 10, 200, 1000]
    X = []
    y = []
    for x in range(min(data), max(data) + 1):
        y.append(score(x, data))
        X.append(x)

    avg = sum(data) / len(data)

    plt.plot(X, y)
    plt.scatter([avg], min(y))
    plt.show()


if __name__ == "__main__":
    main()
