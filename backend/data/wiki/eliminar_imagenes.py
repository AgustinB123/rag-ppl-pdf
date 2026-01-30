#!/usr/bin/env python3
"""
Script para eliminar archivos de imagen (.jpg, .jpeg, .png)
"""

import os
import glob

def eliminar_imagenes(directorio='.'):
    """
    Elimina todos los archivos de imagen en el directorio especificado y sus subdirectorios
    
    Args:
        directorio: Ruta del directorio (por defecto el actual)
    """
    # Extensiones de archivos a buscar
    extensiones = ['.jpg', '.jpeg', '.png', '.JPG', '.JPEG', '.PNG']
    
    archivos_eliminados = []
    
    # Recorrer recursivamente todos los directorios
    for raiz, directorios, archivos in os.walk(directorio):
        for archivo in archivos:
            # Verificar si el archivo tiene una extensión de imagen
            if any(archivo.endswith(ext) for ext in extensiones):
                ruta_completa = os.path.join(raiz, archivo)
                try:
                    os.remove(ruta_completa)
                    archivos_eliminados.append(ruta_completa)
                    print(f"✓ Eliminado: {ruta_completa}")
                except Exception as e:
                    print(f"✗ Error al eliminar {ruta_completa}: {e}")
    
    # Resumen
    print(f"\n{'='*50}")
    print(f"Total de imágenes eliminadas: {len(archivos_eliminados)}")
    print(f"{'='*50}")

if __name__ == "__main__":
    # Solicitar confirmación antes de eliminar
    respuesta = input("¿Estás seguro de que deseas eliminar todas las imágenes (.jpg, .jpeg, .png)? (s/n): ")
    
    if respuesta.lower() in ['s', 'si', 'sí', 'yes', 'y']:
        eliminar_imagenes()
    else:
        print("Operación cancelada.")
