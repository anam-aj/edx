import textwrap
from termcolor import colored

# Wrap your text
wrapped_text = textwrap.fill("Haaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa !", width=20)
print(wrapped_text)

# Split the wrapped text into lines
lines = wrapped_text.split('\n')

# Create the top border
top_border = "+" + "-" * 22 + "+"

# Create the bottom border
bottom_border = top_border

# Add side borders to each line
boxed_text = [top_border]
for line in lines:
    boxed_text.append("| " + line.ljust(20) + " |")
boxed_text.append(bottom_border)

# Join the boxed text into a single string
boxed_text = "\n".join(boxed_text)

# Colorize your text
colored_text = colored(boxed_text, "red")

return colored_text)
