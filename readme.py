import sympy as sp


def print_md(lhs, *rhs):
    if not rhs:
        eq = sp.latex(lhs)
    else:
        eq = f"{sp.latex(lhs)} = " + " ".join(sp.latex(m) for m in rhs)
    eq = eq.replace("\\\\", "\\\\\\\\\n")
    eq = eq.replace("\n- ", "\n-")
    print("$$")
    print(eq)
    print("$$\n")


def main():
    print("# f(2, 3)")
    print("filter\n")
    g = sp.symbols("g0:3")
    print_md(sp.Symbol("g"), sp.Matrix(g).T)

    print("data\n")
    d = sp.symbols("d0:4")
    print_md(sp.Symbol("d"), sp.Matrix(d).T)

    print("output\n")
    y = sp.symbols("y0:2")
    c = sp.symbols("c0:4")
    g_mat = sp.Matrix([[g[0], g[1], g[2], 0], [0, g[0], g[1], g[2]]])
    y_mat = g_mat * sp.Matrix(d)
    print_md(sp.Symbol("y_0"), y_mat[0])
    print_md(sp.Symbol("y_1"), y_mat[1])
    print("6 mul 4 add\n")

    print("# winograd")
    print("min mul = bilinear rank = 2 + 3 - 1 = 4\n")
    print_md(sp.Matrix(y), g_mat, sp.Matrix(d))

    print("# transpose graph")
    print_md(sp.Matrix(c), g_mat.T, sp.Matrix(sp.symbols("h0:2")))

    print("# poly")
    x = sp.Symbol("x")
    g_poly = g[0] + g[1] * x + g[2] * x**2
    print_md(sp.Symbol("g(x)"), g_poly)
    h = sp.symbols("h0:2")
    h_poly = h[0] + h[1] * x
    print_md(sp.Symbol("h(x)"), h_poly)

    print("# lagrange polynomial")
    print("x = 0 1 -1 inf\n")
    c_poly = c[0] + c[1] * x + c[2] * x**2 + c[3] * x**3
    print_md(sp.Symbol("c(x)"), c_poly)
    C_mat = sp.Matrix(
        [
            [1, 0, 0, 0],
            [1, 1, 1, 1],
            [1, -1, 1, -1],
            [0, 0, 0, 1],
        ]
    )
    eval_mat = sp.Matrix(
        [
            sp.Symbol("c(0)"),
            sp.Symbol("c(1)"),
            sp.Symbol("c(-1)"),
            sp.Symbol(r"c(\infty)"),
        ]
    )
    print_md(eval_mat, C_mat, sp.Matrix(c))

    print_md(sp.Symbol("c(x) = g(x)h(x)"))
    G_mat = sp.Matrix([[1, 0, 0], [1, 1, 1], [1, -1, 1], [0, 0, 1]])
    H_mat = sp.Matrix([[1, 0], [1, 1], [1, -1], [0, 1]])
    print_md(
        eval_mat,
        sp.MatMul(G_mat, sp.Matrix(g)),
        sp.Symbol(r"{\odot}"),
        sp.MatMul(H_mat, sp.Matrix(h)),
    )
    print_md(
        sp.Matrix(c),
        C_mat.inv(),
        sp.MatMul(G_mat, sp.Matrix(g)),
        sp.Symbol(r"{\odot}"),
        sp.MatMul(H_mat, sp.Matrix(h)),
    )
    print("$$\n" + r"c = B \left[(Gg) \odot (Ah)\right]" + "\n$$\n")

    print("# transpose graph")
    print("$$\n" + r"y = A^T \left[(Gg) \odot (B^Td)\right]" + "\n$$\n")
    print_md(sp.Symbol("A^T"), H_mat.T)
    print_md(sp.Symbol("G"), G_mat)
    print_md(sp.Symbol("B^T"), C_mat.inv().T)

    print("move div to prefill G\n")
    print_md(
        sp.Symbol("G"), sp.diag(1, sp.Rational(1, 2), sp.Rational(1, 2), 1) * G_mat
    )
    print_md(sp.Symbol("B^T"), sp.diag(1, 2, 2, 1) * C_mat.inv().T)
    print("4 mul 8 add\n")


if __name__ == "__main__":
    main()
