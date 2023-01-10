# "borrowed" from gigalegit#0880 (352062534469156864) from the pycord discord

def progress_bar(percent: int) -> str:
    bar = ""

    for _ in range(round(max(min(percent, 100), 0) / 10)):
        bar += "🟨"

    return bar.ljust(10, "⬛")
