---
title: Deserializar JSON en C#
description: 
published: true
date: 2024-08-16T18:54:40.263Z
tags: 
editor: markdown
dateCreated: 2024-08-16T18:10:56.467Z
---

# Deserializar JSON a un Objeto Dinámico en C# (.NET Framework 4.6.1)

Para deserializar un JSON en formato string y convertirlo en un objeto dinámico en C# con .NET Framework 4.6.1, se puede utilizar la biblioteca **Json.NET** (Newtonsoft.Json). A continuación, se detallan los pasos necesarios.

## Pasos para Deserializar un JSON

### 1. Agregar la Referencia a Newtonsoft.Json

Si estás usando Visual Studio, puedes agregar el paquete `Newtonsoft.Json` mediante NuGet:

- Haz clic derecho en tu proyecto > **Administrar paquetes NuGet**.
- Busca `Newtonsoft.Json` y haz clic en **Instalar**.

### 2. Deserializar el JSON a un Objeto Dinámico

Una vez que tengas `Newtonsoft.Json` instalado, puedes deserializar un JSON string a un objeto dinámico utilizando el método `JsonConvert.DeserializeObject`.

### Ejemplo de Código

```csharp
using System;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;

class Program
{
    static void Main(string[] args)
    {
        string jsonString = @"{
                                'Nombre': 'Juan',
                                'Edad': 30,
                                'Direccion': {
                                    'Calle': 'Calle Falsa 123',
                                    'Ciudad': 'Ciudad Ejemplo'
                                }
                            }";

        // Deserializar el JSON a un objeto dinámico
        dynamic obj = JsonConvert.DeserializeObject<dynamic>(jsonString);

        // Acceder a las propiedades dinámicamente
        Console.WriteLine($"Nombre: {obj.Nombre}");
        Console.WriteLine($"Edad
