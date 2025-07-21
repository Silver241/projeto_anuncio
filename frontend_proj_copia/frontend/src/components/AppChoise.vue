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
            <CustomDropdown
                :options="minutas.map(m => ({ value: m.tipo, label: m.tipo }))"
                v-model="selectedTipo"
            />
            </li>
                
            </ul>
            <ul class="list_form">
                <li><label for="">Região de Difusão</label>
            <CustomDropdown
                :options="[
                    { value: '', label: 'Escolha uma opção' },
                    { value: 'Barlavento', label: 'Barlavento' },
                    { value: 'Sotavento', label: 'Sotavento' }
                ]"
                v-model="regiao"
            />
            </li>
                <li><label for="">Canal de Transmissão</label>
            <CustomDropdown
                :options="[
                    { value: '', label: 'Escolha uma opção' },
                    { value: 'TCV', label: 'TCV' },
                    { value: 'RCV', label: 'RCV' },
                    { value: 'RCV+', label: 'RCV+' }
                ]"
                v-model="canal"
            />
            </li>
                <li><label for="">Horário Pretendido</label>
            <CustomDropdown
                :options="[
                    { value: '', label: 'Escolha uma opção' },
                    { value: '12:30', label: '12:30' },
                    { value: '18:30', label: '18:30' }
                ]"
                v-model="horario"
            />
            </li>
                <li><label for="">Vezes a ser divulgado</label>
            <CustomDropdown
                :options="[
                    { value: '', label: 'Escolha uma opção' },
                    { value: '1', label: 'apenas 1 vez' },
                    { value: '2', label: '2 vezes' },
                    { value: '3', label: '3 vezes' },
                    { value: '4', label: '4 vezes' },
                    { value: '5', label: '5 vezes' },
                    { value: '', label: 'outro' }
                ]"
                v-model="vezes"
            />
            </li>

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
    import axios from 'axios';
    import CustomDropdown from './CustomDropdown.vue';
    export default {
        name: "AppChoice",
        components: { CustomDropdown },
        data() {
            return {
                minutas: [],
                selectedTipo: '',
                showPopupMinuta: false,
                conteudoMinuta: '',
                nomeCompleto: '',
                email: '',
                telefone: '',
                regiao: '',
                canal: '',
                horario: '',
                vezes: ''
            };
        },
        methods: {
            criarAnuncio() {
                const minutaSelecionada = this.minutas.find(m => m.tipo === this.selectedTipo);
                const minuta_id = minutaSelecionada ? minutaSelecionada.id : null;
                let vezesInt = parseInt(this.vezes);
                if (isNaN(vezesInt)) vezesInt = 1;
                axios.post('http://127.0.0.1:8000/anuncios/create/', {
                    minuta_id: minuta_id,
                    user_id: null,
                    regiao: this.regiao,
                    canal: this.canal,
                    horario: this.horario,
                    vezes: vezesInt,
                    conteudo: this.conteudoMinuta,
                    estado: 'Pendente'
                }).then(() => {
                    alert('Anúncio criado com sucesso!');
                    this.showPopupMinuta = false;
                }).catch(error => {
                    let msg = 'Erro ao criar anúncio: ';
                    if (error.response && error.response.data) {
                        msg += JSON.stringify(error.response.data);
                    } else {
                        msg += error.message;
                    }
                    alert(msg);
                });
            }
        },
        mounted() {
            axios.get('http://127.0.0.1:8000/minutas/')
                .then(response => {
                    this.minutas = response.data;
                });
        },
        watch: {
            showPopupMinuta(val) {
                if (val) {
                    const minutaSelecionada = this.minutas.find(m => m.tipo === this.selectedTipo);
                    this.conteudoMinuta = minutaSelecionada ? minutaSelecionada.conteudo : '';
                }
            },
            selectedTipo() {
                if (this.showPopupMinuta) {
                    const minutaSelecionada = this.minutas.find(m => m.tipo === this.selectedTipo);
                    this.conteudoMinuta = minutaSelecionada ? minutaSelecionada.conteudo : '';
                }
            }
        }
    }
</script>

<style>
    .backg{
        /* background-color: aquamarine; */
        margin-left: 4rem;
        margin-right: 4rem;
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .choice_form{
       margin-top: 2.5rem;
       /*  background-color: blue; */
        width: 49rem;
        height: 25rem;
       /*  background-color: #a52a2a; */
        display: flex;
        justify-content: space-between;
        position: relative;
    }
    .list_form{
        display: flex;
        flex-direction: column;
      /*   background-color: aqua; */
        
        padding: 0;
        margin: 0;
    }
    .list_form li{
        margin-bottom: 1.1rem;
        /* background-color: brown; */
    }
    .list_form label {
        display: block;
        margin-bottom: 0.2rem;
        margin-left: 0;
    }
    .width_ajust{
        width: 23rem;
        box-sizing: border-box;
    }
    .btn_submeter{
        position: absolute;
        padding: 0.7rem 1rem;
        font-weight: 550;
        color: white;
        border: none;
        border-radius: 1rem;
        transition: opacity 0.3s ease;
    }
    .btn_submeter:hover{
        opacity: 90%;
    }
    .btn_ajust_position1{
        background-color: #456379;
        bottom: 0rem;
        right: 0rem;
    }
    .btn_ajust_position2{
        background-color: #ff6868;
        bottom: 0rem;
        right: 10rem;
    }
    .title_form{
        margin-bottom: 0rem;
        margin-top: 0rem;
    }




.styled-select {
    appearance: none;
    -webkit-appearance: none;
    -moz-appearance: none;
    background-image: url('data:image/svg+xml;utf8,<svg fill="%23333" height="20" viewBox="0 0 24 24" width="20" xmlns="http://www.w3.org/2000/svg"><path d="M7 10l5 5 5-5z"/></svg>');
    background-repeat: no-repeat;
    background-position: right 0.75rem center;
    background-size: 1rem;
}

.styled-select:invalid {
  color: #888;
}

.option_color{
    color: rgb(238, 238, 238);
}

.popup_minuta {
    position: absolute;
    bottom: 0;
    left: -2rem;
    width: 53rem;
    height: 27rem;
    background-color: white;
    border-radius: 1rem;
    border: 1px solid #cfcfcf;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
    display: flex;
    align-items: center;
    justify-content: center;
}
.textarea_minuta {
    position: absolute;
    top: 2.5rem;
    width: 50rem;
    height: 18.5rem;
    padding: 0.45rem;
    border-radius: 0.5rem;
    /* border: 1px solid #dddddd; */
    border: none;
    outline: none;
    font-size: 0.9rem;
    resize: none; /* Prevent resizing */
}
.btn_cancel {
    position: absolute;
    top: 1.2rem;
    right: 1.2rem;
    width: 0.7rem;
    height: 0.7rem;
    background-color: transparent;
    border: none;
    cursor: pointer;
    background-image: url('../assets/close.png');
    background-size: contain;
    background-repeat: no-repeat;
    opacity: 70%;
}

.btn_ajust_position3{
    background-color: #456379;
    bottom: 1.5rem;
    right: 1rem;
}
</style>