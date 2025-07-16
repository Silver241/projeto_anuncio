<template>
    <LogedNavBar />
    <LogedAppChoise />
    <AppFooter />
</template>

<script>
import LogedNavBar from '../components/LogedNavBar.vue';
import AppFooter from '@/components/AppFooter.vue';
import LogedAppChoise from '@/components/LogedAppChoise.vue';
export default {
    
    name: 'LogedUser',
    components: {
        LogedNavBar,
        LogedAppChoise,
        AppFooter
    },
}
</script>

<style scoped>
</style>