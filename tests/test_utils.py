import pytest

from slippery import utils


@pytest.mark.parametrize(
    'seq, shortened, max_len', [
        (
            (1, 2, 3, 4, 5, 6),
            '(1, 2, 3, ...)',
            3,
        ),
        (
            [1, 2, 3, 4, 5, 6],
            '[1, 2, 3, 4, ...]',
            4,
        ),
    ],
)
def test_shortened(seq, shortened, max_len):
    result = utils.shortened(seq, max_len)
    assert isinstance(result, str)
    assert result == shortened


@pytest.mark.parametrize(
    'args, repr_args', [
        (
            [True, [], .53, 3.14],
            'True, [], 0.53, 3.14',
        ),
    ],
)
@pytest.mark.parametrize(
    'kwargs, repr_kwargs', [
        (
            {'one': 1, 'two': 2},
            [
                'two=2, one=1',
                'one=1, two=2',
            ],
        ),
    ],
)
def test_represent_params(args, repr_args, kwargs, repr_kwargs):
    args, kwargs = utils.represent_params(args, kwargs)

    assert utils.escape_ansi(args) == repr_args
    assert utils.escape_ansi(kwargs) in repr_kwargs
