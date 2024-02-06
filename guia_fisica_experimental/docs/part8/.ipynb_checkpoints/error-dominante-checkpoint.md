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

(sec-errorDominante)=
# Incertidumbre dominante

En el ejemplo de la {numref}`subsec-errorPequeno` la expresión para calcular la incertidumbre de la densidad era

$$ \alpha_{\rho} = \rho \Bigg[ \bigg(\frac{\alpha_m}{m}\bigg)^2 + \bigg(\frac{3\alpha_L}{L}\bigg)^2 \Bigg]^{1/2} = \big(28.935\,\text{g/cm}^3\big) \Bigg[ \bigg(\frac{0.1}{50.0}\bigg)^2 + 9\bigg(\frac{0.03}{1.20}\bigg)^2 \Bigg]^{1/2}  = 2.1709\,\text{g}\text{/cm}^3  ,$$

obtiendo una incertidumbre igual a $\alpha_{\rho} = 2\,\text{g}\text{/cm}^3$.

No obstante, si analizamos las incertidumbres relativas de la masa, $\frac{\alpha_m}{m} = 0.002$, y la longitud, $\frac{\alpha_L}{L} = 0.025$, se observa que la incertidumbre relativa de la longitud es un orden de magnitud superior a la incertidumbre relativa de la masa. Además, como en la expresión para la densidad, la longitud se presenta elevada al cubo, en el cálculo de la incertidumbre de la densidad, la incertidumbre relativa de la longitud se incrementa por un factor de tres. Por lo tanto, para este caso, la incertidumbre de la masa es despreciable, el valor de la masa se puede tomar como exacto, y la expresión para determinar la incertidumbre de la densidad se reduce a

$$ \alpha_{\rho} = \rho \bigg(3\frac{\alpha_L}{L}\bigg) = \big(28.935\,\text{g/cm}^3\big) \bigg(\frac{3\times 0.03}{1.20}\bigg) = 2.1701\,\text{g}\text{/cm}^3  ,$$

obtiendo una incertidumbre igual a $\alpha_{\rho} = 2\,\text{g}\text{/cm}^3$, ¡el mismo valor!

Se puede concluir que un análisis de la función matemática que relaciona la variable dependiente con las independientes, y de las incertidumbres relativas de cada variable independiente, permite identificar posibles incertidumbres dominantes, que faciliten el cálculo de la incertidumbre de la variable dependiente.

Identificar incertidumbres dominantes también puede llevar a la conclusión de que la incertidumbre de una variable dependiente que no sea dominante, se puede medir de forma aproximada, sin hacer mucho énfasis en la precisión. Un científico experimentado puede aprovechar esto para distribuir mejor el tiempo o el presupuesto, que tiene para un experimento dado.

+++

```{seealso}

Para leer más sobre el incertidumbres dominantes mirar la sección 5.1 de {cite}`Squires2001` o las secciones 4.2.6 y 4.4 de {cite}`Hughes2010`.

```
