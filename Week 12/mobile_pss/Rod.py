from typing import Union

from Ball import Ball


class Rod:
    __slots__ = "name", "cord_length", "left_arm", "left_child", "right_arm", "right_child"

    def __init__(self, name, cord_length,
                 left_arm: int, left_child: Union["Rod", Ball],
                 right_arm: int, right_child: Union["Rod", Ball]):
        self.name = name
        self.cord_length = cord_length
        self.left_arm = left_arm
        self.left_child = left_child
        self.right_arm = right_arm
        self.right_child = right_child

    def __str__(self):
        return f"{self.name}"

    def get_weight(self):
        return self.right_child.get_weight() + self.right_child.get_weight()

    def is_balanced(self):
        left_T = self.left_arm * self.left_child.get_weight()
        right_T = self.right_arm * self.right_child.get_weight()
        return left_T == right_T

    def width(self):
        pass
