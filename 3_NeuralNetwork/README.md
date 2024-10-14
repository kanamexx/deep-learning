
## シグモイド関数

シグモイド関数 $f(x)$ は

$$
\begin{align*}
f(x) &= \frac{1}{1 + \exp{(-x)}} \\
\end{align*}
$$

のように定義され、$f(x)$ の微分 $\frac{f(x)}{dx}$ は以下のように計算できる。

$$
\begin{align*}
   \frac{f(x)}{dx} &= (-1)\cdot \frac{\exp{(-x)} \cdot (-1)}{(1 + \exp{(-x)})^2} \\
                  &= \frac{\exp{(-x)}}{(1 + \exp{(-x)})^2} \\
                  &= \frac{1}{1 + \exp{(-x)}} \cdot \frac{\exp{(-x)}}{1 + \exp{(-x)}} \\
                  &= f(x) \cdot \frac{\exp{(-x)}}{1 + \exp{(-x)}} \\
                  &= f(x) \cdot \left\{ 1 - \frac{1}{1 + \exp{(-x)}} \right\} \\
                  &= f(x) \cdot ( 1 - f(x) ) \\
\end{align*}
$$

ここで、

$$
\begin{align}

   \frac{f(x)}{dx} &> 0 & ( ^\forall{x} \in \mathbb{R} )  \\
   \lim _{x \to \infty} f(x) &= 1 \\
   \lim _{x \to -\infty} f(x) &= 0 \\
   f(0) &= \frac{1}{2} \\

\end{align}
$$


### シグモイド関数とステップ関数の比較

- 相違点
  - シグモイド関数は微分可能だが、ステップ関数は微分可能でない
- 共通点
  - 定義域が任意の実数
  - 値域が $(0, 1)$

# 3.5.2


$$
\begin{align*}

   y_k &= \frac{\exp{(a_k)}}{\displaystyle\sum\limits_{i=1}^n \exp{(a_i)}}  \\
        &= \frac{C\exp{(a_k)}}{C \displaystyle\sum\limits_{i=1}^n \exp{(a_i)}}  \\
        &= \frac{\exp{(a_k + \log C)}}{\displaystyle\sum\limits_{i=1}^n \exp{(a_i + \log C)}} 
          & (\because C = e^{\log C} \Leftrightarrow \log C = log C) \\
        &= \frac{\exp{(a_k + C')}}{\displaystyle\sum\limits_{i=1}^n \exp{(a_i + C')}} 
          & (\because \log C = C') \\

\end{align*}
$$
