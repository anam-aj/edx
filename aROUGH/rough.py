def wrap_text(text, color):
    """Colorize and Decorate text in a Box"""

    # Wrap text
    wrapped_text = textwrap.fill(text, width=20)

    # Split the wrapped text into lines
    lines = wrapped_text.split("\n")

    # Create the top border
    top_border = "+" + "-" * 22 + "+"

    # Create the bottom border
    bottom_border = top_border

    # Add side borders to each line
    boxed_text = [top_border]
    for line in lines:
        boxed_text.append("| " + line.center(20) + " |")
    boxed_text.append(bottom_border)

    # Join the boxed text into a single string
    boxed_text = "\n".join(boxed_text)

    # Colorize text
    colored_text = colored(boxed_text, color)

    return colored_text


text = "This is a test text to be wrapped and colorized."
color = "red"

result = wrap_text(text, color)


