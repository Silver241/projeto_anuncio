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
    },
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
import CustomDropdown from './CustomDropdown.vue';
export default {
    name: 'LogedAppChoise',
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
    mounted() {
        this.preencherCamposUsuario();
        // Carregar minutas do backend
        this.carregarMinutas();
    },
    watch: {
        '$route.query.user': function() {
            this.preencherCamposUsuario();
        },
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
    },
    methods: {
        preencherCamposUsuario() {
            let user = null;
            if (this.$route.query.user) {
                try {
                    user = JSON.parse(this.$route.query.user);
                } catch (e) {
                    user = null;
                }
            }
            if (user) {
                this.nomeCompleto = user.nome || '';
                this.email = user.email || '';
                this.telefone = user.telefone || '';
                this.userId = user.id || null;
            } else {
                this.userId = null;
            }
        },
        criarAnuncio() {
            const minutaSelecionada = this.minutas.find(m => m.tipo === this.selectedTipo);
            const minuta_id = minutaSelecionada ? minutaSelecionada.id : null;
            let vezesInt = parseInt(this.vezes);
            if (isNaN(vezesInt)) vezesInt = 1;
            fetch('http://127.0.0.1:8000/anuncios/create/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    minuta_id: minuta_id,
                    user_id: this.userId,
                    regiao: this.regiao,
                    canal: this.canal,
                    horario: this.horario,
                    vezes: vezesInt,
                    conteudo: this.conteudoMinuta,
                    estado: 'Pendente'
                })
            })
            .then(async res => {
                if (res.ok) {
                    alert('Anúncio criado com sucesso!');
                    this.showPopupMinuta = false;
                } else {
                    const error = await res.json();
                    alert('Erro ao criar anúncio: ' + JSON.stringify(error));
                }
            })
            .catch(err => {
                alert('Erro ao criar anúncio: ' + err.message);
            });
        },
        carregarMinutas() {
            // Busca as minutas do backend
            fetch('http://127.0.0.1:8000/minutas/')
                .then(res => res.json())
                .then(data => {
                    this.minutas = data;
                })
                .catch(() => {
                    this.minutas = [];
                });
        },
        
    }
}
</script>
<!-- oi -->

<style >

</style>