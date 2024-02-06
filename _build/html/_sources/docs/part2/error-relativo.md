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

(sec-errorRelativo)=

# Incertidumbre relativa

En la {numref}`subsec-notacionIncertidumbre` se definió la estructura para reportar una cantidad física como $ X = x_{mejor} \pm \alpha_x$, donde la cantidad $\alpha_x$ se refería a la incertidumbre que se tiene de la medida, o incertidumbre absoluta. No obstante, esta cantidad no necesariamente indica si la medida fue precisa o no, es decir, si está más cerca de la realidad o no. Por ejemplo se pueden tener las siguientes dos medidas hechas con una regla:

1. $L = (970.0 \pm 0.5) \,\text{mm}$
2. $L = (1.0 \pm 0.5) \,\text{mm}$

Aunque para ambas medidas la incertidumbre es la misma, es claro que la primera medida es mucho más precisa que la segunda. Una forma más clara de expresar lo anterior es a través de la incertidumbre relativa, que también se le conoce como incertidumbre fraccional o precisión, y que se puede expresar en forma de porcentaje. La incertidumbre relativa será:

$$ \frac{\alpha_x}{|x_{mejor}|},$$

y en términos de porcentaje,

$$100\times \frac{\alpha_x}{|x_{mejor}|} \,\%$$

Para las dos longitudes del ejemplo las incertidumbres relativas son:

1. $\frac{0.5\,\text{mm}}{970.0\,\text{mm}} = 0.000 \,5$, o en porcentaje sería $0.05 \,\%$
2. $\frac{0.5\,\text{mm}}{1.0\,\text{mm}} = 0.5$, o en porcentaje sería $50 \,\%$

Es claro ahora, al presentar la incertidumbre relativa, que la primera medida es muy precisa mientras que la segunda es muy imprecisa. La forma recomendada para reportar una cantidad física con incertidumbre relativa será

$$ X = x_{mejor} \pm \alpha_x\text{,} \, \text{con una incertidumbre relativa de } 100\times \frac{\alpha_x}{|x_{mejor}|} \,\%$$

y también

$$ X = x_{mejor} \,\text{con una incertidumbre relativa de } 100\times \frac{\alpha_x}{|x_{mejor}|} \,\%$$

Para los ejemplos anteriores tenemos:

1. $(970.0 \pm 0.5)\,\text{mm}$, con una incertidumbre relativa de $0.05\,\%$.
2. $1.0 \,\text{mm}$, con una incertidumbre relativa de $50\,\%$.

En la siguiente tabla se da una guía de la catalogación de la precisión de una medida en términos de la incertidumbre relativa

| Incertidumbre relativa    | Precisión    |
| :--- | ---: |
| <1 %    | Muy preciso    |
| 1 % a 5 % | Preciso |
| 5 % a 20 % | Precisión aceptable |
| 20% a 30% | Impreciso |
| >30 % | Muy impreciso |

Finalmente, es importante anotar que la incertidumbre relativa es una cantidad adimensional. Esta particularidad es muy importante porque permite comparar las precisiones de cantidades físicas diferentes, es decir, no es posible comparar la precisión de una medida de tiempo, con una de longitud, a partir de sus respectivas incertidumbres absolutas, porque tienen dimensiones diferentes, pero si es posible comparar sus precisiones usando sus incertidumbres relativas. Por ejemplo, para las medidas:

1. $L = (970.0 \pm 0.5)\,\text{mm}$, con una incertidumbre relativa de $0.05\,\%$.
2. $T = (0.63 \pm 0.01)\,\text{s}$, con una incertidumbre relativa de $1.6\,\%$.

No es posible comparar las incertidumbres absolutas porque una está en milímetros y la otra en segundos. No obstante, si es posible comparar sus incertidumbres relativas porque son adimensionales. De esta forma, para el ejemplo, se concluye que la medida de la longitud $L$ es más precisa que la medida del tiempo $T$, y por lo tanto, para mejorar la medición se deben usar los recursos disponibles para conseguir un cronómetro más preciso.

```{seealso}
Más sobre incertidumbre relativa se puede encontrar en la sección 4.2.6 de {cite}`Hughes2010`, y en las secciones 2.7 y 2.8 de {cite}`Taylor1996`.
```

