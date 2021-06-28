<template>
  <v-flex class="auth-form text-center">
    <v-card light="light">
      <v-card-title class="text-center">
        <h1 class="mb-2">Авторизация</h1>
      </v-card-title>
      <v-card-text>
        <v-form>
          <v-text-field
            :disabled="formLoading"
            light="light"
            label="Логин"
            type="text"
            autocomplete="login"
            required
            v-model.trim="form.login"
            :rules="[(value) => !!value || 'Поле обязательно']"
          ></v-text-field>
          <v-text-field
            :disabled="formLoading"
            light="light"
            label="Пароль"
            :type="passShow ? 'text' : 'password'"
            :append-icon="passShow ? 'mdi-eye' : 'mdi-eye-off'"
            @click:append="passShow = !passShow"
            autocomplete="current-password"
            required
            v-model.trim="form.password"
            :rules="[(value) => !!value || 'Поле обязательно']"
          ></v-text-field>
          <v-btn
            class="mt-8 my-button"
            color="black"
            :dark="!formLoading"
            @click.prevent="logIn"
            block="block"
            type="submit"
            :disabled="formLoading"
            :loading="formLoading"
          >
            Войти
          </v-btn>
        </v-form>
      </v-card-text>
    </v-card>
  </v-flex>
</template>

<script>
export default {
  name: "Login",
  data() {
    return {
      formLoading: false,
      passShow: false,
      form: {
        login: null,
        password: null
      }
    };
  },
  methods: {
    logIn() {
      console.log("login");
    }
  }
};
</script>

<style lang="scss" scoped></style>
