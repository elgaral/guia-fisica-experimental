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

(sec-incertidumbreProcesosAleatorios)=
# Incertidumbre de procesos aleatorios

```{figure} imagenes/ruidoEstatica.png
:figclass: margin
```

En la {numref}`sec-estimacionIncertidumbre`, ante la ausencia de [incertidumbres sistemáticas](subsec-ErrorSistematico), se explicó que si el  instrumento de medida tiene la resolución suficiente, nunca se obtendrá el mismo valor de medida, aunque, en principio, la cantidad física medida no esté cambiando en el tiempo, es decir, se tienen [incertidumbres aleatorias](subsec-ErrorAleatorio). Se definió entonces un método rápido para poder reportar un resultado, a partir de encontrar el valor más probable y un rango dentro del cual se encontraría este valor, y que definiría la incertidumbre que se tiene. Cómo valor más probable se eligió la media aritmética de la distribución de los datos, y como incertidumbre se eligió la mitad de la distancia entre los valores extremos, multiplicado por dos factores: la fracción dos tercios y la raiz cuadrada del total de datos medidos. Los dos factores se usaron sin dar una razón matemática sólida, por lo tanto, el objetivo inicial de esta sección es usar herramientas matemáticas y estadísticas para sentar unas bases que justifiquen el uso de la media aritmética, de la desviación estándar, y de los dos factores. Se comenzará mostrando que sin importar cuál es la distribución de los datos, la distribución de las medias de dicha distribución siempre tiende a una distribución normal. Asegurado que se tiene una distribución normal, el siguiente paso será mostrar que la media, la desviación estándar y la incertidumbre estándar, son los parámetros adecuados para reportar una cantidad física y su incertidumbre. A continuación, se hablará sobre la confiabilidad del valor de incertidumbre reportado, y de como propagar dicha incetidumbre a variables indirectas. Finalmente, se presenta un método para poder comparar cuantitativamente dos cantidades físicas.

El contenido de esta sección sera:

```{tableofcontents}
```
