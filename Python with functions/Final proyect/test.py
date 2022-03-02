from typing import get_args
import pytest
from functions_by_test import alphabet, get_word

def test_alphabet():
    assert alphabet("a") == "abecedario" or "amor" or "araña" or "abeja" or "Ana" or "árbol" \
        or "admiración" or "ancla" or "archivo" or "agua" or "Andrés" or "arcoiris" \
        or "aguacate" or "angustia" or "Argentina" or "águila" or "anillo" or "arquitectura" \
        or "ala" or "ansiedad" or "arroyo" or "alma" or "antena" or "arte" \
        or "altura" or "anteojo" or "automóvil" or "ambulancia" or "antorcha" or "avion" \
        or "abandonar" or "adornar" or "aprovechar" or "ablandar" or "afeitar" or "arder" \
        or "abrir" or "afilar" or "arrojar" or "absorber" or "alimentar" or "asentir" or "acceder" or "amar" or "asistir" or "accionar" or "andar" or "atacar" or "acelerar" or "añadir" or "aterrar" or "aceptar" or "aplicar" or "atrapar" \
        or "admirar" or "apoyar" or "avisar" or "admitir" or "aprender" or "ayudar" or "abatido" or "ágil" or "amigable" or "abierto" or "agudo" or "análogo" \
        or "abismal" or "ajado" or "anaranjado" or "abominable" or "ajustado" or "ancho" or "abrupto" or "alegre" \
        or "angosto" or "aburrido" or "alejado" or "anticuada" or "ácido" or "alpino" or "antiguo" \
        or "activo" or "altaneros" or "artesanal" or "adicto" or "amargo" or "astuta" or "adorable" or "amarillento" or "azul"
    assert alphabet("b") == "baba" or "baúl" or "boda" or "bajo" or "bonito" or "bebé" or "babero" or "bajada" or "begoña"
    assert alphabet("c") == "cena" or "ceniza" or "boca" or "caramelo" or "casa" or "caza"
    assert alphabet("d") == "daño" or "dama" or "daga" or "dato" or "dádiva" or "debajo" or "debate" or "dedo" or "décimo" or "doce" or "duda" or "dureza"
    assert alphabet("e") == "enfático" or "escopeta" or "engaño" or "esfera" or "espejo" or "estable" or "estaca" or "entero" or "embarazo" or "embudo" or "empanada" or "envase" or "excusa" or "escoba"
    assert alphabet("f") == "fábrica" or "fábula" or "fosa" or "famélico" or "fino" or "famoso" or "físico" or "fatigado" or "fe" or "foca" or "futuro"
    assert alphabet("g") == "galope" or "giro" or "gamuza" or "ganado" or "garaje" or "goloso" or "goma" or "gélido" or "gemelo" or "gótico"
    assert alphabet("h") == "Habano" or "Hexágono" or "Haya" or "Hazaña" or "Halo" or "Hamaca" or "haba" or "haber" or "hablar" or "hacendado" or "hacer" or "hacha" or "hache" or "hacía" or "hacienda" or "hacinar" or "hada" or "haga" or "halar" or "halcón" or "hallado" or "hallar" or "hará" or "haremos" or "harina" or "hartar" or "hartazgo" or "harto" or "hasta" or "hastío" or "haya" or "haz" or "he" or "hebilla" or "hebra" or "hebreo" or "hectárea" or "hectómetro" or "hedor" or "heladera"
    assert alphabet("i") == "ícono" or "incidir" or "insignificante" or "idea" or "incipiente" or "insistente" or "identificar" or "inclinación" or "institucional" or"ideología" or "incoherente" or "instruir" or "idolatrar" or "incómoda" or "inteligencia" or "iglesia" or "incorrecto" or "intención" or "iglú" or "increíble" or "intensidad" or "ignorante" or "indagación" or "interferir" or "igualdad" or "indecisión" or "internacional" or "ilegal" or "indicio" or "internet" or "ilógico" or "indignado" or "interrumpir" or "iluminar" or "indispensable" or "intervenir" or "ilusión" or "individua" or "intimidad" or "imaginar" or "indulgencia" or "intolerante" or "imán" or "industria" or "introducir" or "imitar" or "infantil" or "intuitivo"
    assert alphabet("j") == "jabalí" or "jabón" or "jacarandá" or "jactar" or "jacuzzi" or "jade" or "jadear" or "jaguar" or "jalar" or "jalea" or "jaleo" or "jalón" or "jalonar" or "jamás" or "jamón" or "japonés" or "jaque" or "jaquear" or "jaqueca" or "jarabe"
    assert alphabet("k") == "Karate" or "Karaoke" or "Kamikaze" or "Karma" or "Kayac" or "Kebab" or "Kendo" or "Keratina" or "Kernel" or "Kevlar" or "Kevin" or "Kétchup" or "Kia" or "Kiwi" or "Kilo" or "Kilogramo" or "Kilómetros" or "Kilobyte" or "Kimono" or "Kiosko"
    assert alphabet("l") == "laberinto" or "lentitud" or "listar" or "labio" or "leña" or "literario" or "laboratorio" or "lesión" or "litigar" or "lacio" or "letal" or "liviana" or "ladear" or "letra" or "llama" or "ladrido" or "levantar" or "llamar" or "ladrillo" or "levar"
    assert alphabet("m") == "maceta" or "marinar" or "mito" or "machista" or "marítimo" or "mixto" or "macizo" or "marrón" or "moderna" or "madera" or "martillar" or "mojado" or "madre" or "masajear" or "moldear" or "madrugar" or "máscara" or "molesto" or "madurar" or "masivo"
    assert alphabet("n") == "nabo" or "navideño" or "ningunear" or "nácar" or "nazismo" or "niño" or "nacer" or "neblina" or "nirvana" or "nación" or "nebulizar" or "nítido" or "nada" or "nebuloso" or "nivelar" or "nadar" or "neceser" or "noble" or "nafta" or "necesidad"
    assert alphabet("o") == "obediente" or "ofrecer" or "optimista" or "obesidad" or "ofuscado" or "óptimo" or "objetar" or "oír" or "opuesto" or "objetivo" or "ojo" or "oral" or "oblicuo" or "oleaje" or "orar" or "obligación" or "olfatear" or "órbita" or "obnubilar" or "oligárquica"
    assert alphabet("p") == "pacífico" or "perfumar" or "preferir" or "paisaje" or "periodístico" or "pregunta" or "palabra" or "perjudicar" or "preocupado" or "palanca" or "permitir" or "preservar" or "pantanoso" or "persona" or "prestar" or "paralelo" or "persuadir" or "prestigio" or "paralizar" or "peyorativo"
    assert alphabet("q") == "que" or "querella" or "quincena" or "quebracho" or "querellante" or "quiniela" or "quebrada" or "querido" or "quinoa" or "quebradizo" or "quesadilla" or "quinto" or "quebranto" or "queso" or "quíntuple" or "quechua" or "quienquiera" or "quirúrgico" or "quedado" or "quieto"
    assert alphabet("r") == "rapido" or "reir" or "risueño" or "rodrigo" or "rosa" or "rodolfo" or "reunir" or "ricardo" or "reparar" or "roblox" or "rana","rata" or "ratón" or "raya" or "reno" or "rinoceronte" or "ruiseñor" or "riachuelo" or "rivera" or "rio"
    assert alphabet("s") == "Sabático" or "Sabado" or "Sabiduría" or "Sabor" or "Sabor" or "Safari" or "Sal" or "Sala" or "Salario" or "Saliva" or "Salvaje" or "Salud" or "Salón" or "Samba" or "Sangre" or "Santo" or "Sapo" or "Sarro" or "Secreto" or "Secta" or "Seguridad" or "Sello" or "Selva"
    assert alphabet("t") == "Tabaco" or "Tabla" or "Tabú" or "Táctica" or "Tala" or "Talento" or "Tallo" or "Tambor" or "Tarjeta" or "Tatuaje" or "Teatro" or "Techo" or "Teclado" or "Tecnología" or "Teja" or "Tejido" or "Tela" or "Telar" or "Telescopio" or "Temperamento"
    assert alphabet("u") == "Ubre" or "Ungüento" or "Uno" or "Unico" or "Ulcera" or "Ultrasonido" or "Unidad" or "Unilateral" or "Unión" or "Uniciclo" or "Unicelular" or "Unipersonal" or "Unisono" or "Universal" or "Universidad" or "Unisex" or "Uña" or "Uranio" or "Urbano" or "Urgente"
    assert alphabet("v") == "Vacuna" or "Valle" or "Válvula" or "Vanguardia" or "Variable" or "Vector" or "Vegetación" or "Vegetales" or "Vegetariano" or "Vehículo" or "Vela" or "Velocidad" or "Vendaje" or "Vendedor" or "Veneno" or "Venta" or "Ventanas" or "Ventilador" or "Verbo" or "Verdad"
    assert alphabet("w") == "Waffle" or "Waterpolo" or "Walkman" or "Web" or "Wikipedia" or "Wasabi" or "Wisky" or "Wincha" or "WiFi"
    assert alphabet("x") == "xochimilco" or "Xanadu" or "Xavier" or "Xenofobia" or "Xiaomi" or "Xilote" or "Xinca" or "Xilofono" or "Xilofonista" or "Ximena" or "Xiomara" or "Xerocopie" or "Xochimilco" or "Xochicalco"
    assert alphabet("y") == "Ya" or "Yacer" or "Yacente" or "Yacimiento" or "Yaguasa" or "Yapa" or "Yate" or "Yunto" or "Yoga" or "Yogar" or "Yerno" or "Yeso" or "Yerba" or "Yerno" or "Yo" or "Yodo"
    assert alphabet("z") == "Zancudo" or "Zanja" or "Zapata" or "Zapatilla" or "Zapato" or "Zara" or "Zarpa" or "Zarpado" or "Zarpazo" or "Zika" or "Zócalo" or "Zombis","Zona" or "Zorros"


pytest.main(["-v", "--tb=line", "-rN", __file__])