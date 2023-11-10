<script setup>
import { ref } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'

const route = useRoute()
const product = ref('')
const productId = route.params.productId
const storeURL = `https://fakestoreapi.com/products/${productId}`

axios.get(storeURL)
    .then((response) =>{
        //console.log(response)
        product.value = response.data
    }).catch((error)=>{
        console.log(error)
    })
</script>

<template>
    <div>
        <h1>ProductDetail Page</h1>
        <div v-if="product" class="product-card">
            <img :src="product.image">
            <strong>{{ product.title }}</strong>
            <p>Price : ${{ product.price }}</p>
        </div>
        <div v-else>
            <p>loading...</p>
        </div>
    </div>
</template>

<style scoped>

</style>
