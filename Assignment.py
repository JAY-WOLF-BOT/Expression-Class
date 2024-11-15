class ExpressionSolver:
    def __init__(self, expression):
        self.expression = expression

    def solve(self):
        try:
            result = eval(self.expression)
            return result
        except Exception as e:
            return f"Error in evaluating expression: {e}"

if __name__ == "__main__":
    user_input = input("Enter a mathematical expression to solve: ")
    solver = ExpressionSolver(user_input)
    result = solver.solve()
    print(f"The result of the expression is: {result}")