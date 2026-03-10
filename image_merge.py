from PIL import Image, ImageDraw, ImageFont
import os, math, string

# -----------------------------------------------------
# USER SETTINGS
# -----------------------------------------------------

image_paths = [
    "Image_1",
    "Image_2"
]

# 1 row, 2 columns (side by side)
rows = 1     
cols = 2       

label_order = "row"        # "row" or "column"
label_font_size = 40
label_offset = (40, 40)
label_color = "black"

output_png = "merged_location.png"
#output_tif = "merged_corr.tif"
output_eps = "merged_location.eps"

# -----------------------------------------------------
# LOAD BOLD FONT
# -----------------------------------------------------

BOLD_FONTS = [
    "DejaVuSans-Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
]

font = None
for f in BOLD_FONTS:
    if os.path.exists(f):
        font = ImageFont.truetype(f, label_font_size)
        break

if font is None:
    print("⚠️ Bold font not found — using default font.")
    font = ImageFont.load_default()

# -----------------------------------------------------
# LOAD IMAGES (different sizes allowed)
# -----------------------------------------------------

images = [Image.open(p) for p in image_paths]

if rows * cols < len(images):
    raise ValueError("Grid too small for number of images.")

# -----------------------------------------------------
# CALCULATE DYNAMIC CANVAS SIZE
# -----------------------------------------------------

# Compute the max width in each column and max height in each row
col_widths = [0] * cols
row_heights = [0] * rows

# Determine panel positions (row-wise or column-wise)
positions = []

if label_order.lower() == "row":
    for i in range(len(images)):
        r = i // cols
        c = i % cols
        positions.append((r, c))

elif label_order.lower() == "column":
    for i in range(len(images)):
        c = i // rows
        r = i % rows
        positions.append((r, c))

else:
    raise ValueError("label_order must be 'row' or 'column'.")

# First pass: compute necessary column widths & row heights
for img, (r, c) in zip(images, positions):
    w, h = img.size
    col_widths[c] = max(col_widths[c], w)
    row_heights[r] = max(row_heights[r], h)

# Final merged image dimensions (1 row, 2 columns)
merged_w = sum(col_widths)
merged_h = sum(row_heights)

merged = Image.new("RGB", (merged_w, merged_h), "white")
draw = ImageDraw.Draw(merged)

# -----------------------------------------------------
# PASTE IMAGES (no cropping) + LABELS
# -----------------------------------------------------

labels = list(string.ascii_lowercase)

# Track cumulative offsets for rows & columns
col_x_offsets = [sum(col_widths[:i]) for i in range(cols)]
row_y_offsets = [sum(row_heights[:i]) for i in range(rows)]

for i, (r, c) in enumerate(positions):
    img = images[i]
    x = col_x_offsets[c]
    y = row_y_offsets[r]

    merged.paste(img, (x, y))

    # Label inside panel
    lx = x + label_offset[0]
    ly = y + label_offset[1]

    draw.text((lx, ly), f"{labels[i]})", font=font, fill=label_color)

# -----------------------------------------------------
# SAVE OUTPUTS
# -----------------------------------------------------

merged.save(output_png, dpi=(350, 350))
#merged.save(output_tif, dpi=(350, 350), compression="tiff_lzw")
merged.save(output_eps, format="EPS")

print("\n✅ Created outputs:")
print(f"   {output_png}")
#print(f"   {output_tif}")
print(f"   {output_eps}")
