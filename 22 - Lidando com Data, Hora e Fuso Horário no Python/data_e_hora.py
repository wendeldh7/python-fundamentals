# Introdução ao módulo datetime

# O que é o módulo datetime?
# Omódulo 'datetime' em Python é usado para lidar com datas e horas. Ele possui várias classes úteis como date, time e timedelta.

# Exemplo

from datetime import datetime

d = datetime.date(2023, 10, 1)
print(d)  # Saída: 2023-10-01

# Manipulação de datas e horas

# Introdução
#  Podemos criar e manipular objetos date, time e datetime de várias maneiras. Por exemplo, podemos adicionar e subtrair datas, verificar a diferença entre datas e muito mais.

# Exemplo

from datetime import datetime, timedelta
from datetime import date

# Criando um objeto datetime
d1 = datetime(2023, 10, 1, 12, 0, 0)
d2 = datetime(2023, 10, 2, 12, 0, 0)

# Calculando a diferença entre duas datas
delta = d2 - d1
print(delta)  # Saída: 1 day, 0:00:00

# Adicionando e subtraindo dias
d3 = d1 + timedelta(days=5)
print(d3)  # Saída: 2023-10-06 12:00:00

# Subtraindo dias
d4 = d1 - timedelta(days=5)
print(d4)  # Saída: 2023-09-26 12:00:00

# Comparando datas
print(d1 < d2)  # Saída: True
print(d1 > d2)  # Saída: False

# Conversão e formatação de datas e horas

# Introdução
# Python também permite converter e formatar datas e horas. Para isso, usamos os métodos 'strftime' (string format time) e 'strptime' (string parse time).

# Exemplo

from datetime import datetime
from datetime import date

# Criando um objeto datetime
d1 = datetime(2023, 10, 1, 12, 0, 0)
d2 = datetime(2023, 10, 2, 12, 0, 0)

# Formatando datas
print(d1.strftime("%d/%m/%Y"))  # Saída: 01/10/2023
print(d1.strftime("%H:%M:%S"))  # Saída: 12:00:00

# Convertendo strings em datas
data_str = "01/10/2023 12:00:00"
d3 = datetime.strptime(data_str, "%d/%m/%Y %H:%M:%S")
print(d3)  # Saída: 2023-10-01 12:00:00

# Trabalhando com timezones

# Introdução
# Quando trabalhamos com data e hora, lidar com fusos horários é uma necessidade comum. Python facilita isso através do módulo'pytz'.

# Exemplo

from datetime import datetime
import pytz

# Criando um objeto timezone
tz = pytz.timezone("America/Sao_Paulo")

# Criando um objeto datetime com timezone
d1 = tz.localize(datetime(2023, 10, 1, 12, 0, 0))
d2 = tz.localize(datetime(2023, 10, 2, 12, 0, 0))

# Formatando datas
print(d1.strftime("%d/%m/%Y %H:%M:%S %Z%z"))  # Saída: 01/10/2023 12:00:00 BRT-0300
print(d2.strftime("%d/%m/%Y %H:%M:%S %Z%z"))  # Saída: 02/10/2023 12:00:00 BRT-0300

# Convertendo strings em datas
data_str = "01/10/2023 12:00:00"
d3 = tz.localize(datetime.strptime(data_str, "%d/%m/%Y %H:%M:%S"))
print(d3)  # Saída: 2023-10-01 12:00:00-03:00

# Trabalhando com tz sem bibliotecas externas
# O Python permite fazer isso com o módulo datetime padrão, embora seja um pouco mais complexo do que usando bibliotecas como 'pytz'.

from datetime import datetime, timezone, timedelta
from datetime import date

# Criando um objeto timezone
utc = timezone.utc
brt = timezone(timedelta(hours=-3))

# Criando um objeto datetime com timezone
d1 = datetime(2023, 10, 1, 12, 0, 0, tzinfo=brt)
d2 = datetime(2023, 10, 2, 12, 0, 0, tzinfo=brt)

# Formatando datas
print(d1.strftime("%d/%m/%Y %H:%M:%S %Z%z"))  # Saída: 01/10/2023 12:00:00 BRT-0300
print(d2.strftime("%d/%m/%Y %H:%M:%S %Z%z"))  # Saída: 02/10/2023 12:00:00 BRT-0300

# Convertendo strings em datas
data_str = "01/10/2023 12:00:00"
d3 = brt.localize(datetime.strptime(data_str, "%d/%m/%Y %H:%M:%S"))
print(d3)  # Saída: 2023-10-01 12:00:00-03:00
