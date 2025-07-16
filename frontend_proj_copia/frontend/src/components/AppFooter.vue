<template>
    <div class="div_pai">
        <ul>
            <li>Contacts</li>
            <li>Contacts</li>
            <li>Contacts</li>
            <li>Contacts</li>
            <li>Contacts</li>
        </ul>
    </div>
</template>

<script>
export default {
    name:'AppFooter'
}
</script>

<style scoped>
    .div_pai{
        height: 26rem;
        width: 100%;
        border-top: 0.08rem solid #EEEEEE;
        margin-top: 6rem;
        /* background-color: blue; */
    }
    .div_pai ul{
       /*  background-color: aqua; */
        display: flex;
        list-style: none;
        justify-content: space-between;
        margin-top: 3rem;
        margin-left: 9rem;
        margin-right: 9rem;
    }
    li{
        display: inline-block;
        /* background-color: blueviolet; */
        height: 20rem;
    }
</style>