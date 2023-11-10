<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router';
import axios from 'axios'


const movies = ref([])
const router = useRouter()
const TMDBURL = `https://api.themoviedb.org/3/movie/top_rated?language=ko-KR&page=1&api_key=${import.meta.env.VITE_TMDB_api_key}`
axios.get(TMDBURL)
    .then((response) =>{
        movies.value = response.data
    }).catch((error)=>{
        console.log(error)
    })
const MovieEmpty = computed(() => {
    return movies.results.length > 0
})
const goDetail = (movie) =>{
    router.push(`/${movie.id}`)
}
const getPosterImg = (posterURL) => {
    return `https://image.tmdb.org/t/p/original${posterURL}`
  }
</script>

<template>
    <div>
        <h1>MovieList</h1>
        <!-- {{ movies.value }} -->
        <div class="movie-list">
            <div v-for="movie in movies.results" :key='movie.id' class="movie-card">
                    <img :src="getPosterImg(movie.poster_path)" width="200">
                    <strong>{{ movie.title }}</strong>
                    <p>{{ movie.overview }}</p>
                    <button @click="goDetail(movie)">Detail</button>
            </div>
        </div>
    </div>
</template>

<style>
.movie-list{
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
}
.movie-card{
    border: 1px solid black;
    width: 200px;
}
</style>
