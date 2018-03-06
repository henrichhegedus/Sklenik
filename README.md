---


---

<h1 id="automatický-skleník">Automatický skleník</h1>
<p>Cieľom tohoto projektu bolo zostrojiť skleník ktorý by automaticky monitoroval, zalieval a vetral rastliny v ňom.  Tieto funkcie som skúšal na zmenšenom skleníku kvôli tomu aby som ako prvé overil či som schopný zostrojiť všetko čo potrebujem a potom neskôr mohol preniesť svoje skúsenosti na väčšie skleníky. Tento projekt bol podľa mňa relatívne jednoduchý a zvládol by ho každý nováčik do oblasti mikro-ovládačov ja sám sa považujem za nováčika keďže všetky moje doterajšie skúsenosti pochádzali z jedného školského projektu. Ďalej budem popisovať ako som postupoval pri konštrukcii skleníka. Piny ktoré sú na schémach zakreslene sú GPIO piny názov pinu na doske sa líši od čísla GPIO pinu vid obrázok a popisy ku kódu sa nachádzajú v súbore <a href="https://github.com/henrichhegedus/Sklenik/blob/master/main.py">main.py</a><br>
<img src="https://lh3.googleusercontent.com/4pq7eP3Ut9m7YLKFKN-OeRWi-wsX9GHoVgAO_cNYZsU2giNin3LRUyzHna3OnEcbPlZM2vCkqwP3" alt="enter image description here" title="nodemcu_pinnout"></p>
<h2 id="komponenty-ktoré-som-použil">Komponenty ktoré som použil</h2>
<p>plastový skleník, NodeMCU, kovová nádoba na kávu, 6mm vnútorný priemer hadička, female USB konektor, male mikro USB konektor, ME40100V1-G99 40mm ventilátor, DHT-11, YL-69, mini ponorná pumpa, 2*3904 NPN tranzistor, 2*BD140 PNP tranzistor, 4<em>1,5kΩ rezistor, 2</em> BD711 NPN tranzistor, spojovacie kábliky, vývojove dosky, CD mechanika, krabička</p>
<h3 id="pomôcky">Pomôcky</h3>
<p>počítač, USB na USB kábel, USB na mikro USB kábel, tavná pištoľ, spájkovačka, mini brúska</p>
<h2 id="postup">Postup</h2>
<ul>
<li>
<p>Príprava - Najprv som si pripravil všetky diery ktoré som vedel že budem potrebovať.</p>
<ul>
<li>
<p>Diera pre hadičku zo zásobníka</p>
</li>
<li>
<p>Diera pre hadičku do skleníka</p>
</li>
<li>
<p>Diera pre káble do skleníka</p>
</li>
<li>
<p>Otvor pre USB konektor v krabičke (toto nie je nevýhnutné)<br>
<img src="https://lh3.googleusercontent.com/QY8qORHIaYI0MLDthyW0-Uvr1oLJNmJxtW-ubTz1cu-764hWc6OdTRdsg3rXt2O8IzOYGAB8iV_4" alt="enter image description here" title="Diery v skleniku"><br>
<img src="https://lh3.googleusercontent.com/KXOyQRg1tidpFwMQYJiWplUpUz3EJlgRylOXxYcSI2dHC5HJcF8p6rWEoNxX21HRXHFZzHdHjHno" alt="enter image description here" title="Diera na USB"></p>
</li>
</ul>
</li>
<li>
<p><strong>Rozmiestnenie a upevnenie</strong> - Ako druhé som si všetko pripravil a rozmiestnil tak ako by som to chcel mať keď bude projekt hotový (tento krok by bolo možno vhodne nechať na koniec keďže je možne že rozmiestnenie sa bude ešte meniť kvôli jednoduchosti). Položil som si na drevenú dosku kde približne chcem mať skleník kde zásobník na vodu a kde krabičku pre NodeMCU. Skleník som pripevnil 4 skrutkami na vyznačených miestach. Krabičku a zásobník na vodu som pripevnil o dosku tavnou pištoľou.<br>
<img src="https://lh3.googleusercontent.com/Bm_J3F0wludWCJWjF4BCmlcewVJ7eaQ-xlg3C4LBABEKnHqwivNCldKIdVEf_PrDep9MVrUjtEce" alt="enter image description here" title="rozmiestnenie"></p>
</li>
<li>
<p><strong>Spájkovanie</strong> - Tento proces by bol jednoduchší keby ste si boli istý že to čo robíte bude fungovať. Ja som tuto istotu nemal teda každý konektor iný ako konektor do breadboardu som zmenil na takýto konektor. Toto som spravil preto aby bolo jednoduchšie odpájať a zapájať obvody</p>
<ul>
<li>
<p>Prepojenie USB a mikro USB konektoru</p>
</li>
<li>
<p>Napájanie pumpy na breadboard piny</p>
</li>
<li>
<p>Napájanie pumpy na breadboard piny</p>
</li>
</ul>
</li>
<li>
<p><strong>Meranie vlhkosti pôdy</strong> - Keďže všetko som už mal pripravene tak som mohol začať programovať a merať. Prvú som meral vlhkosť pôdy.</p>
<ul>
<li>
<p>Zapojenie obvodu – Čidlo je zapojene dvoma káblikmi do malej dosky. Táto doska je pripojená na NodeMCU pomocou GND a VCC je pripojene na GPIO13 keďže je potrebne vedieť zastaviť prúd cez čidlo aby sa zabránilo korózii. Analógový pin z malej dosky je pripojený na ADC0 keďže to je jediný pin ktorý vie čítať analógovú hodnotu.</p>
</li>
<li>
<p>Kalibrácia - Keďže vlhkosť pôdy sa meria cez jej odpor a z toho ako bol obvod zostavený vyplýva to že výsledky merania budú reprezentovane hodnotou z analógového pinu. Táto hodnota bola 1024 keď odpor bol moc veľký teda keď pôda bola úplne sucha teda so skoro 0% vlhkosťou. Keď bol senzor pokorenený vo vode tak hodnota ktorú ukazoval bola okolo 300 teda vtedy bola vlhkosť 100%. Aktuálna vlhkosť sa teda dala vypočítať ako (1024-hodnota)/724*100</p>
</li>
</ul>
</li>
<li>
<p><strong>Zalievacia hadička</strong> – Hadička slúži na rovnomerne rozdelenie vody určenej na zavlažovanie v rámci skleníka. Hadička prechádza cez nádobu na vodu do ktorej bola vyvŕtaná diera hadička je o nádobu pripevnená pomocou tavnej pištole aby lepšie tesnila, navyše je zvnútra nádoby zrezaná hneď pri vstupe aby bolo dosť miesta pre ventil o ktorom viac poviem pri pumpe. Prechádza cez druhu dieru v skleníku a pozdĺž celého skleníka. Sú do nej vyvŕtane diery na ktoré sú asi 3cm od seba a sú oproti sebe. Koniec hadičky je zalepený tavnou pištoľou aby z neho nevytekala voda. Hadička je pripevnená o skleník pomocou tavnej pištole<br>
<img src="https://lh3.googleusercontent.com/dOqAAWQ_dQM3KqqvIgPg2pCgsthNiThK8zG--kMrxseKqN255un12rrQMZsBXnzqKRGzNxZBoluT" alt="enter image description here" title="hadicka"></p>
</li>
<li>
<p><strong>Pumpa</strong> – Pumpa slúži na zalievanie rastlín v skleníku</p>
<ul>
<li>Zapojenie obvodu – Pumpa je zapojená cez tranzistor kvôli tomu aby vedela byt napojená vyššie napätie. Ovládací pin je pripojený na GPIO0<br>
<img src="https://lh3.googleusercontent.com/24zDbNA_yHgCyV_NW9nskGBh6-zi1iVQvaoPinn-N9nQC0cpYbi40S7s22t29rp93-uxDf4AWhX2" alt="enter image description here" title="zosilovac"></li>
<li>Pripevnenie – Toto bolo obzvlášť náročne keďže keď je v zásobníku voda tak vďaka gravitácii vteká sama od seba do skleníka tomuto sa da zabrániť nejakým ventilom ja som zvolil ventil z Rajec fľaše. Ten je pripevnený sosákom na vývod z pumpy keďže pumpa nie je až tak výkonná a keby bol v opačnom smere tak by nevedela cez neho pretlačiť vodu. Pripevnený na pumpu je tavnou pištoľou a k stene nádoby tiež. Z druhej strany pumpy je L-profil ktorý slúži na dodatočnú oporu pumpy. Tento profil pochádza z konštrukcie CD mechaniky ale môžete použiť hocijaký iný.</li>
<li><img src="https://lh3.googleusercontent.com/F4jLmmMrbDYRB9I3pNcS1QlnQTUdlH8wMORzTuQTtVB8Po_to9sqlnDKioONxsQXgJFEJO1nLyed" alt="enter image description here" title="pumpa"></li>
</ul>
</li>
<li>
<p><strong>Pôda a sadeničky</strong> – Spôsob akým tento krok vykonáte záleží na vás ja som využil sadeničky ktoré som do skleníku naukladal a vysypal pôdou ale da sa sadiť aj rovno do pôdy.</p>
</li>
<li>
<p><strong>Ventilátor</strong> – ventilátor slúži na vetranie skleníka a zároveň na cirkuláciu vzduchu vo vnútri</p>
<ul>
<li>
<p>Zapojenie obvodu – Zapojenie obvodu je rovnaké ako pri Pumpe ale ovládací pin je zapojený do GPIO15. Obvod bol tak zapojený lebo NodeMCU ma iba 3.3V výstupy a na pustenie ventilátora je treba 5V</p>
</li>
<li>
<p>Pripevnenie – Ventilátor je pripevnený z vnútra o vrch skleníka za pomoci tavnej pištole a káble k nemu idu cez pred tým vyvŕtanú dieru<br>
<img src="https://lh3.googleusercontent.com/jWCz5lS4NXVccyAt1U8lI1M6nuXaPeeyh0FY1NKqys9mNO64GADtMOgwUQTnMdtcPxpKLXp1_Gzg" alt="enter image description here" title="ventilator"></p>
</li>
</ul>
</li>
<li>
<p><strong>Vlhkosť a teplota vzduchu</strong> – Toto bolo asi najjednoduchšie merať keďže v micropythone je vstavaná knižnica DHT11 ktorá slúži na čítanie dát z tohoto senzora.</p>
<ul>
<li>
<p>Zapojenie - Na zapojenia senzoru stačí pripojiť GND ku zemi NodeMCU a 3.3v pin k VCC pinu na senzore.</p>
</li>
<li>
<p>Pripevnenie – Senzor je pripevnený z vnútra o stenu skleníka a káble k nemu idu cez pred tým vyvŕtanú dieru</p>
</li>
</ul>
</li>
<li>
<p><strong>Vetranie</strong> – Vetranie slúži na udržiavanie vhodnej vlhkosti a teploty v skleníku</p>
<ul>
<li>
<p>Získanie súčiastok – V mojom prípade som použil otváraciu mechaniku z CD mechaniky ktorú som z konštrukcie pomocou brúsky vyrezal. Využil som všetky prevody vrátane ozubeného pásika na vysúvajúcej sa časti a drážky v ktorej sa ozubený pásik hýbe. Taktiež som vybral z CD mechaniky motor ktorý slúžil na vysúvanie</p>
</li>
<li>
<p>Zapojenie obvodu – Obvod pre ovládanie a zatváranie bol trochu komplikovanejší a to z toho dôvodu že bolo treba meniť smer elektromotora a teda meniť smer prúdu ktorý cez neho prechádzal. Na toto slúžil H mostík. Ktorého obvod je vidno na obrázku<br>
<img src="https://lh3.googleusercontent.com/YvwrZr-zlwIzTSQwxhrjEuIB8BGUIt1GWPWYhvjQ6BvDPEu48x_LatNF32P8aonK1EG-8yEyTKAg" alt="enter image description here" title="h_bridge"></p>
<p>Smer prúdu v motore sa dá ovládať dvoma pinmi podľa toho cez ktorý tečie prúd sa mení smer prúdu v motore. Dôležite je nikdy nemať pustene obidva piny lebo toto spôsobí skrat.</p>
</li>
<li>
<p>Pripevnenie – Všetky prevody boli pripevnene o skleník za pomoci tavnej pištole a ozubený pásik bol pripevnený o posuvne vetranie tiež pomocou tavnej pištole. Na obrázkoch je vidno ešte inú súčiastku medzi zeleným posúvačom a pásikom tá tam je iba kvôli tomu aby bola drážka v ktorej sa hýbe pásik v rovnakej výške ako spoj s posúvačom<br>
<img src="https://lh3.googleusercontent.com/4AnPzqfStfItPhK4s0Hs3CH6u-Qh9NX7UHoKJR8ZVM15HdG6rlO64cawKrKCzKzgoYQo90rBZmHT" alt="enter image description here" title="vetranie"><br>
<img src="https://lh3.googleusercontent.com/SAW7tVC9JWv1oLxLuqfGSkcWGVtbEEjmvrrjGbyJ6lRwcCaOyOWd8R4f4Kab4aEPTcHLGsDXRE7b" alt="enter image description here" title="ovaranie"></p>
</li>
</ul>
</li>
</ul>
<h2 id="záverečné-fotky">Záverečné fotky</h2>
<p><img src="https://lh3.googleusercontent.com/HvkD0nDZwtYg70p26urvdZtbzFpb6hAIdvQeGyz16PAXo4c2ienFi8qX1X5qzizJpwnnVdQ7-A1i" alt="enter image description here"><img src="https://lh3.googleusercontent.com/OPLa16zjWXMzhu2MVFVEG1eQps8L25804rQ9WKu_SyGc3bDUGTyBd2Ko5tf2qPsey21rNoHwt4Lk" alt="enter image description here"></p>

