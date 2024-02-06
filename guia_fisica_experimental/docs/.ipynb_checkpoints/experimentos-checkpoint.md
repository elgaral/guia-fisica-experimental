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

(sec-Experimentos)=
# Guía de experimentos

En esta sección se presenta una guía básica para la realización de los experimentos referidos en el texto. Se presenta el objetivo, los materiales, el montaje y el procedimiento.

(subsec-bolarodando)=
## Bola rodando

**Objetivos**: 
1. Determinar la desaceleración de una bola que rueda sobre una superficie de caucho.

**Materiales**:
1. Canica de cristal.
2. Rampa para el lanzamiento de la canica.
3. Superficie horizontal de caucho.
4. Cámara de video.
5. Regla o cinta métrica.

**Montaje**
```{figure} imagenes/MontajeBola.jpg
:name: fig-MontajeBola

Montaje experimento bola rodando.
```

**Procedimiento**
1. Se inicia la toma del video y se procede a dejar rodar la bola sobre la rampa. Una vez se detenga la bola se detiene el video. A partir del video, se miden los tiempos y la posición de la bola según lo indique la cinta métrica.
2. Se definen las incertidumbres experimentales.
3. Se realiza una tabla con los datos del experimento.
4. Realice una gráfica de posición vs. tiempo. Incluya las incertidumbres.
5. Linearice los datos y grafique nuevamente.
6. Usando mínimos cuadrados determine los parámetros de la línea que se ajusta a los datos linearizados. Grafique.
7. Repita el numeral 6 pero ahora tenga en cuenta las incertidumbres en la posición.
8. Usando chi-cuadrado verificar que el ajuste es bueno.


```{admonition} Ubicaciones del experimento
{numref}`subsec-ejemploBola1`, {numref}`subsec-ejemploBola2`, {numref}`subsec-ejemploBola3`, {numref}`subsec-ejemploBola4`, {numref}`subsec-ejemplobola5`, {numref}`subsec-calidadChiCuadrado`
```

+++

(subsec-ExpDiaCanicas)=
## Diámetro canicas

**Objetivos**: 
1. Medir el díametro de un conjunto de canicas y reportar el diámetro promedio y la dispersión.

**Materiales**:
1. 20 o más canicas del "mismo" diámetro.
2. Un vernier o calibrador.

**Procedimiento**:
1. Medir los diámetros de cada canica con el calibrador.
2. Construir un histograma.
3. Calcular la media de los diámetro.
4. Calcular la desviación estándar de los diámetros.
5. Reportar los resultados correctamente.
6. Usando Chi-cuadrado verificar que la distribución de los diámetros es normal.

```{admonition} Ubicaciones del experimento
{numref}`subsec-DiaCanicas`, {numref}`subsec-bondadChiCuadrado`
```

+++

(subsec-densidadCubo)=
## Densidad volumétrica de un cubo

**Objetivos**: 
1. Medir la densidad volumétrica de un cubo

**Materiales**:
1. Cubo.
2. Balanza o gramera.
3. Calibrador.

**Procedimiento**:
1. Medir la longitud del lado del cubo y reportar con su incertidumbre.
2. Medir la masa del cubo y reportar con su incertidumbre.
3. Determinar la densidad volumétrica del cubo. Reportar el valor con su incertidumbre.
4. Repetir el numeral 4 pero considerando que las incertidumbres son pequeñas.
5. Utilizar residuos normalizados para verificar que los datos se distribuyan aleatoriamente.

```{admonition} Ubicaciones del experimento
{numref}`subsec-errorIndirecta`, {numref}`sec-propagacionError`, {numref}`subsec-ejemploResiduos`
```

+++

(subsec-ExpEstudiantes)=
## Altura estudiantes

**Objetivos**: 
1. Medir la altura de un grupo de estudiantes y reportar la altura promedio y la dispersión.

**Materiales**:
1. 20 estudiantes de un mismo nivel de estudio.
2. Cinta métrica o flexómetro.

**Procedimiento**:
1. Medir las alturas de cada estudiante con la cinta métrica.
2. Construir un histograma.
3. Calcular la media de las alturas.
4. Calcular la desviación estándar de las alturas.
5. Reportar los resultados correctamente.

```{admonition} Ubicaciones del experimento
{numref}`subsec-altEstudiantes`
```

+++

(subsec-ExpAlturaMesa)=
## Altura mesa

**Objetivos**: 
1. Determinar la altura de una mesa a partir de medir el tiempo de caída de un objeto.

**Materiales**:
1. Mesa.
2. Flexómetro.
3. Cronómetro.
4. Objeto macizo.

**Montaje**:
```{figure} imagenes/MontajeMesa.jpg
:name: fig-MontajeMesa

Montaje experimento altura mesa.
```

