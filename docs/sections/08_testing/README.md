# Testing

It is up to each project if a Test Driven Development approach is taken.

Have a look at this [cookiecutter project](https://cookiecutter-cruft-poetry-tox-pre-commit-ci-cd.readthedocs.io/en/latest/)

## Testing Frameworks
- use `pytest` as an easy to use testing framework in python

Consider using testing helpers. Learn more about [mutation testing here](https://hackernoon.com/mutmut-a-python-mutation-testing-system-9b9639356c78)

- you can use [mutmut](https://github.com/boxed/mutmut) for mutation testing

- look at [Hypothesis](https://github.com/HypothesisWorks/hypothesis) to do [property-based testing](https://www.mayhem.security/blog/what-is-property-based-testing#:~:text=While%20unit%20tests%20check%20that,defines%20correctness%20(and%20safety).)

- for benchmarking you can use [pytest-benchmark](https://cookiecutter-cruft-poetry-tox-pre-commit-ci-cd.readthedocs.io/en/latest/)

## Code Coverage
- strive for 100% coverage, 90% must be considered minimum
  - use [coverage.py](https://coverage.readthedocs.io/en/7.4.4/#) to track this

- prioritise critical paths to test

- use [fixtures](/examples/python/pytest/fixtures.py) for setup and teardown

- CI must call all tests and all tests must pass

- refactor tests just as you refactor code