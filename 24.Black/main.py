import logging


def foo():
    print("foo")  # print it


a = [1, 2, 3, 4, 5, 6, 7]

b = {
    "first": 100,
    "second": 50,
    "third": 25,
    "fourth": 15,
    "fifth": 10,
    "sixth": 5,
    "seventh": 5,
    "eighth": 2,
}


def my_cool_function(
    input_size,
    output_size,
    num_classes=2,
    num_feature=5,
    print_output=True,
    include_log=False,
):
    if print_output:
        print(input_size, output_size, num_classes, num_feature)


"""
# Version control integration with black #.pre-commit-config.yaml
repos:
  - repo: https://github.com/psf/black
    rev: stable  # or pin to specific version like "24.3.0"
    hooks:
      - id: black
        language_version: python3

"""
