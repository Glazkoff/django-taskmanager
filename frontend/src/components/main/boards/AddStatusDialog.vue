<template>
  <v-dialog v-model="dialog" persistent width="500">
    <v-card>
      <v-card-title class="text-h5"> Добавить новый статус </v-card-title>
      <v-card-text>
        <v-text-field
          label="Название статуса"
          :rules="[(value) => !!value || 'Поле обязательно']"
          v-model="statusName"
        ></v-text-field>
      </v-card-text>
      <v-divider></v-divider>
      <v-card-actions>
        <v-btn color="primary" text @click="onCancel">Отменить</v-btn>
        <v-spacer></v-spacer>
        <v-btn color="primary" text @click="onSave">Сохранить</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
import { CREATE_STATUS } from "@/graphql/queries.js";
export default {
  name: "AddStatusDialog",
  props: ["dialog"],
  data() {
    return {
      routeId: this.$route.params.id,
      statusName: ""
    };
  },
  methods: {
    onCancel() {
      this.$emit("close");
    },
    onSave() {
      this.$apollo
        .mutate({
          mutation: CREATE_STATUS,
          variables: {
            boardId: this.routeId,
            statusName: this.statusName
          }
        })
        .then(() => {
          this.statusName = "";
        })
        .catch((e) => {
          console.log(e);
        })
        .finally(() => {
          this.$emit("data-refresh");
          this.$emit("close");
        });
    }
  }
};
</script>

<style lang="scss" scoped></style>
