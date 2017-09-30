import slippery.decorators


@slippery.decorators.prettify()
def generator(maximum=100):
    if True:
        pass

    result = [
        k for k in [
            i for i in range(maximum)
        ]
    ]

    return result


if __name__ == '__main__':
    generator(maximum=1000)
