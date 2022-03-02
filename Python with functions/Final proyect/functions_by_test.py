import random
from pylabeador import syllabify


def main():
    try:
        
        input_letter = input("Please type an alphabet letter: ")
        word = alphabet(input_letter)
        print(word)

        silaba = get_word(word)
        print(silaba)
    except AttributeError:
        print(f"Sorry you typed a number")
        print("try with a letter")


def alphabet(input_letter):
    
    a_list = ["abecedario","amor","araña","abeja","Ana","árbol"
        ,"admiración","ancla","archivo","agua","Andrés",	"arcoiris",
        "aguacate",	"angustia","Argentina","águila",	"anillo",	"arquitectura",
        "ala",	"ansiedad",	"arroyo","alma",	"antena"	,"arte",
        "altura",	"anteojo",	"automóvil","ambulancia",	"antorcha",	"avión",
        "abandonar"	,"adornar"	,"aprovechar","ablandar",	"afeitar",	"arder",
        "abrir"	,"afilar",	"arrojar","absorber"	,"alimentar",	"asentir","acceder","amar","asistir","accionar","andar","atacar","acelerar","añadir","aterrar","aceptar","aplicar","atrapar","admirar"	,"apoyar",	"avisar","admitir","aprender","ayudar","abatido","ágil","amigable","abierto","agudo","análogo","abismal","ajado","anaranjado","abominable","ajustado","ancho","abrupto","alegre","angosto","aburrido","alejado","anticuada","ácido","alpino","antiguo"
        ,"activo",	"altaneros","artesanal","adicto","amargo","astuta","adorable","amarillento",	"azul"]
        
    b_list = ["baba","baúl","boda","bajo","bonito","bebé", "babero", "bajada", "begoña"]
    
    c_list = ["cena","ceniza","boca","caramelo","casa","caza"]

    d_list = ["daño", "dama","daga","dato",
        "dádiva","debajo","debate","dedo","décimo","doce","duda","dureza"]

    e_list = ["enfático","escopeta","engaño","esfera","espejo",
        "estable","estaca","entero","embarazo","embudo","empanada","envase","excusa","escoba"]

    f_list = ["fábrica","fábula","fosa","famélico","fino","famoso","físico","fatigado","fe","foca","futuro"]

    g_list = ["galope","giro","gamuza","ganado","garaje","goloso","goma","gélido","gemelo","gótico"]

    h_list = ["Habano","Hexágono","Haya","Hazaña","Halo","Hamaca","haba"
            ,"haber","hablar","hacendado","hacer","hacha","hache","hacía","hacienda","hacinar","hada","haga"
            ,"halar","halcón","hallado","hallar","hará","haremos","harina","hartar","hartazgo"
            ,"harto","hasta","hastío","haya","haz","he","hebilla","hebra","hebreo","hectárea","hectómetro","hedor","heladera"]

    i_list = ["ícono","incidir","insignificante","idea","incipiente","insistente"
            ,"identificar","inclinación","institucional","ideología","incoherente","instruir"
            ,"idolatrar","incómoda","inteligencia","iglesia","incorrecto","intención"
            ,"iglú"	,"increíble","intensidad","ignorante","indagación","interferir","igualdad","indecisión","internacional"
            ,"ilegal","indicio","internet","ilógico","indignado","interrumpir","iluminar","indispensable","intervenir"
            ,"ilusión","individua","intimidad","imaginar","indulgencia","intolerante","imán","industria","introducir"
            ,"imitar","infantil","intuitivo"]

    j_list = ["jabalí","jabón","jacarandá"
            ,"jactar","jacuzzi","jade","jadear","jaguar","jalar","jalea","jaleo","jalón"
            ,"jalonar","jamás","jamón","japonés","jaque","jaquear","jaqueca","jarabe"]
    
    k_list = ["Karate","Karaoke","Kamikaze","Karma","Kayac",
            "Kebab","Kendo","Keratina","Kernel","Kevlar","Kevin","Kétchup","Kia"
            ,"Kiwi","Kilo","Kilogramo","Kilómetros","Kilobyte","Kimono","Kiosko"]
    
    l_list = ["laberinto","lentitud","listar"
            ,"labio","leña","literario","laboratorio","lesión","litigar","lacio","letal","liviana"
            ,"ladear","letra","llama","ladrido","levantar","llamar","ladrillo","levar"]
    
    m_list = ["maceta",	"marinar",	"mito","machista","marítimo","mixto"
        ,"macizo","marrón","moderna","madera","martillar","mojado"
        ,"madre","masajear","moldear","madrugar","máscara","molesto","madurar",	"masivo"]

    n_list = ["nabo","navideño","ningunear","nácar","nazismo","niño","nacer","neblina","nirvana"
        ,"nación","nebulizar","nítido","nada","nebuloso","nivelar","nadar","neceser","noble","nafta","necesidad"]
    
    o_list = ["obediente","ofrecer","optimista","obesidad","ofuscado","óptimo","objetar","oír","opuesto"
        ,"objetivo","ojo","oral","oblicuo","oleaje","orar","obligación","olfatear","órbita","obnubilar","oligárquica"]

    p_list = ["pacífico","perfumar","preferir","paisaje","periodístico","pregunta"
        ,"palabra","perjudicar","preocupado","palanca","permitir","preservar"
        ,"pantanoso","persona","prestar","paralelo","persuadir","prestigio","paralizar","peyorativo"]

    q_list = ["que","querella","quincena","quebracho","querellante","quiniela","quebrada","querido","quinoa"
        ,"quebradizo","quesadilla","quinto","quebranto","queso","quíntuple","quechua","quienquiera","quirúrgico","quedado","quieto"]

    r_list = ["rapido","reir","risueño","rodrigo","rosa","rodolfo","reunir","ricardo","reparar","roblox"
            ,"rana","rata","ratón","raya","reno","rinoceronte","ruiseñor","riachuelo","rivera","rio"]

    s_list = ["Sabático","Sabado","Sabiduría","Sabor","Sabor","Safari"
        ,"Sal","Sala","Salario","Saliva","Salvaje","Salud","Salón"
        ,"Samba","Sangre","Santo","Sapo","Sarro","Secreto","Secta","Seguridad","Sello","Selva"]
            
    t_list = ["Tabaco","Tabla","Tabú","Táctica","Tala","Talento",
        "Tallo","Tambor","Tarjeta","Tatuaje","Teatro""Techo","Teclado","Tecnología"
        ,"Teja","Tejido","Tela","Telar","Telescopio","Temperamento"]

    u_list = ["Ubre","Ungüento","Uno","Unico","Ulcera","Ultrasonido","Unidad","Unilateral"
        ,"Unión","Uniciclo","Unicelular","Unipersonal","Unisono","Universal","Universidad","Unisex","Uña","Uranio","Urbano","Urgente"]
    
    v_list = ["Vacuna","Valle","Válvula","Vanguardia","Variable","Vector","Vegetación"
        ,"Vegetales","Vegetariano","Vehículo","Vela","Velocidad"
        ,"Vendaje","Vendedor","Veneno","Venta","Ventanas","Ventilador","Verbo","Verdad"]
    
    w_list = ["Waffle","Waterpolo","Walkman","Web","Wikipedia","Wasabi","Wisky","Wincha","WiFi"]

    x_list = ["Xanadu","Xavier","Xenofobia","Xiaomi","Xilote","Xinca","Xilofono"
            ,"Xilofonista","Ximena","Xiomara","Xerocopie","Xochimilco","Xochicalco"]

    y_list = ["Ya"
        ,"Yacer","Yacente","Yacimiento","Yaguasa","Yapa","Yate"
        ,"Yunto","Yoga","Yogar","Yerno","Yeso","Yerba","Yerno","Yo","Yodo"]

    z_list = ["Zancudo","Zanja","Zapata","Zapatilla"
        ,"Zapato","Zara","Zarpa","Zarpado"
        ,"Zarpazo","Zika","Zócalo","Zombis","Zona","Zorros"]
    
    if input_letter.lower() == "a":
        imprimir = random.choice(a_list)
        return imprimir
    elif input_letter.lower() == "b":
        imprimir = random.choice(b_list)
        return imprimir
    elif input_letter.lower() == "c":
        imprimir = random.choice(c_list)
        return imprimir
    elif input_letter.lower() == "d":
        imprimir = random.choice(d_list)
        return imprimir
    elif input_letter.lower() == "e":
        imprimir = random.choice(e_list)
        return imprimir
    elif input_letter.lower() == "f":
        imprimir = random.choice(f_list)
        return imprimir
    elif input_letter.lower() == "g":
        imprimir = random.choice(g_list)
        return imprimir
    elif input_letter.lower() == "h":
        imprimir = random.choice(h_list)
        return imprimir    
    elif input_letter.lower() == "i":
        imprimir = random.choice(i_list)
        return imprimir
    elif input_letter.lower() == "j":
        imprimir = random.choice(j_list)
        return imprimir    
    elif input_letter.lower() == "k":
        imprimir = random.choice(k_list)
        return imprimir
    elif input_letter.lower() == "l":
        imprimir = random.choice(l_list)
        return imprimir    
    elif input_letter.lower() == "m":
        imprimir = random.choice(m_list)
        return imprimir
    elif input_letter.lower() == "n":
        imprimir = random.choice(n_list)
        return imprimir
    elif input_letter.lower() == "o":
        imprimir = random.choice(o_list)
        return imprimir
    elif input_letter.lower() == "p":
        imprimir = random.choice(p_list)
        return imprimir    
    elif input_letter.lower() == "q":
        imprimir = random.choice(q_list)
        return imprimir
    elif input_letter.lower() == "r":
        imprimir = random.choice(r_list)
        return imprimir
    elif input_letter.lower() == "s":
        imprimir = random.choice(s_list)
        return imprimir    
    elif input_letter.lower() == "t":
        imprimir = random.choice(t_list)
        return imprimir
    elif input_letter.lower() == "u":
        imprimir = random.choice(u_list)
        return imprimir    
    elif input_letter.lower() == "v":
        imprimir = random.choice(v_list)
        return imprimir
    elif input_letter.lower() == "w":
        imprimir = random.choice(w_list)
        return imprimir    
    elif input_letter.lower() == "x":
        imprimir = random.choice(x_list)
        return imprimir    
    elif input_letter.lower() == "y":
        imprimir = random.choice(y_list)
        return imprimir
    elif input_letter.lower() == "z":
        imprimir = random.choice(z_list)
        return imprimir

def get_word(word):
    
    silabas = syllabify(word)
    return silabas
    
    

        

if __name__ in "__main__":
    main()