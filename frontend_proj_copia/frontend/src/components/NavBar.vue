<template>
    <div class="div_navbar">
        <ul class="ul_navbar">
            <li class="li_navbar"><a class="logo_nav margin0" href="/"></a ></li>
            <li class="li_navbar"><a class="btn_registro" href="/login">Login</a></li>
            <li class="li_navbar"><a class="btn_registro" href="/sign_up">Cadastrar</a></li>
            <li class="li_navbar"><a class="btn_criar_anuncio" href="/choice_ad">Criar Anuncio</a></li>
        </ul>
    </div>
</template>

<script>
export default {
    name: 'NavBar',
    props: {
        teste: String
    },
    emits: ['comprei-banana'],
    data() {
        return {
            // Define any reactive data properties here if needed
            fruta:'banana'
        };
    },
    created() {
        // This lifecycle hook is called when the component is created
        this.$emit('comprei-banana', this.fruta);    
    },
}

</script>

<style>
.div_navbar{
    position: sticky;
    top: 0;
    width: 100%;
    /* border-bottom: 1px solid rgb(238, 238, 238); */
    background: rgba(255, 255, 255, 0.3);
    backdrop-filter: blur(10px);
    z-index: 1;
}
.ul_navbar{
    height: 4rem;
    margin: 0;
    list-style: none;
    /* background-color: blueviolet; */
    display: flex;
    justify-content: end;
    align-items: center;
}
.li_navbar{
    height: 1.1rem;
    display: flex;
    align-items: center;
   /*  background-color: aqua; */
    margin-right: 0.7rem; 
}

.btn_registro{
    padding: 0.5rem;
    border-radius: 0.5rem;
    transition: background-color 0.3s ease;
}

.btn_registro:hover{
    background-color: rgb(238, 238, 238);
}

.li_navbar a{
    text-decoration: none;
    text-align: center;
    color: rgb(34, 40, 49);
    font-weight: 500;
}
.li_navbar .btn_criar_anuncio{
    color: white;
}
.btn_criar_anuncio{
    background-color: rgb(34, 40, 49);
    
    padding: 0.5rem 1rem;
    border-radius: 0.5rem;
    transition: background-color 0.2s ease;
}

.btn_criar_anuncio:hover{
    background-color: rgb(34, 40, 49, 0.8);
}
.logo_nav{
    /* background-color:aqua; */
    background-image: url('../assets/speaker.png');
    background-size: contain;
    background-repeat: no-repeat;
    height: 2rem;
    width: 2rem;
    position: absolute;
    left: 1.7rem;
}
.margin0{
    margin-top: 0px;
}
</style>