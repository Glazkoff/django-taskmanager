<template>
  <v-dialog v-model="dialog" persistent width="500">
    <v-card>
      <v-card-title class="text-h5"> Добавить новый спринт </v-card-title>
      <v-card-text>
        <v-text-field
          label="Название спринта"
          :rules="[(value) => !!value || 'Поле обязательно']"
          v-model="sprint.name"
          outlined
        ></v-text-field>
        <v-text-field
          label="Цель спринта"
          :rules="[(value) => !!value || 'Поле обязательно']"
          v-model="sprint.aim"
          outlined
        ></v-text-field>
        <v-select
          v-model="sprint.project"
          :items="projects"
          item-value="id"
          label="Проект"
          :rules="[(value) => !!value || 'Поле обязательно']"
          outlined
        >
          <template slot="selection" slot-scope="{ item }">
            {{ item.name }} (#{{ item.id }})
          </template>
          <template slot="item" slot-scope="{ item }">
            {{ item.name }} (#{{ item.id }})
          </template>
        </v-select>
        <DatePicker
          label="Дата начала"
          @update="sprint.startDate = $event"
        ></DatePicker>
        <DatePicker
          label="Дата окончания"
          @update="sprint.finishDate = $event"
        ></DatePicker>
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
import { CREATE_SPRINT, PROJECTS } from "@/graphql/queries.js";
import DatePicker from "@/components/global/DatePicker.vue";

export default {
  name: "AddSprintDialog",
  props: ["dialog"],
  components: { DatePicker },
  data() {
    return {
      sprint: {
        name: null,
        aim: null,
        project: null,
        startDate: null,
        finishDate: null
      }
    };
  },
  apollo: {
    projects: {
      query: PROJECTS
    }
  },
  methods: {
    onCancel() {
      this.$emit("close");
    },
    onSave() {
      let startDate;
      let finishDate;
      if (this.sprint.startDate != null) {
        let startDateArr = this.sprint.startDate.split(".");
        startDate = `${startDateArr[2]}-${startDateArr[1]}-${startDateArr[0]}`;
      }
      if (this.sprint.finishDate != null) {
        let finishDateArr = this.sprint.finishDate.split(".");
        finishDate = `${finishDateArr[2]}-${finishDateArr[1]}-${finishDateArr[0]}`;
      }

      this.$apollo
        .mutate({
          mutation: CREATE_SPRINT,
          variables: {
            name: this.sprint.name,
            aim: this.sprint.aim,
            projectId: this.sprint.project,
            startDate,
            finishDate
          }
        })
        .then(() => {
          this.sprint = {
            name: null,
            aim: null,
            project: null,
            startDate: null,
            finishDate: null
          };
          this.$emit("refresh");
          this.$emit("close");
        })
        .catch((err) => {
          console.log(err);
        });
    },
    setProjectValue(projectId) {
      this.sprint.project = projectId;
    }
  }
};
</script>

<style lang="scss" scoped></style>
