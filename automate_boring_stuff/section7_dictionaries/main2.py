#nome = 'Create an online video course, reach students across the globe, and earn money'.upper()
nome = '''Em uma cidade esquecida no interior de Ohio, a esposa de Willard Russell está à beira da morte, não importa o quanto ele beba, reze ou faça sacrifícios e oferendas. Com o passar dos anos, seu filho Arvin, uma criança negligenciada, torna-se um homem frio e cruel. Em torno deles, circula um nefasto e peculiar grupo de moradores — um insano casal de assassinos em série, um pastor que come aranhas e um xerife corrupto —, todos entrelaçados numa viciante narrativa da mais corajosa e sombria lavra americana.

Donald Ray Pollock, o novo autor da DarkSide® Books, promete causar alvoroço nos corações mais frágeis. Ele constrói, com maestria, uma trama hiper-violenta, ambientada no pós-Segunda Guerra, repleta de personagens desagradáveis em um cenário devastador, cruéis o suficiente para cometerem crimes com a casualidade de quem troca de roupa. Mas isso não é tudo. Há muito mais por trás das manchas de sangue, da avareza e da mesquinharia: o desespero e as limitações de uma cidade pequena, a frustração de seus habitantes, a síntese de quem não equilibra luz e sombra dentro de si.

O autor elabora uma narrativa tensa e profundamente perturbadora em seu primeiro romance. Pollock se insere na linhagem dos grandes contadores de histórias da América, como John Steinbeck e seu realismo, William Faulkner e Flannery O’ Connor e o magistral gótico sulista e Cormac McCarthy e seu visceral Onde os Velhos Não Têm Vez.

Uma produção original Netflix, a adaptação cinematográfica do livro — prevista para setembro de 2020 — conta com direção do brasileiro Antonio Campos (Afterschool e The Sinner), produção do ator Jake Gyllenhaal e um elenco cheio de estrelas de Hollywood, protagonizado por Sebastian Stan (Capitão América), Tom Holland (Homem-Aranha), Robert Pattinson (só lembramos de O Farol), Bill Skarsgard (It: A Coisa), Mia Wasikowska (Alice no País das Maravilhas) e Eliza Scanlen (Objetos Cortantes).

Se você é apaixonado por histórias sombrias e sinistras, O Mal Nosso de Cada Dia é o som e a fúria da nova literatura. Feche os olhos e comece a rezar.'''.upper()
contador = {}
for x in range(len(nome)):
    if nome[x] not in contador:
        contador[nome[x]] = 0
    contador[nome[x]] += 1

for k, v in contador.items():
    print(k + ': ' + str(v))
