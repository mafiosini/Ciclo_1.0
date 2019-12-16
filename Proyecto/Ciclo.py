from math import sqrt

class Ciclo:
    def __init__(self, frenado, aceleracion, tramos, dist_tramo):
        assert (frenado < 0) and (frenado, int), "El valor ingresado debe ser negativo y un número entero"
        assert (aceleracion > 0) and (aceleracion, int), "El valor ingresado debe ser negativo y un número entero"
        assert (tramos > 0) and (tramos, int), "El valor ingresado debe ser positivo y un número entero"
        assert (dist_tramo > 0) and (dist_tramo, int), "El valor ingresado debe ser positivo y un número entero"
        
        self.f = frenado
        self.a = aceleracion
        self.t = tramos
        self.dt = dist_tramo/1000
        self.list_tra = []
        self.vel = []
       
    def cantidad_tramos(self):
        i = 0
        while i != self.t:
            self.list_tra.append(i)
            i += 1
        return self.list_tra
    
    def velmax(self):
        for i in self.list_tra:
            v = abs(int(input("Ingrese la velocidad máxima del tramo: ")))
            self.vel.append(v)
            
        return self.vel
    
    def diccionario(self):
        dic = dict(zip(self.cantidad_tramos(), self.velmax()))
        return dic
    
    def ecuacion_tiempo_a(self):
        
        #Ecuación de aceleración
        
        diccionario = self.diccionario()
        diccionario = list(diccionario.values())
        
        tiempo_inicio = abs(sqrt((2*self.dt)/self.a))
        velocidad_inicio = self.a * tiempo_inicio
        #Comprobar que la velocidad inicial alcanzada en el tramo no es mayor a la velocidad máxima, si lo es se reemplaza
        if (velocidad_inicio > diccionario[0]):
            velocidad_inicio = diccionario[0]
        
        
        a = 0.5 * self.a
        b = velocidad_inicio
        c = -self.dt
        #Resolucion de las raices
        x1 = (-b + sqrt(b**2 - 4*a*c))/2*a
        x2 = (-b - sqrt(b**2 - 4*a*c))/2*a
        
        #Retornar solamente el tiempo positivo
        if x1 > 0:
            return x1
        
        elif x2 > 0:
            return x2
    
    def ecuacion_tiempo_b(self):
        
        #Ecuación de frenado

        diccionario = self.diccionario()
        diccionario = list(diccionario.values())
        
        tiempo_inicio = abs(sqrt((2*self.dt)/self.a))
        velocidad_inicio = self.a * tiempo_inicio
        #Comprobar que la velocidad inicial alcanzada en el tramo no es mayor a la velocidad máxima, si lo es se reemplaza
        if (velocidad_inicio > diccionario[0]):
            velocidad_inicio = diccionario[0]
        
        
        a = 0.5 * self.f
        b = velocidad_inicio
        c = -self.dt
        #Resolucion de las raices
        x1 = (-b + sqrt(b**2 - 4*a*c))/2*a
        x2 = (-b - sqrt(b**2 - 4*a*c))/2*a
        
        #Retornar solamente el tiempo positivo
        if x1 > 0:
            return x1
        
        elif x2 > 0:
            return x2
    
    def velocidad(self):
        velocidades = []
        tiempo = []
        velmax = self.diccionario()
        velmax = list(velmax.values())
        
        tiempo_inicio = abs(sqrt((2*self.dt)/self.a))

        velocidad_inicio = self.a * tiempo_inicio
        
        if (velocidad_inicio >= velmax[0]):
            velocidad_inicio = velmax[0]
            velocidades.append(velocidad_inicio)
        else:
            velocidades.append(velocidad_inicio)
            
        velocidad_final = self.a * self.ecuacion_tiempo_a() + velocidad_inicio

        i = 1

        if self.t == 1:
            return velocidades

        else:

            while i != self.t:

                #Comprobar si el scoop debe frenar en el tramo
                if velocidad_inicio > velmax[i]:      

                    a = 0.5 * self.f
                    b = velocidad_inicio
                    c = -self.dt
                    #Resolucion de las raices
                    x1 = (-b + sqrt(b**2 - 4*a*c))/2*a
                    x2 = (-b - sqrt(b**2 - 4*a*c))/2*a
        
                    #Retornar solamente el tiempo positivo
                    if x1 > 0:
                        
                        velocidad_final = self.f * x1 + velocidad_inicio
                        
                        if velocidad_final >= velmax[i]:
                            velocidad_final = velmax[i]
                            velocidad_inicio = velocidad_final
                            velocidades.append(velocidad_final)
                        else:
                            velocidad_inicio = velocidad_final
                            velocidades.append(velocidad_final)

                        i += 1
        
                    elif x2 > 0:
                        
                        velocidad_final = self.f * x2 + velocidad_inicio
                        
                        if velocidad_final >= velmax[i]:
                            velocidad_final = velmax[i]
                            velocidad_inicio = velocidad_final
                            velocidades.append(velocidad_final)
                        else:
                            velocidad_inicio = velocidad_final
                            velocidades.append(velocidad_final)

                        i += 1

                        
            #Comprobar si el scoop debe acelerar en el tramo
                elif velocidad_inicio < velmax[i]:
                    a = 0.5 * self.a
                    b = velocidad_inicio
                    c = -self.dt
                    #Resolucion de las raices
                    x1 = (-b + sqrt(b**2 - 4*a*c))/2*a
                    x2 = (-b - sqrt(b**2 - 4*a*c))/2*a
        
                    #Retornar solamente el tiempo positivo
                    if x1 > 0:
                        
                        velocidad_final = self.a * x1 + velocidad_inicio
                        
                        if velocidad_final >= velmax[i]:
                            velocidad_final = velmax[i]
                            velocidad_inicio = velocidad_final
                            velocidades.append(velocidad_final)
                        else:
                            velocidad_inicio = velocidad_final
                            velocidades.append(velocidad_final)

                        i += 1
        
                    elif x2 > 0:
                
                        velocidad_final = self.a * x2 + velocidad_inicio
                        
                        if velocidad_final >= velmax[i]:
                            velocidad_final = velmax[i]
                            velocidad_inicio = velocidad_final
                            velocidades.append(velocidad_final)
                        else:
                            velocidad_inicio = velocidad_final
                            velocidades.append(velocidad_final)

                        i += 1
                        
        return velocidades

    def tiempo(self):
        tiempo = []
        tiempo_inicio = abs(sqrt((2*self.dt)/self.a))
        tiempo.append(tiempo_inicio)

        velocidad_inicio = self.a * tiempo_inicio
        
        if (velocidad_inicio >= velmax[0]):
            velocidad_inicio = velmax[0]
            
        velocidad_final = self.a * self.ecuacion_tiempo_a() + velocidad_inicio

        i = 1

        if t == 1:
            return tiempo

        else:
            while i != self.t:

                #Comprobar si el scoop debe frenar en el tramo
                if velocidad_inicio > velmax[i]:      

                    a = 0.5 * self.f
                    b = velocidad_inicio
                    c = -self.dt
                    #Resolucion de las raices
                    x1 = (-b + sqrt(b**2 - 4*a*c))/2*a
                    x2 = (-b - sqrt(b**2 - 4*a*c))/2*a
        
                    #Retornar solamente el tiempo positivo
                    if x1 > 0:
                        
                        velocidad_final = self.f * x1 + velocidad_inicio
                        
                        if velocidad_final >= velmax[i]:
                            velocidad_final = velmax[i]
                            velocidad_inicio = velocidad_final
                            tiempo.append(x1)
                        else:
                            velocidad_inicio = velocidad_final
                            tiempo.append(x1)

                        i += 1
        
                    elif x2 > 0:
                        
                        velocidad_final = self.f * x2 + velocidad_inicio
                        
                        if velocidad_final >= velmax[i]:
                            velocidad_final = velmax[i]
                            velocidad_inicio = velocidad_final
                            tiempo.append(x2)
                        else:
                            velocidad_inicio = velocidad_final
                            tiempo.append(x2)

                        i += 1
                        

            #Comprobar si el scoop debe acelerar en el tramo
                elif velocidad_inicio < velmax[i]:
                    a = 0.5 * self.a
                    b = velocidad_inicio
                    c = -self.dt
                    #Resolucion de las raices
                    x1 = (-b + sqrt(b**2 - 4*a*c))/2*a
                    x2 = (-b - sqrt(b**2 - 4*a*c))/2*a
        
                    #Retornar solamente el tiempo positivo
                    if x1 > 0:
                        
                        velocidad_final = self.a * x1 + velocidad_inicio
                        
                        if velocidad_final >= velmax[i]:
                            velocidad_final = velmax[i]
                            velocidad_inicio = velocidad_final
                            tiempo.append(x1)
                        else:
                            velocidad_inicio = velocidad_final
                            tiempo.append(x1)

                        i += 1
        
                    elif x2 > 0:
                
                        velocidad_final = self.a * x2 + velocidad_inicio
                        
                        if velocidad_final >= velmax[i]:
                            velocidad_final = velmax[i]
                            velocidad_inicio = velocidad_final
                            tiempo.append(x2)
                        else:
                            velocidad_inicio = velocidad_final
                            tiempo.append(x2)

                        i += 1

        return sum(tiempo)



        
