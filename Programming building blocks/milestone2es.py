print("Welcome to my Game")
print("Instructions: During this game you will use somethings keywords for continue with the story. You can play again to know the different endings.")
print()
start = input("Type, START ")
print()
print("Wake Up")
print("Yo me desperte en la calle, a mi alrededor escuchaba gritos y veia fuego, al parecer algo ocurria en la ciudad.\n Entonces escuche un ruido en mi bolsillo, era mi telefono, entonces decidi: ")
Q1 = input("Teclea la palabra, CONTESTAR/NO: ")
if Q1.lower() == "contestar":
    print("Yo escuche una voz algo cortada que me decia,\nTe estoy viendo por la camara del poste de luz, en la siguiente calle hay un carro policia con armas y proteccion, tomalas y te ayudare a salir.")
    print("Yo me sentia confundido, no sabia quien era y tenia que tomar una decision")
    Q1_2 = input("Teclea la palabra. SEGUIR/BUSCAR_AYUDA: ")
    if Q1_2.lower() == "seguir":
        print("Decidi seguir a la voz, corri lo mas rapido que podia y llegue al carro policia.")
        print("La proteccion era muy pesada entonces tenia que escoger que arma tomar, entonces elegi: ")
        Q1_3 = input("Teclea la palabra, AK47,ESCOPETA,PISTOLA_DE_MANO: ")
        if Q1_3.lower() == "ak47":
            print("Cuando agarre el arma entendi lo que ocurria.")
            print("Era una invacion alienigena, vi las naves volar en el cielo.")
            print("Una gran  nave empezo a desplegar un arma muy grande.\nEntonces a los pocos metros vi un misil, quizas con eso podria destruir a la nabe\nEntonces tenia que escoger.")
            Q1_4 = input("Teclea la palabra, ESCAPAR/DISPARAR_EL_MISIL: ")
            if Q1_4.lower() == "escapar":
                print("Decidi escapar en el carro pero cuando abri la puerta,\nLa nave grande disparo su arma.")
                print("Cerre los ojos y cuando los abri, Desperte en mi cuarto. Todo fue un sueño")# FINAL 1
            else:
                print("Decidi correr hacia el misil. Cuando estaba listo para destruir la nave,\nvi como todo cambiaba de color, entonces cerre los ojos y cuando los abri, estaba en mi cuarto.")
                print("Todo fue un sueño.") #FINAL 1.2
        elif Q1_3.lower() == "escopeta":
            print("Cuando tome la escopeta, Entendi lo que ocurria.")
            print("Una horda de zombies me rodeaba.\n Dispare hasta quedarme con 1 bala pero todavia eran muchos, entonces tenia que decidir.")
            print("Suicidarme o usar la ultima bala para buscar una salida\nEntonces elegi: ")
            Q1_3_2 = input("Teclea la palabra, SUICIDARME/ULTIMA_OPORTUNIDAD: ")
            if Q1_3_2.lower() == "suicidarme":
                print("Cuando estaba a punto de disparar escuche un ruido como una alarma,\nentonces cerre los ojos y los volvi a abrir,")
                print("Me di cuenta que estaba en mi cuarto y Todo fue un sueño.")# final 2
            else:
                print("Elegi la ultima oportunidad")
                print("Cuando estaba a punto de disparar vi un misil volando en el cielo y entendi que lo destruiria todo")
                print("Cerre los ojos y cuando los abri me di cuenta que estaba en mi cuarto, Todo fue un sueño.")# Final 2.2
        else:
            print("Cuando tome la pistola de mano entendi lo que ocurria.")
            print("Estaba en medio de una protesta politica y yo tenia que proteger al president.\nEntonces el servicio secreto otra vez me llamo y me dijo.")
            print("Ya es hora de despertar")
            print("Cerre y abri los ojos y yo estaba en mi cuarto y mi papa me estaba despertando para ir a la escuela. Todo fue un sueño")# Final 3
    else:
        print("Decidi no hacer caso al hombre de la llamada y busque ayuda.")
        print("Tenia que decidir a quien preguntar por que solo habia un hombre o una mujer, ambos de aspectos raros.")
        Q1_2_1 = input("Teclea la palabra, HOMBRE/MUJER: ")
        if Q1_2_1.lower() == "hombre":
            print("Le pregunte al hombre, pero cuando me acerque su cara cambio.")
            print("Su cara era de huesos y yo no lo podia creer, entonces cerre los ojos y cuando los abri.\nYo estaba en mi cuarto y Todo fue un sueño")# Final 4
        else:
            print("Le pregunte a la mujer pero cuando abrio la boca vi que tenia colmillos como un vampiro")
            print("Entonces salto a mi cuello para beber mi sangre.")
            print("Yo estaba tan asustado que lo unico que pude hacer fue cerrar y abrir los ojos y me di cuenta que estaba en mi cuarto y Todo fue un sueño")#Final 4.2

else:
    print("Decidi no contestar, solo se escuchaba un ruido cada vez mas fuerte.")
    print("Vi a un policia y un bombero y corri hacia el....")
    Q2 = input("Teclea la palabra, POLICIA/BOMBERO: ")
    if Q2.lower() == "policia":
        print("El policia me dijo que varios edificios se desplomaron por un terremoto.")
        print("En ese momento otro edificio estaba cayendo y cuando estaba a punto de llegar al suelo 'grite' y desperte ajitado en mi cama y Todo fue un sueño")# Final 5
    else:
        print("El bombero me dijo que varios edificios estaban en llamas y que probablemente me habia desmayado por el humo.")
        print("Entonces ocurrio una explosion y cuando abri los ojos estaa en mi cuarto y Todo fue un sueño.")# Final 6
print()
print("The End")