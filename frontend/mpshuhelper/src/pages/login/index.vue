<template lang="pug">
  .page
    .content
      h1(square='', flat='', style='position:absolute;top:-5rem;width:100%;')
        div(style='text-align:center;')
          span(style='font-weight:bold;font-size:1.5rem;color:white;text-shadow:blue 0 1px 0;') SHUhelper 小程序
          br
          small(style='color:white;text-shadow:green 0 1px 0;')
            span(style='color:red;') ♥
            //- | meow~
      form
        input(placeholder="一卡通账号" v-model='form.userID', type='number', required='', float-label='一卡通账号')
        //- q-input(v-model='form.userID', type='number', required='', float-label='一卡通账号')
        //- q-input( v-model='form.password', type='password', required='', float-label='密码')
        input(placeholder="请输入密码" v-model='form.password', type='password', required='', float-label='密码')
        //- checkbox(v-model='rememberMe', label='记住我')
        button.full-width(:plain="true",:size="mini",loader='', color='primary', @click='login',:loading='loginLoading' )
          | 确认绑定
      div(square='', flat='', style='position:absolute;bottom:-4rem;width:100%;')
        div(style='text-align:center;color:white;font-size:0.8rem;')
          small 上海大学开源社区
          br
          small 2018 SHU Open Source Community
</template>

<script>
export default {
  //   components: {
  //     QCheckbox,
  //     QInput
  //   },
  data() {
    return {
      form: {
        userID: '',
        password: ''
      },
      authID: '',
      passwordVisiable: true,
      loginLoading: false,
      rememberMe: false
    }
  },
  // validations: {
  //   form: {
  //     userID: { required },
  //     password: { required }
  //   }
  // },
  mounted() {
    // this.$refs.basicModal.open()
  },
  beforeDestory() {
    // this.$refs.basicModal.close()
    // debugger
  },
  methods: {
    login() {
      // var _this = this
      // this.$v.form.$touch()
      // if (this.$v.form.$error) {
      //   done()
      //   Toast.create('请正确填写账号和密码')
      //   return
      // }
      // this.authID = this.$root.$mp.query.authID
      this.form.userID = this.form.userID.toString()
      this.loginLoading = true
      this.$store
        .dispatch('login', {
          userID: this.form.userID,
          password: this.form.password
        })
        .then(() => {
          this.loginLoading = false
          wx.redirectTo({
            url: '/pages/index/main?refresh=true'
          })
        })
        .catch(() => {
          this.loginLoading = false
        })
    }
  }
}
</script>

<style scoped>
.page {
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  background: #03a9f4;
  background: -webkit-linear-gradient(top left, #50a3a2 0%, #53e3a6 100%);
  background: linear-gradient(to bottom, #7EB3EC 0%, #44a9fc 100%);
  height: 100vh; /* Allow spacing based on window height */
  margin: 0;
  min-height: 240px;
  z-index: 6000;
}

/* The background from https://codepen.io/lotap/pen/yNYxRz */
/* The form part */
.content {
  /* A box that the form resides in - centered vertically and horizontally based on the window. The max-width and % width combo allow it to resize for small devices */
  /* background: #eee; */
  /* border-radius: 8px; */
  /* box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); */
  display: block;
  left: 50%;
  max-width: 360px;
  position: absolute;
  top: 50%;
  -ms-transform: translate(-50%, -50%);
  -webkit-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);
  width: 90%;
  z-index: 2;
}
body {
  font-family: 'Source Sans Pro', sans-serif;
  color: white;
  font-weight: 300;
}
body ::input-placeholder {
  /* WebKit browsers */
  font-family: 'Source Sans Pro', sans-serif;
  color: white;
  font-weight: 300;
}
form {
  padding: 20px 0;
  position: relative;
  z-index: 2;
}
form input {
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  outline: 0;
  border: 1px solid rgba(255, 255, 255, 0.4);
  background-color: rgba(255, 255, 255, 0.2);
  width: 250px;
  height: 50px;
  border-radius: 3px;
  /* padding: 10px 15px; */
  margin: 0 auto 10px auto;
  display: block;
  text-align: center;
  font-size: 18px;
  color: white;
  transition-duration: 0.25s;
  font-weight: 300;
}
form input:hover {
  background-color: rgba(255, 255, 255, 0.4);
}
form input:focus {
  background-color: white;
  width: 300px;
  color: #53e3a6;
}
form button {
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  outline: 0;
  background-color: white;
  border: 0;
  /* padding: 10px 15px; */
  color: #85b7d8;
  border-radius: 3px;
  width: 250px;
  cursor: pointer;
  font-size: 18px;
  transition-duration: 0.25s;
}
.button-hover {
  background-color: #f5f7f9;
}
@-webkit-keyframes square {
  0% {
    -webkit-transform: translateY(0);
    transform: translateY(0);
  }
  100% {
    -webkit-transform: translateY(-700px) rotate(600deg);
    transform: translateY(-700px) rotate(600deg);
  }
}
@keyframes square {
  0% {
    -webkit-transform: translateY(0);
    transform: translateY(0);
  }
  100% {
    -webkit-transform: translateY(-700px) rotate(600deg);
    transform: translateY(-700px) rotate(600deg);
  }
}
</style>
