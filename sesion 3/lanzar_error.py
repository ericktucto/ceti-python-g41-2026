class SaldoInsuficienteError(Exception):
    pass


raise SaldoInsuficienteError("No tienes suficiente saldo")