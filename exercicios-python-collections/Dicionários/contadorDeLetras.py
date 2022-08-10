from collections import Counter

texto1 = """
Benefícios do Git Flow
Desenvolvimento Paralelo
Uma das grandes vantagens do Git Flow é que ele torna o desenvolvimento paralelo muito simples, isolando o novo desenvolvimento do trabalho finalizado.

O novo desenvolvimento (como novas funcionalidades e correções de bugs não emergenciais) é feito em Branches de features e só é mesclado de volta ao corpo principal do código quando as pessoas desenvolvedoras estão seguras de que o código está pronto para lançamento.

Outro ponto, é que se você for solicitado a alternar de uma tarefa para outra, tudo o que você precisa fazer é confirmar suas alterações e, em seguida, criar uma nova Branch de feature para sua nova tarefa. Quando essa tarefa estiver concluída, basta fazer o checkout da branch e continuar de onde parou a outra tarefa.
Colaboração
As branches de feature também facilitam a colaboração de duas ou mais pessoas desenvolvedoras em uma mesma tarefa, porque cada branch é uma caixa de proteção onde as únicas alterações que ocorreram são as que aconteceram para realizar a tarefa.

Com isso, conseguimos compartilhar nossa branch com outras pessoas para elas nos ajudarem ou terminarem a tarefa. Isso também torna muito fácil de ver e acompanhar o que cada pessoa está fazendo em um projeto.

Área de preparação
Mais conhecida como a branch develop, com ela é possível ter um local onde podemos testar todas as nossas novas features, isso sem se preocupar se estamos ou não em produção.

Suporte para correções de emergência
Com o suporte a branches de hotfix se torna possível realizar alterações de emergência sem preocupações, sabendo que o hotfix conterá apenas a correção. Não há risco de você acidentalmente mesclar um código que não deveria, pois tudo está devidamente separado.

Mas como nem tudo são flores, agora que vimos os benefícios do Git Flow, vamos ficar por dentro também das desvantagens de utilizar essa abordagem.

Desvantagens do Git Flow
O fluxo e os processos do Git Flow são complexos, além de serem muitos, dependendo da complexidade do projeto ao qual esteja trabalhando, a estrutura do Git Flow pode tornar o processo ainda mais complicado e o desenvolvimento ainda mais lento, pois pense o quão complicado é controlar um repositório onde temos alterações ocorrendo a todo minuto em diversas branches.

Além disso, por violar a regra de branches de curta duração, por conta do ciclo de desenvolvimento longo, o Git Flow não consegue se adaptar bem com o DevOps, mais especificamente com a integração e implantação contínua.

A quantidade de branches que são criadas com o Git Flow e que podem ter diferentes tempos de vida, aumentam potencialmente os conhecidos conflitos do Git na hora do merge.Outro ponto é que se você utilizar o Git Flow, o comando rebase do Git terá que ser esquecido, pois não poderá ser utilizado.

Por esses motivos, se estiver trabalhando em uma startup, onde você pode ter que lançar várias features em um dia; gitflow não é bom para você.

Conclusão
Nesse artigo, conhecemos o conceito do Git Flow e vimos como ele pode nos ajudar - e também atrapalhar o versionamento dos nossos códigos. Além disso, aprendemos a utilizá-lo na prática, com a ajuda de uma CLI e também sem a ajuda dela, apenas com os comandos básicos do Git.

Vimos também o funcionamento esperado para o fluxo de trabalho de uma equipe que utiliza o Git Flow, e entendemos quando essa abordagem é recomendada para ser utilizada.

Não deixe de explorar outras opções, pois além do Git Flow, existem diversos outros fluxos de trabalho, e você deve sempre avaliar o contexto de cada projeto para decidir qual fluxo mais se encaixa para cada situação.

Portanto, é importante ressaltar que, antes de implementar um fluxo, faça um estudo aprofundado com análises técnicas mostrando as vantagens e desvantagens de sua utilização.

E aí, o que você achou? Não deixe de conferir nossos cursos de Git e continue mergulhando em tecnologia!
"""

texto2 = """
Anteriormente implementamos duas soluções de busca e em nossa segunda abordagem, tivemos que ordenar nossa lista de alunos utilizando a função sorted() do Python. Mas imagine se não tivéssemos essa opção, como poderíamos ordenar a lista?

Primeiramente vamos implementar a ordenação de maneira mais intuitiva. Para isso vamos percorrer a lista e para cada posição dessa iteração, percorreremos o restante da lista em busca do menor valor. Caso ele exista, vamos realizar a troca de posições. E chamaremos essa solução de SelectionSort:

Tudo vai funcionar perfeitamente com a nossa pequena lista de 7 alunos! Agora, que tal usarmos a lista de aproximadamente 85 mil alunos? É melhor não, a não ser que possamos esperar um bom tempo pelo retorno.

Mas por que tivemos um desempenho tão ruim para executar essa pequena ordenação?
Podemos perceber que para cada aluno da lista, nós a percorremos novamente em busca do menor nome. Ou seja, para ordenar uma lista de n alunos, nós executamos n² operações e no nosso caso (85000²) = 7.225.000.000 operações, sim, mais de 7 trilhões de operações.

Então consideramos esse algoritmo como O(n²) ou um algoritmo quadrático. Neste artigo falamos mais sobre a notação Big O.

Então, vamos implementar uma outra solução de ordenação mais eficiente?
Vamos recorrer mais uma vez às técnicas de divisão e conquista para resolver o problema de encontrar o menor nome da lista.

Na função de ordenar, vamos chamar a função merge_sort(), que recebe como parâmetros:

A lista de alunos;
Uma lista temporária com o tamanho pré-definido da lista de alunos;
O índice inicial; e
O índice final da lista.
E serão executados os seguintes passos:

Dividiremos a lista em duas e chamaremos, de forma recursiva a função merge_sort(), passando como parâmetros:
Os dados da primeira lista;
Os dados segunda lista,
Por fim, chamaremos a função merge() para mesclar as duas listas ordenadas com o apoio da lista temporária, reescrevendo a lista original.
"""

def analisa_frequencia_de_letras(texto):
    aparicoes = Counter(texto.lower())
    total_de_caracteres = sum(aparicoes.values())

    proporcoes = [(letra, frequencia / total_de_caracteres) for letra, frequencia in aparicoes.items()]
    proporcoes = Counter(dict(proporcoes))
    mais_comuns = proporcoes.most_common(10)
    for caractere, proporcao in mais_comuns:
        print(f'{caractere} => {proporcao * 100 : .2f}%')

analisa_frequencia_de_letras(texto1)
analisa_frequencia_de_letras(texto2)
