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

(sec-InterExtrapolacion)=
# Interpolación y extrapolación de datos experimentales

Una vez se ajusta un modelo teórico, o una función matemática, a unos datos experimentales, cabe la pregunta de si al conocer la expresión analítica es posible determinar valores de la variable de interés en puntos distintos a los obtenidos experimentalmente. Si los valores de interés están entre los puntos experimentales, el procedimiento para hayar nuevos valores se llama **interpolación**. Si los valores están antes, o después, de los puntos experimentales, se llama **extrapolación**.

(subsec-interpolacion)=
## Interpolación

La estimación, usando la función de ajuste, de un valor de la variable dependiente, correspondiente a un valor de la variable independiente, que se encuentre entre dos valores medidos experimentalmente, se llamará *interpolación*. Un ejemplo se puede observar en la {numref}`fig-bola6b`, donde se determinaron los desplazamientos para los tiempos $0.2\,\text{s}$ y $0.8\,\text{s}$, que no fueron determinados experimentalmente.

```{figure} imagenes/bola6b.png
---
scale: 80%
name: fig-bola6b
---

Interpolación de los datos de tiempo y desplazamiento, usando la función $x = v_0 t + a t^2$, con parámetros $a = - 9.0\,\text{cm/s}^2$ y $v_0 = 71.0\,\text{cm/s}$. Los dos valores interpolados correponden a las estrellas verdes, para $t = 0.2\,\text{s}$ y $t = 0.8\,\text{s}$.  
```

(subsec-extrapolacion)=
## Extrapolación

La estimación, usando la función de ajuste, de un valor de la variable dependiente, correspondiente a un valor de la variable independiente que se encuentre fuera del rango de los valores medidos experimentalmente, se llamará *extrapolación*. Un ejemplo se puede observar en la {numref}`fig-bola6c`, donde se determinaron los desplazamientos hasta un tiempo igual a $6$ segundos. Es claro que, para este ejemplo, la extrapolación falla, con seguridad, después de los $4$ segundos, donde empieza a predecir que la esfera se devuelve, lo cual se sabe que no es posible, porque la esfera pierde energía cinética por fricción hasta que se detiene por completo.

```{figure} imagenes/bola6c.png
---
scale: 80%
name: fig-bola6c
---

Extrapolación de los datos de tiempo y desplazamiento, usando la función $x = v_0 t + a t^2$,, con parámetros $a = - 9.0\,\text{cm/s}^2$ y $v_0 = 71.0\,\text{cm/s}$. Los valores extrapolados, estrellas verdes, van hasta el tiempo $t = 6\,\text{s}$.  
```

```{warning}
Tanto la interpolación, como la extrapolación, se deben usar con precaución. En ambos casos, es posible que con los datos medidos experimentalmente no se identifique un comportamiento desconocido de la cantidad física. Por ejemplo, en el caso de la {numref}`fig-bola6c`, es de esperarse que a partir de un tiempo la esfera no se desplace, permaneciendo quieta. No obstante, el modelo usado en el ajuste predice lo contrario, que la bola estará quieta sólo en un instante de tiempo. Un ejemplo para el caso de interpolación puede verse en la {numref}`fig-interpola`. Los puntos experimentales no dieron cuenta correctamente de la caída en el valor de la variable de interés, provocando un ajuste erróneo en esa zona, que deriva en una interpolación que no da cuenta del valor real.
```

```{figure} imagenes/interpola.svg
---
name: fig-interpola
---

Interpolación de los datos experimentales (puntos negros). El punto interpolado (estrella roja) no coincide con el valor real (estrella azul). Las variables son adimensionales.
```
