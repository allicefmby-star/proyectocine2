# tu_app/create_seats.py
import os
import django

# Configura el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cine.settings')
django.setup()

from cinema.models import Auditorium, Seat
from django.db import transaction

def number_to_letter(n):
    """Convierte un número entero a su representación de letra (1=A, 2=B)."""
    if 1 <= n <= 26:
        return chr(64 + n)
    return str(n) # En caso de que haya más de 26 filas

@transaction.atomic
def generate_auditorium_seats():
    """Genera asientos para todos los auditorios existentes."""
    print("Generando asientos para todos los auditorios...")
    auditoriums = Auditorium.objects.all()

    if not auditoriums:
        print("No se encontraron auditorios. Por favor, crea uno primero en el panel de administración.")
        return

    for aud in auditoriums:
        # Borra los asientos viejos para evitar duplicados
        Seat.objects.filter(auditorium=aud).delete()
        
        seats_to_create = []
        for row_num in range(1, aud.total_rows + 1):
            row_letter = number_to_letter(row_num)
            for col_num in range(1, aud.total_cols + 1):
                seats_to_create.append(
                    Seat(auditorium=aud, row=row_letter, col=col_num, seat_type='standard')
                )
        
        Seat.objects.bulk_create(seats_to_create)
        print(f"✅ Se crearon {len(seats_to_create)} asientos para el auditorio '{aud.name}'.")

if __name__ == '__main__':
    generate_auditorium_seats()