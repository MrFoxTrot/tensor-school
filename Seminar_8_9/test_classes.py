from classes import Student
from main import math_quadratic_equation


class TestStudent:
    std1 = Student("Tester_1", 108)
    std1_copy = Student("Tester_1_Copy", 108)
    std2 = Student("Tester_2", 52)

    def test_std1_eq_std1_copy(self):
        assert self.std1 == self.std1_copy

    def test_std1_neq_std2(self):
        assert self.std1 != self.std2

    def test_std1_gt_std2(self):
        assert self.std1 > self.std2

    def test_std2_lt_std1(self):
        assert self.std2 < self.std1

    def test_std1_ge_std2(self):
        assert self.std1 >= self.std2

    def test_std1_le_std1_copy(self):
        assert self.std1 <= self.std1_copy


class TestMathQuadraticEquation:
    def test_equation_d_gt_0(self):
        assert math_quadratic_equation(2, 3, 1) == (-0.5, -1)

    def test_equation_d_eq_0(self):
        assert math_quadratic_equation(9, 6, 1) == (-0.3333333333333333, None)

    def test_equation_d_lt_0(self):
        assert math_quadratic_equation(
            2, 4, 7) == (-1+1.5811388300841898j, -1-1.5811388300841898j)
