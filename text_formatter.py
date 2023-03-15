from http import HTTPStatus

if __name__ == '__main__':
    # with open('verbs.txt', 'r') as f:
    #     data = [line.rstrip() for line in f]
    # res = []
    # for row in data:
    #     row = row.replace(',', ' /')
    #     sep = row.find('to')
    #     if sep == -1:
    #         res.append(row)
    #     else:
    #         res.append(f"{row[sep:]} - {row[:sep]}")
    # print(res)

    # with open('res_verbs.txt', 'w') as f:
    #     for line in res:
    #         f.write(f"{line}\n")

    with open('res_verbs.txt', 'r') as f:
        data = [line.rstrip() for line in f]

    data = [row for row in data if len(row) > 5]
    res = sorted(data, key=lambda x: x.split()[1])

    with open('sorted.txt', 'w') as f:
        for line in res:
            f.write(f"{line}\n")
