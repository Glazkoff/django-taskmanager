<template>
  <v-dialog v-model="dialog" persistent width="500">
    <v-card>
      <v-card-title class="text-h5"> Добавить новую команду </v-card-title>
      <v-card-text>
        <v-text-field
          label="Название команды"
          :rules="[(value) => !!value || 'Поле обязательно']"
          v-model="team.name"
          outlined
        ></v-text-field>
        <v-select
          v-model="team.leader"
          :items="users"
          item-value="id"
          label="Лидер"
          :rules="[(value) => !!value || 'Поле обязательно']"
          outlined
        >
          <template slot="selection" slot-scope="{ item }">
            {{ item.firstName }} {{ item.lastName }} ({{ item.username }})
          </template>
          <template slot="item" slot-scope="{ item }">
            {{ item.firstName }} {{ item.lastName }} ({{ item.username }})
          </template>
        </v-select>
        <v-select
          v-model="team.project"
          :items="projects"
          item-text="name"
          item-value="id"
          label="Проект"
          :rules="[(value) => !!value || 'Поле обязательно']"
          outlined
        ></v-select>
        <v-select
          v-model="team.participants"
          :items="users"
          item-value="id"
          label="Участники"
          :rules="[(value) => !!value || 'Поле обязательно']"
          outlined
          multiple
          chips
        >
          <template slot="selection" slot-scope="{ item }">
            {{ item.firstName }} {{ item.lastName }} ({{ item.username }})
          </template>
          <template slot="item" slot-scope="{ item }">
            {{ item.firstName }} {{ item.lastName }} ({{ item.username }})
          </template>
        </v-select>
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
import { USERS, PROJECTS, CREATE_TEAMS } from "@/graphql/queries.js";
export default {
  name: "AddDeskDialog",
  props: ["dialog"],
  data() {
    return {
      team: {
        name: null,
        leader: null,
        project: null,
        participants: []
      }
    };
  },
  apollo: {
    users: {
      query: USERS
    },
    projects: {
      query: PROJECTS
    }
  },
  methods: {
    onCancel() {
      this.$emit("close");
    },
    onSave() {
      this.$apollo
        .mutate({
          mutation: CREATE_TEAMS,
          variables: {
            name: this.team.name,
            leaderId: this.team.leader,
            projectId: this.team.project,
            participants: this.team.participants
          }
        })
        .then(() => {
          this.$emit("refresh");
          this.$emit("close");
        })
        .catch((err) => {
          console.log(err);
        });
    }
  }
};
</script>

<style lang="scss" scoped></style>
