# Repositório educacional 

Esse repositório foi criado a parti do livro "Lógica de programação: a construção de algoritmos e estrutura de dados" de André Luiz Villar Forbellone, Henri Frederico Eberspachr.

Aqui terá resumos sobre o livro, resolução de exercícios propostos. Isso é um repositório mais educativo e de consulta para mim mesmo. 

### Capítulo 01

Falou muito sobre silogismos. Legal para entender bem básicamente o que é lógica e um pensamento encadeado coerente. 

### Capítulo 02 

Os dados manipulados pelos algoritmos podem ser dos seguintes tipos: inteiro, real caracter ou lógico. Verificamos que para guardar os dados precisamos de identificadores, que servem de rótulo para dados variáveis ou constantes, e que para usá-los é necessária a declaração, na qal associamos o identificador a um tipo primitivo válido. 

As expressões aritméticas, lógicas e relacionais, sendo que as duas últimas devem resultados em valor lógico (true or false). Assim como os operadores relacionais, aritméticos (mod, div, pot rad) e lógicos (e, ou, não). Concluímos o capítulo conhecimentos os comandos de entrada e saída de dados, bem como os conceitos de blocos.


### Capítulo 03

Temos já resumos sobre algoritmos de seleção. Basicamente a manipulação de condicionais a blocos de código. 

Um dos exercícios propostos é a transformações de certas estruturas redundantes de if e else em estrutura de seleção composta ou seleção encadeada, que nesse último caso, existe categorias como homogêneas e heterogênas. 


Estruturas de repetição podem ser feito com enquanto determinada condição for verdadeira, ou com número específicos de repetições. Esses são critérios de parada de loop.
Em uma operação com números indetermináveis de iterações, um bom critério de parada é o "se enquanto". É comum que a estrutura de repetição utilize uma variável acumulativa, que guarda resultados a cada iteração para resultado final.

Neste capítulo vimos que o fluxo de execução de algoritmo segue uma estrutura sequencial, significa ser executado passo a passo, sequencialmente. Vimos a estrutura de seleção, que permite que uma ação seja ou não executada, dependendo do valor resultante da inspeção de uma condição. A seleção pode ser simples, quando contém apenas a cláusula então, ou composta, quando contém então e senão. 
QUando é encadeada, pode ser homogêna ou heterogêna. 
Verificamos que seleções encadeadas homogênas são muito comuns, por isso especificamos a seleção de múltipla escolha, que apresenta casos que são avaliados. 
POr último, a estrutura de repetição, que permite que trechos de algoritmos sejam repetidos conforme certos critérios de parada. Verificando que podemos construir laços de repetição de três maneira.

* Repetição com teste no início - enquanto
* Repetição com teste final - repita
* Repetição com variável de controle - para

Observamos que enquanto o laço pode não ser executado, pois a condição está no ínicio, que no repita o laço é executado pelo menos uma vez, pois a condição está no final, e que o para é necessário um número finito e determinado de iterações, pois é preciso conhecer o valor final da variável de controle do laço. 

## Estruturas de dados 

Estruturas de dados existem, porque apenas os tipos primitivos não são capazes de expressar algumas formas complexas de manipulação de informação. Portanto, é preciso construir novos tipos. Os tipos construídos são uma composição de tipos primitivos, uma estrutura de dados.

### Variáveis compostas homogênas.

As compostas homogênas são do mesmo tipo primitivo dentro de uma estrutura. 
Essas podem ser estrutura unidimensional, vetores. Esses são postos entre colchetes [] 

identificador = vetor *[* LI - limite inicial do vetor, LF - limite final do vetor *]* de tipo primitivo.

Para acesso de item, usa-se o nome do identificador, seu simbolo de representação [], e o índice (uma constante) que indica onde o item se encontra. 

O Acessos a lista são O(1), pois a indicação do índice permite que o programa procura apenas naquela posição em específica