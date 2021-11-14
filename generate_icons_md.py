import os
from collections import defaultdict

with open("icons.md", "w") as icons_md:
    icons_md.write("<!-- This file is generated using generate_icons_md.py -->\n")
    icons_md.write("# Icons\n")
    icons_md.write("\n")
    icons_md.write("|Name|Icon|\n")
    icons_md.write("|---|---|\n")

    for asset_dir in sorted(os.listdir("assets")):
        if asset_dir == ".DS_Store":
            continue

        largest_svg_icon_path_by_weight = {}

        weights = set()

        svg_dir = os.path.join("assets", asset_dir, "SVG")
        for filename in sorted(os.listdir(svg_dir)):
            weight = filename.split("_")[-1].replace(".svg", "")
            weights.add(weight)
            largest_svg_icon_path_by_weight[weight] = filename

        for weight in sorted(weights, reverse=True):
            icons_md.write(
                f"|{asset_dir} ({weight.title()})"
                f'|<img src="{svg_dir}/{largest_svg_icon_path_by_weight[weight]}?raw=true" width="24" height="24">'
                f'|\n'
            )
