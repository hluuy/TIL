<template>
    <div>
        <input type="text" v-model="color">
        <p :class="color">입력창에 올바른 색상 명을 입력하면 글자색이 바껴요.</p>
    </div>
</template>

<script setup>
import {ref} from 'vue'

const color = ref('')
</script>

<style  scoped>
.red {
      color: red;
    }
    .blue {
      color: blue;
    }
    .orange {
      color: orange;
    }
    .green {
      color: green;
    }
    .tomato{
        color: tomato;
    }
    .pdblue{
        color: powderblue
    }

</style>