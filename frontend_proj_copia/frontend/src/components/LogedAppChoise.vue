<template>
    <div class="backg">
        <h1 class="title_form">Formulário de Anúncio</h1>
        <form class="choice_form" action="#">
            <ul class="list_form">
                <li><label for="">Nome Completo</label>
            <input type="text" class="input_text width_ajust" v-model="nomeCompleto" required></li>
                <li><label for="">Email</label>
            <input type="text" class="input_text width_ajust" v-model="email"></li>
                <li><label for="">Telefone</label>
            <input type="text" class="input_text width_ajust" v-model="telefone" required></li>
                <li><label for="">Tipo de Anuncio</label>
            <select class="input_text width_ajust styled-select" v-model="selectedTipo" required>
                <option disabled selected value="" hidden>Escolha uma opção</option>
                <option v-for="minuta in minutas" :key="minuta.id" :value="minuta.tipo">
                  {{ minuta.tipo }}
                </option>
            </select></li>
                
            </ul>
            <ul class="list_form">
                <li><label for="">Região de Difusão</label>
            <select class="input_text width_ajust styled-select" v-model="regiao" required>
                <option value="" disabled selected hidden>Escolha uma opção</option>
                <option value="Barlavento">Barlavento</option>
                <option value="Sotavento">Sotavento</option>
            </select></li>
                <li><label for="">Canal de Transmissão</label>
            <select class="input_text width_ajust styled-select" v-model="canal" required>
                <option value="" disabled selected hidden>Escolha uma opção</option>
                <option value="TCV">TCV</option>
                <option value="RCV">RCV</option>
                <option value="RCV+">RCV+</option>
            </select></li>
                <li><label for="">Horário Pretendido</label>
            <select class="input_text width_ajust styled-select" v-model="horario" required>
                <option value="" disabled selected hidden>Escolha uma opção</option>
                <option value="12:30">12:30</option>
                <option value="18:30">18:30</option>
            </select></li>
                <li><label for="">Vezes a ser divulgado</label>
            <select class="input_text width_ajust styled-select" v-model="vezes" required>
                <option value="" disabled selected hidden>Escolha uma opção</option>
                <option value="1">apenas 1 vez</option>
                <option value="2">2 vezes</option>
                <option value="3">3 vezes</option>
                <option value="4">4 vezes</option>
                <option value="5">5 vezes</option>
                <option value="">outro</option>

            </select></li>
            </ul>
            <button class="btn_submeter btn_ajust_position1" type="button" @click="showPopupMinuta = true">Minuta sugerida</button>
            <button class="btn_submeter btn_ajust_position2">Escrever Anúncio</button>
            <div class="popup_minuta" v-if="showPopupMinuta">
                <textarea name="#" id="" class="textarea_minuta" v-model="conteudoMinuta"></textarea>
                <div class="btn_cancel" @click="showPopupMinuta = false"></div>
                <button class="btn_submeter btn_ajust_position3" type="button" @click="criarAnuncio">Submeter</button>
            </div>
        </form>
    </div>
</template>

<script>
export default {
    name: 'LogedAppChoise'
}
</script>
<!-- oi -->

<style >

</style>