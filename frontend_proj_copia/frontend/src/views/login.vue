<template>
    <div class="div_background">
        <div class="div_form">
            <a class="logo" href="/"></a>
            <h1 class="title">Login</h1>
            <div class="back_login">Não possui uma conta? <a href="/sign_up">Cadastrar</a></div>
            <form class="form_estructure" @submit.prevent="handleLogin">
                <input class="input_text input_width_entire" placeholder="email*" type="text" v-model="email" required>
                <input class="input_text input_width_entire" placeholder="senha*" type="password" v-model="password" required>
                <a class="btn_esqueceu_senha" href="/signup">Esqueceu a senha?</a>
                <button class="btn_submit" type="submit">Login</button>
                <div class="or-separator">
                <hr>
                <span>Ou</span>
                <hr>
                </div>
                <button class="btn_submit log_with_ghrome" href="#"><div class="icone_ghrome"></div><span>Entrar com Google</span></button>
                <!-- <a class="link" href="#">Já tens um conta</a> -->
            </form>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
export default {
    name: "AppLogin",
    data() {
        return {
            email: '',
            password: ''
        };
    },
    methods: {
        async handleLogin() {
            try {
                const response = await axios.post('http://127.0.0.1:8000/users/login/', {
                    email: this.email,
                    password: this.password
                });
                // Redireciona para loged_user.vue passando o usuário logado via params
                this.$router.push({
                    path: '/loged_user',
                    query: { user: JSON.stringify(response.data) }
                });
            } catch (error) {
                let msg = 'Erro ao logar: ';
                if (error.response && error.response.data) {
                    msg += JSON.stringify(error.response.data);
                } else {
                    msg += error.message;
                }
                alert(msg);
            }
        }
    }
}
</script>

<style>
    .btn_esqueceu_senha{
        display: inline-block;
        margin-top: 0.8rem;
        margin-bottom: 0.3rem;
        font-size: 0.7rem;
        color: rgb(34, 40, 49);
    }
</style>