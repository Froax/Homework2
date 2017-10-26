cijferCOR = 8
cijferPROG = 10
cijferCSN = 9

gemiddelde = (cijferCOR + cijferCSN + cijferPROG)/3
print ("gemiddelde is:", gemiddelde)
beloning = ((cijferPROG + cijferCOR + cijferCSN)*30)

overzicht = "Mijn cijfers gemiddeld een {} leveren een beloning van € {} op!".format(gemiddelde,beloning)
print(overzicht)