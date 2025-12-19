    # 1. Importamos la clase Lavadero desde el módulo lavadero

# main_app.py

# Importar la clase desde el otro archivo (módulo)
from lavadero import Lavadero

    # 2. Simulación de lavado con diferentes opciones

# MODIFICACIÓN CLAVE AQUÍ: La función ahora acepta 3 argumentos
def ejecutarSimulacion(lavadero, prelavado, secado_mano, encerado):
    """
    Simula el proceso de lavado para un vehículo con las opciones dadas.
    Ahora acepta una instancia de lavadero.

    :param lavadero: Instancia de Lavadero.
    :param prelavado: bool, True si se solicita prelavado a mano.
    :param secado_mano: bool, True si se solicita secado a mano.
    :param encerado: bool, True si se solicita encerado.
    """
    
    print("--- INICIO: Prueba de Lavado con Opciones Personalizadas ---")
    
    # Mostrar las opciones solicitadas
    print(f"Opciones solicitadas: [Prelavado: {prelavado}, Secado a mano: {secado_mano}, Encerado: {encerado}]")

    # 1. Iniciar el lavado
    try:
        # Esto establece las opciones y pasa a Fase 0 (Inactivo, pero Ocupado=True)
        lavadero.hacerLavado(prelavado, secado_mano, encerado)
        print("\nCoche entra. Estado inicial:")
        lavadero.imprimir_estado()

        # 2. Avanza por las fases
        print("\nAVANZANDO FASE POR FASE:")
        
        # Usamos un contador para evitar bucles infinitos en caso de error o bucles inesperados
        pasos = 0
        while lavadero.ocupado and pasos < 20: 
            # El cobro ahora ocurre en la primera llamada a avanzarFase (transición 0 -> 1)
            lavadero.avanzarFase()
            print(f"-> Fase actual: ", end="")
            lavadero.imprimir_fase()
            print() 
            pasos += 1
        
        print("\n----------------------------------------")
        print("Lavado completo. Estado final:")
        lavadero.imprimir_estado()
        print(f"Ingresos acumulados: {lavadero.ingresos:.2f} €")
        print("----------------------------------------")
        
    except ValueError as e: # Captura la excepción de regla de negocio (Requisito 2)
        print(f"ERROR DE ARGUMENTO: {e}")
    except RuntimeError as e: # Captura la excepción de estado (Requisito 3)
        print(f"ERROR DE ESTADO: {e}")
    except Exception as e:
        print(f"ERROR INESPERADO: {e}")


# Punto de entrada (main): Aquí pasamos los parámetros
if __name__ == "__main__":
    
    lavadero_global = Lavadero() # Usamos una única instancia para acumular ingresos
""""
    # EJEMPLO 1: Lavado completo con prelavado, secado a mano, con encerado (Requisito 8 y 14)
    # Precio esperado: 5.00 + 1.50 + 1.00 + 1.20 = 8.70 €
    print("\n=======================================================")
    print("EJEMPLO 1: Prelavado (S), Secado a mano (S), Encerado (S)")
    ejecutarSimulacion(lavadero_global, prelavado=True, secado_mano=True, encerado=True)
    
    # EJEMPLO 2: Lavado rápido sin extras (Requisito 9)
    # Precio esperado: 5.00 €
    print("\n=======================================================")
    print("EJEMPLO 2: Sin extras (Prelavado: N, Secado a mano: N, Encerado: N)")
    ejecutarSimulacion(lavadero_global, prelavado=False, secado_mano=False, encerado=False)

    # EJEMPLO 3: Lavado con encerado, pero sin secado a mano (Debe lanzar ValueError - Requisito 2)
    print("\n=======================================================")
    print("EJEMPLO 3: ERROR (Encerado S, Secado a mano N)")
    ejecutarSimulacion(lavadero_global, prelavado=False, secado_mano=False, encerado=True)

    # EJEMPLO 4: Lavado con prelavado a mano (Requisito 4 y 10)
    # Precio esperado: 5.00 + 1.50 = 6.50 €
    print("\n=======================================================")
    print("EJEMPLO 4: Prelavado (S), Secado a mano (N), Encerado (N)")
    ejecutarSimulacion(lavadero_global, prelavado=True, secado_mano=False)

    print("\n=======================================================")
print("EJEMPLO ERROR 2: Intentar iniciar un lavado estando ocupado")
"""


# EJEMPLO ERROR 2: Intentar iniciar un lavado estando ocupado (Requisito 3)
"""
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
"""

# EJEMPLO ERROR 3: Precio incorrecto del secado a mano (Requisito 7)
"""
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
"""

# EJEMPLO ERROR 4: Fase incorrecta tras rodillos (sin secado a mano) (Requisito 13)
"""
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
"""

# EJEMPLO ERROR 5: Fase incorrecta tras rodillos (con secado a mano y encerado) (Requisito 13)
""""
print("\n=======================================================")
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
"""

"""
# EJEMPLO ERROR 6: Uso de atributo inexistente self.lavadero
print("\n=======================================================")
print("EJEMPLO ERROR 6: Uso de atributo inexistente self.lavadero")

lavadero_error6 = Lavadero()

# Llamamos al método de prueba
lavadero_error6.ejecutar_y_obtener_fases(prelavado=False,
                                         secado=False,
                                         encerado=False)
"""