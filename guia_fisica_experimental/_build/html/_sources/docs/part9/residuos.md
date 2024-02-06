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

(sec-Residuos)=
# Residuos

Puesto que se partió de la suposición de que la fluctuación en el valor medido de la cantidad física es aleatoria, y sigue una distribución normal, es de esperarse que la distancia entre el valor medido $y_i$ y el valor predicho por la curva de ajuste $y(x_i)$, conocido como el *residuo* $R_i = y_i - y(x_i)$, sea también un valor aleratorio de una distribución normal con media igual a 0. Aquí $x_i$ es la variable independiente. Por lo tanto, si se realiza una gráfica de los residuos es de esperarse que los residuos se distribuyan de manera aleatoria alrededor del cero. Si por el contrario, se observa que los residuos siguen un patrón se podrá concluir que los datos no se ajustan a la curva del modelo.

```{tip}
Si la cantidad de datos es lo suficientemente grande, es mejor realizar un histrograma para verificar que se tiene una distribución normal.
```

**Ejemplo**

Recordando el ejemplo de la {numref}`sec-AjusteNolineal`, al calcular los residuos del ajuste nolineal presentado en la {numref}`fig-bola6`, donde se usó la curva $x = v_0 t + a t^2$, se observa que estos se distribuyen de manera aleatoria alrededor del cero  corroborando que los datos efectivamente se ajustan al modelo (ver {numref}`fig-residuos1`). 

```{figure} imagenes/residuos1.svg
:name: fig-residuos1

Análisis del ajuste de los datos a través de los residuos. En la gráfica superior está el ajuste de los datos usando una función cuadrática de la forma $x = v_0 t + a t^2$. Visualmente, los datos parecen estar correctamente ajustados. En la gráfica inferior se presentan los residuos, los cuales se encuentran distribuidos aleatoriamente alrededor del cero. Esto es un indicativo de que efectivamente el ajuste de los datos a la función cuadrática es correcto.
```

Por el contrario, si se hubiera usado el modelo lineal $x = v_0 + at$, los residuos no se distribuirían de manera aleatoria: seguirían un cierto patrón como se observa en la {numref}`fig-residuos2`.

```{figure} imagenes/residuos2.svg
:name: fig-residuos2

Análisis del ajuste de los datos a través de los residuos. En la gráfica superior está el ajuste de los datos usando una función lineal de la forma $x = v_0 + a t$. Visualmente, los datos parecen estar correctamente ajustados. En la gráfica inferior se presentan los residuos, los cuales se encuentran distribuidos no aleatoriamente alrededor del cero siguiendo un patrón no lineal, posiblemente cuadrático[^cuadrado]. Esto es un indicativo claro de que los datos no se ajustan a una función lineal.
```

[^cuadrado]: Esto es sólo una hipótesis. No obstante, no parece tener una tendencia a una función armónica, por lo que probar con un término cuadrático parece lógico.

+++

(subsec-residuosNorm)=
## Residuos normalizados

En algunos casos es posible que los datos tengan diferentes incertidumbres, lo que podría llevar a una interpretación errónea de los residuos. Para eliminar la dependencia con la incertidumbre y obtener una gráfica de residuos que se corresponda con una distribución normal con media cero y desviación estándar uno, se deben graficar los residuos normalizados. Sea $\alpha_i$ la incertidumbre en la medida $y_i$, el residuo normalizado se define como

$$ R_{Ni} = \frac{y_i - y(x_i)}{\alpha_i} .$$ (ec-residuo1)

Una ventaja extra de usar los residuos normalizados es que directamente de la gráfica se puede observar si la mayoría de datos (apróximadamente el $95\,\%$) están a menos de dos desviaciones de la media (cero para los residuos).

+++

(subsec-ejemploResiduos)=

## Ejemplo: densidad de un líquido

Para un experimento, un estudiante de posgrado necesita determinar la densidad de un líquido. Ella sabe que por definición la densidad volumétrica $\rho$ se relaciona con el volumen $V$ del objeto y la masa $m$ del objeto, según la relación

$$ \rho = \frac{m}{V} $$

En el laboratorio cuenta con una balanza con resolución de un gramo, por lo que la considerará exacta. Por el contrario, para medir el volumen cuenta con una jeringa que tiene una escala hasta $5.0\,\text{mL}$ con resolución de $0.2\,\text{mL}$, y con una vasija que tiene una escala hasta $20\,\text{mL}$ con resolución de $5\,\text{mL}$.

