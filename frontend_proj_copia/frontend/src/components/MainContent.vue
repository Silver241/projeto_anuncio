<template>
  <div class="home_div">
    <div class="home_title"><h1>Anuncie de Forma <br> Simples, Rápido e Eficiente</h1>
    <h2>Anuncie eventos, comunicados e homenagens de forma fácil,  do conforto da sua casa.</h2></div>
    <div class="imagem"></div>
  </div>
</template>

<script>
export default {
  name: 'MainContent'
  /* props: {
    msg: String
  },
  data() {
    return {
      teste:"Oiii"
    }
  }, */
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.home_div{
  display: flex;
  margin-top: 2rem;
}

.home_title{
  margin-left: 6rem;
}

h1{
  font-size: 3.5rem;
}

h2{
  font-size: 1.2rem;
}

.imagem{
  width: 30rem;
  height: 26rem;
  background-image: url('../assets/home_image.png');
  background-size: contain;
  background-repeat: no-repeat;
  margin-right: 5rem;
 /*  background-color: aqua; */
}
</style>
