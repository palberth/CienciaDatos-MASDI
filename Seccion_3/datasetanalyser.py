import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class DatasetAnalyzer:
    def __init__(self, dataframe):
        """
        Inicializa la clase con el dataframe para analizar.
        """
        self.df = dataframe

    def check_missing_and_anomalies(self):
        """
        Comprueba valores faltantes y datos anómalos en el dataframe.
        """
        # Revisar datos faltantes
        print("Valores faltantes por columna:")
        print(self.df.isnull().sum())
        
        # Detectar valores negativos en columnas que no deberían tenerlos
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns
        print("\nValores negativos detectados en columnas numéricas:")
        for col in numeric_cols:
            if (self.df[col] < 0).any():
                print(f"{col}: {self.df[self.df[col] < 0].shape[0]} valores negativos")

    def univariate_analysis(self, columns=None, plot_type='histogram', fig_size=(15, 10)):
        """
        Realiza análisis univariado para una o más columnas.
        
        Parameters:
        - columns (list or None): Lista de nombres de columnas para visualizar. Si es None, se usan todas las columnas numéricas.
        - plot_type (str): Tipo de gráfico ('histogram' o 'boxplot').
        - fig_size (tuple): Tamaño de la figura (ancho, alto).
        """
        # Si no se especifican columnas, tomar todas las numéricas
        if columns is None:
            columns = self.df.select_dtypes(include=[np.number]).columns
        
        # Definir el número de filas y columnas para el layout de subplots
        num_vars = len(columns)
        cols = 3  # Número de columnas para la figura
        rows = (num_vars // cols) + (num_vars % cols > 0)  # Calcular el número de filas necesarias
        
        # Crear la figura con el tamaño proporcionado
        fig, axes = plt.subplots(rows, cols, figsize=fig_size)
        axes = axes.flatten()  # Aplanar los ejes para fácil acceso

        # Generar los gráficos para cada columna
        for i, column in enumerate(columns):
            if plot_type == 'histogram':
                sns.histplot(self.df[column], bins=20, kde=True, ax=axes[i])
                #axes[i].set_title(f"Distribución de {column}")
            elif plot_type == 'boxplot':
                sns.boxplot(x=self.df[column], ax=axes[i])
                #axes[i].set_title(f"Boxplot de {column}")
        
        # Eliminar los subplots sobrantes si hay menos variables que subplots
        for j in range(i + 1, len(axes)):
            fig.delaxes(axes[j])
        
        plt.tight_layout()
        plt.show()

    def bivariate_analysis(self, x_col, y_col, hue=None, plot_type='scatter'):
        """
        Realiza análisis bivariado entre dos columnas específicas.
        """
        plt.figure(figsize=(8, 5))
        if plot_type == 'scatter':
            sns.scatterplot(x=x_col, y=y_col, hue=hue, data=self.df)
            plt.title(f"Relación entre {x_col} y {y_col}")
        elif plot_type == 'violin':
            sns.violinplot(x=x_col, y=y_col, data=self.df)
            plt.title(f"Distribución de {y_col} por {x_col}")
        plt.show()

    def density_analysis(self, columns=None, target_col=None, fig_size=(15, 10)):
        """
        Realiza análisis de densidad (KDE) para una o más columnas en función de una categoría específica.
        
        Parameters:
        - columns (list or None): Lista de nombres de columnas para visualizar. Si es None, se usan todas las columnas numéricas.
        - target_col (str): Columna objetivo para comparar las categorías.
        - fig_size (tuple): Tamaño de la figura (ancho, alto).
        """
        # Verificar que la columna objetivo esté especificada
        if target_col is None:
            print("Debe especificar una columna objetivo para el análisis de densidad.")
            return
        
        # Si no se especifican columnas, tomar todas las numéricas
        if columns is None:
            columns = self.df.select_dtypes(include=[np.number]).columns
        
        # Definir el número de filas y columnas para el layout de subplots
        num_vars = len(columns)
        cols = 3  # Número de columnas para la figura
        rows = (num_vars // cols) + (num_vars % cols > 0)  # Calcular el número de filas necesarias
        
        # Crear la figura con el tamaño proporcionado
        fig, axes = plt.subplots(rows, cols, figsize=fig_size)
        axes = axes.flatten()  # Aplanar los ejes para fácil acceso

        # Generar gráficos de densidad para cada columna en función de la columna objetivo
        for i, column in enumerate(columns):
            sns.kdeplot(data=self.df, x=column, hue=target_col, ax=axes[i], fill=True, warn_singular=False)
            axes[i].set_title(f"Densidad de {column} por {target_col}")
        
        # Eliminar los subplots sobrantes si hay menos gráficos que subplots
        for j in range(i + 1, len(axes)):
            fig.delaxes(axes[j])
        
        plt.tight_layout()
        plt.show()
        
    def correlation_analysis(self, fig_size=(10, 8)):
        """
        Realiza análisis de correlación entre las características del dataframe.
        """
        plt.figure(figsize=fig_size)
        corr = self.df.corr()
        sns.heatmap(corr, annot=True, cmap="coolwarm")
        plt.title("Matriz de Correlación")
        plt.show()

    def group_and_summary(self, group_by_column):
        """
        Agrupa los datos por una columna específica y muestra estadísticas resumidas.
        """
        grouped_summary = self.df.groupby(group_by_column).mean()
        print(f"Resumen estadístico agrupado por {group_by_column}:")
        print(grouped_summary)
        return grouped_summary

    def additional_visualization(self, x_col, y_col):
        """
        Crea visualizaciones adicionales para destacar insights específicos.
        """
        plt.figure(figsize=(8, 5))
        sns.boxplot(x=x_col, y=y_col, data=self.df)
        plt.title(f"{y_col} por {x_col}")
        plt.show()
