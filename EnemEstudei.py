import os
import time

def EnemEstudei():
    #RESUMOS:
    global figuras_de_linguagem, denotacao_conotacao, ecologia, eletricidade, solucoes_quimicas, transportes_no_brasil, area_de_figuras, moda_media_mediana
    figuras_de_linguagem = '''
         ----------------------
        | Figuras de Linguagem |
         ----------------------

        -Figuras de Linguagem, também chamadas de figuras de estilo, são recursos estilísticos usados para dar maior 
        ênfase à comunicação e torná-la mais bonita.

        Pode ser classificadas em:
        * Figuras de palavras ou semânticas: estão associadas ao significado das palavras.    
                -Exemplos: metáfora, comparação, metonímia, catacrese, sinestesia e perífrase. \n
        * Figuras de pensamento: trabalham com a combinação de ideias e pensamentos. 
                -Exemplos: hipérbole, eufemismo, ironia, personificação, antítese, paradoxo, gradação e apóstrofe.\n
        * Figuras de sintaxe ou construção: interferem na estrutura gramatical da frase. 
                -Exemplos: elipse, zeugma, hipérbato, polissíndeto, assíndeto, anacoluto, pleonasmo, silepse e anáfora.\n
        * Figuras de som ou harmonia: estão associadas à sonoridade das palavras. 
                -Exemplos: aliteração, paronomásia, assonância e onomatopeia.\n

        Mesmo existindo diversas figuras de linguagem, as principais, que mais aparecem em provas são: 
            .metáfora
            .comparação
            .metonímia
            .sinestesia
            .eufemismo
            .personificação
            .silepse
            .pleonasmo
            .hipérbole
            .paradoxo
            .ironia
        \n——————————————————————————————————————————————————————————————''——————————————————————————————————————————————————————————————\n
        >Metáfora<

            É a substituição de um termo por outro baseada numa relação de analogia (que significa semelhança de sentido entre dois termos).
            Exemplos:
                -O jogo já vai começar. Já estão todos no grande tapete verde, só aguardando o apito do juiz. (Estão todos no campo).
                -Ele é um leão! (quer dizer que ele é bravo, feroz, forte…)\n
        \n——————————————————————————————————————————————————————————————''——————————————————————————————————————————————————————————————\n
        >Comparação<
            
            É aproximação de dois termos entre os quais existe alguma relação de semelhança.
            
            Exemplos: 
            -Amou como se fosse máquina.

        ATENÇÃO!!! Não confunda comparação com metáfora! Ambas são parecidas, mas na comparação há a presença de um elemento comparativo. 
        Veja os exemplo
        Exemplos::
        -Meu pai é forte como um touro. Aguentou carregar um armário sozinho. (comparação)
        -Meu pai é um touro. Aguentou carregar um armário sozinho. (metáfora)\n
        \n——————————————————————————————————————————————————————————————''——————————————————————————————————————————————————————————————\n
        >Metonímia<
            
            Acontece quando se emprega um termo no lugar de outro, sendo que entre ambos há estreita afinidade ou relação de sentido.
            
            Exemplo: 
            -Sei que ela adora Fernando Pessoa. (adora o que Fernando Pessoa escreveu.)
            -Ele possuía inúmeras cabeças de gado. (bois)
            -Consegui comprar a televisão com meu suor. (trabalho)\n
        \n——————————————————————————————————————————————————————————————''——————————————————————————————————————————————————————————————\n
        >Sinestesia<
            
            Ocorre quando, numa enunciação, há uma mescla de diferentes sensações que são percebidas pelos órgão de sentido.	
            
            Exemplo: 
            -Gosto quando mamãe canta. Ela tem uma voz macia e doce. 
            (Sentidos: voz = audição; macia = tato; doce = paladar)\n
        \n——————————————————————————————————————————————————————————————''——————————————————————————————————————————————————————————————\n
        >Eufemismo<
            
            É a utilização de expressões mais leves para suavizar o impacto de enunciados tristes ou desagradáveis.
            
            Exemplo: 
            -Vovó virou estrelinha, filho, e agora está lá no céu!
            -Sua vizinha é desprovida de beleza.\n
        \n——————————————————————————————————————————————————————————————''——————————————————————————————————————————————————————————————\n
        >Personificação<
            
            Também conhecida como prosopopeia, acontece quando se atribui a seres inanimados qualidades ou sentimentos próprios de seres humanos.
            
            Exemplo: 	
            -O Sol amanheceu triste e escondido hoje. Acho que vai esfriar!\n
        \n——————————————————————————————————————————————————————————————''——————————————————————————————————————————————————————————————\n
        >Silepse<
            
            É uma figura de construção que ocorre quando se faz concordância com um termo oculto na oração, mas que é facilmente subentendido. 
            
            A concordância é feita com a ideia que esse termo representa.
            
            Exemplos:
            -“Dizem que os cariocas somos poucos dados aos jardins públicos.” (Machado de Assis) (termo oculto = nós)\n
        \n——————————————————————————————————————————————————————————————''——————————————————————————————————————————————————————————————\n
        >Pleonasmo<
            
            É usado para intensificar o significado de um termo através da repetição dele próprio ou da ideia contida nele. 	
            
            Exemplos:
            -“Ó mar salgado, quanto do teu sal são lágrimas de Portugal.” (Fernando Pessoa)
            (O mar e sempre salgado, certo!\n
        \n——————————————————————————————————————————————————————————————''——————————————————————————————————————————————————————————————\n
        >Ironia<
            
            Ocorre quando se diz o contrário do que se tem intenção de dizer para satirizar, criticar, questionar certo tipo de pensamento ou para ridicularizá-lo.
            
            Exemplos:
            -Aquele menino dela é um santo. Só derrubou minha coleção de discos de vinil três vezes.
            -Fale mais alto, lá da esquina ainda não dá para ouvir.\n
        \n——————————————————————————————————————————————————————————————''——————————————————————————————————————————————————————————————\n
        >Hipérbole<
            
            Consiste no exagero de uma ideia com a intenção de engrandecer ou diminuir a verdade dos fatos. 	
            
            Exemplos:: 
            -Já disse isso a você um milhão de vezes!\n
        \n——————————————————————————————————————————————————————————————''——————————————————————————————————————————————————————————————\n
        >Paradoxo<
            
            Consiste em empregar palavras que, ainda opostas quanto ao sentido, se fundem num mesmo enunciado, resultando numa proposição aparentemente absurda, 
        já que desafia, muitas vezes, a opinião compartilhada pela maioria.
            
            Exemplo:
            “A explosiva descoberta.		
            Ainda me atordoa.		
            Estou cego e vejo.		
            Arranco os olhos e vejo”.
            (Carlos Drummond de Andrade)\n
        \n——————————————————————————————————————————————————————————————''——————————————————————————————————————————————————————————————\n
        >Antítese<
            
            É a aproximação, na linguagem escrita ou falada, de termos ou expressões que têm sentidos opostos. 	
            
            Exemplo:
            -Um misto de alegria e tristeza tomou conta de Jonas quando pisou novamente na rua onde havia passado sua infância.

        ATENÇÃO!!! Não confunda antítese e paradoxo. 
        Veja os exemplos:
        -A verdade e a mentira fazem parte do dia a dia. (A antítese é marcada por palavras naturalmente opostas)
        -Os mesmo braços que serviram de abrigo hoje transmitem solidão. (O paradoxo é marcado por ideias opostas)\n
        \n——————————————————————————————————————————————————————————————''——————————————————————————————————————————————————————————————\n'''
    denotacao_conotacao = '''
         -----------------------
        | Denotação e Conotação |
         ----------------------- 
        
        A Conotação e a Denotação são as variações de significados que ocorrem no signo linguístico. 
        O signo linguístico é composto de um significante (letras e sons) e um significado (conceito, ideia).
        \n——————————————————————————————————————————————————————————————''——————————————————————————————————————————————————————————————\n
        >Sentido Conotativo<
            Sentido conotativo é a linguagem em que a palavra é utilizada em sentido figurado, subjetivo ou expressivo. 
            Ele depende do contexto em que é empregado, sendo muito utilizado na literatura.
            Exemplo:
                -Aquele homem é um cachorro.
                -Ana é um doce de pessoa.
                -Francis é fera em fazer sushi.
        \n——————————————————————————————————————————————————————————————''——————————————————————————————————————————————————————————————\n
        >Sentido Denotativo<
            Sentido denotativo é a linguagem em que a palavra é utilizada em seu sentido próprio, literal, 
            original, real, objetivo.
            Exemplo:
                -O cachorro da vizinha fugiu essa manhã.
                -O telefone quebrou.
                -A comida estava deliciosa.
        \n——————————————————————————————————————————————————————————————''——————————————————————————————————————————————————————————————\n'''
    ecologia = '''
         ----------
        | Ecologia |
         ----------

        A Ecologia é a ciência que estuda a interação entre os seres vivos e o ambiente em que vivem.
        Ao estudar ecologia é importante saber que ela se divide em Níveis de Organização, compostos por:
        -População
        -Comunidade
        -Ecossistemas 
        -Biosfera.

        >População< 

            A população representa o conjunto de organismos da mesma espécie que vivem juntos e apresentam maiores 
        chances de reprodução entre si.
        \n——————————————————————————————————————————————————————————————''——————————————————————————————————————————————————————————————\n      
        >Comunidade< 

            A comunidade representa o conjunto das populações que vivem numa mesma região, no qual vivem em determinado local,
        com condições ambientais específicas e interagindo entre si. 
        \n——————————————————————————————————————————————————————————————''——————————————————————————————————————————————————————————————\n
        >Ecossistemas< 

            O ecossistemas é o conjunto de comunidades que interagem entre si e com o ambiente.
            Ele é formado pela interação de biocenoses e biótopos. 
            A reunião de diferentes ecossistemas é conhecido como bioma e nele estão reunidas características próprias 
        de diversidade biológica e condições ambientais.
        \n——————————————————————————————————————————————————————————————''——————————————————————————————————————————————————————————————\n
        >Biosfera< 

            A biosfera é o nível mais amplo, pois ele corresponde ao conjunto de todos os ecossistemas das diferentes 
        regiões do planeta, ou seja, o local onde estão todos os seres vivos. 
        É a reunião de toda a biodiversidade existente na Terra.
        \n——————————————————————————————————————————————————————————————''——————————————————————————————————————————————————————————————\n
            Para melhor compreensão do mundo vivo, além dos níveis de organização, a ecologia moderna abrange diversos 
        conceitos que são fundamentais. 
            Conheça a seguir o seguir as definições dos principais conceitos que a ecologia estuda.
        \n——————————————————————————————————————————————————————————————''——————————————————————————————————————————————————————————————\n
        >Habitat< 

            O habitat é o ambiente físico em que vivem determinadas espécies. 
            As condições do ambiente dependem de fatores abióticos que afetam diretamente os seres vivos presentes. 
            Alguns exemplos são: o habitat do leão, as savanas e, o habitat do tatu, as florestas.
        \n——————————————————————————————————————————————————————————————''——————————————————————————————————————————————————————————————\n
        >Nicho Ecológico< 

            O Nicho Ecológico representa os hábitos e o modo de vida dos animais que representam seu nicho.
            Por exemplo: no grupo dos leões são as leoas que caçam e cuidam dos filhotes, enquanto os machos defendem de invasores.
        \n——————————————————————————————————————————————————————————————''——————————————————————————————————————————————————————————————\n
        >Cadeia Alimentar< 

            A cadeia alimentar representa as relações alimentares entre os organismos da biota.
            É através dos níveis tróficos da cadeia alimentar que é realizado o fluxo contínuo de energia e matéria.
        \n——————————————————————————————————————————————————————————————''——————————————————————————————————————————————————————————————\n
        >Relações Ecológicas<

            As relações ecológicas são as interações que ocorrem entre os seres vivos dentro dos ecossistemas. 
            Elas podem ser entre indivíduos da mesma espécie (intraespecífica) ou entre espécies diferentes (interespecíficas). 
            E também podem ser benéficas (positivas) ou prejudiciais (negativas) para as partes envolvidas.
        \n——————————————————————————————————————————————————————————————''——————————————————————————————————————————————————————————————\n
        >Ciclos Bioquímicos<

            Os ciclos bioquímicos representam o processo realizado entre energia e a matéria, que por sua vez, 
        se movimentam pelo ambiente de forma cíclica, fazendo assim a ciclagem dos nutrientes essenciais à manutenção da vida. 
        Alguns exemplos dos ciclos biogeoquímicos são: ciclo do carbono, do nitrogênio, do oxigênio e da água.
        \n——————————————————————————————————————————————————————————————''——————————————————————————————————————————————————————————————\n'''
    eletricidade = '''
         --------------
        | Eletricidade |
         --------------

            A Eletricidade é o movimento, usualmente de elétrons, produzido a partir de dois pontos de um condutor. 
            É a área da Física que estuda os fenômenos causados pelo trabalho das cargas elétricas. 
            Essa forma de energia está presente no nosso cotidiano não só nos aparelhos eletrônicos, mas também na natureza: 
        descargas elétricas que resultam em relâmpagos, por exemplo. 
            A eletricidade é, atualmente, o principal tipo de energia existente.

        O conceito é tão amplo que existem áreas de estudo que se ocupam cada uma de um aspecto da eletricidade:
        \n--------------------------------------------------------------''--------------------------------------------------------------\n
        >Eletrostática<

            Dedica-se ao comportamento das cargas elétricas sem movimento, ou em estado de repouso.
        \n——————————————————————————————————————————————————————————————''——————————————————————————————————————————————————————————————\n
        >Eletrodinâmica< 

            Ao contrário da eletricidade estática, a eletrodinâmica é, como indica o seu nome, dinâmica e, portanto, 
        está em constante movimento.
        \n——————————————————————————————————————————————————————————————''——————————————————————————————————————————————————————————————\n
        >Eletromagnetismo< 

            Estuda a relação da eletricidade com a capacidade de atrair e reprimir polos.
        \n----------------------------------------------------------------''---------------------------------------------------------------\n
        >História da Eletricidade<

            A eletricidade foi descoberta pelo “pai da Ciência”, o filósofo grego Tales de Mileto (625 a.C. - 547 a.C.).
            O achado que viria a revolucionar o mundo foi descoberto ao acaso, quando o pensador esfregou uma substância chamada 
        âmbar com pele de animal e observou que a partir disso pequenos objetos se movimentavam atraídos como pelo 
        efeito de um ímã.
            Com isso, iniciaram e aumentaram os estudos nessa área. 
            Entre outros pesquisadores, Otto von Guericke inventa uma máquina de cargas elétricas e Stephen Gray examina a 
        diferença do comportamento dos condutores e dos isolantes elétricos.
            Benjamin Franklin inventou o para-raios no século XVIII. 
            No século XIX, Luigi Galvani inventou a pilha voltaica, até que Hans Christian Orsted descobriu a 
        relação da eletricidade e o magnetismo. 
            Finalmente, surge a hidrelétrica, que é atualmente a principal fonte de energia do Brasil.
        \n----------------------------------------------------------------''---------------------------------------------------------------\n
        >O que é Eletricidade Estática?<
    
            A eletricidade estática é o processo de concentração de cargas elétricas em repouso que, a partir do contato ou 
        aproximação com outro corpo se atrita e, transferindo carga para este corpo, manifesta-se.
            Exemplo disso são as explosões que podem acontecer com materiais inflamáveis. 
            A eletricidade estática é objeto de estudo da área eletrostática, tal como foi mencionado acima.
        \n——————————————————————————————————————————————————————————————''——————————————————————————————————————————————————————————————\n
        >Eletricidade e Magnetismo<

            Eletricidade e Magnetismo são ambos fenômenos que se relacionam entre si. 
            Uma vez que o magnetismo tem a capacidade de atrair corpos, a eletricidade, por sua vez, produz um efeito magnético na 
        medida em que está sujeita a condutores que permitem a sua movimentação.
            O eletromagnetismo se ocupa da relação estabelecida entre eletricidade e magnetismo.
        \n——————————————————————————————————————————————————————————————''——————————————————————————————————————————————————————————————\n'''
    solucoes_quimicas = '''
         -------------------
        | Soluções Químicas |
         -------------------
        
        As soluções químicas são misturas homogêneas formadas por duas ou mais substâncias. 
        Os componentes de uma solução são denominados de soluto e solvente, onde: 
        
        -Soluto: Representa a substância dissolvida. 
        -Solvente: É a substância que dissolve.

        Um exemplo de solução é a mistura de água e açúcar, tendo a água como solvente e o açúcar como soluto.
        \n——————————————————————————————————————————————————————————————''——————————————————————————————————————————————————————————————\n
        >Classificação das soluções<
        
            Como vimos, uma solução consiste de duas partes: o soluto e o solvente. 
            Porém, esses dois componentes podem apresentar diferentes quantidades e características. 
            Como resultado, existem diversos tipos de soluções e cada uma delas baseia-se em uma determinada condição.
        \n——————————————————————————————————————————————————————————————''——————————————————————————————————————————————————————————————\n
        >Quantidade de soluto<

            De acordo com a quantidade de soluto que possuem, as soluções químicas podem ser:

                Soluções Saturadas:
                    Solução com a quantidade máxima de soluto totalmente dissolvido pelo solvente. 
                    Se mais soluto for acrescentado, o excesso acumula-se formando um corpo de fundo.

                Soluções Insaturadas:
                    Também chamada de não saturada, esse tipo de solução contém menor quantidade de soluto.

                Soluções Supersaturadas:
                    São soluções instáveis, nas quais a quantidade de soluto excede a capacidade de solubilidade do solvente.
        \n——————————————————————————————————————————————————————————————''——————————————————————————————————————————————————————————————\n
        >Estado Físico<
        
            As soluções também podem ser classificadas de acordo com o seu estado físico:
            
                Soluções Sólidas:
                    Formadas por solutos e solventes em estado sólido. 
                    Por exemplo, a união de cobre e níquel, que forma uma liga metálica.

                Soluções Líquidas:
                    Formadas por solventes em estado líquido e solutos que podem estar em estado sólido, líquido ou gasoso. 
                    Por exemplo, o sal dissolvido em água.

                Soluções Gasosas:
                    Formadas por solutos e solventes em estado gasoso. 
                    Por exemplo, o ar atmosférico.
        \n——————————————————————————————————————————————————————————————''——————————————————————————————————————————————————————————————\n
        >Natureza do soluto<

            Além disso, segundo a natureza do soluto, as soluções químicas são classificadas em:

                Soluções Moleculares:
                    Quando as partículas dispersas na solução são moléculas, por exemplo, o açúcar (molécula C12H22O11).

                Soluções Iônicas<:
                    Quando as partículas dispersas na solução são íons, por exemplo, o sal comum cloreto de sódio (NaCl), 
                formado pelos íons Na+ e Cl-.
        \n——————————————————————————————————————————————————————————————''——————————————————————————————————————————————————————————————\n
        >Coeficiente de Solubilidade<

            O coeficiente de solubilidade representa a capacidade máxima do soluto de se dissolver em uma determinada 
        quantidade de solvente. 
            Isso conforme as condições de temperatura e pressão.
            Conforme a solubilidade, as soluções podem ser:
            
                Soluções diluídas: 
                    A quantidade de soluto é menor em relação ao solvente.

                Soluções concentradas:
                    A quantidade de soluto é maior que a de solvente.

                Para calcular o coeficiente de solubilidade é utilizada a seguinte fórmula:

                    C = 100 x M1 ÷ M2

            C: coeficiente de solubilidade
            m1: massa do soluto
            m2: massa do solvente
        \n——————————————————————————————————————————————————————————————''——————————————————————————————————————————————————————————————\n
        >Concentração das Soluções<

            A concentração da solução indica a quantidade, em gramas, de soluto existente em um litro de solução. 
            Para se calcular a concentração utiliza-se a seguinte fórmula:

                C = M ÷ V

            C: concentração
            M: massa do soluto
            V: volume da solução
        \n——————————————————————————————————————————————————————————————''——————————————————————————————————————————————————————————————\n
        >Diluição das soluções<
            A diluição de soluções corresponde à adição mais solvente em uma solução. 
            Como resultado, passamos de uma solução mais concentrada para uma solução mais diluída.
            É importante ressaltar que a mudança ocorre no volume da solução e não na massa do soluto.
            Podemos concluir então que quando há o aumento do volume, a concentração diminui. 
            Em outras palavras, o volume e a concentração de uma solução são inversamente proporcionais.
        \n——————————————————————————————————————————————————————————————''——————————————————————————————————————————————————————————————\n'''
    transportes_no_brasil = '''
             -----------------------
            | Transportes no Brasil |
             -----------------------

            Os Transportes no Brasil reúnem os mais diversos meios de transporte, são eles: os terrestres, aquáticos, aéreos
            e dutoviários. 
            Entretanto o mais utilizado no país, seja para o transporte de carga ou de pessoas, é o transporte terrestre rodoviário, 
            realizado pelas estradas e rodovias, por veículos como carro, ônibus e caminhão.
            \n——————————————————————————————————————————————————————————————''—————————————————————————————————————————————————————————-—————\n
            >Meios de Transporte<

            Antes de mais nada, vale lembrar as categorias existentes para os meios de transporte, são classificadas segundo o local 
            em que ocorrem:
            \n——————————————————————————————————————————————————————————————''——————————————————————————————————————————————————————————-————\n
            >Transporte Terrestre<

            Realizado pela terra, sendo classificados em: rodoviário (rodovias), metroviário (metrovias) e ferroviário (ferrovias).
            \n——————————————————————————————————————————————————————————————''———————————————————————————————————————————————————————————-———\n    
            >Transporte Aquático< 

            Ocorrem nas hidrovias (vias de água), sendo classificadas em: marítimos (mar), fluviais (rios) e lacustre (lagos e lagoas)
            \n——————————————————————————————————————————————————————————————''——————————————————————————————————————————————————————————-————\n    
            >Transporte Aéreo< 

            Realizado pelas aerovias (vias no ar), como os aviões, helicópteros, balões, dentre outros.
            \n——————————————————————————————————————————————————————————————''———————————————————————————————————————————————————————————-———\n    
            >Transporte Dutoviário<

            Ocorre por meio de tubos (dutos).
            \n——————————————————————————————————————————————————————————————''—————————————————————————————————————————————————————————————-—\n
            >Resumo<

            Os sistemas de transportes no Brasil têm início no século XIX, com a construção de algumas ferrovias e, mais tarde, com a 
            expansão da malha rodoviária. 
            A denominada “Era das Ferrovias” marcou o período de expansão da malha ferroviária no país, que durou de 1870 a 1920.
            Em meados do século XX com o processo de industrialização, os governos democráticos, os quais buscavam o desenvolvimento político, 
            econômico e social do Brasil, focaram na construção de estradas, pondo de lado, o sistema ferroviário, que passou a ser considerado 
            lento e com elevado preço de implementação.
            As consequências desse feito são notórias até os dias de hoje, em que poucas linhas de ferro são utilizadas para o transporte de 
            pessoas, enquanto o sistema rodoviário sofre com uma infraestrutura problemática oferecida à população, donde muitas estradas e 
            rodovias apresentam péssimas condições para o transporte, desde a superlotação, a não pavimentação, falta de fiscalização, 
            excesso de pedágios e etc.
            Dentre os transportes aquáticos (fluvial, lacustre e marítimo), o transporte fluvial é o mais frequente no país, que conta com 
            16 hidrovias e 20 portos fluviais, sendo mais usado na região norte, tanto para o transporte de mercadorias quanto para o de pessoas.
            \n——————————————————————————————————————————————————————————————''—————————————————————————————————————————————————————————————-—\n'''
    area_de_figuras = '''
      ---------------------
     | Área figuras planas |
      ---------------------

     As áreas das figuras planas medem o tamanho da superfície da figura. Desse modo, podemos pensar que quanto maior a superfície da figura, maior será sua área.
     \n——————————————————————————————————————————————————————————————''——————————————————————————————————————————————————————————————\n
     >Principais Figuras Planas:<
        -Triangulo: Área = (base * altura)/2
        -Quadrado: Área = lado**2
        -Retângulo: Área = base * altura
        -Círculo: Área = π * raio**2
        -Trapézio: Área = ((basemaior + basemenor) * altura) ÷ 2
        -Losango: Área = (diagonalmaior * diagonalmenor) ÷ 2
     \n——————————————————————————————————————————————————————————————''——————————————————————————————————————————————————————————————\n
     >Área do cilindro<

     A área do cilindro corresponde a medida da superfície dessa figura.
     Lembre-se que o cilindro é uma figura geométrica espacial alongada e arredondada. 
     Ela possui dois círculos com raios de medidas equivalentes, os quais estão situados em planos paralelos.
     \n——————————————————————————————————————————————————————————————''——————————————————————————————————————————————————————————————\n
     >Fórmulas da Área< 
        -Área da base (Ab): essa figura é formada por duas bases: uma superior e outra inferior.
        Ab = π * r**2
        
        -Área Lateral: corresponde a medida da superfície lateral da figura.

     Al = 2π * r * h

        -Área total (At): é a medida total da superfície da figura.

     At = 2 * Ab + Al
     At = 2(π * r^2) + 2(π * r * h)
     \n——————————————————————————————————————————————————————————————''——————————————————————————————————————————————————————————————\n
     >Área da Esfera<

        A área da esfera corresponde a medida da superfície dessa figura geométrica espacial. 
        Lembre-se que a esfera é uma figura sólida e simétrica tridimensional.
        Para calcular a área da superfície esférica, utiliza-se a fórmula:
     Ae = 4.π.r2

     Onde:
     Ae: área da esfera
     r: raio
     \n——————————————————————————————————————————————————————————————''——————————————————————————————————————————————————————————————\n'''
    moda_media_mediana =  '''
      ----------------------- 
     | Média, Moda e Mediana |
      -----------------------
     \n——————————————————————————————————————————————————————————————''——————————————————————————————————————————————————————————————\n
     >Média<
         A média (Me) é calculada somando-se todos os valores de um conjunto de dados e dividindo-se pelo número de elementos 
     deste conjunto.
         Como a média é uma medida sensível aos valores da amostra, é mais adequada para situações em que os dados são distribuídos 
     mais ou menos de forma uniforme, ou seja, valores sem grandes discrepâncias.

        Me = (x1 + x2 + x3 + ... + xn )/n
     \n——————————————————————————————————————————————————————————————''——————————————————————————————————————————————————————————————\n
     >Moda<
         A Moda (Mo) representa o valor mais frequente de um conjunto de dados, sendo assim, para defini-la basta observar a 
     frequência com que os valores aparecem.
         Um conjunto de dados é chamado de bimodal quando apresenta duas modas, ou seja, dois valores são mais frequentes.

     \n——————————————————————————————————————————————————————————————''——————————————————————————————————————————————————————————————\n
     >Mediana<
         A Mediana (Md) representa o valor central de um conjunto de dados. Para encontrar o valor da mediana é necessário 
     colocar os valores em ordem crescente ou decrescente.
         Quando o número elementos de um conjunto é par, a mediana é encontrada pela média dos dois valores centrais. 
         Assim, esses valores são somados e divididos por dois.
     \n——————————————————————————————————————————————————————————————''——————————————————————————————————————————————————————————————\n'''
    
    #EXERCÍCIOS (LINGUAGENS)
    global linguagens1, linguagens2, linguagens3, linguagens4, linguagens5, linguagens6
    linguagens1 = '''
     Leia estes versos de Murilo Mendes:

     “As ondas amarguradas
     Encostam a cabeça nas pedras do cais.
     Até as ondas possuem
     Uma pedra para descansar a cabeça.
     Eu na verdade possuo
     Todas as pedras que há no mundo,
     Mas não descanso”.

     A figura de linguagem que ocorre nos versos 5 e 6 é:

     a) metáfora. 
     b) sinédoque.
     c) hipérbole. ---------
     d) aliteração.
     e) anáfora.
     \n——————————————————————————————————————————————————————————————''——————————————————————————————————————————————————————————————\n'''
    linguagens2 = '''
     Identifique a figura de linguagem no fragmento a seguir de Mário de Andrade:

     Moça linda, bem tratada,
     Três séculos de família,
     Burra como uma porta:
     Um amor!

     a) Sinédoque
     b) Aliteração
     c) Metáfora
     d) Personificação.
     e) Ironia. --------
     \n——————————————————————————————————————————————————————————————''——————————————————————————————————————————————————————————————\n'''
    linguagens3 = '''
      Quando o Rio de Janeiro derrubou pesos-pesados como Chicago e Tóquio e venceu a disputa para sediar os Jogos de 2016, 
      os olhos do mundo se viraram com otimismo para um emergente Brasil. 
      Em 2009, o ano da escolha carioca, com a crise mundial a emperrar as grandes economias, apostava-se que patrocinadores 
      afluiriam aos montes à medida que o projeto olímpico tomasse corpo. 
      Feitas as contas, porém, percebeu-se que entrou menos dinheiro no caixa do comitê organizador local do que se esperava 
      a um ano do grande espetáculo – algo em torno de 400 milhões de reais abaixo do projetado nos tempos em que o Cristo 
      Redentor disparava como um foguete na capa da revista inglês The Economist. 
      Um misto de burocracia e marasmo econômico dentro e fora do país espantou as empresas. 
      Os patrocínios não são a única razão, mas a principal, para o comitê, preocupado em não entrar no vermelho, rever o plano 
      original e passar a tesoura em uma lista de itens. 

     Ainda sobre o texto, as expressões “passar a tesoura”, “disparar como um foguete” e “entrar no vermelho” 
     foram utilizadas no sentido:

     a) denotativo, porque seus significados são literais.
     b) denotativo, visto que se referem ao sentido figurado.
     c) conotativo e denotativo, dependendo da parte do texto em que foram empregadas tais expressões.
     d) conotativo, já que se referem ao sentido figurado. -------
     e) conotativo, pois foram utilizados no sentido literal.
     \n——————————————————————————————————————————————————————————————''——————————————————————————————————————————————————————————————\n'''
    linguagens4 = '''
     Analise as frases a seguir.

     1. Frase é qualquer enunciado linguístico com sentido acabado.
     2. José, vem cá!
     3. Alô, quem fala?
     4. O sol é uma estrela de quinta grandeza.
    
     Levando-se em consideração as funções da linguagem, é correto afirmar-se que as frases acima são caracterizadas 
     respectivamente, pelas funções:

     a) 1. referencial,       2. fática,      3. emotiva,       4. conotativa.
     b) 1. conotativa,        2. fática,      3. conotativa,    4. referencial.
     c) 1. referencial,       2. emotiva,     3. fática,        4. metalinguística.
     d) 1. metalinguística,   2. conotativa,  3. fática,        4. referencial. ------
     e) 1. metalinguística,   2. fática,      3. emotiva,       4. conotativa.
     \n——————————————————————————————————————————————————————————————''——————————————————————————————————————————————————————————————\n'''
    linguagens5 = '''
     Leia o texto de Mario Quintana.

     Verbete
     Autodidata. — Ignorante por conta própria.
     (A vaca e o hipogrifo, 2008.) 

     O efeito de humor do texto está associado:

     a) à ironia, porque o termo “ignorante” é comumente contrário à ideia de instrução, ---------
     vinculada à palavra “autodidata”. 

     b) à personificação, porque os termos “autodidata” e “ignorante” conferem, no texto, 
     características humanas a um conceito abstrato.

     c) ao pleonasmo, porque a palavra “ignorante” retoma, de modo repetitivo, o sentido 
     já apresentado pelo termo “autodidata”.

     d) ao eufemismo, porque a expressão “ignorante por conta própria” atenua o sentido 
     negativo que geralmente se atribui ao termo “autodidata”.

     e) à hipérbole, porque a expressão “por conta própria” contribui para descrever as 
     virtudes do autodidata de maneira exagerada.
     \n——————————————————————————————————————————————————————————————''——————————————————————————————————————————————————————————————\n'''
    linguagens6 = '''
     Assinale a alternativa que defina ou explique o Eufemismo corretamente:

     a) É a substituição de um termo por outro baseada numa relação de analogia.
     b) Ocorre quando, numa enunciação, há uma mescla de diferentes sensações que são percebidas pelos órgão de sentido.    
     c) É a utilização de expressões mais leves para suavizar o impacto de enunciados tristes ou desagradáveis. ----------
     d) É aproximação de dois termos entre os quais existe alguma relação de semelhança.
     e) É a aproximação, na linguagem escrita ou falada, de termos ou expressões que têm sentidos opostos.
     \n——————————————————————————————————————————————————————————————''——————————————————————————————————————————————————————————————\n'''

    #EXERCÍCIOS (NATUREZA):
    global natureza1, natureza2, natureza3, natureza4, natureza5
    natureza1 = ''' 
     Em usinas hidrelétricas, a queda d’água move turbinas que acionam geradores. 
     Em usinas eólicas, os geradores são acionados por hélices movidas pelo vento. 
     Na conversão direta solar-elétrica são células fotovoltaicas que produzem tensão elétrica. 
     Além de todos produzirem eletricidade, esses processos têm em comum o fato de:
    
     a) não provocarem impacto ambiental.
     b) independerem de condições climáticas. 
     c) a energia gerada poder ser armazenada.
     d) utilizarem fontes de energia renováveis. -------
     e) dependerem das reservas de combustíveis fósseis.
     \n——————————————————————————————————————————————————————————————''——————————————————————————————————————————————————————————————\n'''
    natureza2 = '''
     Um estudante de Biologia pretende estudar uma espécie de planta que vive em uma região de serra de sua cidade. 
     Os indivíduos dessa espécie, que são encontrados apenas nessa região, recebem a denominação de:

     a) comunidade.
     b) população. ------
     c) biosfera.
     d) sociedade.
     e) colônia.
     \n——————————————————————————————————————————————————————————————''——————————————————————————————————————————————————————————————\n'''
    natureza3 = '''
     Os organismos vivos de um ecossistema interagem entre si e também com o meio em que vivem.
     O conjunto de todas as espécies de uma região é conhecido por:

     a) população.
     b) biosfera.
     c) comunidade. ------
     d) ecossistema.
     e) biótopo.
     \n——————————————————————————————————————————————————————————————''——————————————————————————————————————————————————————————————\n'''
    natureza4 = '''
     Se duas populações de animais de espécies diferentes, que pertencem ao mesmo gênero e ocupam o mesmo nicho 
     ecológico, forem colocadas num mesmo meio, espera-se que:

     a) ocorra competição entre elas e ambas desapareçam.
     b) adaptem-se ao meio, reduzindo, cada uma, sua população à metade.
     c) uma delas vença a competição, determinando a eliminação da outra. ------
     d) ocorra mutualismo e ambas aumentem suas populações.
     e) ambas continuem com o mesmo número populacional.
     \n——————————————————————————————————————————————————————————————''——————————————————————————————————————————————————————————————\n'''
    natureza5 = '''
     Uma população apresenta sempre um crescimento limitado, uma vez que uma grande quantidade de indivíduos 
     pode prejudicar a captação de recursos. 
     Entre os fatores expostos a seguir, qual promove o aumento de uma população?

     a) Mortalidade.
     b) Imigração. -------
     c) Predação.
     d) Emigração.
     e) Competição intraespecífica.
     \n——————————————————————————————————————————————————————————————''——————————————————————————————————————————————————————————————\n'''

    #EXERCÍCIOS (HUMANAS):
    global humanas1, humanas2, humanas3, humanas4, humanas5
    humanas1 = '''
     Em geral, países com dimensões continentais encontram mais dificuldade em desenvolver uma logística eficiente, pois, além de enfrentar as distâncias, há o desafio de se superar as diversidades climáticas e os obstáculos naturais. Nesse sentido, esses países precisam desenvolver políticas que visem à diversificação de seus modais e ampliação da tecnologia adequada.

     O meio de transporte mais recomendado para a integração terrestre em territórios com as características acima é o:
     a) rodoviário
     b) ferroviário
     c) aéreo
     d) subterrâneo
     e) dutoviário
     \n——————————————————————————————————————————————————————————————''——————————————————————————————————————————————————————————————\n'''
    humanas2 = '''
     As ferrovias são frequentemente indicadas como a melhor opção para o escoamento de cargas e, até mesmo, 
     de pessoas em todo o território nacional. Entre as vantagens que esse tipo de transporte oferece para o país, 
     podemos assinalar, EXCETO:

     a) Baixo custos de manutenção e consumo.
     b) Participação no deslocamento de todo o percurso da mercadoria a ser entregue.
     c) Desafogamento do trânsito nas rodovias.
     d) Melhorias na relação entre cargas transportadas e combustível consumido.
     e) Menor quantidade estatística de acidentes e perdas de carga.
     \n——————————————————————————————————————————————————————————————''——————————————————————————————————————————————————————————————\n'''
    humanas3 = '''
     As ferrovias no Brasil estão geograficamente concentradas:

     a) na região Nordeste, como resultado das políticas coloniais de transportes das commodities aqui cultivadas pela metrópole.

     b) na região Sudeste, em razão das estruturas instaladas no auge da economia cafeeira.

     c) no Centro-Oeste, como uma obra de promoção da política da Marcha para o Oeste.

     d) no Sul, para atender os interesses das oligarquias gaúchas.

     e) em todo o litoral, como herança da concentração populacional nessa faixa do país.
     \n——————————————————————————————————————————————————————————————''——————————————————————————————————————————————————————————————\n'''
    humanas4 = '''
     Sobre o transporte aéreo no país, é correto afirmar:
     a)A ponte aérea Rio-São Paulo tornou-se uma das mais movimentadas do mundo.
     b)Esse tipo de transporte de carga superou o ferroviário.
     c)Tradicionalmente o transporte aéreo sempre atendeu a uma grande parcela da população brasileira.
     d)O ritmo de investimento na infraestrutura acompanhou ao aumento da demanda verificada nos últimos anos.
     e)A ponte aérea São Paulo- Brasília tornou-se nos últimos anos a mais movimentada rota latino-americana.
     \n——————————————————————————————————————————————————————————————''——————————————————————————————————————————————————————————————\n'''
    humanas5 = '''
     "O transporte público no Brasil sempre foi alvo de muitas reclamações ao longo do tempo. Na maioria das vezes, as queixas referem-se ao fato de os veículos estarem sempre lotados, às condições ruins dos carros e à baixa qualidade dos serviços prestados […]. A insatisfação da população com o transporte coletivo nas cidades brasileiras, no entanto, não é uma questão recente. Pesquisas realizadas pelo Instituto de Pesquisa Econômica Aplicada (IPEA), em 2011 e 2012, revelaram um quadro negativo, com avaliações classificadas como “péssimas ou ruins” ultrapassando os 60%”.

     Assinale a alternativa que indica um dos principais elementos responsáveis pelos problemas do transporte público no Brasil.

     a) Ausência de veículos particulares para a população.
     b) Crescimento das cidades menor que o do campo.
     c) Barateamento das passagens, elevando a procura e diminuindo os serviços.
     d) Crescimento desordenado urbano sem um acompanhamento em infraestrutura.
     e) Federalização do transporte coletivo pela Constituição de 1988.
     \n——————————————————————————————————————————————————————————————''——————————————————————————————————————————————————————————————\n'''

    #EXERCÍCIOS (MATEMÁTICA):
    global matematica1, matematica2, matematica3, matematica4
    matematica1 = '''
     Nos quatro primeiros dias úteis de uma semana o gerente de uma agência bancária atendeu 19, 15, 17 e 21 clientes. 
     No quinto dia útil dessa semana esse gerente atendeu n clientes.
     Se a média do número diário de clientes atendidos por esse gerente nos cinco dias úteis dessa semana foi 19, 
     a mediana foi:

     a) 21.
     b) 19.
     c) 18.
     d) 20.
     e) 23.
     \n——————————————————————————————————————————————————————————————''——————————————————————————————————————————————————————————————\n'''
    matematica2 = '''
     Um festival foi realizado num campo de 240 m por 45 m. Sabendo que por cada 2 m2 havia, em média, 7 pessoas, 
     quantas pessoas havia no festival?

     a) 42.007
     b) 41.932
     c) 37.800
     d) 24.045
     e) 10.000
     \n——————————————————————————————————————————————————————————————''——————————————————————————————————————————————————————————————\n'''
    matematica3 = '''
     Um cilindro circular reto de altura 7 cm tem volume igual a 28π cm³. A área total desse cilindro, em cm², é:

     a) 30π
     b) 32π
     c) 34π
     d) 36π
     \n——————————————————————————————————————————————————————————————''——————————————————————————————————————————————————————————————\n'''
    matematica4 = '''
     Qual é a área de uma esfera cujo raio mede 63 cm? 
     Considere π = 3.

     a) 47628 cm2
     b) 48628 cm2
     c) 49628 cm2
     d) 50000 cm2
     e) 51628 cm2
     \n——————————————————————————————————————————————————————————————''——————————————————————————————————————————————————————————————\n'''

    def menu_inicial():
        os.system('clear') or None
        def menu_materias():
            materias = '''
            |-----------------------------------|
            |        Selecione a matéria        |
            |             desejada:             |
            |                                   |
            |     [1] Matemática                |
            |     [2] Linguagens                |
            |     [3] Ciêcias da Natureza       |
            |     [4] Ciências Humanas          |
            |                                   |
            |     [0] Voltar ao Menu Inicial    |
            |-----------------------------------|'''

            #ESCOLHA DE MATÉRIA
            while 1:
                print(materias)
                opcao_materia = int(input("\nDigite a opção desejada: "))
                
                #OPÇÕES
                if opcao_materia == 1:          #MATEMÁTICA
                    os.system('clear') or None
                    temas = '''
                    |----------------------------------|
                    |       Temas de Matemática:       |
                    |                                  |
                    |    [1] Média, Moda e Mediana     |
                    |    [2] Área de figuras planas,   |
                    |    prismas, cilindros, cones     |     
                    |            e esferas.            |
                    |                                  |
                    |    [0] Voltar ao Menu Inicial    |
                    |----------------------------------|'''

                    #SELECIONAR
                    while 1:
                        print(temas)
                        opcao_temas = int(input("\nDigite a opção desejada: "))
                        
                        #OPÇÕES
                        if opcao_temas == 1:
                            os.system('clear') or None
                            print(moda_media_mediana)
                            break
                        elif opcao_temas == 2:
                            os.system('clear') or None
                            print(area_de_figuras)
                            break
                        elif opcao_temas == 0:
                            os.system('clear') or None 
                            menu_inicial()
                            break
                        else:
                            os.system('clear') or None
                            print("\nOpção inválida! \nTente novamente.\n")
                            time.sleep(2)
                            os.system('clear') or None
                    break
                elif opcao_materia == 2:        #LINGUAGENS
                    os.system('clear') or None
                    temas = '''
                    |----------------------------------|
                    |       Temas de Linguagens:       |
                    |                                  |
                    |     [1] Figuras de Linguagem     |
                    |     [2] Denotação e Conotação    |
                    |                                  |
                    |    [0] Voltar ao Menu Inicial    |
                    |----------------------------------|'''

                    #SELECIONAR
                    while 1:
                        print(temas)
                        opcao_temas = int(input("\nDigite a opção desejada: "))
                        
                        #OPÇÕES
                        if opcao_temas == 1:
                            os.system('clear') or None
                            print(figuras_de_linguagem)
                            break
                        elif opcao_temas == 2:
                            os.system('clear') or None
                            print(denotacao_conotacao)
                            break
                        elif opcao_temas == 0:
                            os.system('clear') or None 
                            menu_inicial()
                            break
                        else:
                            os.system('clear') or None
                            print("\nOpção inválida! \nTente novamente.\n")
                            time.sleep(2)
                            os.system('clear') or None
                    break
                elif opcao_materia == 3:        #CIÊNCIAS DA NATUREZA
                    os.system('clear') or None
                    temas = ('''
                    |----------------------------------|
                    |       Temas de Ciências          |
                    |           da Natureza:           |
                    |                                  |
                    |     [1] Ecologia                 |
                    |     [2] Eletricidade             |
                    |     [3] Soluções Químicas        |
                    |                                  |
                    |    [0] Voltar ao Menu Inicial    |
                    |----------------------------------|''')  

                    #SELECIONAR
                    while 1:
                        print(temas)
                        opcao_temas = int(input("\nDigite a opção desejada: "))
                        
                        #OPÇÕES
                        if opcao_temas == 1:
                            os.system('clear') or None
                            print(ecologia)
                            break
                        elif opcao_temas == 2:
                            os.system('clear') or None
                            print(eletricidade)
                            break
                        elif opcao_temas == 3:
                            os.system('clear') or None
                            print(solucoes_quimicas)
                            break
                        elif opcao_temas == 0:
                            os.system('clear') or None 
                            menu_inicial()
                            break
                        else:
                            os.system('clear') or None
                            print("\nOpção inválida! \nTente novamente.\n")
                            time.sleep(2)
                            os.system('clear') or None          

                    break
                elif opcao_materia == 4:        #CIÊNCIAS HUMANAS
                    os.system('clear') or None
                    temas = '''
                    |----------------------------------|
                    |       Temas de Linguagens:       |
                    |                                  |
                    |     [1] Transportes no Brasil    |
                    |                                  |
                    |    [0] Voltar ao Menu Inicial    |
                    |----------------------------------|'''

                    #SELECIONAR
                    while 1:
                        print(temas)
                        opcao_temas = int(input("\nDigite a opção desejada: "))
                        
                        #OPÇÕES
                        if opcao_temas == 1:
                            os.system('clear') or None
                            print("c_humanas_resumo_DIT()")
                            break
                        elif opcao_temas == 0:
                            os.system('clear') or None 
                            menu_inicial()
                            break
                        else:
                            os.system('clear') or None
                            print("\nOpção inválida! \nTente novamente.\n")
                            time.sleep(2)
                            os.system('clear') or None
                    break
                elif opcao_materia == 0:        #MENU INICIAL
                    os.system('clear') or None 
                    menu_inicial()
                    break
                else:                           #OPÇÃO INVÁLIDA
                    os.system('clear') or None
                    print("\nOpção inválida! \nTente novamente.\n")
                    time.sleep(2)
                    os.system('clear') or None    

        def menu_competicao():
            competicao ='''
            |------------------------------------|
            |        Selecione o modo de         |
            |        competição desejado:        |
            |                                    |
            |     [1] Modo Solo                  |
            |                                    |
            |     [0] Voltar ao Menu Inicial     |
            |------------------------------------|'''

            #SELECIONAR
            while 1:
                print(competicao)
                opcao_competicao = int(input("\nDigite a opção desejada: "))
                
                #OPÇÕES
                if opcao_competicao == 1:           #MODO SOLO 
                    os.system('clear') or None
                    listas = '''
                    |------------------------------|
                    |        Escolha o tema        |
                    |        para competir:        |
                    |                              |
                    |    [1] Matemática            |
                    |    [2] Linguagens            |
                    |    [3] Ciências da Natureza  |
                    |    [4] Ciências Humanas      |
                    |------------------------------|'''

                    #SELECIONAR
                    while 1:
                        print(listas)
                        opcao_lista = int(input("\nDigite a opção desejada: "))
                        pontos_linguagens = 0
                        pontos_natureza = 0
                        pontos_humanas = 0
                        pontos_matematica = 0

                        #OPÇÕES:
                        if opcao_lista == 1:       #MATEMÁTICA
                            os.system('clear') or None
                            print(matematica1)
                            matematica1_resposta = input("Resposta: ")
                            os.system('clear') or None
                            print(matematica2)
                            matematica2_resposta = input("Resposta: ")
                            os.system('clear') or None
                            print(matematica3)
                            matematica3_resposta = input("Resposta: ")
                            os.system('clear') or None
                            print(matematica4)
                            matematica4_resposta = input("Resposta: ")
                            os.system('clear') or None
                            print(matematica5)
                            
                            if matematica1_resposta == 'd':     #QST 1
                                print("Resposta 1 correta!")
                                pontos_matematica += 10
                            else:
                                print("Resposta 1 errada!")     
                            if matematica2_resposta == 'b':     #QST 2
                                print("Resposta 2 correta!")
                                pontos_matematica += 20
                            else:
                                print("Resposta 2 errada!") 
                            if matematica3_resposta == 'c':     #QST 3
                                print("Resposta 3 correta!")
                                pontos_matematica += 30
                            else:
                                print("Resposta 3 errada!")
                            if matematica4_resposta == 'c':     #QST 4
                                print("Resposta 4 correta!")
                                pontos_matematica += 50
                            else:
                                print("Resposta 4 errada!")

                            print("\nPontuação = %d\n" %pontos_matematica)
                            time.sleep(3)
                            os.system('clear') or None
                            break
                        elif opcao_lista == 2:     #LINGUAGENS
                            os.system('clear') or None
                            print(linguagens1)
                            linguagens1_resposta = input("Resposta: ")
                            os.system('clear') or None
                            print(linguagens2)
                            linguagens2_resposta = input("Resposta: ")
                            os.system('clear') or None
                            print(linguagens3)
                            linguagens3_resposta = input("Resposta: ")
                            os.system('clear') or None
                            print(linguagens4)
                            linguagens4_resposta = input("Resposta: ")
                            os.system('clear') or None
                            print(linguagens5)
                            linguagens5_resposta = input("Resposta: ")
                            os.system('clear') or None
                            print(linguagens6)
                            linguagens6_resposta = input("Resposta: ")
                            os.system('clear') or None

                            if linguagens1_resposta == 'c':     #QST 1
                                print("Resposta 1 correta!")
                                pontos_linguagens += 10
                            else:
                                print("Resposta 1 errada!")     
                            if linguagens2_resposta == 'e':     #QST 2
                                print("Resposta 2 correta!")
                                pontos_linguagens += 15
                            else:
                                print("Resposta 2 errada!") 
                            if linguagens3_resposta == 'd':     #QST 3
                                print("Resposta 3 correta!")
                                pontos_linguagens += 20
                            else:
                                print("Resposta 3 errada!")
                            if linguagens4_resposta == 'd':     #QST 4
                                print("Resposta 4 correta!")
                                pontos_linguagens += 25
                            else:
                                print("Resposta 4 errada!")
                            if linguagens5_resposta == 'a':     #QST 5
                                print("Resposta 5 correta!")
                                pontos_linguagens += 30
                            else:
                                print("Resposta 5 errada!")
                            if linguagens6_resposta == 'c':     #QST 6
                                print("Resposta 6 correta!")
                                pontos_linguagens += 35
                            else:
                                print("Resposta 6 errada!")
                            print("\nPontuação = %d\n" %pontos_linguagens)
                            time.sleep(3)
                            os.system('clear') or None
                            break
                        elif opcao_lista == 3:     #CIENCIAS DA NATUREZA
                            os.system('clear') or None
                            print(natureza1)
                            natureza1_resposta = input("Resposta: ")
                            os.system('clear') or None
                            print(natureza2)
                            natureza2_resposta = input("Resposta: ")
                            os.system('clear') or None
                            print(natureza3)
                            natureza3_resposta = input("Resposta: ")
                            os.system('clear') or None
                            print(natureza4)
                            natureza4_resposta = input("Resposta: ")
                            os.system('clear') or None
                            print(natureza5)
                            natureza5_resposta = input("Resposta: ")
                            os.system('clear') or None
                            
                            if natureza1_resposta == 'd':     #QST 1
                                print("Resposta 1 correta!")
                                pontos_natureza += 10
                            else:
                                print("Resposta 1 errada!")     
                            if natureza2_resposta == 'b':     #QST 2
                                print("Resposta 2 correta!")
                                pontos_natureza += 15
                            else:
                                print("Resposta 2 errada!") 
                            if natureza3_resposta == 'c':     #QST 3
                                print("Resposta 3 correta!")
                                pontos_natureza += 20
                            else:
                                print("Resposta 3 errada!")
                            if natureza4_resposta == 'c':     #QST 4
                                print("Resposta 4 correta!")
                                pontos_natureza += 25
                            else:
                                print("Resposta 4 errada!")
                            if natureza5_resposta == 'b':     #QST 5
                                print("Resposta 5 correta!")
                                pontos_natureza += 30
                            else:
                                print("Resposta 5 errada!")
                            print("\nPontuação = %d\n" %pontos_natureza)
                            time.sleep(3)
                            os.system('clear') or None
                            break
                        elif opcao_lista == 4:     #CIÊNCIAS HUMANAS
                            os.system('clear') or None
                            print(humanas1)
                            humanas1_resposta = input("Resposta: ")
                            os.system('clear') or None
                            print(humanas2)
                            humanas2_resposta = input("Resposta: ")
                            os.system('clear') or None
                            print(humanas3)
                            humanas3_resposta = input("Resposta: ")
                            os.system('clear') or None
                            print(humanas4)
                            humanas4_resposta = input("Resposta: ")
                            os.system('clear') or None
                            print(humanas5)
                            humanas5_resposta = input("Resposta: ")
                            os.system('clear') or None

                            if humanas1_resposta == 'c':     #QST 1
                                print("Resposta 1 correta!")
                                pontos_humanas += 10
                            else:
                                print("Resposta 1 errada!")     
                            if humanas2_resposta == 'e':     #QST 2
                                print("Resposta 2 correta!")
                                pontos_linguagens += 15
                            else:
                                print("Resposta 2 errada!") 
                            if humanas3_resposta == 'd':     #QST 3
                                print("Resposta 3 correta!")
                                pontos_humanas += 20
                            else:
                                print("Resposta 3 errada!")
                            if humanas4_resposta == 'd':     #QST 4
                                print("Resposta 4 correta!")
                                pontos_humanas += 25
                            else:
                                print("Resposta 4 errada!")
                            if humanas5_resposta == 'a':     #QST 5
                                print("Resposta 5 correta!")
                                pontos_humanas += 30
                            else:
                                print("Resposta 5 errada!")

                            print("\nPontuação = %d\n" %pontos_humanas)
                            time.sleep(3)
                            os.system('clear') or None 
                            break                
                        else:                      #OPÇÃO INVÁLIDA
                            os.system('clear') or None
                            print("\nOpção inválida! \nTente novamente.\n")
                            time.sleep(2)
                            os.system('clear') or None
                        break
                     
                elif opcao_competicao == 0:         #MENU INICIAL
                    os.system('clear') or None 
                    menu_inicial()
                    break
                else:                               #OPÇÃO INVÁLIDA
                    os.system('clear') or None      
                    print("\nOpção inválida! \nTente novamente.\n")
                    time.sleep(2)
                    os.system('clear') or None 
        
        def menu_simulado():
            simulados = '''
            |------------------------------|
            |       Selecione o modo       |
            |     de simulado desejado:    |
            |                              |
            |    [1] Matemática            |
            |    [2] Linguagens            |
            |    [3] Ciências da Natureza  |
            |    [4] Ciências Humanas      |
            |                              |
            |  [0] Voltar ao Menu Inicial  |
            |------------------------------|'''


            #SELECIONAR
            while 1:
                print(simulados)
                opcao_simulado = int(input("\nDigite a opção desejada: "))
                
                #OPÇÕES
                if opcao_simulado == 1:                 #MATEMÁTICA
                    os.system('clear') or None
                    print("Matematica")
                    break
                elif opcao_simulado== 2:                #LINGUAGENS
                    os.system('clear') or None
                    print(linguagens1)
                    linguagens1_resposta = input("Resposta: ")
                    os.system('clear') or None
                    print(linguagens2)
                    linguagens2_resposta = input("Resposta: ")
                    os.system('clear') or None
                    print(linguagens3)
                    linguagens3_resposta = input("Resposta: ")
                    os.system('clear') or None
                    print(linguagens4)
                    linguagens4_resposta = input("Resposta: ")
                    os.system('clear') or None
                    print(linguagens5)
                    linguagens5_resposta = input("Resposta: ")
                    os.system('clear') or None
                    print(linguagens6)
                    linguagens6_resposta = input("Resposta: ")
                    os.system('clear') or None

                    if linguagens1_resposta == 'c':     #QST 1
                        print("Resposta 1 correta! :D\n")
                    else:
                        print("Resposta 1 incorreta! :(")
                        print("Que tal estudarmos mais um pouco de Figuras de Liguagem?\n")
                    if linguagens2_resposta == 'e':     #QST 2
                        print("Resposta 2 correta! :D\n")
                    else:
                        print("Resposta 2 incorreta! :(")
                        print("Que tal estudarmos mais um pouco de Figuras de Liguagem?\n")
                    if linguagens3_resposta == 'd':     #QST 3
                        print("Resposta 3 correta! :D\n")
                    else:
                        print("Resposta 3 incorreta! :(")
                        print("Que tal estudarmos mais um pouco de Denotação e Conotação?\n")
                    if linguagens4_resposta == 'd':     #QST 4
                        print("Resposta 4 correta! :D\n")
                    else:
                        print("Resposta 4 incorreta! :(")
                        print("Que tal estudarmos mais um pouco de Figuras de Liguagem?\n")
                    if linguagens5_resposta == 'a':     #QST 5
                        print("Resposta 5 correta! :D\n")
                    else:
                        print("Resposta 5 incorreta! :(")
                        print("Que tal estudarmos mais um pouco de Figuras de Liguagem?\n")
                    if linguagens6_resposta == 'c':     #QST 6
                        print("Resposta 6 correta! :D\n")
                    else:
                        print("Resposta 6 incorreta! :(")
                        print("Que tal estudarmos mais um pouco de Figuras de Liguagem?\n")

                    time.sleep(5) 
                    os.system('clear') or None
                    menu_simulado
                    break
                elif opcao_simulado== 3:                #CIÊNCIAS DA NATUREZA
                    os.system('clear') or None
                    print(natureza1)
                    natureza1_resposta = input("Resposta: ")
                    os.system('clear') or None
                    print(natureza2)
                    natureza2_resposta = input("Resposta: ")
                    os.system('clear') or None
                    print(natureza3)
                    natureza3_resposta = input("Resposta: ")
                    os.system('clear') or None
                    print(natureza4)
                    natureza4_resposta = input("Resposta: ")
                    os.system('clear') or None
                    print(natureza5)
                    natureza5_resposta = input("Resposta: ")
                    os.system('clear') or None

                    if natureza1_resposta == 'd':     #QST 1
                        print("Resposta 1 correta! :D\n")
                    else:
                        print("Resposta 1 incorreta! :(")
                        print("Que tal estudarmos mais um pouco de Eletricidade?\n")
                    if natureza2_resposta == 'b':     #QST 2
                        print("Resposta 2 correta! :D\n")
                    else:
                        print("Resposta 2 incorreta! :(")
                        print("Que tal estudarmos mais um pouco de Ecologia?\n")
                    if natureza3_resposta == 'c':     #QST 3
                        print("Resposta 3 correta! :D\n")
                    else:
                        print("Resposta 3 incorreta! :(")
                        print("Que tal estudarmos mais um pouco de Ecologia?\n")
                    if natureza4_resposta == 'c':     #QST 4
                        print("Resposta 4 correta! :D\n")
                    else:
                        print("Resposta 4 incorreta! :(")
                        print("Que tal estudarmos mais um pouco de Ecologia\n")
                    if natureza5_resposta == 'b':     #QST 5
                        print("Resposta 5 correta! :D\n")
                    else:
                        print("Resposta 5 incorreta! :(")
                        print("Que tal estudarmos mais um pouco de Ecologia\n")

                    time.sleep(5) 
                    os.system('clear') or None
                    menu_simulado
                    break
                elif opcao_simulado== 4:                #CIÊNCIAS HUMANAS 
                    os.system('clear') or None
                    print(humanas1)
                    humanas1_resposta = input("Resposta: ")
                    os.system('clear') or None
                    print(humanashumanas2)
                    humanas2_resposta = input("Resposta: ")
                    os.system('clear') or None
                    print(humanas3)
                    humanas3_resposta = input("Resposta: ")
                    os.system('clear') or None
                    print(humanas4)
                    humanas4_resposta = input("Resposta: ")
                    os.system('clear') or None
                    print(humanas5)
                    humanas5_resposta = input("Resposta: ")
                    os.system('clear') or None

                    if humanas1_resposta == 'c':     #QST 1
                        print("Resposta 1 correta! :D\n")
                    else:
                        print("Resposta 1 incorreta! :(")
                        print("Que tal estudarmos mais um pouco de Transportes no Brasil?\n")
                    if humanas2_resposta == 'b':     #QST 2
                        print("Resposta 2 correta! :D\n")
                    else:
                        print("Resposta 2 incorreta! :(")
                        print("Que tal estudarmos mais um pouco de Transportes no Brasil?\n")
                    if humanas3_resposta == 'b':     #QST 3
                        print("Resposta 3 correta! :D\n")
                    else:
                        print("Resposta 3 incorreta! :(")
                        print("Que tal estudarmos mais um pouco de Transportes no Brasil?\n")
                    if humanas4_resposta == 'a':     #QST 4
                        print("Resposta 4 correta! :D\n")
                    else:
                        print("Resposta 4 incorreta! :(")
                        print("Que tal estudarmos mais um pouco de Transportes no Brasil\n")
                    if humanasa5_resposta == 'd':     #QST 5
                        print("Resposta 5 correta! :D\n")
                    else:
                        print("Resposta 5 incorreta! :(")
                        print("Que tal estudarmos mais um pouco de Transportes no Brasil?\n")
                elif opcao_simulado == 0:
                    os.system('clear') or None 
                    menu_inicial()
                    break
                else:
                    os.system('clear') or None
                    print("\nOpção inválida! \nTente novamente.\n")
                    time.sleep(2)
                    os.system('clear') or None  
        
        def menu_creditos():
            os.system('clear') or None
            print("Jogo desenvolvido por alunos da Universidade Presbiteriana Mackenzie. \n")
            time.sleep(3)
            print("Francis Kenji Teruya          TIA: 41912055")
            time.sleep(1)        
            print("Guilherme Heitor Pensutti     TIA: 41921704")
            time.sleep(1)
            print("João Vitor Duarte Queiroz     TIA: 41930096") 
            time.sleep(4)
            os.system('clear') or None

        inicio = '''
        |------------------------------|
        |        |Enem -------|        |
        |        |---- Estudei|        |
        |                              |
        |    [1] Resumos/Exercicíos    |
        |    [2] Competição            |
        |    [3] Simulados             |
        |    [4] Créditos              |
        |------------------------------|'''

        #SELECIONAR
        while 1:
            print(inicio)
            opcao_menu = int(input("\nDigite a opção desejada: "))
            
            #OPÇÕES:
            if opcao_menu == 1:       #RESUMOS/EXERCÍCIOS
                os.system('clear') or None
                menu_materias()
                break
            elif opcao_menu == 2:     #COMPETIÇÃO
                os.system('clear') or None
                menu_competicao()
                break
            elif opcao_menu == 3:     #SIMULADOS
                os.system('clear') or None
                menu_simulado()
                break
            elif opcao_menu == 4:     #CRÉDITOS
                os.system('clear') or None
                menu_creditos()    
                break
            else:                     #OPÇÃO INVÁLIDA
                os.system('clear') or None
                print("\nOpção inválida! \nTente novamente.\n")
                time.sleep(2)
                os.system('clear') or None

    menu_inicial()

EnemEstudei()
