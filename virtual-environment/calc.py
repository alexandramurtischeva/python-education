"""This module has a class named Calculator encompasses basic arithmetic operations"""
from typing import Union


class Calculator:
    """This class realizes basic arithmetic operations"""

    def __init__(self, operand_1: Union[int, float], operand_2: Union[int, float]) -> None:
        """
        Initiates parameters:
            operand_1 (int | float): first number taking part in calculations
            operand_2 (int | float): second number taking part in calculations
        """
        self.operand_1 = operand_1
        self.operand_2 = operand_2

    def add(self):
        """
        Performs addition with 2 operands
        Returns:
            Calculator: result of addiction
        """

        return self.operand_1 + self.operand_2

    def subtract(self):
        """
        Performs subtraction with 2 operands
        Returns:
            Calculator: result of subtraction
        """

        return self.operand_1 - self.operand_2

    def multiply(self):
        """
        Performs multiplication with 2 operands
        Returns:
            Calculator: result of multiplication
        """

        return self.operand_1 * self.operand_2

    def divide(self):
        """
        Performs division with 2 operands
        Returns:
            Calculator: result of division
        """

        return self.operand_1 / self.operand_2
