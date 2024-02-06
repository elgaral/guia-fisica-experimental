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

(sec-ejerciciosV2P7)=
# Ejercicios

**Método de mínimos cuadrados**

**1**. Derivar las ecuaciones {eq}`ec-mc1` y {eq}`ec-mc2`.

+++

**Método de ajuste nolineal**

**2.** Usando el método de z-scan usted mide en el laboratorio la transmitancia de la luz cuando un pulso láser atraviesa una muestra de un material semiconductor. Los parámetros del experimento son:
* Espesor de la muestra. $L = 1\,\text{mm}$
* Irradiancia del láser en la muestra: $I_0 = 1\,\text{TW/m}$
* Longitud de onda del láser: $\lambda = 780\,\text{nm}$
* Tamaño del spot láser: $w_0 = 65\,\mu\text{m}$

Sabiendo que el modelo que predice la transmitancia $T$ está dado por la expresión

$$ T = 1 - \frac{\beta I_0 L}{2\sqrt 2} \Bigg(1 + \bigg(\frac{z}{z_0}\bigg)^2\Bigg)^{-1} ,$$

donde $z_0 = kw_0^2$, $k = 2\pi/\lambda$, y $\beta$ es el coeficiente de absorción nolineal. (a) Realice una gráfica de la transmitancia en función de la variable adimensional $z/z_0$. (b) Realice un ajuste nolineal para determinar $\beta$. Reporte correctamente el valor con su incertidumbre, en cm/GW, y reporte la incertidumbre relativa. (c) Determine la incertidumbre común de los datos de transmitancia. (d) Si el valor real de $\beta$ es $8\,\text{cm/GW}$, indique si el valor que encontró en (b) coincide significativamente con el valor real. A continuación se presentan los datos de transmitancia (*`datos`*) y posición (*`z`*).

```{code-cell} ipython3
:tags: ['hide-cell']

import numpy as np
datos = np.array([1.00107518, 1.00146765, 0.99886514, 0.99659094, 0.9997498 ,
       1.00061351, 1.00256587, 1.00223257, 0.99864485, 0.99819449,
       0.99568751, 0.99315836, 0.98915297, 0.98957013, 0.97418306,
       0.97432637, 0.98315578, 0.99412608, 0.99277016, 0.99736102,
       0.99700683, 1.00019505, 0.99880234, 0.9977386 , 1.00024404,
       1.00130404, 1.00069017, 1.00124834, 0.9994404 , 1.00003864])

z = np.array([-0.3       , -0.27931034, -0.25862069, -0.23793103, -0.21724138,
       -0.19655172, -0.17586207, -0.15517241, -0.13448276, -0.1137931 ,
       -0.09310345, -0.07241379, -0.05172414, -0.03103448, -0.01034483,
        0.01034483,  0.03103448,  0.05172414,  0.07241379,  0.09310345,
        0.1137931 ,  0.13448276,  0.15517241,  0.17586207,  0.19655172,
        0.21724138,  0.23793103,  0.25862069,  0.27931034,  0.3])

```

+++

**Interpolación y extrapolación**

**3**. Con los datos del problema anterior, realice una interpolación y extrapolación para crear una gráfica que vaya desde $z/z_0 = -15$ hasta $z/z_0 = 15$, y que contenga 200 puntos. Superponga a esta gráfica los datos experimentales con la incertidumbre común.

+++