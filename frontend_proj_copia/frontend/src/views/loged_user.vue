<template>
    <LogedNavBar />
    <AppChoise />
    <AppFooter />
</template>

<script>
import LogedNavBar from '../components/LogedNavBar.vue';
import AppFooter from '@/components/AppFooter.vue';
import AppChoise from '@/components/AppChoise.vue';
export default {
    
    name: 'LogedUser',
    components: {
        LogedNavBar,
        AppChoise,
        AppFooter
    },
}
</script>

<style scoped>
</style>