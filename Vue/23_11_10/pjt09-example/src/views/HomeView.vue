<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router';
import axios from 'axios'

const products = ref([])
const router = useRouter()
const storeURL = 'https://fakestoreapi.com/products'

axios.get(storeURL)
    .then((response) =>{
        //console.log(response)
        products.value = response.data
    }).catch((error)=>{
        console.log(error)
    })

    const productEmpty = computed(() => {
        return products.value.length > 0
    })

const goDetail = (product) =>{
    router.push(`/${product.id}`)
}

const addCart = (product) =>{
    // localStorage.setItem('cart', JSON.stringify(product))
    const existingCart = JSON.parse(localStorage.getItem('cart')) || []

    const isDuplicate = existingCart.length > 0 && existingCart.find((item) => item.id === product.id)
    if(!isDuplicate){
        alert('add to cart!')
        existingCart.push(product)
     } else {
        alert("It's already exist at cart!")
     }
    localStorage.setItem('cart', JSON.stringify(existingCart))

    router.push('/cart')
}
</script>

<template>
    <div>
        <h1>Main Page</h1>
        <div v-if="productEmpty" class="product-list">
            <div v-for="product in products" :key="product.id" class="product-card">
                <img :src="product.image">
                <strong>{{ product.title }}</strong>
                <p>Price : {{ product.price }}</p>
                <button @click="goDetail(product)">Detail</button>
                <button @click="addCart(product)">add to cart</button>
            </div>
        </div>
        <div v-else>
            <p>loading or nothing</p>
        </div>        
    </div>
</template>

<style scoped>


</style>
<style>
.product-list{
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
}
.product-card{
    border: 1px solid black;
    width: 200px;
}
.product-card img {
    width: 200px;
    height: 200px;
    object-fit: fill;
}
</style>