Los datos que obtiene para la jeringa se listan en la {numref}`tabla-jeringa`, y para el vaso en la {numref}`tabla-vaso`.

```{list-table} Datos tomados con la jeringa. Resolución de la balanza de $0.1$ $\text{g}$. Resolución de la jeringa de $0.2$ $\text{mL}$.
:header-rows: 0
:name: tabla-jeringa

* - $m/\text{g}$
  - 0.9
  - 2.1
  - 2.9
  - 3.9
  - 5.0
* - $V/\text{mL}$
  - 1.0
  - 2.0
  - 3.0
  - 4.0
  - 5.0
```

```{list-table} Datos tomados del vaso. Resolución de la balanza de $0.1$ $\text{g}$. Resolución del vaso de $5$ $\text{mL}$.
:header-rows: 0
:name: tabla-vaso

* - $m/\text{g}$
  - 8.9
  - 11.3
  - 18.0
* - $V/\text{mL}$
  - 10
  - 15
  - 20
```

Para definir las incertidumbres, la estudiante nota que, para el caso de la jeringa, es dificil subdividir la escala que tiene, por lo que decide que existe la misma probabilidad de que su lectura difiera en $\pm 0.1\,\text{mL}$ del valor leído. Por lo tanto, la distribución de los datos será uniforme y la incertidumbre será $\alpha_J = \pm \frac{0.2}{\sqrt 12}\,\text{mL} = \pm 0.06\,\text{mL}$ (ver ecuación {eq}`ec-gum2`). Por el contrario, para el caso del vaso si le es posible identificar si la medida está más cerca del valor central, por lo que decide para el vaso considerar una distribución triángular, cuya incertidumbre será $\alpha_V = \pm \frac{5}{2\sqrt 6}\,\text{mL} = \pm 1.0\,\text{mL}$ (ver ecuación {eq}`ec-gum4`). 

Definidas las incertidumbres realiza una regresión lineal encontrando para el inverso de la densidad el valor de $1/\rho = (1.014 \pm 0.015)\,\text{mL/g}$ (ver {numref}`fig-residuosNorm`a). Aplicando propagación de la incertidumbre, encuentra que la densidad del líquido es $\rho = (0.986 \pm 0.014)\,\text{g/mL}$.

```{figure} imagenes/residuosNorm.svg
:name: fig-residuosNorm

Análisis del ajuste usando residuos. (a) Ajuste lineal de los datos de volumen y masa: los puntos negros son los datos experimentales, las barras rojas son las incertidumbres y la línea azúl es la curva de ajuste. (b) Gráfica de los residuos y (c) gráfica de los residuos normalizados.
```

Decide ahora verificar que tan bueno es el ajuste. Para ello calcula los residuos y los grafica (ver {numref}`fig-residuosNorm`b). Encuentra lo que parece ser un patrón correspondiente a una función lineal, con la particularidad de que los primeros seis datos están muy cercanos al cero. No obstante, se da cuenta que esto puede ser debido a la diferencia en el valor absoluto de la incertidumbre de los primeros cinco datos con respecto al resto. Para eliminar cualquier efecto debido a la magnitud de las incertidumbres, grafica los residuos normalizados, encontrando la gráfica de la {numref}`fig-residuosNorm`c. De esta nueva gráfica puede concluir que sus datos si se distribuyen aleatoriamente alrededor del cero y que la gran mayoría están a menos de dos desviaciones estándar del cero, indicando que puede confiar en el ajuste de los datos a la función lineal del modelo.

```{admonition} En la gráfica de residuos normalizados, el punto correspondiente a la masa de $11.3$ $\mathsf{g}$ está a más de tres deviaciones. Use el criterio de Chauvenet y verifique si es un dato sesgado que puede eliminar. Si la respuesta es positiva calcule la nueva densidad. *Despliegue para ver la respuesta*
:class: 'dropdown'


Al aplicar el criterio se encuentra que para los ocho datos se esperan $0.004 \approx 0$ datos a más de $2.5$ desviaciones. El dato es sesgado y se elimina. La nueva densidad es $\rho = (0.988 \pm 0.011)\,\text{g/mL}$
```



```{seealso}

Para más información sobre residuos leer las secciones 5.2.1, 5.3 y 6.3.2 de {cite}`Hughes2010`.

```
