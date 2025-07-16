<template>
    <NavBar/>
    <AppChoice/>
    <AppFooter/>
</template>

<script>
    import NavBar from '../components/NavBar.vue'
    import AppFooter from '../components/AppFooter.vue'
    import AppChoice from '../components/AppChoise.vue'
    export default {
        name:"ChoiceAd",
        components:{
            NavBar,
            AppFooter,
            AppChoice
        }
    }
</script>

<style></style>