from sys import argv


def findSubsequence(arr):
    if len(arr) == 0:
        return None

    isint = map(lambda x: isinstance(x, int), arr)
    if sum(isint) != len(arr):
        return None

    max = arr[0]
    current = arr[0]

    for i in xrange(1, len(arr)):
        current = current + arr[i]
        if current > max:
            max = current
    return max


def main(arr):
    print findSubsequence(arr)


if __name__ == '__main__':
    arr = [int(arg) for arg in argv[1:]]
    main(arr)