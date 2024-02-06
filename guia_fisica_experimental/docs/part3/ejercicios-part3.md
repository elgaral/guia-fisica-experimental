---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.0
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

(sec-ejerciciosV1P3)=
# Ejercicios

**Graficación**

**1**. Con base en los datos de temperatura tomados cada cinco minutos a partir de las 11:40 a. m., realice un gráfico de la temperatura en función del tiempo. Según el fabricante la resolución e incertidumbre del equipo es de $0.01 \,\text{°C}$ y $0.3 \,\text{°C}$, respectivamente. Los datos de temperatura son (en °C): 28.25, 28.04, 28.31, 28.73, 28.75, 28.74, 28.55, 28.34, 28.45, 28.39, 28.81, 29.16, 29.31, 29.17, 29.25, 29.35, 29.29, 29.2, 29.16, 29.26. Realice una gráfica de la temperatura en función del tiempo; no olvide incluir la incertidumbre.

**Linearización**

**2**. Sea $y$ la variable dependiente y $x$ la variable independiente, realice las transformaciones necesarias para linearizar las siguientes funciones: **(a)** $y = a(x+b)^3$, **(b)** $y = ae^{-bx} + c$.

**3**. Ahora considere que los parámetros $a$, $b$ o $c$ del punto anterior son desconocidos, y que por lo tanto no pueden quedar en la parte izquierda de la igualdad para poder realizar la gráfica. Verifique si las soluciones que dió para las funciones en el punto anterior funcionan, si debe modificarlas o si no resulta posible linearizar la función.

**Ajuste lineal**

**4**. Usando los datos del problema 1., realice un ajuste lineal así: **(a)** Grafique los datos y la función lineal encontrada, ¿Visualmente puede decir que los datos se ajustan a una curva lineal? (tenga en cuenta que dadas las funciones los puntos deben estar distribuidos aleatoriamente alrededor de la curva). **(b)** A partir del ajuste  lineal ¿cuál es la razón de cambio de la temperatura en el tiempo? (incluya la incertidumbre) **(c)** Determine la incertidumbre común y verifique si es similar a la incertidumbre reportada por el fabricante.

**5**. Usted está verificando la relación entre la irradiancia de un láser y el tamaño del spot láser enfocado. La teoría dice que la relación es

$$ I_0 = \frac{2P_0}{\pi w_0^2}$$

donde $I_0$ es la irradiancia, $P_0$ es la potencia del láser y $w_0$ es el radio del spot enfocado. Se estima que la incertidumbre en la irradiancia es de $0.2 \, \text{W/mm}^2$. Los resultados de la medición fueron:
| $w_0$/$\mu$m | 30 | 40 | 50 | 60 | 70 | 80 | 90 |
| :--- | ---| --- | --- | --- | --- | --- | ---: |
| $I_0$/(W/mm$^2$) | 5.0 | 1.8 | 1.3 | 1.0 | 0.5 | 0.5 | 0.4 |

**(a)** Grafique la irradiancia en función del radio del spot ¿Puede asegurar que el modelo predice la relación entre irradiancia y radio del spot? **(b)** Linearice la ecuación y grafique la función linearizada. Recuerde incluir la nueva incertidumbre ¿Puede asegurar con mayor seguridad que el modelo predice la relación entre irradiancia y radio del spot? **(c)** Realice el ajuste lineal de mínimos cuadrados y grafique la función linearizada y la solución de mínimos cuadrados. Incluya líneas para los casos extremos de la incertidumbre en la pendiente. ¿Puede asegurar con mayor seguridad que el modelo predice la relación entre irradiancia y radio del spot?


