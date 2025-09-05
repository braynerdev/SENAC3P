let indiceAtual = 0;
let score = 0;

const perguntaEl = document.getElementById("pergunta");
const opcoesEl = document.getElementById("opcoes");
const contadorEl = document.getElementById("contador");

function carregarPergunta() {
  if (indiceAtual >= perguntas.length) {
    perguntaEl.textContent = `Quiz finalizado! Você acertou ${score} de ${perguntas.length}.`;
    opcoesEl.innerHTML = "";
    contadorEl.textContent = "";
    return;
  }

  const pergunta = perguntas[indiceAtual];
  perguntaEl.textContent = pergunta.enunciado;

  opcoesEl.innerHTML = "";
  pergunta.opcoes.forEach(opcao => {
    const btn = document.createElement("button");
    btn.textContent = opcao;
    btn.onclick = () => verificarResposta(btn, pergunta.resposta);
    opcoesEl.appendChild(btn);
  });

  contadorEl.textContent = `Pergunta ${indiceAtual + 1} de ${perguntas.length}`;
}

function verificarResposta(botao, respostaCerta) {
  const botoes = document.querySelectorAll("#opcoes button");

  botoes.forEach(btn => btn.disabled = true);

  if (botao.textContent === respostaCerta) {
    botao.classList.add("correto");
    score++;
  } else {
    botao.classList.add("errado");
    botoes.forEach(btn => {
      if (btn.textContent === respostaCerta) {
        btn.classList.add("correto");
      }
    });
  }

  setTimeout(() => {
    indiceAtual++;
    carregarPergunta();
  }, 1500);
}

carregarPergunta();
