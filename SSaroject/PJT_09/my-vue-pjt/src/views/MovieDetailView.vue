<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRoute } from 'vue-router';
import axios from 'axios'
import TrailerModal from '@/components/TrailerModal.vue';

const route = useRoute()
const movie = ref('')
const movieId = route.params.movieId
const MovieURL = `https://api.themoviedb.org/3/movie/${movieId}?language=ko-KR&api_key=${import.meta.env.VITE_TMDB_api_key}`
const showModal = ref(false);
const trailerUrl = ref('');

const YT_API_KEY = 'AIzaSyCBPRPtb4ysgvNmcPkSS7Ckkd2mJmQNHo4'
const TMDB_API_KEY = '8fbda498ce79ea454eec38fe2012ea37'

axios.get(MovieURL)
    .then((response) => {
        movie.value = response.data
    }).catch((error) => {
        console.log(error)
    })
const getPosterImg = (posterURL) => {
    return `https://image.tmdb.org/t/p/original${posterURL}`
  }

const fetchMovieDetails = async () => {
    try {
        const response = await axios.get(`https://api.themoviedb.org/3/movie/${route.params.movieId}?api_key=${TMDB_API_KEY}`);
        movie.value = response.data;
    } catch (error) {
        console.error(error);
    }
};

  const showTrailerModal = async () => {
    try {
        const searchResponse = await axios.get(`https://www.googleapis.com/youtube/v3/search?part=snippet&q=${encodeURIComponent(movie.value.title)} official trailer&type=video&key=${YT_API_KEY}`);
        if (searchResponse.data.items.length > 0) {
            const videoId = searchResponse.data.items[0].id.videoId;
            trailerUrl.value = `https://www.youtube.com/embed/${videoId}`;
            showModal.value = true;
        }
    } catch (error) {
        console.error(error);
    }
};

onMounted(fetchMovieDetails);
</script>

<template>
    <div>
        <h1>Movie Detail Page</h1>
        <img :src="getPosterImg(movie.poster_path)" width="200">
        <h2>{{ movie.title }}</h2>
        <p><strong>개봉일 : </strong>{{ movie.release_date }}</p>
        <p><strong>러닝타임 : </strong>{{ movie.runtime }} 분</p>
        <p><strong>TMDB 평점 : </strong>{{ movie.vote_average}}</p>
        <h2>장르</h2>
        <div v-for="genre in movie.genres">
            <p>{{ genre.name }}</p>
        </div>
        <h2>줄거리</h2>
        <p>{{ movie.overview }}</p>
        <h2>공식 예고편</h2>
        <button @click="showTrailerModal">
        <img src="@/assets/youtube.png" width="30" alt="유튜브 아이콘" />
        </button>
        <TrailerModal v-if="showModal" :trailerUrl="trailerUrl" @close="showModal = false" />
    </div>
</template>

<style scoped>
.movie-details {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
    text-align: center;
}

.movie-details img {
    max-width: 100%;
    height: auto;
    margin-bottom: 20px;
}

.movie-details h1 {
    margin-bottom: 10px;
    color: #333;
    font-size: 2em;
}

.movie-details p {
    margin-bottom: 10px;
    color: #666;
}

.movie-details button {
    background: none;
    border: none;
    cursor: pointer;
    padding: 0;
}

.movie-details button img {
    width: 40px;
    height: auto;
}

.movie-details button:hover {
    opacity: 0.8;
}
</style>
