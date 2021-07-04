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
            :error-messages="errorMessages"
            :rules="[(value) => !!value || 'Поле обязательно']"
            @input="errorMessages = []"
            @blur="errorMessages = []"
          ></v-text-field>
          <v-text-field
            :disabled="formLoading"
            light="light"
            label="Пароль"
            :type="passShow ? 'text' : 'password'"
            :append-icon="passShow ? 'mdi-eye' : 'mdi-eye-off'"
            :error-messages="errorMessages"
            @click:append="passShow = !passShow"
            autocomplete="current-password"
            required
            v-model.trim="form.password"
            :rules="[(value) => !!value || 'Поле обязательно']"
            @input="errorMessages = []"
            @blur="errorMessages = []"
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
import { CREATE_USER_AUTH } from "@/graphql/queries.js";
export default {
  name: "Login",
  data() {
    return {
      formLoading: false,
      passShow: false,
      errorMessages: [],
      form: {
        login: null,
        password: null
      }
    };
  },
  methods: {
    logIn() {
      this.$apollo
        .mutate({
          mutation: CREATE_USER_AUTH,
          variables: {
            username: this.form.login,
            password: this.form.password
          }
        })
        .then((res) => {
          if (res.data.createUserAuth.isOk) {
            this.form.login = null;
            this.form.password = null;
            let role = res.data.createUserAuth.employee.teamRole || "USER";
            this.$store.commit("SET_ROLE", role);
            localStorage.setItem(
              "user",
              JSON.stringify(res.data.createUserAuth)
            );
            localStorage.setItem("isAuthorized", true);
            localStorage.setItem("role", role);
            this.$router.push("/");
          } else {
            this.form.login = null;
            this.form.password = null;
            this.errorMessages.push("Неправильные логин или пароль!");
          }
        })
        .catch((err) => {
          console.log(err);
        });
    }
  }
};
</script>

<style lang="scss" scoped></style>
