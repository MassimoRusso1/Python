import ctypes

def empty_recycle_bin():
    SHELL32 = ctypes.windll.shell32
    SHELL32.SHEmptyRecycleBinW(None, None, 1)

empty_recycle_bin()
