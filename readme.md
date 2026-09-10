# f(2, 3)
filter

$$
g = \left[\begin{matrix}g_{0} & g_{1} & g_{2}\end{matrix}\right]
$$

data

$$
d = \left[\begin{matrix}d_{0} & d_{1} & d_{2} & d_{3}\end{matrix}\right]
$$

output

$$
y_{0} = d_{0} g_{0} + d_{1} g_{1} + d_{2} g_{2}
$$

$$
y_{1} = d_{1} g_{0} + d_{2} g_{1} + d_{3} g_{2}
$$

6 mul 4 add

# winograd
min mul = bilinear rank = 2 + 3 - 1 = 4

$$
\left[\begin{matrix}y_{0}\\\\
y_{1}\end{matrix}\right] = \left[\begin{matrix}g_{0} & g_{1} & g_{2} & 0\\\\
0 & g_{0} & g_{1} & g_{2}\end{matrix}\right] \left[\begin{matrix}d_{0}\\\\
d_{1}\\\\
d_{2}\\\\
d_{3}\end{matrix}\right]
$$

# transpose graph
$$
\left[\begin{matrix}c_{0}\\\\
c_{1}\\\\
c_{2}\\\\
c_{3}\end{matrix}\right] = \left[\begin{matrix}g_{0} & 0\\\\
g_{1} & g_{0}\\\\
g_{2} & g_{1}\\\\
0 & g_{2}\end{matrix}\right] \left[\begin{matrix}h_{0}\\\\
h_{1}\end{matrix}\right]
$$

# poly
$$
g(x) = g_{0} + g_{1} x + g_{2} x^{2}
$$

$$
h(x) = h_{0} + h_{1} x
$$

# lagrange polynomial
x = 0 1 -1 inf

$$
c(x) = c_{0} + c_{1} x + c_{2} x^{2} + c_{3} x^{3}
$$

$$
\left[\begin{matrix}c(0)\\\\
c(1)\\\\
c(-1)\\\\
c(\infty)\end{matrix}\right] = \left[\begin{matrix}1 & 0 & 0 & 0\\\\
1 & 1 & 1 & 1\\\\
1 & -1 & 1 & -1\\\\
0 & 0 & 0 & 1\end{matrix}\right] \left[\begin{matrix}c_{0}\\\\
c_{1}\\\\
c_{2}\\\\
c_{3}\end{matrix}\right]
$$

$$
c(x) = g(x)h(x)
$$

$$
\left[\begin{matrix}c(0)\\\\
c(1)\\\\
c(-1)\\\\
c(\infty)\end{matrix}\right] = \left[\begin{matrix}1 & 0 & 0\\\\
1 & 1 & 1\\\\
1 & -1 & 1\\\\
0 & 0 & 1\end{matrix}\right] \left[\begin{matrix}g_{0}\\\\
g_{1}\\\\
g_{2}\end{matrix}\right] {\odot} \left[\begin{matrix}1 & 0\\\\
1 & 1\\\\
1 & -1\\\\
0 & 1\end{matrix}\right] \left[\begin{matrix}h_{0}\\\\
h_{1}\end{matrix}\right]
$$

$$
\left[\begin{matrix}c_{0}\\\\
c_{1}\\\\
c_{2}\\\\
c_{3}\end{matrix}\right] = \left[\begin{matrix}1 & 0 & 0 & 0\\\\
0 & \frac{1}{2} & - \frac{1}{2} & -1\\\\
-1 & \frac{1}{2} & \frac{1}{2} & 0\\\\
0 & 0 & 0 & 1\end{matrix}\right] \left[\begin{matrix}1 & 0 & 0\\\\
1 & 1 & 1\\\\
1 & -1 & 1\\\\
0 & 0 & 1\end{matrix}\right] \left[\begin{matrix}g_{0}\\\\
g_{1}\\\\
g_{2}\end{matrix}\right] {\odot} \left[\begin{matrix}1 & 0\\\\
1 & 1\\\\
1 & -1\\\\
0 & 1\end{matrix}\right] \left[\begin{matrix}h_{0}\\\\
h_{1}\end{matrix}\right]
$$

$$
c = B \left[(Gg) \odot (Ah)\right]
$$

# transpose graph
$$
y = A^T \left[(Gg) \odot (B^Td)\right]
$$

$$
A^{T} = \left[\begin{matrix}1 & 1 & 1 & 0\\\\
0 & 1 & -1 & 1\end{matrix}\right]
$$

$$
G = \left[\begin{matrix}1 & 0 & 0\\\\
1 & 1 & 1\\\\
1 & -1 & 1\\\\
0 & 0 & 1\end{matrix}\right]
$$

$$
B^{T} = \left[\begin{matrix}1 & 0 & -1 & 0\\\\
0 & \frac{1}{2} & \frac{1}{2} & 0\\\\
0 & - \frac{1}{2} & \frac{1}{2} & 0\\\\
0 & -1 & 0 & 1\end{matrix}\right]
$$

move div to prefill G

$$
G = \left[\begin{matrix}1 & 0 & 0\\\\
\frac{1}{2} & \frac{1}{2} & \frac{1}{2}\\\\
\frac{1}{2} & - \frac{1}{2} & \frac{1}{2}\\\\
0 & 0 & 1\end{matrix}\right]
$$

$$
B^{T} = \left[\begin{matrix}1 & 0 & -1 & 0\\\\
0 & 1 & 1 & 0\\\\
0 & -1 & 1 & 0\\\\
0 & -1 & 0 & 1\end{matrix}\right]
$$

4 mul 8 add

