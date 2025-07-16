<template>
    <div class="div_navbar">
        <ul class="ul_navbar">
            <li class="li_navbar"><a class="logo_nav margin0" href="/"></a ></li>
                <li class="li_navbar"><a class="btn_registro" href="/sign_up">Meus Anuncios</a>
                <div class="nav_bell"></div></li>
                <li class="li_navbar"><a class="user_icon" href="/choice_ad"></a></li>
    
        </ul>
    </div>
</template>

<script>
 export default {
    name: 'LogedNavBar'
 }
</script>

<style scoped>
.user_icon{
    background-image: url('../assets/user.png');
    background-size: contain;
    background-repeat: no-repeat;
    width: 1.3rem;
    height: 1.3rem;
    display: inline-block;
    margin-right: 1.3rem;
    margin-left: 0.7rem;
}
.nav_bell{
    background-image: url('../assets/bell.png');
    background-size: contain;
    background-repeat: no-repeat;
    width: 0.7rem;
    height: 0.7rem;
    display: inline-block;
    position: absolute;
    top: 0.8rem;
    right: 4.7rem;
}
</style>