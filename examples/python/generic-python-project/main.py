import emoji


def print_zen(author: str) -> None:
    """Prints the Zen of Python

    You can read more here:
    https://www.python.org/doc/humor/#the-zen-of-python

    Args:
        author (str): Author name
    """
    zen = f"""
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than right now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
— {author}
"""
    print(zen)


def run() -> None:
    """Runs the application"""

    print_zen("Tim Peters")

    print(emoji.emojize("Right? :thumbs_up:"))


if __name__ == "__main__":
    run()
