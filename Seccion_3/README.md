# Métricas de Desempeño

## Introducción
En el contexto del aprendizaje automático y la minería de datos, las métricas de desempeño son esenciales para evaluar la calidad y eficacia de los modelos. Estas métricas permiten medir la precisión, la eficiencia y la capacidad de generalización de los algoritmos, proporcionando información valiosa para la toma de decisiones y la optimización de modelos.

En esta sección se utilizarán datasets sintéticos creados para ejemplificar el uso de diferentes métricas de desempeño en modelos de regresión, clasificación y clustering. Se presentarán las métricas más comunes y se explicará su interpretación y aplicación en diferentes contextos.

## Métricas para Modelos de Regresión

### Error Cuadrático Medio (MSE)
El MSE mide la media de los cuadrados de los errores entre los valores predichos y los valores reales. Es útil para penalizar errores grandes y proporciona una medida global del desempeño del modelo.

$MSE = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2$

### Raíz del Error Cuadrático Medio (RMSE)
El RMSE es la raíz cuadrada del MSE y tiene la misma unidad que la variable de interés. Es una métrica que facilita la interpretación de los errores, siendo más sensible a grandes errores que el MAE.

$RMSE = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2}$

### Error Absoluto Medio (MAE)
El MAE calcula la media de los valores absolutos de los errores entre las predicciones y los valores reales. Es menos sensible a valores atípicos en comparación con el MSE.

$MAE = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i|$

### Coeficiente de Determinación (R²)
El R² indica qué proporción de la variabilidad en los datos se explica mediante el modelo. Un valor de 1 indica una predicción perfecta, mientras que valores cercanos a 0 sugieren que el modelo no explica la variabilidad.

El coeficiente de determinación, $R^2$, se calcula como:

$R^2 = 1 - \frac{SS_{res}}{SS_{tot}}$

Donde:
- $SS_{res}$ es la **suma de los cuadrados de los residuos**:
  $SS_{res} = \sum_{i=1}^{n} (y_i - \hat{y}_i)^2$
- $SS_{tot}$ es la **suma total de los cuadrados**:
  $SS_{tot} = \sum_{i=1}^{n} (y_i - \bar{y})^2$

### Coeficiente de Correlación de Pearson (r)
El coeficiente r mide la correlación lineal entre las predicciones y los valores reales, con valores que varían entre -1 y 1. Un valor de 1 indica una correlación positiva perfecta.

El coeficiente de correlación de Pearson, $r$, se calcula como:

$r = \frac{\sum_{i=1}^{n} (y_i - \bar{y})(\hat{y}_i - \bar{\hat{y}})}{\sqrt{\sum_{i=1}^{n} (y_i - \bar{y})^2} \sqrt{\sum_{i=1}^{n} (\hat{y}_i - \bar{\hat{y}})^2}}$

Donde:
- $y_i$ representa los valores reales.
- $\hat{y}_i$ representa los valores predichos.
- $\bar{y}$ es la media de los valores reales.
- $\bar{\hat{y}}$ es la media de los valores predichos.

### Error Porcentual Absoluto Medio (MAPE)
El MAPE expresa el error promedio como un porcentaje de los valores reales, permitiendo evaluar el rendimiento del modelo en diferentes escalas de datos.

$MAPE = \frac{1}{n} \sum_{i=1}^{n} \left| \frac{y_i - \hat{y}_i}{y_i} \right| \times 100$

## Métricas para Modelos de Clasificación

### Matriz de Confusión
Una matriz que muestra el número de verdaderos positivos, verdaderos negativos, falsos positivos y falsos negativos, permitiendo una evaluación detallada del rendimiento del modelo.


<figure align="center" style="margin-bottom: 20px;">
    <img src="https://github.com/DiegoPaezA/CienciaDatos-MASDI/blob/main/Seccion_3/imagenes/matriz_confusion_1.jpg" width="60%">
    <figcaption>Figura 1. Matriz de Confusión - Ejemplo 1</figcaption>
</figure>

<br>
<br>

<figure align="center" style="margin-bottom: 20px;">
    <img src="https://github.com/DiegoPaezA/CienciaDatos-MASDI/blob/main/Seccion_3/imagenes/matriz_confusion_2.jpg" width="60%">
    <figcaption>Figura 2. Matriz de Confusión - Ejemplo 2</figcaption>
</figure>
<br>
<br>

- Verdaderos Positivos (TP): Instancias positivas correctamente clasificadas.
- Verdaderos Negativos (TN): Instancias negativas correctamente clasificadas.
- Falsos Positivos (FP): Instancias negativas incorrectamente clasificadas como positivas.
- Falsos Negativos (FN): Instancias positivas incorrectamente clasificadas como negativas.

### Precisión (Accuracy)
La precisión indica la proporción de predicciones correctas entre el total de predicciones realizadas por el modelo. Es adecuada cuando las clases están balanceadas.

$Accuracy = \frac{TP + TN}{TP + TN + FP + FN}$

### Recall
El recall, o sensibilidad, mide la capacidad del modelo para identificar correctamente las instancias positivas, siendo útil en situaciones donde los falsos negativos son costosos.

$Recall = \frac{TP}{TP + FN}$

### F1-Score
El F1-Score es la media armónica de la precisión y el recall, proporcionando una métrica equilibrada cuando es importante considerar tanto los falsos positivos como los falsos negativos.

$F1 = 2 \times \frac{Precision \times Recall}{Precision + Recall}$

### Curva ROC
La curva ROC visualiza la relación entre la tasa de verdaderos positivos y la tasa de falsos positivos a diferentes umbrales de decisión, permitiendo evaluar la capacidad del modelo para discriminar entre clases.

### Área bajo la curva ROC
El área bajo la curva ROC (AUC-ROC) mide la capacidad general del modelo para distinguir entre clases. Un valor de 1 representa una discriminación perfecta.

## Métricas para Modelos de Clustering

### Coeficiente de Silueta
El coeficiente de silueta mide qué tan bien se agrupan los datos dentro de un cluster y qué tan separados están de otros clusters. Valores cercanos a 1 indican una buena agrupación.

### Distorsión - Inercia
La distorsión mide la suma de las distancias al cuadrado entre los puntos y sus centroides, proporcionando una idea de la compacidad de los clusters.

### Coeficiente de Davies-Bouldin
El índice de Davies-Bouldin evalúa la relación entre la compacidad de los clusters y la distancia entre ellos. Valores más bajos indican clusters bien definidos y separados.

## Lista de Ejemplos

Los ejemplos presentados en esta sección son los siguientes:

- [Ejemplo 1: Métricas de Desempeño - Regresión](Ejemplo_1_performance_metrics_regression.ipynb)
- [Ejemplo 2: Métricas de Desempeño - Clasificación](Ejemplo_2_performance_metrics_classification.ipynb)
- [Ejemplo 3: Métricas de Desempeño - Clustering](Ejemplo_3_performance_metrics_clustering.ipynb)

## Referencias

[1]: Géron, A. (2019). Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow: Concepts, Tools, and Techniques to Build Intelligent Systems. O'Reilly Media.
