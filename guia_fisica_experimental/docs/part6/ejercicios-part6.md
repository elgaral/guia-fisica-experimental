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

(sec-ejerciciosV2P6)=
# Ejercicios

**Teorema central del límite, incertidumbre estándar e intervalos de confianza**

**1**. En el laboratorio, se utiliza un detector especial para medir la emisión de fotones de una fuente térmica de pocos fotones. En la unidad de tiempo que se usó para medir, se realizan $100$ medidas, y se reportan los conteos de fotones para cada medida (el arreglo con los datos se presenta en la parte inferior de la pregunta). (a) Se espera que la distribución sea de Poisson, realice un histograma y verifique visualmente. (b) Determine el promedio de fotones en la unidad de tiempo, y la desviación estándar. Reporte el valor promedio de fotones usando la desviación estándar como inceritumbre, y la incertidumbre relativa. Usando la función de densidad de la distribución de Poisson, confirme que la confiabilidad para el rango reportado es aproximadamente $66\,\%$. (c) Usando el teorema central del límite y la incertidumbre estándar, agrupe los datos de a cinco, calcule el promedio, y con el nuevo conjunto de datos reporte el promedio de fotones en la unidad de tiempo con su incertidumbre, y una confiabilidad del $68\,\%$. Calcule la incertidumbre relaiva. (d) Repita el numeral (c) pero ahora agrupando de a diez datos. (e) Ahora tome todos los datos y reporte el promedio de fotones usando la incertidumbre estándar. (f) Compare los resultados de (b), (c) y (d) y comente al respecto.

```{code-cell} ipython3
:tags: ['hide-cell']

import numpy as np
datos = np.array([3, 2, 5, 1, 0, 0, 7, 1, 3, 3, 5, 2, 2, 0, 1, 3, 1, 2, 1, 0, 1, 1,
       1, 1, 5, 1, 1, 1, 0, 2, 1, 3, 0, 2, 1, 1, 2, 3, 1, 4, 5, 4, 1, 2,
       2, 2, 3, 3, 2, 3, 2, 0, 4, 6, 2, 1, 1, 2, 2, 1, 2, 4, 1, 2, 1, 1,
       2, 1, 0, 0, 5, 2, 2, 4, 3, 3, 1, 0, 1, 2, 2, 1, 3, 1, 5, 3, 1, 0,
       4, 0, 4, 4, 3, 0, 1, 4, 1, 1, 1, 6])
```

+++

**2**. En el ejemplo de la {numref}`subsec-distPoisson-ejemplo1` la estudiante obtuvo el promedio de gotas en un decasegundo con una precisión muy baja, correspondiente a una incertidumbre relativa de $50\,\%$. (a) Usando los mismos datos, el teorema del límite central, y la incertidumbre estándar, reporte el promedio de gotas con una mayor precisión. Indique la confiabilidad de su resultado. (b) Compare su resultado con el obtenido por el estudiante en el ejemplo de la {numref}`subsec-distPoisson-ejemplo2`, y concluya.

+++

**Propagación de la incertidumbre**

**3**. Recordando el ejemplo de la {numref}`subsec-estimacionEjemplo2`, se tiene que el tiempo de caída medido es $(0.486 \pm 0.011)\,\text{s}$. Considerando que el valor conocido para la aceleración de la gravedad es $(980  \pm 10)\,\text{cm/s}^2$, determine la altura de la mesa (a) usando el método de valores máximos y valores mínimos, (b) y suponiendo que las incertidumbres son pequeñas.

+++

**Comparación de resultados**

**4**. Actualmente, el valor de la constane de Planck se definió como exacto, y es igual a $h = 6.626\,070\,15\times 10^{-34}\,\text{J s}$. No obtante, no siempre fue así, y a lo largo de la historia se han hecho diferentes mediciones que han dado valores, no siempre coincidentes. En la siguiente tabla se presentan algunos de los más representativos:

```{list-table} Valores de la constante de Planck $h$, en unidades de $10^{-34}$ J s
:header-rows: 1
:name: tabla-planck

* - h
  - $\alpha_h/10^{-6}$
  - 
* - $6.55$
  - $100\,00$
  - Birge, 1919
* - $6.626\,20$
  - $50$
  - Taylor, 1969
* - $6.626\,075\,6$
  - $0.4$
  - Cohen y Taylor, 1986
* - $6.626\,069\,3$
  - $1.1$
  - Mohr y Taylor, 2002
* - $6.626\,070\,04$
  - $0.08$
  - Mohr et al, 2014
```

(a) Realice una gráfica como la {numref}`fig-resistencia`. Incluya como una línea vertical el valor aceptado actualmente. (b) Compare los diferentes resultados con el aceptado actualmente, e indique si coinciden o discrepan. (c) Compare los valores de Mohr de 2002 y 2014. (d) Comente sobre los resultados que se aproximan bastante al actualmente aceptado, pero que por la incertidumbre reportada discrepan del valor aceptado.
