# lavadero.py

    # 1. Clase principal Lavadero

class Lavadero:
    """
    Simula el estado y las operaciones de un túnel de lavado de coches.
    Cumple con los requisitos de estado, avance de fase y reglas de negocio.
    """

    # 2. Definición de fases del lavadero como constantes de clase

    FASE_INACTIVO = 0 # Estado inicial, lavadero inactivo
    FASE_COBRANDO = 1 # Estado de cobro al cliente
    FASE_PRELAVADO_MANO = 2 # Estado de prelavado a mano
    FASE_ECHANDO_AGUA = 3 # Estado de echado de agua
    FASE_ENJABONANDO = 4  # Estado de enjabonado
    FASE_RODILLOS = 5 # Estado de paso por rodillos
    FASE_SECADO_AUTOMATICO = 6 # Estado de secado automático
    FASE_SECADO_MANO = 7 # Estado de secado a mano
    FASE_ENCERADO = 8 # Estado de encerado a man

    # 3. Constructor

    def __init__(self):
        """
        Constructor de la clase. Inicializa el lavadero.
        Cumple con el requisito 1.
        """
        # Atributos privados del lavadero:
        
        # Almacena los ingresos totales del lavadero
        self.__ingresos = 0.0
        # Estado inicial del lavadero
        self.__fase = self.FASE_INACTIVO
        # Indica si el lavadero está ocupado
        self.__ocupado = False
        # Opciones del lavado seleccionadas por el cliente
        self.__prelavado_a_mano = False
        self.__secado_a_mano = False
        self.__encerado = False
        # Asegura que el lavadero comienza en estado inactivo
        self.terminar() 

        # 4. Propiedades de acceso a los atributos privados

    @property # ¿Qué fase está actualmente el lavadero?
    def fase(self):
        """
        Devuelve la fase actual del lavadero.
        """
        return self.__fase

    @property # ¿Qué ingresos tiene el lavadero?
    def ingresos(self):
        """
        Devuelve los ingresos acumulados del lavadero.
        """
        return self.__ingresos

    @property # ¿Está ocupado el lavadero?
    def ocupado(self):
        """
        Devuelve si el lavadero está ocupado.
        """
        return self.__ocupado
    
    @property # ¿Se ha seleccionado prelavado a mano?
    def prelavado_a_mano(self):
        """
        Devuelve si se ha seleccionado prelavado a mano.
        """
        return self.__prelavado_a_mano

    @property # ¿Se ha seleccionado secado a mano?
    def secado_a_mano(self):
        """
        Devuelve si se ha seleccionado secado a mano.
        """
        return self.__secado_a_mano

    @property # ¿Se ha seleccionado encerado?
    def encerado(self):
        """
        Devuelve si se ha seleccionado encerado.
        """
        return self.__encerado
    
        # 5. Métodos principales del lavadero

    def terminar(self): # Reinicia el lavadero al estado inicial
        """
        Finaliza el lavado y devuelve el sistema a su estado inicial.
        Se utiliza al terminar un ciclo completo o para reiniciar el sistema.
        """
        self.__fase = self.FASE_INACTIVO # Estado inicial
        self.__ocupado = False # Lavadero libre
        self.__prelavado_a_mano = False # Lavado sin prelavado a mano
        self.__secado_a_mano = False # Lavado sin secado a mano
        self.__encerado = False # Lavado sin encerado
    
    def hacerLavado(self, prelavado_a_mano, secado_a_mano, encerado): # Inicia el nuevo ciclo de lavado
        """
        Inicia un nuevo ciclo de lavado, validando reglas de negocio.
        
        :raises RuntimeError: Si el lavadero está ocupado (Requisito 3). --> Esto hace que no se pueda iniciar un nuevo lavado si el lavadero ya está en uso.
        :raises ValueError: Si se intenta encerar sin secado a mano (Requisito 2). --> Esto asegura que no se pueda seleccionar encerado si no se ha seleccionado secado a mano.
        """

        # 6. Condiciones de inicio del lavado

        # Condición que evita iniciar un lavado si el lavadero está ocupado
        if self.__ocupado: # Si el lavadero ya está en uso
            raise RuntimeError("No se puede iniciar un nuevo lavado mientras el lavadero está ocupado") # Esto hace que no se pueda iniciar un nuevo lavado si el lavadero ya está en uso.

        # Condición que evita encerar sin secado a mano
        if not secado_a_mano and encerado: # Si no se ha seleccionado secado a mano pero sí encerado
            raise ValueError("No se puede encerar el coche sin secado a mano") # Esto asegura que no se pueda seleccionar encerado si no se ha seleccionado secado a mano.
        
        # Se inicializan las opciones y el estado del lavadero
        self.__fase = self.FASE_INACTIVO # Se inicia en fase inactiva
        self.__ocupado = True # Lavadero ocupado
        self.__prelavado_a_mano = prelavado_a_mano # Se asigna la opción de prelavado a mano
        self.__secado_a_mano = secado_a_mano # Se asigna la opción de secado a mano
        self.__encerado = encerado # Se asigna la opción de encerado

    def _hacer_lavado(self, prelavado_a_mano, secado_a_mano, encerado):
        """
          Método interno utilizado para pruebas unitarias.
         Aplica las mismas reglas de negocio que hacerLavado.
        """
        self.hacerLavado(prelavado_a_mano, secado_a_mano, encerado)
        
        # 7. Cobrar al cliente según las opciones seleccionadas

    def _cobrar(self):
        """
        Calcula y añade los ingresos según las opciones seleccionadas (Requisitos 4-8).
        Precio base: 5.00€ (Implícito, 5.00€ de base + 1.50€ de prelavado + 1.00€ de secado + 1.20€ de encerado = 8.70€)
        """
         # Precio base del lavado
        coste_lavado = 5.00
        
        # SE añade el coste del prelavado si está seleccionado
        if self.__prelavado_a_mano:
            coste_lavado += 1.50 
        
        # Se añade el coste del secado si está seleccionado
        if self.__secado_a_mano:
            coste_lavado += 1.20 
            
        # Se añade el coste del encerado si está seleccionado
        if self.__encerado:
            coste_lavado += 1.00 
            
        # Se suman los ingresos al total acumulado
        self.__ingresos += coste_lavado


        # 8. Avanza la fase del lavadero

    def avanzarFase(self):
       
       # Si el lavadero no está ocupado, no se avanza
        if not self.__ocupado:
            return

        # Fase inicial: se cobra al cliente
        if self.__fase == self.FASE_INACTIVO:
            coste_cobrado = self._cobrar()
            self.__fase = self.FASE_COBRANDO
            print(f" (COBRADO: {coste_cobrado:.2f} €) ", end="") # Muestra el importe cobrado al avanzar de fase

        # Tras cobrar, se decide si hay prelavado a mano
        elif self.__fase == self.FASE_COBRANDO:
            if self.__prelavado_a_mano:
                self.__fase = self.FASE_PRELAVADO_MANO
            else:
                self.__fase = self.FASE_ECHANDO_AGUA 
        
        # Se pasa del prelavado a mano al echado de agua
        elif self.__fase == self.FASE_PRELAVADO_MANO:
            self.__fase = self.FASE_ECHANDO_AGUA
        
        # Se pasa del agua al enjabonado
        elif self.__fase == self.FASE_ECHANDO_AGUA:
            self.__fase = self.FASE_ENJABONANDO

        # Se pasa del enjabonado a los rodillos
        elif self.__fase == self.FASE_ENJABONANDO:
            self.__fase = self.FASE_RODILLOS
        
        # Tras los rodillos, se decide el tipo de secado
        elif self.__fase == self.FASE_RODILLOS:
            if self.__secado_a_mano:
                self.__fase = self.FASE_SECADO_AUTOMATICO 

            else:
                self.__fase = self.FASE_SECADO_MANO
        
        # Finaliza el lavado tras el secado automático
        elif self.__fase == self.FASE_SECADO_AUTOMATICO:
            self.terminar()
        
        # Finaliza el lavado tras el secado a mano
        elif self.__fase == self.FASE_SECADO_MANO:

            self.terminar() 
        
        # Finaliza el lavado tras el encerado
        elif self.__fase == self.FASE_ENCERADO:
            self.terminar() 
        
        # Control de estados no válidos
        else:
            raise RuntimeError(f"Estado no válido: Fase {self.__fase}. El lavadero va a estallar...") 
        # Esto asegura que no se pueda avanzar a una fase no definida.

    
        # 9. Muestra por pantalla

    def imprimir_fase(self):
        fases_map = {
            self.FASE_INACTIVO: "0 - Inactivo",
            self.FASE_COBRANDO: "1 - Cobrando",
            self.FASE_PRELAVADO_MANO: "2 - Haciendo prelavado a mano",
            self.FASE_ECHANDO_AGUA: "3 - Echándole agua",
            self.FASE_ENJABONANDO: "4 - Enjabonando",
            self.FASE_RODILLOS: "5 - Pasando rodillos",
            self.FASE_SECADO_AUTOMATICO: "6 - Haciendo secado automático",
            self.FASE_SECADO_MANO: "7 - Haciendo secado a mano",
            self.FASE_ENCERADO: "8 - Encerando a mano",
        }
        print(fases_map.get(self.__fase, f"{self.__fase} - En estado no válido"), end="")


    def imprimir_estado(self):
        print("----------------------------------------")
        print(f"Ingresos Acumulados: {self.ingresos:.2f} €") # Muestra los ingresos acumulados con dos decimales
        print(f"Ocupado: {self.ocupado}") # Muestra si el lavadero está ocupado
        print(f"Prelavado a mano: {self.prelavado_a_mano}") # Muestra si se ha seleccionado prelavado a mano
        print(f"Secado a mano: {self.secado_a_mano}") # Muestra si se ha seleccionado secado a mano
        print(f"Encerado: {self.encerado}") # Muestra si se ha seleccionado encerado
        print("Fase: ", end="") # Muestra la fase actual
        self.imprimir_fase() # Imprime la descripción de la fase actual
        print("\n----------------------------------------")
        
       
        # 10. Pruebas unitarias.
        # No forma parte del lavadero.
       
    def ejecutar_y_obtener_fases(self, prelavado, secado, encerado): # Simula un ciclo completo y devuelve las fases visitadas
        """Ejecuta un ciclo completo y devuelve la lista de fases visitadas."""
        self.lavadero.hacerLavado(prelavado, secado, encerado)
        fases_visitadas = [self.lavadero.fase]
        
        while self.lavadero.ocupado:
            # Usamos un límite de pasos para evitar bucles infinitos en caso de error
            # Si se superan 15 fases, lanzamos una excepción
            # Esto es una medida de seguridad para pruebas unitarias
            if len(fases_visitadas) > 15:
                raise Exception("Bucle infinito detectado en la simulación de fases.")
            self.lavadero.avanzarFase()
            fases_visitadas.append(self.lavadero.fase)

         # Al finalizar, devolvemos la lista de fases visitadas
        return fases_visitadas