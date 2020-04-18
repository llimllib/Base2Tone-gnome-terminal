import re

# map the colors in base16 (keys) to base2tone (values)
base16_base2tone_map = {
    "00": "A0",
    "01": "A1",
    "02": "A2",
    "03": "A3",
    "04": "A4",
    # 05 maps to A6 for Bold Color, but D0 for Cursor Color. Not sure which to
    # use here.
    "05": "A6",
    "06": "B6",
    "07": "B7",
    "08": "B2",
    "09": "D5",
    "0A": "D7",
    "0B": "D4",
    "0C": "B4",
    "0D": "B3",
    "0E": "D4",
    "0F": "D3",
}


def fix_refs(template):
    return re.sub(
        r'(base\[")(..)',
        lambda x: x.group(1) + base16_base2tone_map[x.group(2)],
        template,
    )


# now we need to replace the base16 colors with our base2tone ones
dark = open("templates/dark.ejs").read()
light = open("templates/light.ejs").read()
darkfixed = fix_refs(dark)
lightfixed = fix_refs(light)

open("templates/dark_2tone.ejs", "w").write(darkfixed)
open("templates/light_2tone.ejs", "w").write(lightfixed)
