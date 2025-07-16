<template>
  <NavBar teste="123" @comprei-banana="receberBanana"/>
  <MainContent/>
  <TutorialContent/>
  <AppFooter/>
</template>

<script>
import MainContent from '../components/MainContent.vue'
import TutorialContent from '../components/TutorialContent.vue'
import NavBar from '../components/NavBar.vue'
import AppFooter from '../components/AppFooter.vue'

export default {
  name: 'AppHome',
  components: {
    NavBar,
    MainContent,
    TutorialContent,
    AppFooter
  },

  methods: {
    receberBanana(fruta) {
      console.log('Recebi a fruta:', fruta);
    }
  }
}
</script>

<style>

</style>
