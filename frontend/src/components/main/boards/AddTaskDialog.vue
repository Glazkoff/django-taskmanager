<template>
  <v-dialog v-model="dialog" persistent width="500">
    <v-card>
      <v-card-title class="text-h5" v-if="editTaskObj == null">
        Добавить задачу
      </v-card-title>
      <v-card-title class="text-h5" v-else> Редактировать задачу </v-card-title>

      <v-card-text>
        <v-text-field
          label="Описание задачи"
          v-model="task.body"
          :rules="[(value) => !!value || 'Поле обязательно']"
          outlined
        ></v-text-field>
        <v-select
          v-model="task.storyPoints"
          :items="storyPointEstimate"
          item-text="number"
          item-value="number"
          label="Story points"
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
          :items="updatedStatusSet"
          item-text="name"
          item-value="id"
          label="Статус"
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
import { CREATE_TASK, UPDATE_TASK } from "@/graphql/queries.js";

export default {
  name: "AddTaskDialog",
  props: [
    "dialog",
    "storyPointEstimate",
    "statusSet",
    "employees",
    "sprints",
    "newStatusId",
    "editTaskObj"
  ],
  data() {
    return {
      task: {
        storyPoints:
          this.editTaskObj != null ? this.editTaskObj.storyPoints : null,
        body: this.editTaskObj != null ? this.editTaskObj.body : null,
        executor:
          this.editTaskObj != null && this.editTaskObj.executor != null
            ? this.editTaskObj.executor.id
            : null,
        sprint:
          this.editTaskObj != null && this.editTaskObj.sprint != null
            ? this.editTaskObj.sprint.id
            : null,
        status:
          this.editTaskObj != null && this.editTaskObj.status != null
            ? this.editTaskObj.status.id
            : null,
        comments: []
      },
      formLoading: false
    };
  },
  methods: {
    setStatusValue(statusValue) {
      this.task.status = statusValue;
    },
    setValues(editTaskObj) {
      if (editTaskObj != null) {
        this.task.storyPoints = editTaskObj.storyPoints;
        this.task.body = editTaskObj.body;
        if (editTaskObj.executor != null) {
          this.task.executor = editTaskObj.executor.id;
        }
        if (editTaskObj.sprint != null) {
          this.task.sprint = editTaskObj.sprint.id;
        }
        if (editTaskObj.status != null) {
          this.task.status = editTaskObj.status.id;
        }
      }
    },
    onCancel() {
      this.task = {
        storyPoints: null,
        body: null,
        executor: null,
        sprint: null,
        status: null,
        comments: []
      };
      this.$emit("close");
    },
    onSave() {
      this.formLoading = true;
      if (this.editTaskObj != null) {
        this.$apollo
          .mutate({
            mutation: UPDATE_TASK,
            variables: {
              taskId: this.editTaskObj.id,
              body: this.task.body,
              sprintId: this.task.sprint,
              executorId: this.task.executor || 0,
              storyPoints: this.task.storyPoints || 0,
              statusId: this.task.status || 0
            }
          })
          .then(() => {
            this.formLoading = false;
            this.task = {
              storyPoints: null,
              body: null,
              executor: null,
              sprint: null,
              status: null,
              comments: []
            };
            this.$emit("refresh");
            this.$emit("close");
          })
          .catch((err) => {
            this.formLoading = false;
            console.log(err);
          });
      } else {
        this.$apollo
          .mutate({
            mutation: CREATE_TASK,
            variables: {
              body: this.task.body,
              sprintId: this.task.sprint,
              executorId: this.task.executor || 0,
              storyPoints: this.task.storyPoints || 0,
              statusId: this.task.status || 0,
              board: this.$route.params.id
            }
          })
          .then(() => {
            this.formLoading = false;
            this.task = {
              storyPoints: null,
              body: null,
              executor: null,
              sprint: null,
              status: null,
              comments: []
            };
            this.$emit("refresh");
            this.$emit("close");
          })
          .catch((err) => {
            this.formLoading = false;
            console.log(err);
          });
      }
    }
  },
  computed: {
    updatedStatusSet() {
      let updArr = [];
      updArr[0] = {
        id: null,
        name: "Без статуса"
      };
      for (let index = 0; index < this.statusSet.length; index++) {
        const element = this.statusSet[index];
        updArr.push(element);
      }
      // updArr.concat(this.statusSet);
      return updArr;
    }
  }
};
</script>

<style lang="scss" scoped></style>
