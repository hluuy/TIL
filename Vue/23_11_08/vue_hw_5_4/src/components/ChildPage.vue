<template>
    <div>
        <h3>자식 페이지입니다.</h3>
        <p>이름 : {{ props.childInfo.name }}</p>
        <p>나이 : {{ props.childInfo.age }}</p>
        <p>용돈 : {{ props.childInfo.balance }}</p>
        <button @click="buttonClick">용돈 주세요.</button>
    </div>
</template>

<script setup>
const props = defineProps({
  'childInfo': Object,
})

const emit = defineEmits(['plusMoney'])

const buttonClick = function() {
  emit('plusMoney', props.childInfo)
}
</script>

<style scoped>
div {
  border: 1px solid #ccc;
  padding: 10px;
  margin-top: 10px;
}
h3 {
  font-size: 18px;
}
p {
  font-size: 14px;
}

</style>
