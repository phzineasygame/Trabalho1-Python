Este programa em Python é um quiz interativo de conhecimentos gerais. O usuário digita seu nome, responde perguntas, podendo tentar novamente ou pular digitando "sair". Ao final, o programa mostra a pontuação e o total de tentativas.

Para usar, basta executar o arquivo quiz.py no terminal com python quiz.py e seguir as instruções.

O código usa um for para percorrer as perguntas e um while para repetir a tentativa da mesma pergunta até o usuário acertar ou sair. O continue impede respostas vazias e faz o programa pedir a resposta novamente. O break sai do loop da pergunta quando o usuário acerta ou escolhe pular.

A entrada do nome e das respostas é validada para não aceitar valores vazios. As decisões são controladas com if e else, verificando respostas corretas, erradas ou o comando para sair.