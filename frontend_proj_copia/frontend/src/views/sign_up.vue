<template>
    <div class="div_background">
        <div class="div_form">
            <a class="logo" href="/"></a>
            <h1 class="title">Cadastrar</h1>
            <div class="back_login">Já possui uma conta? <a href="/login">Logar</a></div>
            <form class="form_estructure" @submit.prevent="handleSignup">
                <input class="input_text input_width_half" placeholder="Nome*" type="text" v-model="firstName" required>
                <input class="input_text input_width_half" placeholder="Sobrenome*" type="text" v-model="lastName" required>
                <input class="input_text input_width_entire" placeholder="Telefone*" type="text" v-model="telefone" required>
                <input class="input_text input_width_entire" placeholder="email*" type="text" v-model="email" required>
                <input class="input_text input_width_entire" placeholder="password*" type="password" v-model="password" required>
                <button class="btn_submit" type="submit">Cadastrar</button>
                <div class="or-separator">
                <hr>
                <span>Ou</span>
                <hr>
                </div>
                <a class="btn_submit log_with_ghrome" href="#"><div class="icone_ghrome"></div><span>Continuar com Google</span></a>
                <!-- <a class="link" href="#">Já tens um conta</a> -->
            </form>
        </div>
    </div>
</template>


<script>
import axios from 'axios';
export default {
    name: 'AppSignup',
    data() {
        return {
            firstName: '',
            lastName: '',
            telefone: '',
            email: '',
            password: '',
        };
    },
    methods: {
        async handleSignup() {
            try {
                // Juntar nome e sobrenome
                const nome = `${this.firstName} ${this.lastName}`;
                // Ajuste o endpoint abaixo conforme sua API
                await axios.post('http://127.0.0.1:8000/users/create/', {
                    nome,
                    telefone: this.telefone,
                    email: this.email,
                    password: this.password,
                    perfil_id: 1
                });
                alert('Cadastro realizado com sucesso!');
                // Redirecionar ou limpar formulário
                this.firstName = '';
                this.lastName = '';
                this.telefone = '';
                this.email = '';
                this.password = '';
                this.$router.push('/login');
            } catch (error) {
                let msg = 'Erro ao cadastrar: ';
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

<style >
.div_background {
    width: 100vw;
    height: 100vh;
    background-image: url('../assets/background(3).png');
    background-size: 15rem;
    background-repeat: repeat;
    display: flex;
    justify-content: center;
    align-items: center;
    animation: moveBackground 170s linear infinite;
}

/* animação do movimento oblíquo para baixo */
@keyframes moveBackground {
    0% {
        background-position: 0 0;
    }
    100% {
        background-position: 300px 600px; /* para a direita e para baixo */
    }
}

    
    .div_form{
        padding-bottom: 2.5rem;
        margin-top: 3.5rem;
        margin-bottom: 3.5rem;
        width: 27rem;
        background-color: rgb(255, 255, 255);
        border-radius: 2rem;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
        display: flex;
        align-items: center;
        flex-direction: column;
        position: relative;
    }
    .form_estructure{
        margin-left: 2.4rem;
        margin-right: 2.4rem;
       /*  background-color: #a52a2a; */
        display: flex;
        flex-wrap: wrap;
        justify-content: space-between;
    }
    .input_text{
        display: inline-block;
        padding: 0.8rem 1.09rem;
        border-radius: 0.8rem;
        margin-top: 0.48rem;
        border: 1px solid #dddddd;
        outline: none;
        transition: border-color 0.5s ease;
        height: 2.7rem;
        box-sizing: border-box;
        font-size: 0.8rem;
    }
    .input_text:focus{
        border-color:  #30526a;
    }
    .input_text::placeholder{
        font-size: 0.8rem;
    }
    .input_width_half{
        width: 8.6rem;         
    }
    .input_width_entire{
        flex: 100%;             
    }
    .btn_submit{
        padding: 1rem 1rem;
        border: none;
        border-radius: 2rem;
        flex: 100%;
        background-color: #30526a;
        text-decoration: none;
        color: white;
        margin-top: 0.48rem;
        /* margin-bottom: 2.5rem; */
        font-weight: 600;
        font-size: 0.9rem;
        text-align: center;
        transition: background-color 0.3s ease;
    }
    .btn_submit:hover{
        background-color: #456379;
    }
    .log_with_ghrome{
        /* margin-bottom: 2.5rem; */
        padding: 0.95rem 0.8rem;
        margin-top: 0rem;
        background-color: white;
        color: rgb(34, 40, 49);
        /* border: 1px solid rgb(57, 62, 70); */
        box-shadow: 0 0 0 0.8px rgb(57, 62, 70);
        display: flex;
        justify-content: center;
        align-items: center;
        transition: box-shadow 0.3s ease;
    }
    .log_with_ghrome:hover{
        /* border: 2px solid rgb(57, 62, 70); */
        box-shadow: 0 0 0 1.2px rgb(57, 62, 70);
        background-color: white;
    }
    .icone_ghrome
    {
        background-image: url('../assets/google.png');
        background-size: contain;
        background-repeat: no-repeat;
        height: 0.9rem;
        width: 1.4rem;
        display: inline-block;
        
    }
    .logo{
    /* background-color:aqua; */
    background-image: url('../assets/speaker.png');
    background-size: contain;
    background-repeat: no-repeat;
    height: 2rem;
    width: 2rem;
    margin-top: 2rem;
    }
    .title{
        font-size: 1.5rem;
        margin-top: 0.7rem;
        margin-bottom: 0.3rem;
    }
    .back_login{
        font-size: 0.7rem;
        margin-bottom: 0.7rem;
    }
    .or-separator {
    display: flex;
    align-items: center;
    width: 100%;
    margin: 1rem 0 1rem 0;
    gap: 0.7rem;
    }

.or-separator hr {
  flex: 1;
  border: none;
  height: 0.5px;
  background: #bbb;
  margin: 0;
}

.or-separator span {
  padding: 0 0.5rem;
  font-size: 1rem;
  font-weight: 600;
  color: #888;
  background: #fff;
}

</style>