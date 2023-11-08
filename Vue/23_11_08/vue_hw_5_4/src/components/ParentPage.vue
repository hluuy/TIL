<template>
    <div>
        <h1>부모 페이지 입니다.</h1>
        <ChildPage v-for="child in children" :child-info="child" 
        @plus-money="plusmoney"
        />

    </div>
</template>

<script setup>
import ChildPage from "@/components/ChildPage.vue"
import { ref } from 'vue'

const children = ref([
    {
        name : '김하나',
        age: 30,
        balance: ref(100000)
    },
    {
        name : '김두리',
        age: 20,
        balance: ref(10000)
    },
    {
        name : '김서이',
        age : 10,
        balance: ref(1000)
    }
])
const plusmoney = function(child) {
    child.balance += 1000
}

</script>

<style  scoped>

</style>