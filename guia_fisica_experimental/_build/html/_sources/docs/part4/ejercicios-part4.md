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

(sec-ejerciciosV1P4)=
# Ejercicios

**Conceptos básicos de estadística**

**1**. Con base en las definiciones de variables discretas y continuas investigue qué tipo de variables son: (a) la temperatura promedio en una ciudad, (b) la irradiancia de un haz láser, (c) el número de estrellas en el firmamento, (d) razone sobre si el tipo de variable cambia en virtud al detector (sensor) usado, por ejemplo, ¿qué pasa si la temperatura se mide con un termómetro digital?

**2**. En la ciudad de Envigado, en el transcurso de tres semanas, el promedio diario de partículas contaminantes de hasta 2.5 micrómetros de diámetro, en micrógramos por metrocúbico, fue: 17, 21, 16, 21, 19, 23, 20, 15, 16, 14, 19, 23, 24, 19, 27, 22, 27, 22, 22, 25, 28. **(a)** Organice los datos y preséntelos en una tabla (una columna para los valores y otra para su repetición), **(b)** escoja un intervalo de 3 $\mu$g/m$^3$ y construya un histograma para la densidad de días por $\mu$g/m$^3$, **(c)** determine la probabilidad de que en un día la lectura de polución esté entre 23 $\mu$g/m$^3$ y 29 $\mu$g/m$^3$, **(d)** determine la probabilidad de que en un día la polución esté entre 14 $\mu$g/m$^3$ y 29 $\mu$g/m$^3$, **(e)** determine la media y la desviación estándar de la distribución y concluya a partir de estos dos parámetros como se comporta la polución en la ciudad de Envigado.

**Distribución binomial**

**3**. De la igualdad de la expansión binomial, que se expresa con la siguiente fórmula:

$$ (p + q)^n = \sum_{x=0}^n \frac{n!}{x! (n-x)!}p^x q^{n-x} $$

muestre que efectivamente de la expresión de la función de probabilidad binomial se deduce que la probabilidad total es igual a la unidad.

**4**. Usando la definición de función de probabilidad binomial, demuestre que la media de la distribución binomial es igual a $\mu = np$, donde $n$ es el número de intentos y $p$ es la probabilidad de obtener éxito en un intento.

**5**. A un grupo de 200 jóvenes universitarios se les preguntó cuál era su estatura en centímetros. El procedimiento fue preguntarle a grupos de 10 jóvenes y anotar como respuesta el número de veces que la altura era inferior a 160 cm. Se le pregunta a 20 grupos y las respuestas fueron: 0, 0, 1, 1, 4, 1, 2, 1, 2, 0, 3, 0, 1, 1, 1, 2, 3, 1, 4, 1. **(a)** Determine la media y la desviación estándar. **(b)** Si se sabe que la altura media es de 170 cm y que por lo tanto sólo el $16 \ \%$ de los jóvenes tiene una altura inferior a 160 cm, es decir, la probabilidad de que al preguntarle a un joven este tenga una altura infieror a 160 cm es de $16 \ \%$, usted puede suponer que los datos siguen una distribución binomial. En una misma figura grafique la distribución de los resultados y una distribución binomial teórica con los mismos parámetros de la distribución de los resultados. A partír de la gráfica ¿puede decir que los resultados si siguen una distribución binomial? **(c)** Considerando que si siguen una distribución binomial, ¿cuál es la probabilidad de que al preguntarle a 10 jóvenes 2 tengan una altura inferior a 160 cm? **(d)** ¿Cuál es la probabilidad de que 3 o más tengan una altura  inferior a 160 cm?
