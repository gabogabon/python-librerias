"""Librería: datetime
Trabaja con fechas: formato, diferencias, suma de días y cálculo de edad."""
from datetime import datetime, date, timedelta


def calcular_edad(nacimiento: date) -> int:
    hoy = date.today()
    return hoy.year - nacimiento.year - (
        (hoy.month, hoy.day) < (nacimiento.month, nacimiento.day)
    )


def main():
    ahora = datetime.now()
    print("Fecha y hora actual:", ahora.strftime("%d/%m/%Y %H:%M:%S"))

    en_30_dias = date.today() + timedelta(days=30)
    print("Dentro de 30 días será:", en_30_dias.strftime("%A %d de %B de %Y"))

    fin_de_anio = date(date.today().year, 12, 31)
    print("Días que faltan para fin de año:", (fin_de_anio - date.today()).days)

    print("Edad de alguien nacido el 15/05/2000:", calcular_edad(date(2000, 5, 15)))

    fecha = datetime.strptime("25/12/2026", "%d/%m/%Y")
    print("Texto convertido a fecha:", fecha.date())


if __name__ == "__main__":
    main()
