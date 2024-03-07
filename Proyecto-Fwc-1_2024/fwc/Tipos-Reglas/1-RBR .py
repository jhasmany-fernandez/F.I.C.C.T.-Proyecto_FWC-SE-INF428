# SE basado en reglas o RBR (Rule Based Reasoning)

class SistemaExpertoActividades:
    def __init__(self):
        self.base_conocimiento = [
            {"condicion": "clima == 'soleado'", "actividad": "jugar_futbol()"},
            {"condicion": "clima == 'lluvioso'", "actividad": "ver_peliculas()"},
            {"condicion": "clima == 'nublado'", "actividad": "caminar_en_el_parque()"},
            # Agrega más reglas según sea necesario
        ]

    def tomar_decision(self, contexto):
        for regla in self.base_conocimiento:
            condicion = regla["condicion"]
            actividad = regla["actividad"]
            
            if eval(condicion, {}, contexto):
                eval(actividad, {}, contexto)

def jugar_futbol():
    print("¡El clima es soleado! ¡Te recomiendo jugar al fútbol!")

def ver_peliculas():
    print("El clima está lluvioso. ¡Es un buen momento para ver películas!")

def caminar_en_el_parque():
    print("El clima está nublado. ¿Qué te parece dar un paseo por el parque?")

# Ejemplo de uso
sistema_actividades = SistemaExpertoActividades()
contexto_clima = {"clima": "soleado", "temperatura": 25, "viento": "ligero"}
sistema_actividades.tomar_decision(contexto_clima)