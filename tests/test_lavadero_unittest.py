# tests/test_lavadero_unittest.py

import unittest
# Importamos la clase Lavadero desde el módulo padre
from src.lavadero import Lavadero

class TestLavadero(unittest.TestCase):
    
    # Método que se ejecuta antes de cada test.
    # Es el equivalente del @pytest.fixture en este contexto.
    def setUp(self):
        """Prepara una nueva instancia de Lavadero antes de cada prueba."""
        self.lavadero = Lavadero()

    # ----------------------------------------------------------------------    
    # Función para resetear el estado cuanto terminamos una ejecución de lavado
    # ----------------------------------------------------------------------
    """
    def test_reseteo_estado_con_terminar(self):
        #Test 4: Verifica  terminar() resetea todas las flags y el estado.
        self.lavadero._hacer_lavado(True, True, True)
        self.lavadero._cobrar()
        self.lavadero.terminar()
        
        self.assertEqual(self.lavadero.fase, Lavadero.FASE_INACTIVO)
        self.assertFalse(self.lavadero.ocupado)
        self.assertFalse(self.lavadero.prelavado_a_mano)
        self.assertTrue(self.lavadero.ingresos > 0) # Los ingresos deben mantenerse
    """ 

    # ----------------------------------------------------------------------
    # TESTS  
    # ----------------------------------------------------------------------

    # Test 1. Cuando se crea un lavadero, éste no tiene ingresos, no está ocupado, está en fase 0 y todas las opciones de lavado (prelavado a mano, secado a mano y encerado) están puestas a false.
   
    """
    def test1_estado_inicial_correcto(self):
        # Test 1: Verifica que el estado inicial es Inactivo y con 0 ingresos.
        self.assertEqual(self.lavadero.fase, Lavadero.FASE_INACTIVO) # Fase inicial
        self.assertEqual(self.lavadero.ingresos, 0.0) # Ingresos iniciales
        self.assertFalse(self.lavadero.ocupado) # No está ocupadoS
        # Opciones de lavado iniciales a false.
        self.assertFalse(self.lavadero.prelavado_a_mano)
        self.assertFalse(self.lavadero.secado_a_mano)
        self.assertFalse(self.lavadero.encerado)
    """

    # Test 2. Cuando se intenta comprar un lavado con encerado pero sin secado a mano, se produce una ValueError.
    """
    def test2_excepcion_encerado_sin_secado(self):
        #Test 2: Comprueba que encerar sin secado a mano lanza ValueError.
        # _hacer_lavado: (Prelavado: False, Secado a mano: False, Encerado: True)
        with self.assertRaises(ValueError):
            self.lavadero._hacer_lavado(False, False, True)
    """

    # Test 3. Cuando se intenta hacer un lavado mientras que otro ya está en marcha, se produce una ValueError.
    """
    def test3_excepcion_lavado_mientras_otro_en_marcha(self):
        # Test 3: Comprueba que no se puede iniciar un lavado si ya hay otro en marcha
        # Primer lavado válido
        self.lavadero._hacer_lavado(False, False, False)

        # Segundo lavado mientras el primero sigue activo → ValueError
        with self.assertRaises(ValueError):
            self.lavadero._hacer_lavado(False, False, False)
    """

    # Test 4. Si seleccionamos un lavado con prelavado a mano, los ingresos de lavadero son 6,50€.

    """
    def test4_ingresos_prelavado_a_mano(self):
        # Test 4: Comprueba que un lavado con prelavado a mano cuesta 6,50 €
        # _hacer_lavado: (Prelavado: True, Secado a mano: False, Encerado: False)

        self.lavadero._hacer_lavado(True, False, False)

        # Avanzamos una fase para que se realice el cobro
        self.lavadero.avanzarFase()

        self.assertEqual(self.lavadero.ingresos, 6.50)
    """

    # Test 5. Si seleccionamos un lavado con secado a mano, los ingresos son 6,00€.
    """
    def test5_ingresos_secado_a_mano(self):
        # Test 5: Comprueba que un lavado con secado a mano cuesta 6,00 €
        # _hacer_lavado: (Prelavado: False, Secado a mano: True, Encerado: False)

        self.lavadero._hacer_lavado(False, True, False)

        # Avanzamos una fase para que se realice el cobro
        self.lavadero.avanzarFase()

        self.assertEqual(self.lavadero.ingresos, 6.00)
    """

    # Test 6. Si seleccionamos un lavado con secado a mano y encerado, los ingresos son 7,20€.

    """
    def test6_ingresos_secado_mano_y_encerado(self):
        # Test 6: Comprueba que un lavado con secado a mano y encerado cuesta 7,20 €
        # _hacer_lavado: (Prelavado: False, Secado a mano: True, Encerado: True)

        self.lavadero._hacer_lavado(False, True, True)

        # Avanzamos una fase para que se realice el cobro
        self.lavadero.avanzarFase()

        self.assertEqual(self.lavadero.ingresos, 7.20)
        """
    
    # Test 7. Si seleccionamos un lavado con prelavado a mano y secado a mano, los ingresos son 7,50€.

    """
    def test7_ingresos_prelavado_y_secado_mano(self):
        # Test 7: Comprueba que un lavado con prelavado a mano y secado a mano cuesta 7,50 €
        # _hacer_lavado: (Prelavado: True, Secado a mano: True, Encerado: False)

        self.lavadero._hacer_lavado(True, True, False)

        # Avanzamos una fase para que se realice el cobro
        self.lavadero.avanzarFase()

        self.assertEqual(self.lavadero.ingresos, 7.50)
        """

    # Test 8. Si seleccionamos un lavado con prelavado a mano, secado a mano y encerado, los ingresos son 8,70€.

    """
    def test8_ingresos_prelavado_secado_y_encerado(self):
    # Test 8: Comprueba que un lavado con prelavado a mano, secado a mano y encerado cuesta 8,70 €
    # _hacer_lavado: (Prelavado: True, Secado a mano: True, Encerado: True)

        self.lavadero._hacer_lavado(True, True, True)

    # Avanzamos una fase para que se realice el cobro
        self.lavadero.avanzarFase()

        self.assertEqual(self.lavadero.ingresos, 8.70)
    """
    
    # ----------------------------------------------------------------------
    # Tests de flujo de fases
    # Utilizamos la función def ejecutar_y_obtener_fases(self, prelavado, secado, encerado)
    # Estos tests dan errores ya que en el código original hay errores en las las fases esperados, en los saltos.
    # ----------------------------------------------------------------------

    # Test 9. Si seleccionamos un lavado sin extras y vamos avanzando fases, el lavadero pasa por las fases 0, 1, 3, 4, 5, 6, 0.

    """
    def test9_flujo_rapido_sin_extras(self):
        #Test 9: Simula el flujo rápido sin opciones opcionales.
        fases_esperadas = [0, 1, 3, 4, 5, 6, 0]
        # Ejecutar el ciclo completo y obtener las fases
        fases_obtenidas = self.lavadero.ejecutar_y_obtener_fases(prelavado=False, secado=False, encerado=False)
        
        # Verificar que las fases obtenidas coinciden con las esperadas
        self.assertEqual(fases_obtenidas, fases_esperadas, 
                        f"Secuencia de fases incorrecta.\nEsperadas: {fases_esperadas}\nObtenidas: {fases_obtenidas}")
    """

    # Test 10. Si seleccionamos un lavado con prelavado a mano y vamos avanzando fases, el lavadero pasa por las fases 0, 1, 2, 3, 4, 5, 6, 0.
    
    """
    def test10_flujo_con_prelavado(self):
        #Test 10: Flujo de fases para un lavado con prelavado a mano.
        
        fases_esperadas = [0, 1, 2, 3, 4, 5, 6, 0]

        fases_obtenidas = self.lavadero.ejecutar_y_obtener_fases(
            prelavado=True,
            secado=False,
            encerado=False
        )

        self.assertEqual(
            fases_obtenidas,
            fases_esperadas,
            f"Secuencia de fases incorrecta.\nEsperadas: {fases_esperadas}\nObtenidas: {fases_obtenidas}"
        )
        """


    # Test 11. Si seleccionamos un lavado con secado a mano y vamos avanzando fases, el lavadero pasa por las fases 0, 1, 3, 4, 5, 7, 0.
    """
    def test11_flujo_con_secado_mano(self):
        fases_esperadas = [0, 1, 3, 4, 5, 7, 0]

        fases_obtenidas = self.lavadero.ejecutar_y_obtener_fases(
            prelavado=False,
            secado=True,
            encerado=False
        )

        self.assertEqual(
            fases_obtenidas,
            fases_esperadas,
            f"Esperadas: {fases_esperadas} | Obtenidas: {fases_obtenidas}"
        )
    """

    # Test 12. Si seleccionamos un lavado con secado a mano y encerado, y vamos avanzando fases, el lavadero pasa por las fases 0, 1, 3, 4, 5, 7, 8, 0.

    """
    def test12_flujo_con_secado_mano_y_encerado(self):
        
        Test 12: Si seleccionamos un lavado con secado a mano y encerado y vamos avanzando fases,
        el lavadero pasa por las fases 0, 1, 3, 4, 5, 7, 8, 0.
        
        fases_esperadas = [0, 1, 3, 4, 5, 7, 8, 0]

        fases_obtenidas = self.lavadero.ejecutar_y_obtener_fases(
            prelavado=False,
            secado=True,
            encerado=True
        )

        self.assertEqual(
            fases_obtenidas,
            fases_esperadas,
            f"Secuencia incorrecta.\nEsperadas: {fases_esperadas}\nObtenidas: {fases_obtenidas}"
        )
        """
    
    # Test 13. Si seleccionamos un lavado con prelavado a mano, secado a mano y encerado, y vamos avanzando fases, el lavadero pasa por las fases 0, 1, 2, 3, 4, 5, 7, 8, 0.
    """
    def test14_flujo_prelavado_y_secado_mano(self):
        fases_esperadas = [0, 1, 2, 3, 4, 5, 7, 0]

        fases_obtenidas = self.lavadero.ejecutar_y_obtener_fases(
            prelavado=True,
            secado=True,
            encerado=False
        )

        self.assertEqual(
            fases_obtenidas,
            fases_esperadas,
            f"Secuencia incorrecta.\nEsperadas: {fases_esperadas}\nObtenidas: {fases_obtenidas}"
        )
    """

    # Test 14. Si seleccionamos un lavado con prelavado a mano, secado a mano y encerado, y vamos avanzando fases, el lavadero pasa por las fases 0, 1, 2, 3, 4, 5, 7, 8, 0.

    def test15_flujo_prelavado_secado_y_encerado(self):
        """
        Test 15: Si seleccionamos un lavado con prelavado a mano, secado a mano y encerado
        y vamos avanzando fases, el lavadero pasa por las fases
        0, 1, 2, 3, 4, 5, 7, 8, 0.
        """

        fases_esperadas = [0, 1, 2, 3, 4, 5, 7, 8, 0]

        fases_obtenidas = self.lavadero.ejecutar_y_obtener_fases(
            prelavado=True,
            secado=True,
            encerado=True
        )

        self.assertEqual(
            fases_obtenidas,
            fases_esperadas,
            f"Secuencia incorrecta.\nEsperadas: {fases_esperadas}\nObtenidas: {fases_obtenidas}"
        )











# Bloque de ejecución para ejecutar los tests si el archivo es corrido directamente
if __name__ == '__main__':
    unittest.main()