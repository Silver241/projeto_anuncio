<template>
    <div class="div_pai">
        <div class="div_left">
            <div class="img_select"></div>
            <div class="option">
            </div>
        </div>
        <div class="div_right">
            <div class="img_form"></div>
            <div class="form">
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'TutorialContent',
    /* props: {
        variavel: String
    },
    data() {
        return {
            valor: 10
        }
    } */
}
</script>

<style scoped>
    .div_pai{
        display: flex;
        justify-content: center;
        margin-top: 0;
        
    }
    .div_pai .div_right{
        height: 26rem;
        width: 29rem;
        margin-left: 1rem;
        margin-right: 1rem;
        border-radius: 1rem;
        border: 0.15rem solid #eaeef0;
        position: relative;
        background-color: #eaeef0;
        overflow: hidden;
        transition: border-color 0.3s ease;
    }
    .div_pai .div_right:hover{
        border: 0.15rem solid;
        border-color: #d6dce1;
    }
    .div_right .form{
        position: absolute;
        bottom: 0;
        right: 0;
        width: 25rem;
        background-color: white;
        height: 22rem;
        border-radius: 1rem 0rem 0rem;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
    }
    .div_right .img_form{
        height: 2rem;
        width: 2rem;
        background-image: url('../assets/form.png');
        background-size: contain;
        background-repeat: no-repeat;
        position: absolute;
        top: 0.9rem;
        left: 1rem;
    }
    .div_pai .div_left{
        position: relative;
        background-color: #ffeeee;
        height: 26rem;
        width: 29rem;
        margin-left: 1rem;
        margin-right: 1rem;
        border-radius: 1rem;
        border: 0.15rem solid #ffeeee;
        overflow: hidden;
        transition: border-color 0.3s ease;
    }
    .div_pai .div_left:hover{
        border: 0.15rem solid;
        border-color: #ffdddd;
    }
    .div_left .img_select{
        height: 2rem;
        width: 2rem;
        background-image: url('../assets/question.png');
        background-size: contain;
        background-repeat: no-repeat;
        position: absolute;
        top: 0.9rem;
        left: 1rem;
    }
    .div_left .option{
        position: absolute;
        bottom: 0;
        right: 0;
        width: 25rem;
        background-color: white;
        height: 22rem;
        border-radius: 1rem 0rem 0rem;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
    }
</style>