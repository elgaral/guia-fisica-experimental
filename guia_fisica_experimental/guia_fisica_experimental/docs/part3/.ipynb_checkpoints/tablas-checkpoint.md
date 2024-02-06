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

(sec-tablas)=
# Recopilación de datos experimentales: tablas

Usualmente los datos experimentales se presentan en la forma de números por lo que su almacenamiento en forma de tablas permite mantener un orden y evita la pérdida de la información allí contenida. En la mayoría de los casos [^caso] se tienen parejas de datos donde el primer valor corresponde a la variable controlada por el experimentador o variable independiente, y el segundo valor corresponde a la variable medida o variable dependiente. Aunque no es una regla extricta, las parejas se suelen presentar en filas con dos columnas, cada una correspodiente a una de las variables. En la primera fila se debe poner el nombre de la variable, sus unidades, y un prefijo a las unidades si esto hace más fácil la lectura de los datos. En la parte superior[^lugar] de la tabla se debe poner el número de la tabla y una leyenda que explique su contenido. Usualmente, si todos los valores tienen la misma incertidumbre esta se suele presentar en la leyenda. No obstante, la regla genreal es que la tabla contenga toda la información y sea lo más fácil de leer posible.

[^lugar]: También puede ser en la parte inferior. Se usa en la parte superior porque en ocasiones las tablas son muy extensas y ocupan varias páginas.

(subsec-ejemploBola1)=
## Ejemplo: bola rodando (parte 1)
Se deja caer una bola de cristal por una rampa para que ruede sobre un piso de caucho. Se observa que la bola finalmente se detiene a cierta distancia. La pregunta que se formula el investigador es ¿cuál es el valor de la desaceleración de la bola cuando rueda sobre el caucho?. Para averiguarlo mide para diferentes tiempos la posición de la bola a medida que se desplaza sobre la superficie de caucho. Los datos recopilados los presenta en la siguiente tabla:

```{list-table} Posición de la bola en función  del tiempo. El tiempo se mide con una resolución de una centésima de segundo por lo que se considera exacto. Las posiciones hasta el tiempo correspondiente a $2.68 \ \text{s}$ tienen una incertidumbre de $1 \ \text{cm}$. Para tiempos superiores la incertidumbre en la posición es de $2 \ \text{cm}$.
:header-rows: 1
:name: tabla-bola
* - Tiempo/s
  - Posición/cm
* - 2.32
  - 10
* - 2.48
  - 21
* - 2.58
  - 27
* - 2.68
  - 34
* - 2.79
  - 40
* - 2.88
  - 47
* - 3.02
  - 55
* - 3.29
  - 69
* - 3.43
  - 78
* - 3.58
  - 85
* - 3.77
  - 93
```

[^caso]: Una excepción es cuando se tabulan datos de un conteo como por ejemplo los datos de la {numref}`tiemp-caida`.


```{note}
No me extenderé más en el tema de las tablas dado que el énfasis es en las gráficas. más información sobre tablas se puede encontrar en el capítulo dos de {cite}`Mahecha2009`, o en la sección 2.1.1 de {cite}`Thompson2008`.
```

```{code-cell} ipython3

```

