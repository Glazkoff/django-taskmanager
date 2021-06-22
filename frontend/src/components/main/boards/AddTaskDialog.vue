<template>
  <v-dialog v-model="dialog" persistent width="500">
    <v-card>
      <v-card-title class="text-h5"> Добавить задачу </v-card-title>

      <v-card-text>
        <v-text-field
          label="Описание задачи"
          :rules="[(value) => !!value || 'Поле обязательно']"
        ></v-text-field>
        <!-- <v-text-field
          label="Story points"
          :rules="[(value) => !!value || 'Поле обязательно']"
        ></v-text-field> -->
        <v-select
          v-model="task.storyPoints"
          :items="storyPointEstimate"
          item-text="number"
          item-value="number"
          label="Story points"
          :rules="[(value) => !!value || 'Поле обязательно']"
          return-object
          outlined
        ></v-select>
        <v-text-field
          label="Спринт"
          :rules="[(value) => !!value || 'Поле обязательно']"
        ></v-text-field>
        <v-select
          v-model="task.status"
          :items="statusSet"
          item-text="name"
          item-value="id"
          label="Статус"
          :rules="[(value) => !!value || 'Поле обязательно']"
          return-object
          outlined
        ></v-select>
        <v-select
          v-model="task.employee"
          :items="employees"
          item-text="user.firstName"
          item-value="user.id"
          label="Исполнитель задачи"
          :rules="[(value) => !!value || 'Поле обязательно']"
          return-object
          outlined
        ></v-select>
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
  props: ["dialog", "storyPointEstimate", "statusSet", "employees", "sprints"],
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