**Procedimiento**:
1. Medir la altura de la mesa con el flexómetro y reportar el valor con su respectiva incertidumbre.
2. Realizar siete medidas del tiempo de caída del objeto.
3. Reportar los tiempos en una tabla.
4. Usando el valor aceptado para la aceleración de la gravedad, determinar la altura de la mesa con su incertidumbre suponiendo que los datos del tiempo siguen una distribución normal.
5. Calcule el intervalo para una confiabilidad del $95\,\%$.

```{admonition} Ubicaciones del experimento
{numref}`subsec-estimacionEjemplo1`, {numref}`subsec-unoEjemplo`, {numref}`subsec-estimacionEjemplo2`,{numref}`subsec-estimacionEjemplo1b`, {numref}`subsec-gum-evaluacion`,{numref}`subsec-corr-tstudent`
```

+++

(subsec-ruidoEstatica)=
## Amplitud ruido estática

**Objetivos**: 
1. Determinar la distribución de la amplitudes de una señal de radio estática.

**Materiales**:
1. Grabador digital de sonido.
2. Generador de señal de radio estática (sintonizador de señales de radio).

**Procedimiento**:
1. Con un sintonizador de señales de radio sintonizar una frecuencia que no corresponda con la de una emisora de radio, de forma tal que se escuche ruido.
2. Grabar de forma digital en archivo WAV la señal emitida por el parlante del sintonizador.
3. Determinar el tiempo total de la grabación y la frecuencia de grabación de datos.
4. Graficar la señal obtenida, o parte de ella.
5. Graficar el histograma y calcular la media y desviación estándar. Superponer la función densidad de probabilidad de la distribución normal con la misma media y desviación.

```{admonition} Ubicaciones del experimento
{numref}`subsec-distNormal-ejemplo`
```

+++

(subsec-conteoGotas)=
## Conteo de gotas

**Objetivos**: 
1. Determinar la distribución de la amplitudes de una señal de radio estática.

**Materiales**:
1. Valde lleno de agua.
2. Canilla o manguera para generar un hilo de agua sobre el valde.
3. Superficie lisa y plana, por ejemplo la pantalla de un teléfono móvil.

**Monjaje**:
```{figure} imagenes/MontajeGota.jpg
:name: fig-MontajeGota

Montaje experimento conteo gotas.
```

**Procedimiento**:
1. Ubique la superficie lisa y plana según el montaje.
2. Abra la canilla para que salga el hilo de agua.
3. Espere $10\,\text{s}$ y cierre la canilla.
4. Contabilice el número de gotas que cayeron sobre la superficie lisa.
5. Seque bien la superficie y repita los numerales 1 al 4 $35$ veces.
6. Calcule la media y desviación estándar de los datos obtenidos.
7. Suponga que los datos siguen una distribución de Poisson. Calcule nuevamente la desviación estándar y compare con la obtenida en el numeral 6.
8. Grafique el histograma de los datos, superponga la distribución de Poisson correspondiente.
9. Calcule la probabilidad de que caigan tres gotas, seis gotas, once gotas, hasta seis gotas.
10. Calcule la probabilidad de que en las 35 mediciones caigan siempre 11 gotas, nunca caigan 11 gotas, o que en algúna de las mediciones caigan 11 gotas.

```{admonition} Ubicaciones del experimento
{numref}`subsec-distPoisson-ejemplo1`
```

+++


(subsec-expResistencia)=
## Valor de la resistencia

**Objetivos**: 
1. Comparar los resultados de mediciones de una resistencia hechas con diferentes multímetros.

**Materiales**:
1. Dos multímetros diferentes.
2. Resistencia de $100\,\ohm$ con incertidumbre relativa de $5\,\%$.
3. Superficie lisa y plana, por ejemplo la pantalla de un teléfono móvil.

**Procedimiento**:
1. Medir la resistencia con el primer multímetro realizando 12 mediciones y reportar el resultado con su respectiva incertidumbre.
2. Medir una vez la resistencia con el primer multímetro y reportar usando la incertidumbre sugerida por el fabricante.
3. Repetir los numerales 1 y 2 para el segundo multímetro.
4. Comparar los resultados con los del fabricante de la resistencia.

```{admonition} Ubicaciones del experimento
{numref}`sec-comparaResul`
```

+++

(subsec-ruidoMaquina)=
## Señal sonora máquina de afeitar

**Objetivos**: 
1. Determinar si existen datos sesgados en una señal sonora de una máquina de afeitar.

**Materiales**:
1. Grabador digital de sonido.
2. Máquina de afeitar.

**Procedimiento**:
1. Encender la máquina de afeitar.
2. Grabar de forma digital en archivo WAV la señal emitida por la máquina de afeitar.
3. Determinar el tiempo total de la grabación y la frecuencia de grabación de datos.
4. Graficar la señal obtenida, o parte de ella.
5. Determinar el valor esperado de intensidad de ruido con su incertidumbre, en decibeles.
6. Usar el criterio de Chauvenet para determinar si hay datos sesgados.
7. Eliminar los datos sesgados  y repetir el numeral 5.

```{admonition} Ubicaciones del experimento
{numref}`sec-Chauvenet`
```