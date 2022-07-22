from datetime import datetime, timedelta

class Cadastro:

    def __init__(self):
        self.momento_cadastro = datetime.today()

    def tempo_cadastro(self):
        agora = datetime.today() + timedelta(days=15, minutes=20, seconds=30)
        return (agora - self.momento_cadastro)
