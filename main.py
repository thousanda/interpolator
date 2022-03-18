import numpy as np


def create_random(d: int) -> np.ndarray:
    #return np.random.rand(10, d)
    return np.array([
        [1, 6], [2, 7], [3, 8]
    ])


# a: 入力, n_div: 分割数
def interpolate(a: np.ndarray, n_div: int) -> np.ndarray:
    ip_array =[]  # interpolated
    for i in range(len(a)-1):
        for j in range(0, n_div):
            w1 = n_div - j  # weight
            w2 = j  # weight
            ip = (w1*a[i] + w2*a[i+1]) / n_div
            ip_array.append(ip)
    ip_array.append(a[-1])
    return np.stack(ip_array)


def main():
    a = create_random(2)
    print(a)
    ipa = interpolate(a, 3)
    print(ipa)


if __name__ == '__main__':
    main()
