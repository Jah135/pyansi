from typing import Self, Optional
from .color import AnsiColor
from .codes import RESET
from .masks import *


class AnsiStyle:
    def __init__(
        self,
        *_,
        fg: Optional[AnsiColor] = None,
        bg: Optional[AnsiColor] = None,
        flags: int = 0
    ):
        self.foreground = fg
        self.background = bg
        self.flags = flags

    def __str__(self) -> str:
        if self.__is_plain():
            return ""

        output = "\x1b["
        has_written = False

        def append(text: str):
            nonlocal output
            nonlocal has_written

            if has_written:
                output += ";"

            output += text
            has_written = True

        if self.get_flag(BOLD_MASK):
            append("1")
        if self.get_flag(DIM_MASK):
            append("2")
        if self.get_flag(ITALIC_MASK):
            append("3")
        if self.get_flag(UNDERLINE_MASK):
            append("4")
        if self.get_flag(STRIKETHROUGH_MASK):
            append("9")

        if self.foreground != None:
            append(self.foreground.get_sequence(False))
        if self.background != None:
            append(self.background.get_sequence(True))

        output += "m"

        return output

    def __is_plain(self) -> bool:
        return self.foreground == None and self.background == None and self.flags == 0

    def set_flag(self, mask: int, enabled: bool) -> Self:
        if enabled:
            self.flags |= mask
        else:
            self.flags &= ~mask

        return self

    def get_flag(self, mask: int) -> bool:
        return self.flags & mask == mask

    def fg(self, color: Optional[AnsiColor]) -> Self:
        self.foreground = color
        return self

    def bg(self, color: Optional[AnsiColor]) -> Self:
        self.background = color
        return self

    def bold(self, enabled: bool = True) -> Self:
        return self.set_flag(BOLD_MASK, enabled)

    def italic(self, enabled: bool = True) -> Self:
        return self.set_flag(ITALIC_MASK, enabled)

    def dim(self, enabled: bool = True) -> Self:
        return self.set_flag(DIM_MASK, enabled)

    def underline(self, enabled: bool = True) -> Self:
        return self.set_flag(UNDERLINE_MASK, enabled)

    def strikethrough(self, enabled: bool = True) -> Self:
        return self.set_flag(STRIKETHROUGH_MASK, enabled)

    def apply(self, text: str) -> str:
        return str(self) + text

    def apply_with_reset(self, text: str) -> str:
        return self.apply(text) + RESET
