def calificandoEstudiantes(calificaciones):
    for i in range(len(calificaciones)):
        if calificaciones[i] > 40:
            x = [int(n) for n in str(calificaciones[i])]
            if x[1] != 5 and x[1] != 0:
                if x[1] > 5:
                    redondeo = str(x[0] + 1) + "0"
                    if int(redondeo) - calificaciones[i] < 3:
                        calificaciones_redondeadas.append(int(redondeo))
                    else: 
                        calificacion = str(x[0]) + str(x[1])
                        calificaciones_redondeadas.append(int(calificacion))
                else:
                    redondeo = str(x[0]) + "5"
                    if int(redondeo) - calificaciones[i] < 3:
                        calificaciones_redondeadas.append(int(redondeo))
                    else: 
                        calificacion = str(x[0]) + str(x[1])
                        calificaciones_redondeadas.append(int(calificacion))
            else:
                calificaciones_redondeadas.append(calificaciones[i])
        else:
            calificaciones_redondeadas.append(calificaciones[i])
    return calificaciones_redondeadas

calificaciones = [22, 87, 54, 66, 95, 99]
calificaciones_redondeadas = []
calificandoEstudiantes(calificaciones)
print("Las calificaciones de los estudiantes han sido las siguientes: " + str(calificaciones))
print("Las calificaciones redondeadas de los estudiantes son las siguientes: " + str(calificaciones_redondeadas))