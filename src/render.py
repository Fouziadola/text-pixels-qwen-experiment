from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import textwrap


def get_font(size=24):
    """Load a readable font available on Windows."""
    font_paths = [
        "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/calibri.ttf",
    ]

    for path in font_paths:
        if Path(path).exists():
            return ImageFont.truetype(path, size)

    return ImageFont.load_default()


def render_text(text, output_path):
    """
    Convert a text document into a PNG image.

    The image height is calculated from the amount of text,
    so the document is not intentionally truncated.
    """

    width = 1600
    margin = 60
    font_size = 28
    line_spacing = 12

    font = get_font(font_size)

    # Approximate characters that fit on one line.
    characters_per_line = 90

    lines = []

    for paragraph in text.splitlines():
        if not paragraph.strip():
            lines.append("")
            continue

        wrapped = textwrap.wrap(
            paragraph,
            width=characters_per_line,
            break_long_words=False,
            break_on_hyphens=False,
        )

        lines.extend(wrapped)

    if not lines:
        lines = [""]

    line_height = font_size + line_spacing
    height = (len(lines) * line_height) + (2 * margin)

    image = Image.new(
        "RGB",
        (width, height),
        "white"
    )

    draw = ImageDraw.Draw(image)

    y = margin

    for line in lines:
        draw.text(
            (margin, y),
            line,
            fill="black",
            font=font
        )

        y += line_height

    output_path = Path(output_path)
    output_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    image.save(output_path)

    return output_path
  
if __name__ == "__main__":
    sample_text = """
This is a test document.

SkyByte allows users to enhance drones with different add-on modules.

The purpose of this test is to make sure that our text-to-image
renderer works correctly and produces a readable PNG image.
"""

    output = render_text(
        sample_text,
        "results/test_render.png"
    )

    print(f"Image saved to: {output}")