# Ejecución y Depuración

En este apartado muestro, en primer lugar, la corrección del código y, después, la ejecución y depuración del código. Muestro en cada apartado las correcciones realizadas.

---

# 1. Corrección del código

- En mi IDE, utilizaré la herramienta de Ejecución y Depuración que viene integrada en el entorno para ejecutar, depurar, ver los errores del código y corregirlos.

En primer lugar, desde la propiar herramienta de depuración crearé un archivo .json para la automatización. En mi caso, le he creado dentro del propio proyecto y muestro la herramienta preparada para depurar los archuvos.

![Creación archivo .json para la automatización](img/Ejecucion_depuracion/ejecucion_depuracion_json.png)

- Error 1. Iniciar un lavado estando ocupado --> El tipo de excepción que se produce no es correcto, debe lanzarse _ValueError_ y no _RuntimeError_.

Mediante la ejecución de dos llamadas consecutivas al método hacerLavado sin finalizar el primer ciclo, y usando un breakpoint en la validación de estado, compruebo que el sistema detecta que el lavadero está ocupado y lanza una excepción.

![Error1](img/Ejecucion_depuracion(error1.png)

Solución:

``` raise ValueError("No se puede iniciar un nuevo lavado mientras el lavadero está ocupado")```
 

Ejemplo añadido al main para ejecutar la depuración y probar el error:

```
lavadero_error = Lavadero()

try:
    # Primer lavado (arranca correctamente)
    lavadero_error.hacerLavado(prelavado_a_mano=False,
                               secado_a_mano=False,
                               encerado=False)

    print("Primer lavado iniciado correctamente")

    # Segundo lavado SIN terminar el primero
    lavadero_error.hacerLavado(prelavado_a_mano=True,
                               secado_a_mano=False,
                               encerado=False)

except Exception as e:
    print(f"EXCEPCIÓN CAPTURADA: {type(e).__name__} -> {e}") # Esperado: RuntimeError
```


- Error 2. Precio incorrecto del secado a mano --> Según el enunciado, el total deberían de ser 6€ y no 6,20€.

![Error2](img/Ejecucion_depuracion(error2.png)

Solución:

```      if self.__secado_a_mano: 
	 coste_lavado += 1.00 ```

Ejemplo añadido al main para ejecutar la depuración y probar el error:

```
print("\n=======================================================")
print("EJEMPLO ERROR 3: Precio incorrecto del secado a mano")

lavadero_error3 = Lavadero()

# Lavado SOLO con secado a mano
lavadero_error3.hacerLavado(prelavado_a_mano=False,
                            secado_a_mano=True,
                            encerado=False)

# Avanzamos SOLO UNA FASE para que se cobre
lavadero_error3.avanzarFase()

print(f"Ingresos tras el cobro: {lavadero_error3.ingresos:.2f} €")
```

- Error 3: Fase incorrecta tras rodillos (condición invertida) --> Sin secado a mano debería de pasar a secado automático (fase 6).

![Error3](img/Ejecucion_depuracion(error3.png)

Solución:

```
       elif self.__fase == self.FASE_RODILLOS:
            if self.__secado_a_mano:
                self.__fase = self.FASE_SECADO_MANO

            else:
                self.__fase = self.FASE_SECADO_AUTOMATICO
```
 
Ejemplo añadido al main para ejecutar la depuración y probar el error:


```
print("\n=======================================================")
print("EJEMPLO ERROR 4: Fase incorrecta tras rodillos (sin secado a mano)")

lavadero_error4 = Lavadero()

# Lavado SIN secado a mano
lavadero_error4.hacerLavado(prelavado_a_mano=False,
                            secado_a_mano=False,
                            encerado=False)

# Avanzamos fases manualmente
while lavadero_error4.ocupado:
    print(f"Fase actual: {lavadero_error4.fase}")
    lavadero_error4.avanzarFase()

print(f"Fase final: {lavadero_error4.fase}")
```

- Error 4. La fase de encerado (fase 8) nunca se ejecuta --> La fase 8 nunca se ejecuta, incumpliendo el enunciado.

![Error4](img/Ejecucion_depuracion(error4.png)

Solución:

```
elif self.__fase == self.FASE_SECADO_MANO:
    if self.__encerado:
        self.__fase = self.FASE_ENCERADO
    else:
        self.terminar()

elif self.__fase == self.FASE_ENCERADO:
    self.terminar()
```

Ejemplo añadido al main para ejecutar la depuración y probar el error:

```
print("\=======================================================")
print("EJEMPLO ERROR 5: La fase de encerado nunca se ejecuta")

lavadero_error5 = Lavadero()

# Lavado con secado a mano y encerado
lavadero_error5.hacerLavado(prelavado_a_mano=False,
                            secado_a_mano=True,
                            encerado=True)

# Avanzamos fases y mostramos todas
while lavadero_error5.ocupado:
    print(f"Fase actual: {lavadero_error5.fase}")
    lavadero_error5.avanzarFase()

print(f"Fase final: {lavadero_error5.fase}")
```

---

Adjunto los archivos corregidos:

- 
- 
