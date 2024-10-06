
## XOR

入力 x1, x2 のどちらか片方のみが 1 のときに 出力 y が 1 となる演算子。

| 入力A | 入力B | 出力 |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

### AND, NAND, OR で表す。

XOR は AND, NAND, OR で表すことができる。

$$
\begin{align*}
x1 \oplus x2 &\Leftrightarrow
                (x1 \land \overline{x2})
                \lor (\overline{x1} \land x2) \\
             &\Leftrightarrow
                1
                \land (x1 \lor x2)
                \land (\overline{x1} \lor \overline{x2})
                \land 1 \\
             &\Leftrightarrow
                (x1 \lor x2)
                \land (\overline{x1} \lor \overline{x2}) \\
             &\Leftrightarrow
                (x1 \lor x2)
                \land \overline{(x1 \land x2)} \\
\end{align*}

$$