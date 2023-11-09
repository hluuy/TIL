<template>
    <div>
        <h1>Students List</h1>
        <p v-for="student in studentsList">
            <router-link :to="{ name: 'studentsdetail', params: {name: student.name }}">{{ student.name }} 학생 정보 보기</router-link>
        </p>
    </div>
</template>

<script setup>
const studentsList =[
    { name: "김하나" },
    { name: "김두리" },
    { name: "김서이" },
]
</script>

<style scoped>

</style>