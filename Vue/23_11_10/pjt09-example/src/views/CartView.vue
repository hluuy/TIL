<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router';


const router = useRouter()

const cartItems = ref(null)

cartItems.value = JSON.parse(localStorage.getItem('cart'))

const goDetail = (product) =>{
    router.push(`/${product.id}`)
}

const removeCart = (product)=>{
    const existingCart = JSON.parse(localStorage.getItem('cart'))

    const itemIdx = existingCart.findIndex((item) => item.id == product.id)
    existingCart.splice(itemIdx, 1)
    localStorage.setItem('cart', JSON.stringify(existingCart))
    cartItems.value = existingCart
}
</script>

<template>
    <div>
        <h1>Cart</h1>
        <div v-if="cartItems" class="product-list">
            <div v-for="product in cartItems" :key="product.id" class="product-card">
                <img :src="product.image">
                <strong>{{ product.title }}</strong>
                <p>Price : {{ product.price }}</p>
                <button @click="goDetail(product)">Detail</button>
                <button @click="removeCart(product)">remove at cart</button>
            </div>
        </div>
        <div v-else>
            <p>Nothing!</p>
        </div>
    </div>
</template>

<style scoped>

</style>
