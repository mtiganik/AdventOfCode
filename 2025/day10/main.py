from sympy import symbols, Eq, solve, Integer




f = open("input.txt")
btnWiring = []


def p2Res(btns, jolts ):
    n = len(btns)
    vars = symbols(" ".join(f"f{k}" for k in range(n)))
    eqs = []
    for i in range(len(jolts)):
        terms = []
        for k,b in enumerate(btns):
            if i in b:
                terms.append(vars[k])
        eqs.append(Eq(sum(terms), jolts[i]))
    sol_list = solve(eqs, vars, dict=True)
    if not sol_list:
        raise Exception("No solution!")

    sol = sol_list[0]

    # If fully numeric: verify positivity and return result
    if all(isinstance(sol[v], (int, Integer)) for v in vars):
        if any(sol[v] <= 0 for v in vars):
            raise Exception("Solution has non-positive values.")
        return sum(sol[v] for v in vars), sol

    # ---- Parametric case: solve integer optimization ----
    # Free variables = variables missing from solution dict
    free_vars = [v for v in vars if sol[v].free_symbols]
    
    # Define bounds for free variables
    # Start small: 1..10 (expand if needed)
    BOUND = 10

    best_sum = None
    best_assign = None

    def evaluate_solution(assign):
        """Given values for free vars, compute full solution numeric dict."""
        numeric_sol = {}
        for v in vars:
            expr = sol[v]
            # substitute free var assignments
            val = expr.subs(assign)
            # must resolve to number
            if not val.is_number:
                return None
            val = int(val)
            if val <= 0:  # must be positive integer
                return None
            numeric_sol[v] = val
        return numeric_sol

    # Brute-force search over free variables within BOUND
    # Usually free_vars is small (1–3)
    from itertools import product
    for values in product(range(1, BOUND + 1), repeat=len(free_vars)):
        assign = dict(zip(free_vars, values))
        numeric_sol = evaluate_solution(assign)
        if numeric_sol is None:
            continue  # invalid candidate

        S = sum(numeric_sol[v] for v in vars)
        if best_sum is None or S < best_sum:
            best_sum = S
            best_assign = numeric_sol

    if best_assign is None:
        raise Exception("No positive integer solution within bounds.")

    return best_sum, best_assign
        


cnt = 0
for x in f:
    btnWiring,jolts = x.split(" {")
    
    btnWiring = btnWiring.split("]")[1]
    btnWiring = btnWiring.strip().split(" ")
    jolts = jolts.strip().replace("}","")
    jolts = jolts.split(",")
    btns = []
    for k in btnWiring:
        res = []
        k = k.replace("(", "")
        k = k.replace(")","")

        k = k.split(",")
        for i in k:
            res.append(int(i))
        btns.append(res)
    joltsRes = []
    for i in range(len(jolts)):
        joltsRes.append(int(jolts[i]))
    total, solution = p2Res(btns, joltsRes)
    print("Solution:", solution)
    print("Sum of variables:", total)
print(cnt)