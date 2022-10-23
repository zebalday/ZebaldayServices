def segToMins(segundos):
    
    minutos = int(segundos / 60)
    segundos = segundos % 60

    if segundos == 0:
        return (f"{minutos}:00")
    elif segundos < 10:
        return (f"{minutos}:0{segundos}")
    
    return (f"{minutos}:{segundos}")
