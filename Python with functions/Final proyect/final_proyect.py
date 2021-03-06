# wrote by Marcos Uc

# This is a simple program for to help children to learn words in spanish and to learn the syllable division.

# Libraries
import random # I used this library for get a random word from list.
import tkinter as tk # I used this library for build the graphic interface.
from pylabeador import syllabify # I used this library to help me to divide the words in syllables.

def main():
    # Create the TK object.
    root = tk.Tk()

    window = tk.Frame(root)
    window.master.title("Learn to read in spanish")
    window.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)

    # Call the functions and display the graphic interface. 
    labels_window(window)
    

    root.mainloop()

# This function performance the labels and has two anidade functions that choose a word and divide in syllabes.
def labels_window(window):
    #variables
    instruction_text = "This is a quick way to learn Spanish words. \n Just ask the child to choose a letter and write it in the input box below. \
    \n Then a word will appear according to the letter you chose and its syllable division will appear below. \
    \n Help the child to pronounce the word and then to pronounce the syllables of the word"
    
    #labels
    instruction = tk.Label(window, text= instruction_text, borderwidth=2, relief="groove")
    label_1 = tk.Label(window,text="Type a letter:  ")
    letter = tk.Entry(window,width=12)
    label_2 = tk.Label(window,text="Word:    ")
    word = tk.Label(window,width=12,fg="green",bg="white",relief="ridge")
    label3 = tk.Label(window,text="Word in syllabe:    ")
    word_syllabe = tk.Label(window, width=20,fg="black",bg="yellow",relief="ridge")

    # Layout all the labels, entry boxes, and buttons in a grid.
    instruction.grid(row=0, column=0, columnspan=2, padx=1, pady=1,)
    label_1.grid(row=1, column=0, padx=3, pady=3)
    letter.grid(row=1, column=1, padx=3, pady=3)
    label_2.grid(row=2, column=0, padx=3, pady=3)
    word.grid(row=2, column=1, padx=3, pady=3)
    label3.grid(row=3, column=0, padx=3, pady=3)
    word_syllabe.grid(row=3, column=1, padx=3, pady=3)
    
    
    # This function choice a word and return this word in the graphic interface
    def alphabet(event):
        # list of words
        a_list = ["abecedario","amor","ara??a","abeja","Ana","??rbol"
            ,"admiraci??n","ancla","archivo","agua","Andr??s",	"arcoiris",
            "aguacate",	"angustia","Argentina","??guila",	"anillo",	"arquitectura",
            "ala",	"ansiedad",	"arroyo","alma",	"antena"	,"arte",
            "altura",	"anteojo",	"autom??vil","ambulancia",	"antorcha",	"avi??n",
            "abandonar"	,"adornar"	,"aprovechar","ablandar",	"afeitar",	"arder",
            "abrir"	,"afilar",	"arrojar","absorber"	,"alimentar",	"asentir","acceder","amar","asistir","accionar","andar","atacar","acelerar","a??adir","aterrar","aceptar","aplicar","atrapar","admirar"	,"apoyar",	"avisar","admitir","aprender","ayudar","abatido","??gil","amigable","abierto","agudo","an??logo","abismal","ajado","anaranjado","abominable","ajustado","ancho","abrupto","alegre","angosto","aburrido","alejado","anticuada","??cido","alpino","antiguo"
            ,"activo",	"altaneros","artesanal","adicto","amargo","astuta","adorable","amarillento",	"azul"]

        b_list = ["baba","ba??l","boda","bajo","bonito","beb??", "babero", "bajada", "bego??a"]

        c_list = ["cena","ceniza","boca","caramelo","casa","caza"]

        d_list = ["da??o", "dama","daga","dato",
            "d??diva","debajo","debate","dedo","d??cimo","doce","duda","dureza"]

        e_list = ["enf??tico","escopeta","enga??o","esfera","espejo",
            "estable","estaca","entero","embarazo","embudo","empanada","envase","excusa","escoba"]

        f_list = ["f??brica","f??bula","fosa","fam??lico","fino","famoso","f??sico","fatigado","fe","foca","futuro"]

        g_list = ["galope","giro","gamuza","ganado","garaje","goloso","goma","g??lido","gemelo","g??tico"]

        h_list = ["Habano","Hex??gono","Haya","Haza??a","Halo","Hamaca","haba"
            ,"haber","hablar","hacendado","hacer","hacha","hache","hac??a","hacienda","hacinar","hada","haga"
            ,"halar","halc??n","hallado","hallar","har??","haremos","harina","hartar","hartazgo"
            ,"harto","hasta","hast??o","haya","haz","he","hebilla","hebra","hebreo","hect??rea","hect??metro","hedor","heladera"]

        i_list = ["??cono","incidir","insignificante","idea","incipiente","insistente"
            ,"identificar","inclinaci??n","institucional","ideolog??a","incoherente","instruir"
            ,"idolatrar","inc??moda","inteligencia","iglesia","incorrecto","intenci??n"
            ,"igl??"	,"incre??ble","intensidad","ignorante","indagaci??n","interferir","igualdad","indecisi??n","internacional"
            ,"ilegal","indicio","internet","il??gico","indignado","interrumpir","iluminar","indispensable","intervenir"
            ,"ilusi??n","individua","intimidad","imaginar","indulgencia","intolerante","im??n","industria","introducir"
            ,"imitar","infantil","intuitivo"]

        j_list = ["jabal??","jab??n","jacarand??"
            ,"jactar","jacuzzi","jade","jadear","jaguar","jalar","jalea","jaleo","jal??n"
            ,"jalonar","jam??s","jam??n","japon??s","jaque","jaquear","jaqueca","jarabe"]

        k_list = ["Karate","Karaoke","Kamikaze","Karma","Kayac",
            "Kebab","Kendo","Keratina","Kernel","Kevlar","Kevin","K??tchup","Kia"
            ,"Kiwi","Kilo","Kilogramo","Kil??metros","Kilobyte","Kimono","Kiosko"]

        l_list = ["laberinto","lentitud","listar"
            ,"labio","le??a","literario","laboratorio","lesi??n","litigar","lacio","letal","liviana"
            ,"ladear","letra","llama","ladrido","levantar","llamar","ladrillo","levar"]

        m_list = ["maceta",	"marinar",	"mito","machista","mar??timo","mixto"
            ,"macizo","marr??n","moderna","madera","martillar","mojado"
            ,"madre","masajear","moldear","madrugar","m??scara","molesto","madurar",	"masivo"]

        n_list = ["nabo","navide??o","ningunear","n??car","nazismo","ni??o","nacer","neblina","nirvana"
            ,"naci??n","nebulizar","n??tido","nada","nebuloso","nivelar","nadar","neceser","noble","nafta","necesidad"]

        o_list = ["obediente","ofrecer","optimista","obesidad","ofuscado","??ptimo","objetar","o??r","opuesto"
            ,"objetivo","ojo","oral","oblicuo","oleaje","orar","obligaci??n","olfatear","??rbita","obnubilar","olig??rquica"]

        p_list = ["pac??fico","perfumar","preferir","paisaje","period??stico","pregunta"
            ,"palabra","perjudicar","preocupado","palanca","permitir","preservar"
            ,"pantanoso","persona","prestar","paralelo","persuadir","prestigio","paralizar","peyorativo"]

        q_list = ["que","querella","quincena","quebracho","querellante","quiniela","quebrada","querido","quinoa"
            ,"quebradizo","quesadilla","quinto","quebranto","queso","qu??ntuple","quechua","quienquiera","quir??rgico","quedado","quieto"]

        r_list = ["rapido","reir","risue??o","rodrigo","rosa","rodolfo","reunir","ricardo","reparar","roblox"
            ,"rana","rata","rat??n","raya","reno","rinoceronte","ruise??or","riachuelo","rivera","rio"]

        s_list = ["Sab??tico","Sabado","Sabidur??a","Sabor","Sabor","Safari"
            ,"Sal","Sala","Salario","Saliva","Salvaje","Salud","Sal??n"
            ,"Samba","Sangre","Santo","Sapo","Sarro","Secreto","Secta","Seguridad","Sello","Selva"]

        t_list = ["Tabaco","Tabla","Tab??","T??ctica","Tala","Talento",
            "Tallo","Tambor","Tarjeta","Tatuaje","Teatro""Techo","Teclado","Tecnolog??a"
            ,"Teja","Tejido","Tela","Telar","Telescopio","Temperamento"]

        u_list = ["Ubre","Ung??ento","Uno","Unico","Ulcera","Ultrasonido","Unidad","Unilateral"
            ,"Uni??n","Uniciclo","Unicelular","Unipersonal","Unisono","Universal","Universidad","Unisex","U??a","Uranio","Urbano","Urgente"]

        v_list = ["Vacuna","Valle","V??lvula","Vanguardia","Variable","Vector","Vegetaci??n"
            ,"Vegetales","Vegetariano","Veh??culo","Vela","Velocidad"
            ,"Vendaje","Vendedor","Veneno","Venta","Ventanas","Ventilador","Verbo","Verdad"]

        w_list = ["Waffle","Waterpolo","Walkman","Web","Wikipedia","Wasabi","Wisky","Wincha","WiFi"]

        x_list = ["Xanadu","Xavier","Xenofobia","Xiaomi","Xilote","Xinca","Xilofono"
            ,"Xilofonista","Ximena","Xiomara","Xerocopie","Xochimilco","Xochicalco"]

        y_list = ["Ya"
            ,"Yacer","Yacente","Yacimiento","Yaguasa","Yapa","Yate"
            ,"Yunto","Yoga","Yogar","Yerno","Yeso","Yerba","Yerno","Yo","Yodo"]

        z_list = ["Zancudo","Zanja","Zapata","Zapatilla"
            ,"Zapato","Zara","Zarpa","Zarpado"
            ,"Zarpazo","Zika","Z??calo","Zombis","Zona","Zorros"]

        # if the user choice a letter, the user get a word and sillabic division.
        try:
            
            letter_V = letter.get()

            if letter_V.lower() == "a":
                word_list = random.choice(a_list)
            elif letter_V.lower() == "b":
                word_list = random.choice(b_list)
            elif letter_V.lower() == "c":
                word_list = random.choice(c_list)
            elif letter_V.lower() == "d":
                word_list = random.choice(d_list)
            elif letter_V.lower() == "e":
                word_list = random.choice(e_list)
            elif letter_V.lower() == "f":
                word_list = random.choice(f_list)
            elif letter_V.lower() == "g":
                word_list = random.choice(g_list)
            elif letter_V.lower() == "h":
                word_list = random.choice(h_list)
            elif letter_V.lower() == "i":
                word_list = random.choice(i_list)
            elif letter_V.lower() == "j":
                word_list = random.choice(j_list)
            elif letter_V.lower() == "k":
                word_list = random.choice(k_list)
            elif letter_V.lower() == "l":
                word_list = random.choice(l_list)
            elif letter_V.lower() == "m":
                word_list = random.choice(m_list)
            elif letter_V.lower() == "n":
                word_list = random.choice(n_list)
            elif letter_V.lower() == "o":
                word_list = random.choice(o_list)
            elif letter_V.lower() == "p":
                word_list = random.choice(p_list)
            elif letter_V.lower() == "q":
                word_list = random.choice(q_list)
            elif letter_V.lower() == "r":
                word_list = random.choice(r_list)
            elif letter_V.lower() == "s":
                word_list = random.choice(s_list)
            elif letter_V.lower() == "t":
                word_list = random.choice(t_list)
            elif letter_V.lower() == "u":
                word_list = random.choice(u_list)
            elif letter_V.lower() == "v":
                word_list = random.choice(v_list)
            elif letter_V.lower() == "w":
                word_list = random.choice(w_list)
            elif letter_V.lower() == "x":
                word_list = random.choice(x_list)
            elif letter_V.lower() == "y":
                word_list = random.choice(y_list)
            elif letter_V.lower() == "z":
                word_list = random.choice(z_list)
            word.config(text=f"{word_list}")


            # syllabic division
            get_label_word = word.cget("text")
            silabas = syllabify(get_label_word)
            word_syllabe.config(text=f"{silabas}")

        except UnboundLocalError:
            word.config(text="")
            word_syllabe.config(text="")
        except letter_V == int:
            word.config(text="")
            word_syllabe.config(text="")
            

    letter.bind("<KeyRelease>",alphabet)


# call the main function
if __name__ == "__main__":
    main()