$("#data_inicial").on("change", function () {
    const dt_inicial = $(this).val();
    const dt_final = $("#data_final").val();

    if (dt_inicial && dt_final) {
        requisicao(dt_inicial,dt_final);
    }
});
$("#data_final").on("change", function () {
    const dt_inicial = $(this).val();
    const dt_final = $("#data_inicial").val();

    if (dt_inicial && dt_final) {
        requisicao(dt_inicial,dt_final);
    }
});

function requisicao(dt_inicial, dt_final){
    const datas = limparData(dt_inicial,dt_final);
    const url = `https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL,CHF-BRL,ARS-BRL,BNB-BRL,AUD-BRL,BOB-BRL,COP-BRL,DOGE-BRL,ETH-BRL,GBP-BRL/?start_date=${datas['dt_inicial']}&end_date=${datas['dt_final']}`
    fetch(url)
    .then(response => response.json())
    .then(data =>{
        console.log(data);
        const div = document.getElementById("container");
        div.innerHTML = '';
        for (let chave in data){
            var moeda = data[chave]; 
            div.innerHTML += `
                <div class="card" style="width: 18rem;">
                    <div class="card-body">
                        <h5 class="card-title">${moeda.name}</h5>
                        <div class="card-subtitle text-body-secondary">Maior Valor: ${moeda.high}</div>
                        <div class="card-subtitle text-body-secondary">Menor Valor: ${moeda.low}</div>
                        <div class="card-subtitle text-body-secondary"><span class="aovivo"></span> Oferta de Compra: ${moeda.bid}</div>
                        <div class="card-subtitle text-body-secondary"><span class="aovivo"></span> Oferta de venda: ${moeda.ask}</div>
                    </div>
                </div>    
            `;
        };
        div.style.display = "flex";
        div.scrollIntoView({
            "behavior": "smooth",
            "block": "start"
        });
    });
}

function limparData(dt_inicial,dt_final){
    dataInicialReplace = dt_inicial.replaceAll("-","");
    dataFinalReplace = dt_final.replaceAll("-","");
    return {"dt_inicial": dataInicialReplace, "dt_final": dataFinalReplace};
}


