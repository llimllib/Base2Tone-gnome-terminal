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


# translate base16 colors to base2tone
def fix_refs(template):
    return re.sub(
        r'(base\[")(..)',
        lambda x: x.group(1) + base16_base2tone_map[x.group(2)],
        template,
    )


# for some unknown reason, base16-builder is not replacing the comment at the
# head of the files, which makes them invalid bash scripts
def remove_head_comment(template):
    return re.sub(r"{#.*#}", "", template, flags=re.S)

def main():
    # now we need to replace the base16 colors with our base2tone ones
    dark = open("templates/dark.ejs").read()
    light = open("templates/light.ejs").read()
    darkfixed = remove_head_comment(fix_refs(dark))
    lightfixed = remove_head_comment(fix_refs(light))

    open("templates/dark_2tone.ejs", "w").write(darkfixed)
    open("templates/light_2tone.ejs", "w").write(lightfixed)

if __name__=="__main__":
    main()
