from .codes import *
from .color import AnsiColor
from re import compile

ANSI_ESCAPE = compile("\x1b(?:[@-Z\\-_]|\\[[0-?]*[ -/]*[@-~])")


def remove_ansi(text: str) -> str:
    return ANSI_ESCAPE.sub("", text)


def apply_flag(text: str, flag: str) -> str:
    return f"\x1b[{flag}m{text}{RESET}"


def bold(text: str) -> str:
    return apply_flag(text, BOLD)


def dim(text: str) -> str:
    return apply_flag(text, DIM)


def italic(text: str) -> str:
    return apply_flag(text, ITALIC)


def underline(text: str) -> str:
    return apply_flag(text, UNDERLINE)


def strikethrough(text: str) -> str:
    return apply_flag(text, STRIKETHROUGH)


def tint(text: str, color: AnsiColor, bg: bool = False):
    return f"\x1b[{color.get_sequence(bg)}m{text}{RESET}"
