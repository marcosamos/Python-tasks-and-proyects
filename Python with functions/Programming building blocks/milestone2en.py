print("Welcome to my Game")
print("Instructions: During this game you will use some things keywords for continue with the story. You can play again to know the different endings.")
print()
start = input("Type, START ")
print()
print("Wake Up")
print("I woke up in the street, around me I heard screams and saw fire, apparently something was happening in the city.\nThen I heard a noise in my pocket, it was my phone, so I decided: ")
Q1 = input("Type the word, ANSWER/NO: ")
if Q1.lower() == "answer":
    print("I heard a somewhat cut voice that said to me,\nI am seeing you through the camera on the light pole, on the next street there is a police car with weapons and protection, take them and I will help you out.")
    print("I felt confused, I didn't know who the man on the phone was and I had to make a decision.")
    Q1_2 = input("Type the word, FOLLOW/LOOK_FOR_HELP: ")
    if Q1_2.lower() == "follow":
        print("I decided to follow the voice, ran as fast as I could and reached the police car.")
        print("The protection was very heavy so I had to choose which weapon to take, so I chose: ")
        Q1_3 = input("Type the word, AK47,SHOTGUN,HAND_GUN: ")
        if Q1_3.lower() == "ak47":
            print("When I took the gun I understood what was happening.")
            print("It was an alien invasion, I saw the spaceships fly in the sky.")
            print("A large spaceship began to deploy a very large weapon.\nThen after a few meters I saw a missile, perhaps with that I could destroy the nabe.\nThen I had to choose.")
            Q1_4 = input("Type the word, ESCAPE/SHOOT_THE_MISSILE: ")
            if Q1_4.lower() == "escape":
                print("I decided to escape in the car but when he opened the door, \nThe large sapceship fired its weapon.")
                print("I closed my eyes and when I opened them, I woke up in my room. All was a dream")# FINAL 1
            else:
                print("I decided to run towards the missile. When I was ready to destroy the spaceship,\nI saw how everything changed color, so I closed my eyes and when I opened them, I was in my room.")
                print("All was a dream.") #FINAL 1.2
        elif Q1_3.lower() == "shotgun":
            print("When I took the shotgun, I understood what was happening.")
            print("A horde of zombies surrounded me.\nI shot until I was left with 1 bullet but there were still many, so I had to decide.")
            print("Kill myself or use the last bullet to find a way out\nThen I chose:")
            Q1_3_2 = input("Type the word, KILLMYSELF/LAST_CHANCE: ")
            if Q1_3_2.lower() == "killmyself":
                print("When I was about to shoot I heard a noise like an alarm,\nthen I closed my eyes and opened them again,")
                print("I realized that I was in my room and it was all a dream.")# final 2
            else:
                print("I chose the last chance")
                print("When I was about to shoot I saw a missile flying in the sky and I understood that it would destroy everything")
                print("I closed my eyes and when I opened them I realized that I was in my room. It was all a dream.")# Final 2.2
        else:
            print("When I took the handgun I understood what was happening.")
            print("I was in the middle of a political protest and I had to protect the president.\nThen the secret service called me again and told me.")
            print("It's time to wake up")
            print("I closed and opened my eyes and I was in my room and my dad was waking me up to go to school. All was a dream")# Final 3
    else:
        print("I decided to ignore the man on the call and seek help.")
        print("I had to decide who to ask because there was only one man or one woman, both of strange aspects.")
        Q1_2_1 = input("Type the word, MAN/WOMAN: ")
        if Q1_2_1.lower() == "man":
            print("I asked the man, but when I got closer his face changed.")
            print("His face was made of bones and I couldn't believe it, so I closed my eyes and when he opened them.\nI was in my room and it was all a dream")# Final 4
        else:
            print("I asked the woman but when she opened her mouth I saw that she had fangs like a vampire")
            print("Then she leapt to my neck to drink my blood.")
            print("I was so scared that the only thing I could do was close and open my eyes and I realized that I was in my room and it was all a dream")#Final 4.2

else:
    print("I decided not to answer, I only heard a noise that was getting louder.")
    print("I saw a policeman and a firefighter and ran towards him ...")
    Q2 = input("Type the word, POLICEMAN/:FIREFIGHTER ")
    if Q2.lower() == "policeman":
        print("The police officer told me that several buildings collapsed due to an earthquake.")
        print("At that moment another building was falling and when I was about to reach the ground 'scream' and woke up shaken in my bed and everything was a dream")# Final 5
    else:
        print("The firefighter told me that several buildings were on fire and that I had probably passed out from the smoke.")
        print("Then an explosion happened and when I opened my eyes I was in my room and it was all a dream.")# Final 6
print()
print("The End")