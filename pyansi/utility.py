from .codes import *

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
