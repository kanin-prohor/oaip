colors = {
    "красный": (255, 0, 0),
    "зеленый": (0, 255, 0),
    "синий": (0, 0, 255),
    "желтый": (255, 255, 0),
    "белый": (255, 255, 255),
    "черный": (0, 0, 0)
}

red = colors["красный"]
blue = colors["синий"]
purple = tuple((r + b) // 2 for r, b in zip(red, blue))
print(f"Смесь красного и синего: {purple}")

inverted_red = tuple(255 - c for c in red)
print(f"Инвертированный красный: {inverted_red}")