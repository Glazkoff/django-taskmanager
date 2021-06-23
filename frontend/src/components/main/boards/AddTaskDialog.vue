<template>
  <v-dialog v-model="dialog" persistent width="500">
    <v-card>
      <v-card-title class="text-h5"> Добавить задачу </v-card-title>

      <v-card-text>
        <v-text-field
          label="Описание задачи"
          v-model="task.body"
          :rules="[(value) => !!value || 'Поле обязательно']"
        ></v-text-field>
        <v-select
          v-model="task.storyPoints"
          :items="storyPointEstimate"
          item-text="number"
          item-value="number"
          label="Story points"
          :rules="[(value) => !!value || 'Поле обязательно']"
          outlined
        ></v-select>
        <v-select
          v-model="task.sprint"
          :items="sprints"
          item-text="name"
          item-value="id"
          label="Спринт"
          :rules="[(value) => !!value || 'Поле обязательно']"
          outlined
        ></v-select>
        <v-select
          v-model="task.status"
          :items="statusSet"
          item-text="name"
          item-value="id"
          label="Статус"
          :rules="[(value) => !!value || 'Поле обязательно']"
          outlined
        ></v-select>
        <v-select
          v-model="task.executor"
          :items="employees"
          item-text="user.firstName"
          item-value="user.id"
          label="Исполнитель задачи"
          :rules="[(value) => !!value || 'Поле обязательно']"
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
import { CREATE_TASK } from "@/graphql/queries.js";

export default {
  name: "AddTaskDialog",
  props: [
    "dialog",
    "storyPointEstimate",
    "statusSet",
    "employees",
    "sprints",
    "newStatusId"
  ],
  data() {
    return {
      task: {
        storyPoints: null,
        body: "Купить коту еды",
        executor: null,
        sprint: null,
        status: this.newStatusId,
        comments: []
      },
      formLoading: false
    };
  },
  methods: {
    onCancel() {
      this.$emit("close");
    },
    onSave() {
      this.formLoading = true;
      this.$apollo
        .mutate({
          mutation: CREATE_TASK,
          variables: {
            body: this.task.body,
            sprintId: this.task.sprint,
            executorId: this.task.executor,
            storyPoints: this.task.storyPoints,
            statusId: this.task.status,
            board: this.$route.params.id
          }
        })
        .then(() => {
          this.formLoading = false;
          this.$emit("refresh");
          this.$emit("close");
        })
        .catch((err) => {
          this.formLoading = false;
          console.log(err);
        });
    }
  }
};
</script>

<style lang="scss" scoped></style>
