<template>
  <div>
    <h1 class="form-title">로그인</h1>
    <div class="input-wrap">
        <label for="email">이메일</label>
        <input type="email" id="email" v-model="email" class="input-text"/>
    </div>
    <div class="input-wrap">
        <label for="password">패스워드</label>
        <input type="password" id="password" v-model="password" class="input-text"/>
    </div>
    <div style="max-width: 350px; margin: 0 auto;">
        <button @click="loginSubmit()" class="form-btn my-shadow">로그인</button>
    </div>
  </div>
</template>

<script setup>
// import axios from 'axios'
// export default {
//   data () {
//     return {
//       email: null,
//       password: null
//       }
//   },
//   mounted() {
//   },
//   methods: {
//     loginSubmit () {
//       const saveData = {}
//       saveData.email = this.email
//       saveData.password = this.password
//       axios
//         .post('Login API URL', saveData) // 로그인 API URL로 ID, PW를 보냄
//         .then((res) => {
//           console.log(res.data)
//           const token = res.data.access_token
//           localStorage.setItem('access_token', token) // 토큰을 저장함
//           const refretoken = res.data.refresh_token
//           localStorage.setItem('refresh_token', refretoken) // 토큰을 저장함
//         })
//     },
// }
// }
import { ref } from 'vue'
import axios from 'axios'

// 반응형 데이터 정의
const email = ref(null)
const password = ref(null)

// 로그인 함수 정의
const loginSubmit = async () => {
  try {
    const saveData = { email: email.value, password: password.value }
    const response = await axios.post('Login API URL', saveData)
    console.log(response.data)

    const token = response.data.access_token
    localStorage.setItem('access_token', token)
    const refretoken = response.data.refresh_token
    localStorage.setItem('refresh_token', refretoken)
  } catch (error) {
    console.error("Login error", error)
  }
}
</script>

<style>

</style>
