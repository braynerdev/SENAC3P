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
    const url = `https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL/?start_date=${datas['dt_inicial']}&end_date=${datas['dt_final']}`
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
                        <h6 class="card-subtitle mb-2 text-body-secondary">high: ${moeda.high}</h6>
                        <h6 class="card-subtitle mb-2 text-body-secondary">low: ${moeda.low}</h6>
                        <h6 class="card-subtitle mb-2 text-body-secondary cardaovivo"><span class="aovivo"></span> bid: ${moeda.bid}</h6>
                        <h6 class="card-subtitle mb-2 text-body-secondary"><span class="aovivo"></span> ask: ${moeda.ask}</h6>
                        <h6 class="card-subtitle mb-2 text-body-secondary">create date: ${moeda.create_date}</h6>
                    </div>
                </div>    
            `;
        };
        div.scrollIntoView({
            "behavior": "smooth",
            "block": "center"
        });
    });
}

function limparData(dt_inicial,dt_final){
    dataInicialReplace = dt_inicial.replaceAll("-","");
    dataFinalReplace = dt_final.replaceAll("-","");
    return {"dt_inicial": dataInicialReplace, "dt_final": dataFinalReplace};
}


