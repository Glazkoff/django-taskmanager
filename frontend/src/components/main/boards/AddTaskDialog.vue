<template>
  <v-dialog v-model="dialog" persistent width="500">
    <v-card>
      <v-card-title class="text-h5"> Добавить задачу </v-card-title>

      <v-card-text>
        <v-text-field
          label="Название статуса"
          :rules="[(value) => !!value || 'Поле обязательно']"
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
export default {
  name: "AddTaskDialog",
  props: ["dialog"],
  data() {
    return {
      task: {
        id: 1,
        storyPoints: 1,
        body: "Купить коту еды",
        executor: 2,
        sprint: 1,
        status: 1,
        comments: []
      }
    };
  },
  methods: {
    onCancel() {
      this.$emit("close");
    },
    onSave() {
      this.$emit("close");
    }
  }
};
</script>

<style lang="scss" scoped></style>
