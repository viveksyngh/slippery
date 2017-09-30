import slippery


@slippery.execution_time()
def generator(no=True, maximum=100, registry=None):
    if True:
        pass

    if not registry:
        pass

    result = [
        k for k in [
            i for i in range(maximum)
        ]
    ]

    return result


if __name__ == '__main__':
    generator(True, 50, [1, 2, 3])
