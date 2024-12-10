from decimal import Decimal , ROUND_HALF_UP ,ROUND_CEILING
team_lead=Decimal(1.02506)
x = team_lead.quantize(Decimal('1'), rounding=ROUND_CEILING)

print("value of adding team lead : ",x)


without_team_lead=Decimal(0.99906)
x1 = without_team_lead.quantize(Decimal('1'), rounding=ROUND_CEILING)

print("value of without adding team lead too : ",x1)